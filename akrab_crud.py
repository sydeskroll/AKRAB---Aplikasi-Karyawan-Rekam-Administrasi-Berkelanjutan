import csv
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, 'employees.csv')
APP_NAME = 'AKRAB'
APP_DESCRIPTION = 'Aplikasi Karyawan Rekam Administrasi Berkelanjutan'
FIELD_NAMES = [
    'id',
    'first_name',
    'last_name',
    'email',
    'phone',
    'department',
    'position',
    'salary',
    'hire_date',
    'is_active'
]


def create_data_file_if_missing(filename):
    if not os.path.exists(filename):
        with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=FIELD_NAMES)
            writer.writeheader()


def load_employees(filename):
    create_data_file_if_missing(filename)
    employees = []
    with open(filename, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if not row.get('id'):
                continue
            try:
                employees.append({
                    'id': int(row['id']),
                    'first_name': row.get('first_name', '').strip(),
                    'last_name': row.get('last_name', '').strip(),
                    'email': row.get('email', '').strip(),
                    'phone': row.get('phone', '').strip(),
                    'department': row.get('department', '').strip(),
                    'position': row.get('position', '').strip(),
                    'salary': parse_float(row.get('salary', 0)),
                    'hire_date': row.get('hire_date', '').strip(),
                    'is_active': parse_bool(row.get('is_active', 'False'))
                })
            except ValueError:
                print(f"Peringatan: baris data tidak valid dilewati: {row}")
    return employees


def save_employees(filename, employees):
    with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=FIELD_NAMES)
        writer.writeheader()
        for emp in employees:
            row = emp.copy()
            row['salary'] = f'{emp["salary"]:.2f}'
            row['is_active'] = 'True' if emp['is_active'] else 'False'
            writer.writerow(row)


def next_employee_id(employees):
    if not employees:
        return 1
    return max(emp['id'] for emp in employees) + 1


def input_nonempty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print('Masukan tidak boleh kosong. Silakan coba lagi.')


def input_float(prompt):
    while True:
        value = input(prompt).strip()
        try:
            return float(value)
        except ValueError:
            print('Masukan angka yang valid. Contoh: 4500000')


def input_date(prompt):
    while True:
        value = input(prompt).strip()
        try:
            datetime.strptime(value, '%Y-%m-%d')
            return value
        except ValueError:
            print('Format tanggal harus YYYY-MM-DD. Contoh: 2025-05-15')


def parse_float(value, default=0.0):
    try:
        return float(value)
    except (ValueError, TypeError):
        return default


def parse_bool(value):
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        return value.strip().lower() in {'true', '1', 'y', 'yes', 'ya', 't'}
    return False


def format_rupiah(amount):
    try:
        amount = float(amount)
    except (ValueError, TypeError):
        amount = 0.0
    formatted = f"{amount:,.2f}"
    formatted = formatted.replace(',', 'X').replace('.', ',').replace('X', '.')
    return f"Rp{formatted}"


def input_yesno(prompt, default=True):
    yes = {'y', 'yes', 'ya', 'true', 't'}
    no = {'n', 'no', 'tidak', 'false', 'f'}
    while True:
        value = input(prompt).strip().lower()
        if not value:
            return default
        if value in yes:
            return True
        if value in no:
            return False
        print('Masukan "y"/"n" atau "ya"/"tidak".')


def format_employee(emp):
    status = 'Aktif' if emp['is_active'] else 'Tidak Aktif'
    return (
        f"[{emp['id']}] {emp['first_name']} {emp['last_name']} - {emp['position']} ({emp['department']})\n"
        f"    Email: {emp['email']} | Telepon: {emp['phone']} | Gaji: {format_rupiah(emp['salary'])}\n"
        f"    Tanggal Masuk: {emp['hire_date']} | Status: {status}"
    )


def list_employees(employees):
    if not employees:
        print('\nBelum ada data karyawan. Tambahkan karyawan terlebih dahulu.\n')
        return
    print('\nDaftar Karyawan Perusahaan:')
    print('-' * 60)
    for emp in employees:
        status = 'Aktif' if emp['is_active'] else 'Tidak Aktif'
        print(f"{emp['id']}. {emp['first_name']} {emp['last_name']} - {emp['position']} ({emp['department']}) | {status} | Gaji: {format_rupiah(emp['salary'])}")
    print('-' * 60)


def view_employee(employees):
    if not employees:
        print('\nTidak ada data untuk dilihat.\n')
        return
    try:
        emp_id = int(input('Masukkan ID karyawan yang ingin dilihat: ').strip())
    except ValueError:
        print('ID harus berupa angka.')
        return
    employee = next((emp for emp in employees if emp['id'] == emp_id), None)
    if employee:
        print('\nDetail Karyawan:')
        print(format_employee(employee) + '\n')
    else:
        print(f'Tidak ditemukan karyawan dengan ID {emp_id}.')


