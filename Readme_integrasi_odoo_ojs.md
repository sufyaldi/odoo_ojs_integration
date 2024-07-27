Integrasi Custom OJS

Modul Odoo ini mengintegrasikan PKP OJS (Open Journal Systems) dengan Odoo dengan menerima dan menyimpan data publikasi. Modul ini juga menampilkan data publikasi di situs web Odoo dalam tampilan kanban dengan foto penulis yang diambil dari catatan karyawan.

Fitur
Menerima dan menyimpan data publikasi.
Menampilkan data publikasi di situs web Odoo dalam tampilan kanban.
Menampilkan foto penulis yang diambil dari catatan karyawan.
Menyertakan detail publikasi seperti judul, abstrak, penulis, tanggal publikasi, URL jurnal, dan foto penulis.
Instalasi
Clone repositori ini ke direktori addons Odoo Anda:

sh
Copy code
git clone https://github.com/yourusername/custom_ojs_integration.git /path/to/odoo/addons/custom_ojs_integration
Restart server Odoo Anda untuk mengenali modul baru:

sh
Copy code
./odoo-bin -d your_database_name -i custom_ojs_integration
Buka Odoo dan perbarui daftar aplikasi dengan menavigasi ke Aplikasi > Perbarui Daftar Aplikasi.

Cari Custom OJS Integration dan instal modul tersebut.

Konfigurasi
Arahkan ke Publications di bawah menu utama.
Buat atau edit publikasi, tautkan ke karyawan dan isi detail yang diperlukan.
Pastikan karyawan memiliki foto mereka yang diunggah dalam catatan mereka.
Penggunaan
Untuk melihat publikasi di situs web, navigasikan ke http://localhost:8069/publications.
Publikasi akan ditampilkan dalam tampilan kanban dengan detail dan foto penulis.
Model
publication.module:
title: Char (Judul)
abstract: Text (Abstrak)
authors: Char (Penulis)
publication_date: Date (Tanggal Publikasi)
journal_url: Char (URL Jurnal)
author_id: Many2one (Referensi ke hr.employee)
Tampilan
Form View untuk publication.module
Tree View untuk publication.module
Template Kanban untuk menampilkan data publikasi di situs web
Kustomisasi
Menambahkan Kolom
Untuk menambahkan lebih banyak kolom ke modul publikasi:

Perbarui model publication.module di publication.py.
Perbarui tampilan form dan tree di publication_views.xml.
Perbarui template kanban di website_publication_kanban_template.xml.
Memperbarui Gaya
Untuk memperbarui gaya tampilan kanban:

Modifikasi CSS di static/src/css/website_publication_kanban.css.
Kontribusi
Fork repositori ini.
Buat branch baru (git checkout -b feature/FiturAnda).
Commit perubahan Anda (git commit -am 'Menambahkan fitur tertentu').
Push ke branch (git push origin feature/FiturAnda).
Buat Pull Request baru.
Lisensi
Proyek ini dilisensikan di bawah Lisensi MIT - lihat file LICENSE untuk detail lebih lanjut.

Penulis
sufyALDI - IT Architect