def add_employee(employees):
    print('\nTambah Karyawan Baru')
    first_name = input_nonempty('Nama Depan: ')
    last_name = input_nonempty('Nama Belakang: ')
    email = input_nonempty('Email: ')
    phone = input('Telepon: ').strip()
    department = input_nonempty('Departemen: ')
    position = input_nonempty('Posisi: ')
    salary = input_float('Gaji (contoh: 4500000): ')
    hire_date = input_date('Tanggal Masuk (YYYY-MM-DD): ')
    is_active = input_yesno('Status Aktif? (y/n, default y): ', default=True)

    new_employee = {
        'id': next_employee_id(employees),
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'phone': phone,
        'department': department,
        'position': position,
        'salary': salary,
        'hire_date': hire_date,
        'is_active': is_active
    }
    employees.append(new_employee)
    print(f"\nKaryawan {first_name} {last_name} berhasil ditambahkan dengan ID {new_employee['id']}.\n")


def find_employee_by_id(employees, prompt_text):
    if not employees:
        print('\nTidak ada data karyawan.\n')
        return None
    try:
        emp_id = int(input(prompt_text).strip())
    except ValueError:
        print('ID harus berupa angka.')
        return None
    employee = next((emp for emp in employees if emp['id'] == emp_id), None)
    if not employee:
        print(f'Tidak ditemukan karyawan dengan ID {emp_id}.')
    return employee


def edit_employee(employees):
    print('\nUbah Data Karyawan')
    employee = find_employee_by_id(employees, 'Masukkan ID karyawan yang ingin diubah: ')
    if not employee:
        return

    print('\nBiarkan kosong jika tidak ingin mengubah nilai tertentu.')
    first_name = input(f"Nama Depan [{employee['first_name']}]: ").strip() or employee['first_name']
    last_name = input(f"Nama Belakang [{employee['last_name']}]: ").strip() or employee['last_name']
    email = input(f"Email [{employee['email']}]: ").strip() or employee['email']
    phone = input(f"Telepon [{employee['phone']}]: ").strip() or employee['phone']
    department = input(f"Departemen [{employee['department']}]: ").strip() or employee['department']
    position = input(f"Posisi [{employee['position']}]: ").strip() or employee['position']

    salary_input = input(f"Gaji [{employee['salary']:.2f}]: ").strip()
    salary = employee['salary']
    if salary_input:
        try:
            salary = float(salary_input)
        except ValueError:
            print('Gaji tidak valid. Menggunakan nilai lama.')

    hire_date_input = input(f"Tanggal Masuk [{employee['hire_date']}]: ").strip()
    hire_date = employee['hire_date']
    if hire_date_input:
        try:
            datetime.strptime(hire_date_input, '%Y-%m-%d')
            hire_date = hire_date_input
        except ValueError:
            print('Format tanggal tidak valid. Menggunakan nilai lama.')

    is_active = input_yesno(f"Status Aktif saat ini ({'y' if employee['is_active'] else 'n'})? (y/n, kosong = tidak berubah): ", default=employee['is_active'])

    employee.update({
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'phone': phone,
        'department': department,
        'position': position,
        'salary': salary,
        'hire_date': hire_date,
        'is_active': is_active
    })
    print(f"\nData karyawan ID {employee['id']} berhasil diperbarui.\n")


def delete_employee(employees):
    print('\nHapus Karyawan')
    employee = find_employee_by_id(employees, 'Masukkan ID karyawan yang ingin dihapus: ')
    if not employee:
        return
    confirm = input_yesno(f"Yakin hapus {employee['first_name']} {employee['last_name']}? (y/n): ", default=False)
    if confirm:
        employees.remove(employee)
        print(f"\nKaryawan ID {employee['id']} berhasil dihapus.\n")
    else:
        print('\nPenghapusan dibatalkan.\n')


def search_employee(employees):
    query = input('Cari nama atau departemen: ').strip().lower()
    if not query:
        print('Masukan pencarian tidak boleh kosong.')
        return
    results = [emp for emp in employees if query in emp['first_name'].lower() or query in emp['last_name'].lower() or query in emp['department'].lower() or query in emp['position'].lower()]
    if not results:
        print('\nTidak ditemukan karyawan dengan kata kunci tersebut.\n')
        return
    print(f"\nHasil pencarian untuk '{query}':")
    print('-' * 60)
    for emp in results:
        print(format_employee(emp))
        print('-' * 60)


def show_menu():
    print(f'''
{APP_NAME} - {APP_DESCRIPTION}
=================================
1. Tampilkan semua karyawan
2. Lihat detail karyawan
3. Tambah karyawan
4. Ubah karyawan
5. Hapus karyawan
6. Cari karyawan
0. Keluar
''')


def main():
    employees = load_employees(DATA_FILE)
    while True:
        show_menu()
        choice = input('Pilih menu: ').strip()

        if choice == '1':
            list_employees(employees)
        elif choice == '2':
            view_employee(employees)
        elif choice == '3':
            add_employee(employees)
            save_employees(DATA_FILE, employees)
        elif choice == '4':
            edit_employee(employees)
            save_employees(DATA_FILE, employees)
        elif choice == '5':
            delete_employee(employees)
            save_employees(DATA_FILE, employees)
        elif choice == '6':
            search_employee(employees)
        elif choice == '0':
            print('Keluar dari aplikasi. Sampai jumpa!')
            break
        else:
            print('Pilihan tidak valid. Silakan pilih angka 0-6.')


if __name__ == '__main__':
    main()
