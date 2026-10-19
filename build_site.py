#!/usr/bin/env python3
"""Build core pages for Solved Sindh Textbook Board Books (index, books, solved, about, contact, legal, SEO files).
Run: python3 build_site.py  (then python3 build_blog.py for the 50 blog posts)
Data source: assets/data/books.json is generated here from BOOKS below.
To add a book: add an entry to BOOKS (or edit assets/data/books.json) + drop the PDF in assets/pdfs/.
"""
import json, os
from datetime import date

SITE = os.path.dirname(os.path.abspath(__file__))
BASE = "https://solved-stbb-books.vercel.app"
TODAY = date.today().isoformat()

# ---------------- Book catalogue ----------------
REAL = [
{'id': 'isl-6-sd', 'cover': 'assets/images/covers/isl-6-sd.jpg', 'title': 'Class 6 Islamiat — Solved Exercises (Sindhi Medium)', 'cls': 6, 'subject': 'Islamiat', 'medium': 'Sindhi', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class6-Islamiat-SolvedExercises-Sindhi.pdf', 'pages': 28, 'desc': "Complete solved exercises for Sindh Textbook Board Class 6 Islamiat, Sindhi medium — handwritten-style notes in the book's own format.", 'chapters': ['Quran Majeed — Nazra, Hifz, Duaein', 'Imaniyat & Ibadat — Tauheed, Azan, Namaz, Hajj', 'Seerat Tayyaba — Sulah Hudaibiya se Ghazwa Khyber', 'Akhlaq & Adab — Taharat, Sadaqat, Amanat, Huqooq-ul-Ibad', 'Mashahir-e-Islam — Khadija, Ali, Data Ganj Bakhsh, Tariq bin Ziyad']},
{'id': 'isl-6-ur', 'cover': 'assets/images/covers/isl-6-ur.jpg', 'title': 'Class 6 Islamiat — Solved Exercises (Urdu Medium)', 'cls': 6, 'subject': 'Islamiat', 'medium': 'Urdu', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class6-Islamiat-SolvedExercises-Urdu.pdf', 'pages': 28, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 6 Islamiat, Urdu medium — clear answers in exam format.', 'chapters': ['Quran Majeed — Nazra, Hifz, Duaein', 'Imaniyat & Ibadat — Tauheed, Azan, Namaz, Hajj', 'Seerat Tayyaba — Sulah Hudaibiya se Ghazwa Khyber', 'Akhlaq & Adab — Taharat, Sadaqat, Amanat, Huqooq-ul-Ibad', 'Mashahir-e-Islam — Khadija, Ali, Data Ganj Bakhsh, Tariq bin Ziyad']},
{'id': 'isl-8-sd', 'cover': 'assets/images/covers/isl-8-sd.jpg', 'title': 'Class 8 Islamiat — Solved Exercises (Sindhi Medium)', 'cls': 8, 'subject': 'Islamiat', 'medium': 'Sindhi', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class8-Islamiat-SolvedExercises-Sindhi.pdf', 'pages': 32, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 8 Islamiat, Sindhi medium — Aakhirat, Roza, Seerat, Akhlaq solved.', 'chapters': ['Quran Majeed — Nazra, Hifz, Ayat-ul-Kursi', 'Imaniyat & Ibadat — Aakhirat, Roza, Hajj', 'Seerat Tayyaba — Khulq-e-Azeem, Sabr, Adl, Husn-e-Muashrat', 'Akhlaq & Adab — Halal Kamai, Itehad-e-Milli, Huqooq-ul-Ibad', 'Mashahir-e-Islam — Fatima-tuz-Zahra, Muhammad bin Qasim, Ibn-e-Sina, Shah Waliullah']},
{'id': 'isl-8-ur', 'cover': 'assets/images/covers/isl-8-ur.jpg', 'title': 'Class 8 Islamiat — Solved Exercises (Urdu Medium)', 'cls': 8, 'subject': 'Islamiat', 'medium': 'Urdu', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class8-Islamiat-SolvedExercises-Urdu.pdf', 'pages': 32, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 8 Islamiat, Urdu medium — exam-ready answers.', 'chapters': ['Quran Majeed — Nazra, Hifz, Ayat-ul-Kursi', 'Imaniyat & Ibadat — Aakhirat, Roza, Hajj', 'Seerat Tayyaba — Khulq-e-Azeem, Sabr, Adl, Husn-e-Muashrat', 'Akhlaq & Adab — Halal Kamai, Itehad-e-Milli, Huqooq-ul-Ibad', 'Mashahir-e-Islam — Fatima-tuz-Zahra, Muhammad bin Qasim, Ibn-e-Sina, Shah Waliullah']},
{'id': 'isl-9-sd', 'cover': 'assets/images/covers/isl-9-sd.jpg', 'title': 'Class 9 Islamiat — Solved Exercises (Sindhi Medium)', 'cls': 9, 'subject': 'Islamiat', 'medium': 'Sindhi', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class9-Islamiat-SolvedExercises-Sindhi.pdf', 'pages': 40, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 9 Islamiat (IX–X volume), Sindhi medium — Quran, Hadith, Tauheed, Seerat.', 'chapters': ['Quran Majeed — Taaruf, Fazilat, Chuninda Ayaat', 'Hadith Sharif — Taaruf, Sunnat, Chuninda Ahadith', 'Imaniyat — Tauheed, Risalat', 'Ibadat — Ahmiyat, Jihad', 'Seerat Tayyaba — Baasat, Dawat, Hijrat, Ghazwat, Shamail', 'Akhlaq — Ilm, Khandan, Ehtram-e-Insaniyat, Adl, Haya', 'Mashahir — Imam Hussain, Abu Ubaidah, Jabir bin Hayyan']},
{'id': 'isl-9-ur', 'cover': 'assets/images/covers/isl-9-ur.jpg', 'title': 'Class 9 Islamiat — Solved Exercises (Urdu Medium)', 'cls': 9, 'subject': 'Islamiat', 'medium': 'Urdu', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class9-Islamiat-SolvedExercises-Urdu.pdf', 'pages': 40, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 9 Islamiat (IX–X volume), Urdu medium — board-exam-ready answers.', 'chapters': ['Quran Majeed — Taaruf, Fazilat, Chuninda Ayaat', 'Hadith Sharif — Taaruf, Sunnat, Chuninda Ahadith', 'Imaniyat — Tauheed, Risalat', 'Ibadat — Ahmiyat, Jihad', 'Seerat Tayyaba — Baasat, Dawat, Hijrat, Ghazwat, Shamail', 'Akhlaq — Ilm, Khandan, Ehtram-e-Insaniyat, Adl, Haya', 'Mashahir — Imam Hussain, Abu Ubaidah, Jabir bin Hayyan']},
{'id': 'sindhi-6-si', 'title': 'Class 6 Sindhi — Solved Exercises (Sindhi Medium)', 'cls': 6, 'subject': 'Sindhi', 'medium': 'Sindhi', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class6-Sindhi-SolvedExercises-Sindhi.pdf', 'pages': 39, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 6 Sindhi, Sindhi medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-66.jpg'},
{'id': 'sindhi-6-ur', 'title': 'Class 6 Sindhi — Solved Exercises (Urdu Medium)', 'cls': 6, 'subject': 'Sindhi', 'medium': 'Urdu', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class6-Sindhi-SolvedExercises-Urdu.pdf', 'pages': 39, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 6 Sindhi, Urdu medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-66.jpg'},
{'id': 'sindhi-6-en', 'title': 'Class 6 Sindhi — Solved Exercises (English Medium)', 'cls': 6, 'subject': 'Sindhi', 'medium': 'English', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class6-Sindhi-SolvedExercises-English.pdf', 'pages': 49, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 6 Sindhi, English medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-66.jpg'},
{'id': 'english-6-si', 'title': 'Class 6 English — Solved Exercises (Sindhi Medium)', 'cls': 6, 'subject': 'English', 'medium': 'Sindhi', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class6-English-SolvedExercises-Sindhi.pdf', 'pages': 39, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 6 English, Sindhi medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-143.jpg'},
{'id': 'english-6-ur', 'title': 'Class 6 English — Solved Exercises (Urdu Medium)', 'cls': 6, 'subject': 'English', 'medium': 'Urdu', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class6-English-SolvedExercises-Urdu.pdf', 'pages': 39, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 6 English, Urdu medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-143.jpg'},
{'id': 'english-6-en', 'title': 'Class 6 English — Solved Exercises (English Medium)', 'cls': 6, 'subject': 'English', 'medium': 'English', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class6-English-SolvedExercises-English.pdf', 'pages': 43, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 6 English, English medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-143.jpg'},
{'id': 'arabic-6-ar', 'title': 'Class 6 Arabic — Solved Exercises (Arabic Medium)', 'cls': 6, 'subject': 'Arabic', 'medium': 'Arabic', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class6-Arabic-SolvedExercises-Arabic.pdf', 'pages': 162, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 6 Arabic, Arabic medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-41.jpg'},
{'id': 'math-6-si', 'title': 'Class 6 Math — Solved Exercises (Sindhi Medium)', 'cls': 6, 'subject': 'Math', 'medium': 'Sindhi', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class6-Math-SolvedExercises-Sindhi.pdf', 'pages': 133, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 6 Math, Sindhi medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-270.jpg'},
{'id': 'math-6-ur', 'title': 'Class 6 Math — Solved Exercises (Urdu Medium)', 'cls': 6, 'subject': 'Math', 'medium': 'Urdu', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class6-Math-SolvedExercises-Urdu.pdf', 'pages': 141, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 6 Math, Urdu medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-96.jpg'},
{'id': 'math-6-en', 'title': 'Class 6 Math — Solved Exercises (English Medium)', 'cls': 6, 'subject': 'Math', 'medium': 'English', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class6-Math-SolvedExercises-English.pdf', 'pages': 144, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 6 Math, English medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-96.jpg'},
{'id': 'science-6-si', 'title': 'Class 6 Science — Solved Exercises (Sindhi Medium)', 'cls': 6, 'subject': 'Science', 'medium': 'Sindhi', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class6-Science-SolvedExercises-Sindhi.pdf', 'pages': 22, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 6 Science, Sindhi medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-115.jpg'},
{'id': 'science-6-ur', 'title': 'Class 6 Science — Solved Exercises (Urdu Medium)', 'cls': 6, 'subject': 'Science', 'medium': 'Urdu', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class6-Science-SolvedExercises-Urdu.pdf', 'pages': 22, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 6 Science, Urdu medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-115.jpg'},
{'id': 'science-6-en', 'title': 'Class 6 Science — Solved Exercises (English Medium)', 'cls': 6, 'subject': 'Science', 'medium': 'English', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class6-Science-SolvedExercises-English.pdf', 'pages': 24, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 6 Science, English medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-115.jpg'},
{'id': 'social-studies-6-si', 'title': 'Class 6 Social Studies — Solved Exercises (Sindhi Medium)', 'cls': 6, 'subject': 'Social Studies', 'medium': 'Sindhi', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class6-Social-SolvedExercises-Sindhi.pdf', 'pages': 98, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 6 Social Studies, Sindhi medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-131.jpg'},
{'id': 'social-studies-6-ur', 'title': 'Class 6 Social Studies — Solved Exercises (Urdu Medium)', 'cls': 6, 'subject': 'Social Studies', 'medium': 'Urdu', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class6-Social-SolvedExercises-Urdu.pdf', 'pages': 102, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 6 Social Studies, Urdu medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-131.jpg'},
{'id': 'social-studies-6-en', 'title': 'Class 6 Social Studies — Solved Exercises (English Medium)', 'cls': 6, 'subject': 'Social Studies', 'medium': 'English', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class6-Social-SolvedExercises-English.pdf', 'pages': 139, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 6 Social Studies, English medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-131.jpg'},
{'id': 'islamiat-6-en', 'title': 'Class 6 Islamiat — Solved Exercises (English Medium)', 'cls': 6, 'subject': 'Islamiat', 'medium': 'English', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class6-Islamiat-SolvedExercises-English.pdf', 'pages': 54, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 6 Islamiat, English medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-260.jpg'},
{'id': 'mazhabi-taleemat-6-si', 'title': 'Class 6 Mazhabi Taleemat — Solved Exercises (Sindhi Medium)', 'cls': 6, 'subject': 'Mazhabi Taleemat', 'medium': 'Sindhi', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class6-Mazhabi-SolvedExercises-Sindhi.pdf', 'pages': 53, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 6 Mazhabi Taleemat, Sindhi medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-238.jpg'},
{'id': 'mazhabi-taleemat-6-ur', 'title': 'Class 6 Mazhabi Taleemat — Solved Exercises (Urdu Medium)', 'cls': 6, 'subject': 'Mazhabi Taleemat', 'medium': 'Urdu', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class6-Mazhabi-SolvedExercises-Urdu.pdf', 'pages': 53, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 6 Mazhabi Taleemat, Urdu medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-249.jpg'},
{'id': 'mazhabi-taleemat-6-en', 'title': 'Class 6 Mazhabi Taleemat — Solved Exercises (English Medium)', 'cls': 6, 'subject': 'Mazhabi Taleemat', 'medium': 'English', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class6-Mazhabi-SolvedExercises-English.pdf', 'pages': 54, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 6 Mazhabi Taleemat, English medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-249.jpg'},
{'id': 'computer-6-si', 'title': 'Class 6 Computer — Solved Exercises (Sindhi Medium)', 'cls': 6, 'subject': 'Computer', 'medium': 'Sindhi', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class6-Computer-SolvedExercises-Sindhi.pdf', 'pages': 25, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 6 Computer, Sindhi medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-289.jpg'},
{'id': 'computer-6-ur', 'title': 'Class 6 Computer — Solved Exercises (Urdu Medium)', 'cls': 6, 'subject': 'Computer', 'medium': 'Urdu', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class6-Computer-SolvedExercises-Urdu.pdf', 'pages': 26, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 6 Computer, Urdu medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-288.jpg'},
{'id': 'computer-6-en', 'title': 'Class 6 Computer — Solved Exercises (English Medium)', 'cls': 6, 'subject': 'Computer', 'medium': 'English', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class6-Computer-SolvedExercises-English.pdf', 'pages': 34, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 6 Computer, English medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-287.jpg'},
{'id': 'sindhi-7-si', 'title': 'Class 7 Sindhi — Solved Exercises (Sindhi Medium)', 'cls': 7, 'subject': 'Sindhi', 'medium': 'Sindhi', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class7-Sindhi-SolvedExercises-Sindhi.pdf', 'pages': 92, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 7 Sindhi, Sindhi medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-93.jpg'},
{'id': 'english-7-en', 'title': 'Class 7 English — Solved Exercises (English Medium)', 'cls': 7, 'subject': 'English', 'medium': 'English', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class7-English-SolvedExercises-English.pdf', 'pages': 231, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 7 English, English medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-145.jpg'},
{'id': 'arabic-7-ar', 'title': 'Class 7 Arabic — Solved Exercises (Arabic Medium)', 'cls': 7, 'subject': 'Arabic', 'medium': 'Arabic', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class7-Arabic-SolvedExercises-Arabic.pdf', 'pages': 146, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 7 Arabic, Arabic medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-232.jpg'},
{'id': 'math-7-si', 'title': 'Class 7 Math — Solved Exercises (Sindhi Medium)', 'cls': 7, 'subject': 'Math', 'medium': 'Sindhi', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class7-Math-SolvedExercises-Sindhi.pdf', 'pages': 164, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 7 Math, Sindhi medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-282.jpg'},
{'id': 'math-7-ur', 'title': 'Class 7 Math — Solved Exercises (Urdu Medium)', 'cls': 7, 'subject': 'Math', 'medium': 'Urdu', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class7-Math-SolvedExercises-Urdu.pdf', 'pages': 172, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 7 Math, Urdu medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-279.jpg'},
{'id': 'math-7-en', 'title': 'Class 7 Math — Solved Exercises (English Medium)', 'cls': 7, 'subject': 'Math', 'medium': 'English', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class7-Math-SolvedExercises-English.pdf', 'pages': 232, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 7 Math, English medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-97.jpg'},
{'id': 'science-7-si', 'title': 'Class 7 Science — Solved Exercises (Sindhi Medium)', 'cls': 7, 'subject': 'Science', 'medium': 'Sindhi', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class7-Science-SolvedExercises-Sindhi.pdf', 'pages': 33, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 7 Science, Sindhi medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-125.jpg'},
{'id': 'science-7-ur', 'title': 'Class 7 Science — Solved Exercises (Urdu Medium)', 'cls': 7, 'subject': 'Science', 'medium': 'Urdu', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class7-Science-SolvedExercises-Urdu.pdf', 'pages': 34, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 7 Science, Urdu medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-116.jpg'},
{'id': 'science-7-en', 'title': 'Class 7 Science — Solved Exercises (English Medium)', 'cls': 7, 'subject': 'Science', 'medium': 'English', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class7-Science-SolvedExercises-English.pdf', 'pages': 44, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 7 Science, English medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-114.jpg'},
{'id': 'social-studies-7-si', 'title': 'Class 7 Social Studies — Solved Exercises (Sindhi Medium)', 'cls': 7, 'subject': 'Social Studies', 'medium': 'Sindhi', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class7-Social-SolvedExercises-Sindhi.pdf', 'pages': 53, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 7 Social Studies, Sindhi medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-130.jpg'},
{'id': 'social-studies-7-ur', 'title': 'Class 7 Social Studies — Solved Exercises (Urdu Medium)', 'cls': 7, 'subject': 'Social Studies', 'medium': 'Urdu', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class7-Social-SolvedExercises-Urdu.pdf', 'pages': 55, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 7 Social Studies, Urdu medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-130.jpg'},
{'id': 'social-studies-7-en', 'title': 'Class 7 Social Studies — Solved Exercises (English Medium)', 'cls': 7, 'subject': 'Social Studies', 'medium': 'English', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class7-Social-SolvedExercises-English.pdf', 'pages': 81, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 7 Social Studies, English medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-130.jpg'},
{'id': 'islamiat-7-si', 'title': 'Class 7 Islamiat — Solved Exercises (Sindhi Medium)', 'cls': 7, 'subject': 'Islamiat', 'medium': 'Sindhi', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class7-Islamiat-SolvedExercises-Sindhi.pdf', 'pages': 51, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 7 Islamiat, Sindhi medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-137.jpg'},
{'id': 'islamiat-7-ur', 'title': 'Class 7 Islamiat — Solved Exercises (Urdu Medium)', 'cls': 7, 'subject': 'Islamiat', 'medium': 'Urdu', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class7-Islamiat-SolvedExercises-Urdu.pdf', 'pages': 50, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 7 Islamiat, Urdu medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-136.jpg'},
{'id': 'islamiat-7-en', 'title': 'Class 7 Islamiat — Solved Exercises (English Medium)', 'cls': 7, 'subject': 'Islamiat', 'medium': 'English', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class7-Islamiat-SolvedExercises-English.pdf', 'pages': 49, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 7 Islamiat, English medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-261.jpg'},
{'id': 'mazhabi-taleemat-7-si', 'title': 'Class 7 Mazhabi Taleemat — Solved Exercises (Sindhi Medium)', 'cls': 7, 'subject': 'Mazhabi Taleemat', 'medium': 'Sindhi', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class7-Mazhabi-SolvedExercises-Sindhi.pdf', 'pages': 55, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 7 Mazhabi Taleemat, Sindhi medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-239.jpg'},
{'id': 'mazhabi-taleemat-7-ur', 'title': 'Class 7 Mazhabi Taleemat — Solved Exercises (Urdu Medium)', 'cls': 7, 'subject': 'Mazhabi Taleemat', 'medium': 'Urdu', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class7-Mazhabi-SolvedExercises-Urdu.pdf', 'pages': 57, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 7 Mazhabi Taleemat, Urdu medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-251.jpg'},
{'id': 'mazhabi-taleemat-7-en', 'title': 'Class 7 Mazhabi Taleemat — Solved Exercises (English Medium)', 'cls': 7, 'subject': 'Mazhabi Taleemat', 'medium': 'English', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class7-Mazhabi-SolvedExercises-English.pdf', 'pages': 65, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 7 Mazhabi Taleemat, English medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-251.jpg'},
{'id': 'computer-7-si', 'title': 'Class 7 Computer — Solved Exercises (Sindhi Medium)', 'cls': 7, 'subject': 'Computer', 'medium': 'Sindhi', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class7-Computer-SolvedExercises-Sindhi.pdf', 'pages': 27, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 7 Computer, Sindhi medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-319.jpg'},
{'id': 'computer-7-ur', 'title': 'Class 7 Computer — Solved Exercises (Urdu Medium)', 'cls': 7, 'subject': 'Computer', 'medium': 'Urdu', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class7-Computer-SolvedExercises-Urdu.pdf', 'pages': 27, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 7 Computer, Urdu medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-320.jpg'},
{'id': 'computer-7-en', 'title': 'Class 7 Computer — Solved Exercises (English Medium)', 'cls': 7, 'subject': 'Computer', 'medium': 'English', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class7-Computer-SolvedExercises-English.pdf', 'pages': 31, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 7 Computer, English medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-317.jpg'},
{'id': 'sindhi-8-si', 'title': 'Class 8 Sindhi — Solved Exercises (Sindhi Medium)', 'cls': 8, 'subject': 'Sindhi', 'medium': 'Sindhi', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class8-Sindhi-SolvedExercises-Sindhi.pdf', 'pages': 162, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 8 Sindhi, Sindhi medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-94.jpg'},
{'id': 'urdu-8-ur', 'title': 'Class 8 Urdu — Solved Exercises (Urdu Medium)', 'cls': 8, 'subject': 'Urdu', 'medium': 'Urdu', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class8-Urdu-SolvedExercises-Urdu.pdf', 'pages': 156, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 8 Urdu, Urdu medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-23.jpg'},
{'id': 'english-8-en', 'title': 'Class 8 English — Solved Exercises (English Medium)', 'cls': 8, 'subject': 'English', 'medium': 'English', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class8-English-SolvedExercises-English.pdf', 'pages': 135, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 8 English, English medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-146.jpg'},
{'id': 'arabic-8-ar', 'title': 'Class 8 Arabic — Solved Exercises (Arabic Medium)', 'cls': 8, 'subject': 'Arabic', 'medium': 'Arabic', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class8-Arabic-SolvedExercises-Arabic.pdf', 'pages': 127, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 8 Arabic, Arabic medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-233.jpg'},
{'id': 'math-8-si', 'title': 'Class 8 Math — Solved Exercises (Sindhi Medium)', 'cls': 8, 'subject': 'Math', 'medium': 'Sindhi', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class8-Math-SolvedExercises-Sindhi.pdf', 'pages': 148, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 8 Math, Sindhi medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-272.jpg'},
{'id': 'math-8-ur', 'title': 'Class 8 Math — Solved Exercises (Urdu Medium)', 'cls': 8, 'subject': 'Math', 'medium': 'Urdu', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class8-Math-SolvedExercises-Urdu.pdf', 'pages': 156, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 8 Math, Urdu medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-284.jpg'},
{'id': 'math-8-en', 'title': 'Class 8 Math — Solved Exercises (English Medium)', 'cls': 8, 'subject': 'Math', 'medium': 'English', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class8-Math-SolvedExercises-English.pdf', 'pages': 201, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 8 Math, English medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-283.jpg'},
{'id': 'science-8-si', 'title': 'Class 8 Science — Solved Exercises (Sindhi Medium)', 'cls': 8, 'subject': 'Science', 'medium': 'Sindhi', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class8-Science-SolvedExercises-Sindhi.pdf', 'pages': 36, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 8 Science, Sindhi medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-126.jpg'},
{'id': 'science-8-ur', 'title': 'Class 8 Science — Solved Exercises (Urdu Medium)', 'cls': 8, 'subject': 'Science', 'medium': 'Urdu', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class8-Science-SolvedExercises-Urdu.pdf', 'pages': 39, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 8 Science, Urdu medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-98.jpg'},
{'id': 'science-8-en', 'title': 'Class 8 Science — Solved Exercises (English Medium)', 'cls': 8, 'subject': 'Science', 'medium': 'English', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class8-Science-SolvedExercises-English.pdf', 'pages': 50, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 8 Science, English medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-123.jpg'},
{'id': 'islamiat-8-en', 'title': 'Class 8 Islamiat — Solved Exercises (English Medium)', 'cls': 8, 'subject': 'Islamiat', 'medium': 'English', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class8-Islamiat-SolvedExercises-English.pdf', 'pages': 72, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 8 Islamiat, English medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-262.jpg'},
{'id': 'mazhabi-taleemat-8-si', 'title': 'Class 8 Mazhabi Taleemat — Solved Exercises (Sindhi Medium)', 'cls': 8, 'subject': 'Mazhabi Taleemat', 'medium': 'Sindhi', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class8-Mazhabi-SolvedExercises-Sindhi.pdf', 'pages': 61, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 8 Mazhabi Taleemat, Sindhi medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-240.jpg'},
{'id': 'mazhabi-taleemat-8-ur', 'title': 'Class 8 Mazhabi Taleemat — Solved Exercises (Urdu Medium)', 'cls': 8, 'subject': 'Mazhabi Taleemat', 'medium': 'Urdu', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class8-Mazhabi-SolvedExercises-Urdu.pdf', 'pages': 61, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 8 Mazhabi Taleemat, Urdu medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-248.jpg'},
{'id': 'mazhabi-taleemat-8-en', 'title': 'Class 8 Mazhabi Taleemat — Solved Exercises (English Medium)', 'cls': 8, 'subject': 'Mazhabi Taleemat', 'medium': 'English', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class8-Mazhabi-SolvedExercises-English.pdf', 'pages': 75, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 8 Mazhabi Taleemat, English medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-248.jpg'},
{'id': 'computer-8-si', 'title': 'Class 8 Computer — Solved Exercises (Sindhi Medium)', 'cls': 8, 'subject': 'Computer', 'medium': 'Sindhi', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class8-Computer-SolvedExercises-Sindhi.pdf', 'pages': 25, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 8 Computer, Sindhi medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-292.jpg'},
{'id': 'computer-8-ur', 'title': 'Class 8 Computer — Solved Exercises (Urdu Medium)', 'cls': 8, 'subject': 'Computer', 'medium': 'Urdu', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class8-Computer-SolvedExercises-Urdu.pdf', 'pages': 26, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 8 Computer, Urdu medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-292.jpg'},
{'id': 'computer-8-en', 'title': 'Class 8 Computer — Solved Exercises (English Medium)', 'cls': 8, 'subject': 'Computer', 'medium': 'English', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class8-Computer-SolvedExercises-English.pdf', 'pages': 30, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 8 Computer, English medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-322.jpg'},
{'id': 'sindhi-9-si', 'title': 'Class 9 Sindhi — Solved Exercises (Sindhi Medium)', 'cls': 9, 'subject': 'Sindhi', 'medium': 'Sindhi', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class9-Sindhi-SolvedExercises-Sindhi.pdf', 'pages': 98, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 9 Sindhi, Sindhi medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-212.jpg'},
{'id': 'urdu-9-ur', 'title': 'Class 9 Urdu — Solved Exercises (Urdu Medium)', 'cls': 9, 'subject': 'Urdu', 'medium': 'Urdu', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class9-Urdu-SolvedExercises-Urdu.pdf', 'pages': 112, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 9 Urdu, Urdu medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-13.jpg'},
{'id': 'english-9-en', 'title': 'Class 9 English — Solved Exercises (English Medium)', 'cls': 9, 'subject': 'English', 'medium': 'English', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class9-English-SolvedExercises-English.pdf', 'pages': 196, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 9 English, English medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-147.jpg'},
{'id': 'math-9-si', 'title': 'Class 9 Math — Solved Exercises (Sindhi Medium)', 'cls': 9, 'subject': 'Math', 'medium': 'Sindhi', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class9-Math-SolvedExercises-Sindhi.pdf', 'pages': 110, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 9 Math, Sindhi medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-275.jpg'},
{'id': 'math-9-ur', 'title': 'Class 9 Math — Solved Exercises (Urdu Medium)', 'cls': 9, 'subject': 'Math', 'medium': 'Urdu', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class9-Math-SolvedExercises-Urdu.pdf', 'pages': 111, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 9 Math, Urdu medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-180.jpg'},
{'id': 'math-9-en', 'title': 'Class 9 Math — Solved Exercises (English Medium)', 'cls': 9, 'subject': 'Math', 'medium': 'English', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class9-Math-SolvedExercises-English.pdf', 'pages': 140, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 9 Math, English medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-180.jpg'},
{'id': 'islamiat-9-en', 'title': 'Class 9 Islamiat — Solved Exercises (English Medium)', 'cls': 9, 'subject': 'Islamiat', 'medium': 'English', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class9-Islamiat-SolvedExercises-English.pdf', 'pages': 113, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 9 Islamiat, English medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-267.jpg'},
{'id': 'mazhabi-taleemat-9-si', 'title': 'Class 9 Mazhabi Taleemat — Solved Exercises (Sindhi Medium)', 'cls': 9, 'subject': 'Mazhabi Taleemat', 'medium': 'Sindhi', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class9-Mazhabi-SolvedExercises-Sindhi.pdf', 'pages': 58, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 9 Mazhabi Taleemat, Sindhi medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-252.jpg'},
{'id': 'mazhabi-taleemat-9-ur', 'title': 'Class 9 Mazhabi Taleemat — Solved Exercises (Urdu Medium)', 'cls': 9, 'subject': 'Mazhabi Taleemat', 'medium': 'Urdu', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class9-Mazhabi-SolvedExercises-Urdu.pdf', 'pages': 59, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 9 Mazhabi Taleemat, Urdu medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-252.jpg'},
{'id': 'mazhabi-taleemat-9-en', 'title': 'Class 9 Mazhabi Taleemat — Solved Exercises (English Medium)', 'cls': 9, 'subject': 'Mazhabi Taleemat', 'medium': 'English', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class9-Mazhabi-SolvedExercises-English.pdf', 'pages': 63, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 9 Mazhabi Taleemat, English medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-252.jpg'},
{'id': 'computer-9-si', 'title': 'Class 9 Computer — Solved Exercises (Sindhi Medium)', 'cls': 9, 'subject': 'Computer', 'medium': 'Sindhi', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class9-Computer-SolvedExercises-Sindhi.pdf', 'pages': 31, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 9 Computer, Sindhi medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-184.jpg'},
{'id': 'computer-9-ur', 'title': 'Class 9 Computer — Solved Exercises (Urdu Medium)', 'cls': 9, 'subject': 'Computer', 'medium': 'Urdu', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class9-Computer-SolvedExercises-Urdu.pdf', 'pages': 32, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 9 Computer, Urdu medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-291.jpg'},
{'id': 'computer-9-en', 'title': 'Class 9 Computer — Solved Exercises (English Medium)', 'cls': 9, 'subject': 'Computer', 'medium': 'English', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class9-Computer-SolvedExercises-English.pdf', 'pages': 40, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 9 Computer, English medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-121.jpg'},
{'id': 'physics-9-si', 'title': 'Class 9 Physics — Solved Exercises (Sindhi Medium)', 'cls': 9, 'subject': 'Physics', 'medium': 'Sindhi', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class9-Physics-SolvedExercises-Sindhi.pdf', 'pages': 39, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 9 Physics, Sindhi medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-174.jpg'},
{'id': 'physics-9-ur', 'title': 'Class 9 Physics — Solved Exercises (Urdu Medium)', 'cls': 9, 'subject': 'Physics', 'medium': 'Urdu', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class9-Physics-SolvedExercises-Urdu.pdf', 'pages': 37, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 9 Physics, Urdu medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-174.jpg'},
{'id': 'physics-9-en', 'title': 'Class 9 Physics — Solved Exercises (English Medium)', 'cls': 9, 'subject': 'Physics', 'medium': 'English', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class9-Physics-SolvedExercises-English.pdf', 'pages': 54, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 9 Physics, English medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-174.jpg'},
{'id': 'chemistry-9-si', 'title': 'Class 9 Chemistry — Solved Exercises (Sindhi Medium)', 'cls': 9, 'subject': 'Chemistry', 'medium': 'Sindhi', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class9-Chemistry-SolvedExercises-Sindhi.pdf', 'pages': 41, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 9 Chemistry, Sindhi medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-196.jpg'},
{'id': 'chemistry-9-ur', 'title': 'Class 9 Chemistry — Solved Exercises (Urdu Medium)', 'cls': 9, 'subject': 'Chemistry', 'medium': 'Urdu', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class9-Chemistry-SolvedExercises-Urdu.pdf', 'pages': 44, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 9 Chemistry, Urdu medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-197.jpg'},
{'id': 'chemistry-9-en', 'title': 'Class 9 Chemistry — Solved Exercises (English Medium)', 'cls': 9, 'subject': 'Chemistry', 'medium': 'English', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class9-Chemistry-SolvedExercises-English.pdf', 'pages': 62, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 9 Chemistry, English medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-195.jpg'},
{'id': 'biology-9-si', 'title': 'Class 9 Biology — Solved Exercises (Sindhi Medium)', 'cls': 9, 'subject': 'Biology', 'medium': 'Sindhi', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class9-Biology-SolvedExercises-Sindhi.pdf', 'pages': 37, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 9 Biology, Sindhi medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-119.jpg'},
{'id': 'biology-9-ur', 'title': 'Class 9 Biology — Solved Exercises (Urdu Medium)', 'cls': 9, 'subject': 'Biology', 'medium': 'Urdu', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class9-Biology-SolvedExercises-Urdu.pdf', 'pages': 38, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 9 Biology, Urdu medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-118.jpg'},
{'id': 'biology-9-en', 'title': 'Class 9 Biology — Solved Exercises (English Medium)', 'cls': 9, 'subject': 'Biology', 'medium': 'English', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class9-Biology-SolvedExercises-English.pdf', 'pages': 50, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 9 Biology, English medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-117.jpg'},
{'id': 'pakistan-studies-9-si', 'title': 'Class 9 Pakistan Studies — Solved Exercises (Sindhi Medium)', 'cls': 9, 'subject': 'Pakistan Studies', 'medium': 'Sindhi', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class9-PakistanStudies-SolvedExercises-Sindhi.pdf', 'pages': 34, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 9 Pakistan Studies, Sindhi medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-183.jpg'},
{'id': 'pakistan-studies-9-ur', 'title': 'Class 9 Pakistan Studies — Solved Exercises (Urdu Medium)', 'cls': 9, 'subject': 'Pakistan Studies', 'medium': 'Urdu', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class9-PakistanStudies-SolvedExercises-Urdu.pdf', 'pages': 35, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 9 Pakistan Studies, Urdu medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-183.jpg'},
{'id': 'pakistan-studies-9-en', 'title': 'Class 9 Pakistan Studies — Solved Exercises (English Medium)', 'cls': 9, 'subject': 'Pakistan Studies', 'medium': 'English', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class9-PakistanStudies-SolvedExercises-English.pdf', 'pages': 53, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 9 Pakistan Studies, English medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-183.jpg'},
{'id': 'sindhi-10-si', 'title': 'Class 10 Sindhi — Solved Exercises (Sindhi Medium)', 'cls': 10, 'subject': 'Sindhi', 'medium': 'Sindhi', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class10-Sindhi-SolvedExercises-Sindhi.pdf', 'pages': 98, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 10 Sindhi, Sindhi medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-212.jpg'},
{'id': 'urdu-10-ur', 'title': 'Class 10 Urdu — Solved Exercises (Urdu Medium)', 'cls': 10, 'subject': 'Urdu', 'medium': 'Urdu', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class10-Urdu-SolvedExercises-Urdu.pdf', 'pages': 112, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 10 Urdu, Urdu medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-13.jpg'},
{'id': 'english-10-en', 'title': 'Class 10 English — Solved Exercises (English Medium)', 'cls': 10, 'subject': 'English', 'medium': 'English', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class10-English-SolvedExercises-English.pdf', 'pages': 369, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 10 English, English medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-201.jpg'},
{'id': 'math-10-si', 'title': 'Class 10 Math — Solved Exercises (Sindhi Medium)', 'cls': 10, 'subject': 'Math', 'medium': 'Sindhi', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class10-Math-SolvedExercises-Sindhi.pdf', 'pages': 101, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 10 Math, Sindhi medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-285.jpg'},
{'id': 'math-10-ur', 'title': 'Class 10 Math — Solved Exercises (Urdu Medium)', 'cls': 10, 'subject': 'Math', 'medium': 'Urdu', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class10-Math-SolvedExercises-Urdu.pdf', 'pages': 108, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 10 Math, Urdu medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-277.jpg'},
{'id': 'math-10-en', 'title': 'Class 10 Math — Solved Exercises (English Medium)', 'cls': 10, 'subject': 'Math', 'medium': 'English', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class10-Math-SolvedExercises-English.pdf', 'pages': 151, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 10 Math, English medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-205.jpg'},
{'id': 'islamiat-10-si', 'title': 'Class 10 Islamiat — Solved Exercises (Sindhi Medium)', 'cls': 10, 'subject': 'Islamiat', 'medium': 'Sindhi', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class10-Islamiat-SolvedExercises-Sindhi.pdf', 'pages': 70, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 10 Islamiat, Sindhi medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-264.jpg'},
{'id': 'islamiat-10-ur', 'title': 'Class 10 Islamiat — Solved Exercises (Urdu Medium)', 'cls': 10, 'subject': 'Islamiat', 'medium': 'Urdu', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class10-Islamiat-SolvedExercises-Urdu.pdf', 'pages': 73, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 10 Islamiat, Urdu medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-265.jpg'},
{'id': 'islamiat-10-en', 'title': 'Class 10 Islamiat — Solved Exercises (English Medium)', 'cls': 10, 'subject': 'Islamiat', 'medium': 'English', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class10-Islamiat-SolvedExercises-English.pdf', 'pages': 113, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 10 Islamiat, English medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-267.jpg'},
{'id': 'mazhabi-taleemat-10-si', 'title': 'Class 10 Mazhabi Taleemat — Solved Exercises (Sindhi Medium)', 'cls': 10, 'subject': 'Mazhabi Taleemat', 'medium': 'Sindhi', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class10-Mazhabi-SolvedExercises-Sindhi.pdf', 'pages': 58, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 10 Mazhabi Taleemat, Sindhi medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-252.jpg'},
{'id': 'mazhabi-taleemat-10-ur', 'title': 'Class 10 Mazhabi Taleemat — Solved Exercises (Urdu Medium)', 'cls': 10, 'subject': 'Mazhabi Taleemat', 'medium': 'Urdu', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class10-Mazhabi-SolvedExercises-Urdu.pdf', 'pages': 59, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 10 Mazhabi Taleemat, Urdu medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-252.jpg'},
{'id': 'mazhabi-taleemat-10-en', 'title': 'Class 10 Mazhabi Taleemat — Solved Exercises (English Medium)', 'cls': 10, 'subject': 'Mazhabi Taleemat', 'medium': 'English', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class10-Mazhabi-SolvedExercises-English.pdf', 'pages': 63, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 10 Mazhabi Taleemat, English medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-252.jpg'},
{'id': 'computer-10-si', 'title': 'Class 10 Computer — Solved Exercises (Sindhi Medium)', 'cls': 10, 'subject': 'Computer', 'medium': 'Sindhi', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class10-Computer-SolvedExercises-Sindhi.pdf', 'pages': 30, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 10 Computer, Sindhi medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-204.jpg'},
{'id': 'computer-10-ur', 'title': 'Class 10 Computer — Solved Exercises (Urdu Medium)', 'cls': 10, 'subject': 'Computer', 'medium': 'Urdu', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class10-Computer-SolvedExercises-Urdu.pdf', 'pages': 32, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 10 Computer, Urdu medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-204.jpg'},
{'id': 'computer-10-en', 'title': 'Class 10 Computer — Solved Exercises (English Medium)', 'cls': 10, 'subject': 'Computer', 'medium': 'English', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class10-Computer-SolvedExercises-English.pdf', 'pages': 37, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 10 Computer, English medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-204.jpg'},
{'id': 'physics-10-si', 'title': 'Class 10 Physics — Solved Exercises (Sindhi Medium)', 'cls': 10, 'subject': 'Physics', 'medium': 'Sindhi', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class10-Physics-SolvedExercises-Sindhi.pdf', 'pages': 54, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 10 Physics, Sindhi medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-223.jpg'},
{'id': 'physics-10-ur', 'title': 'Class 10 Physics — Solved Exercises (Urdu Medium)', 'cls': 10, 'subject': 'Physics', 'medium': 'Urdu', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class10-Physics-SolvedExercises-Urdu.pdf', 'pages': 57, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 10 Physics, Urdu medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-202.jpg'},
{'id': 'physics-10-en', 'title': 'Class 10 Physics — Solved Exercises (English Medium)', 'cls': 10, 'subject': 'Physics', 'medium': 'English', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class10-Physics-SolvedExercises-English.pdf', 'pages': 72, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 10 Physics, English medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-202.jpg'},
{'id': 'chemistry-10-si', 'title': 'Class 10 Chemistry — Solved Exercises (Sindhi Medium)', 'cls': 10, 'subject': 'Chemistry', 'medium': 'Sindhi', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class10-Chemistry-SolvedExercises-Sindhi.pdf', 'pages': 39, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 10 Chemistry, Sindhi medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-199.jpg'},
{'id': 'chemistry-10-ur', 'title': 'Class 10 Chemistry — Solved Exercises (Urdu Medium)', 'cls': 10, 'subject': 'Chemistry', 'medium': 'Urdu', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class10-Chemistry-SolvedExercises-Urdu.pdf', 'pages': 41, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 10 Chemistry, Urdu medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-200.jpg'},
{'id': 'chemistry-10-en', 'title': 'Class 10 Chemistry — Solved Exercises (English Medium)', 'cls': 10, 'subject': 'Chemistry', 'medium': 'English', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class10-Chemistry-SolvedExercises-English.pdf', 'pages': 52, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 10 Chemistry, English medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-198.jpg'},
{'id': 'biology-10-si', 'title': 'Class 10 Biology — Solved Exercises (Sindhi Medium)', 'cls': 10, 'subject': 'Biology', 'medium': 'Sindhi', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class10-Biology-SolvedExercises-Sindhi.pdf', 'pages': 33, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 10 Biology, Sindhi medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-186.jpg'},
{'id': 'biology-10-ur', 'title': 'Class 10 Biology — Solved Exercises (Urdu Medium)', 'cls': 10, 'subject': 'Biology', 'medium': 'Urdu', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class10-Biology-SolvedExercises-Urdu.pdf', 'pages': 33, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 10 Biology, Urdu medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-188.jpg'},
{'id': 'biology-10-en', 'title': 'Class 10 Biology — Solved Exercises (English Medium)', 'cls': 10, 'subject': 'Biology', 'medium': 'English', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class10-Biology-SolvedExercises-English.pdf', 'pages': 41, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 10 Biology, English medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-188.jpg'},
{'id': 'pakistan-studies-10-si', 'title': 'Class 10 Pakistan Studies — Solved Exercises (Sindhi Medium)', 'cls': 10, 'subject': 'Pakistan Studies', 'medium': 'Sindhi', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class10-PakistanStudies-SolvedExercises-Sindhi.pdf', 'pages': 34, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 10 Pakistan Studies, Sindhi medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-227.jpg'},
{'id': 'pakistan-studies-10-ur', 'title': 'Class 10 Pakistan Studies — Solved Exercises (Urdu Medium)', 'cls': 10, 'subject': 'Pakistan Studies', 'medium': 'Urdu', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class10-PakistanStudies-SolvedExercises-Urdu.pdf', 'pages': 35, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 10 Pakistan Studies, Urdu medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-227.jpg'},
{'id': 'pakistan-studies-10-en', 'title': 'Class 10 Pakistan Studies — Solved Exercises (English Medium)', 'cls': 10, 'subject': 'Pakistan Studies', 'medium': 'English', 'type': 'solved-notes', 'status': 'live', 'pdf': 'assets/pdfs/Class10-PakistanStudies-SolvedExercises-English.pdf', 'pages': 53, 'desc': 'Complete solved exercises for Sindh Textbook Board Class 10 Pakistan Studies, English medium — solved from the official textbook, exam-ready answers.', 'chapters': [], 'cover': 'assets/images/covers/portal-235.jpg'}
]
SUBJ_SLUG = {"Sindhi":"sindhi","Urdu":"urdu","English":"english","Arabic":"arabic","Math":"math","Science":"science","Social Studies":"social-studies","Islamiat":"islamiat","Mazhabi Taleemat":"mazhabi-taleemat","Computer":"computer","Physics":"physics","Chemistry":"chemistry","Biology":"biology","Pakistan Studies":"pakistan-studies","Mathematics":"math"}
SUBJECT_COVERS = {s: f"assets/images/covers/subjects/{slug}.svg" for s, slug in SUBJ_SLUG.items()}
# REAL entries keep their real official covers (set in the REAL list above).
# Coming-soon entries below still use the illustrated SVG covers.
SUBJECTS_BY_CLASS = {
 1:["Sindhi","Urdu","English","Math","Islamiat"], 2:["Sindhi","Urdu","English","Math","Islamiat"],
 3:["Sindhi","Urdu","English","Math","Science"], 4:["Sindhi","Urdu","English","Math","Science"],
 5:["Sindhi","Urdu","English","Math","Science"], 6:["Sindhi","Urdu","English","Math","Science","Social Studies"],
 7:["Sindhi","Urdu","English","Math","Science","Islamiat"], 8:["Sindhi","Urdu","English","Math","Science","Social Studies"],
 9:["Urdu","English","Math","Physics","Chemistry","Biology","Pakistan Studies"],
 10:["Urdu","English","Math","Physics","Chemistry","Biology","Pakistan Studies"],
}
MEDIUMS = ["Sindhi","Urdu","English"]
REAL_IDS = {b['id'] for b in REAL}
BOOKS = list(REAL)
for cls, subjects in SUBJECTS_BY_CLASS.items():
    for j, subj in enumerate(subjects):
        med = MEDIUMS[(cls + j) % 3]
        if subj == "Islamiat" and cls in (6,8,9) and med in ("Sindhi","Urdu"):
            continue  # already live above
        if f"{subj.lower().replace(' ','-')}-{cls}-{med.lower()[:2]}" in REAL_IDS:
            continue  # already live in REAL
        BOOKS.append({"id":f"{subj.lower().replace(' ','-')}-{cls}-{med.lower()[:2]}","title":f"Class {cls} {subj} — Solved Exercises ({med} Medium)","cls":cls,"subject":subj,"medium":med,"type":"solved-notes","status":"coming-soon","pdf":None,"pages":None,"desc":f"Sindh Textbook Board Class {cls} {subj} solved exercises, {med} medium — coming soon. Browse the 119 live solved books while this one is prepared.","chapters":[],"cover":SUBJECT_COVERS[subj]})
for subj in ["Physics","Chemistry","Biology","Mathematics","Urdu","English"]:
    BOOKS.append({"id":f"{subj.lower()}-11-en","title":f"Class 11 {subj} — Solved Exercises (English Medium)","cls":11,"subject":subj,"medium":"English","type":"solved-notes","status":"coming-soon","pdf":None,"pages":None,"desc":f"Sindh Textbook Board Class 11 {subj} solved exercises, English medium — coming soon.","chapters":[],"cover":SUBJECT_COVERS[subj]})
for subj in ["Physics","Chemistry","Biology","Mathematics","Urdu","English"]:
    BOOKS.append({"id":f"{subj.lower()}-12-en","title":f"Class 12 {subj} — Solved Exercises (English Medium)","cls":12,"subject":subj,"medium":"English","type":"solved-notes","status":"coming-soon","pdf":None,"pages":None,"desc":f"Sindh Textbook Board Class 12 {subj} solved exercises, English medium — coming soon.","chapters":[],"cover":SUBJECT_COVERS[subj]})

def w(path, content):
    full = os.path.join(SITE, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    return full


CSS = r"""
:root{--green:#0B6B4A;--green2:#0E8A5F;--green-dark:#065F46;--dark:#14201B;--muted:#5A6B62;--bg:#F7FAF8;--card:#fff;--line:#E3ECE7;--amber:#F5B301;--radius:16px}
*{box-sizing:border-box}html{scroll-behavior:smooth}html,body{width:100%}body{overflow-x:clip;margin:0;font-family:system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif;color:var(--dark);background:#fff;line-height:1.65}
a{color:var(--green)}a:hover{color:var(--green2)}:focus-visible{outline:3px solid rgba(14,138,95,.45);outline-offset:2px;border-radius:6px}.container{width:100%;max-width:1180px;margin:0 auto;padding:0 20px}
.skip-link{position:absolute;left:-9999px}.skip-link:focus{position:static;background:var(--green);color:#fff;padding:8px 14px;display:block}
.site-header{background:#fff;border-bottom:1px solid #EEF2EF;position:sticky;top:0;z-index:50}.header-inner{display:flex;align-items:center;gap:18px;min-height:68px}
.logo{display:flex;align-items:center;gap:10px;text-decoration:none;color:var(--dark);line-height:1.15;white-space:nowrap}.logo-mark{display:inline-flex;align-items:center;justify-content:center;min-width:40px;width:40px;height:40px;border-radius:11px;background:linear-gradient(135deg,#0E8A5F,#0B6B4A);color:#fff;font-size:23px;font-weight:800;box-shadow:0 4px 10px rgba(11,107,74,.25)}.logo-text{font-weight:800;font-size:16.5px;white-space:nowrap;letter-spacing:-.2px}
.main-nav{margin-left:auto;display:flex;align-items:center;gap:2px;flex-wrap:wrap}.main-nav a{padding:9px 14px;border-radius:999px;text-decoration:none;color:var(--dark);font-weight:600;font-size:15px}.main-nav a.active{background:var(--green);color:#fff!important}.main-nav a:hover{background:#EAF4EF;color:var(--green)}
.btn{display:inline-block;background:linear-gradient(135deg,#0E8A5F,#0B6B4A);color:#fff!important;text-decoration:none;padding:12px 22px;border-radius:999px;font-weight:700;border:2px solid var(--green);cursor:pointer;box-shadow:0 6px 16px rgba(11,107,74,.22);transition:transform .2s ease,box-shadow .2s ease,background .2s ease}.btn:hover{background:linear-gradient(135deg,#12A06E,#0B6B4A);border-color:var(--green2);transform:translateY(-1px);box-shadow:0 10px 22px rgba(11,107,74,.28)}.btn.small{padding:9px 16px;font-size:14px}.btn .ic{vertical-align:-2px;margin-right:5px}.btn.outline{background:#fff;color:var(--green)!important}.btn.light{background:#fff;color:var(--green)!important;border-color:#fff}.btn.amber{background:var(--amber);border-color:var(--amber);color:#222!important}.btn.amber:hover{background:#FFC61A;border-color:#FFC61A}.nav-toggle{display:none;margin-left:auto;background:none;border:1px solid var(--line);border-radius:8px;padding:8px 12px;font-size:18px;cursor:pointer}
.hero{position:relative;overflow:hidden;padding:32px 0 28px;background:url('/assets/images/covers/hero-banner.jpg') center/cover no-repeat,#063E2A;color:#fff}
.hero-copy{max-width:600px}
.hero-badge{display:inline-flex;align-items:center;gap:7px;background:rgba(255,255,255,.14);border:1px solid rgba(255,255,255,.22);padding:7px 15px;border-radius:999px;font-size:13.5px;font-weight:700}
.hero h1{font-size:clamp(24px,3vw,30px);line-height:1.14;margin:18px 0 14px;font-weight:800;letter-spacing:-.3px}
.hero-yellow{color:#FDE047}
.hero-lead{font-size:16px;opacity:.92;max-width:560px;margin:0 0 14px}
.hero-search{display:flex;gap:8px;background:#fff;border-radius:999px;padding:7px 7px 7px 18px;max-width:560px;box-shadow:0 10px 24px rgba(0,0,0,.18);align-items:center}
.hero-search .search-ic{color:#6B7280;flex-shrink:0}
.hero-search input{flex:1;border:0;outline:0;font-size:15.5px;min-width:0;background:transparent}
.hero-search .btn{padding:11px 24px}
.hero-cta{display:flex;gap:12px;flex-wrap:wrap;margin-top:18px}
.btn-white{background:#fff;color:var(--green)!important;border-color:#fff}
.trust-bar{background:#fff;border-bottom:1px solid #EEF2EF;padding:22px 0}
.trust-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:18px}
.trust-item{display:flex;gap:13px;align-items:flex-start}
.trust-ic{flex-shrink:0;width:46px;height:46px;border-radius:50%;background:#E6F4EC;display:flex;align-items:center;justify-content:center;color:var(--green)}
.trust-item b{display:block;font-size:15.5px;line-height:1.3}
.trust-item small{color:var(--muted);font-size:13.5px}
.section{padding:52px 0}.section h2{font-size:30px;margin:0 0 8px}.section .sub{color:var(--muted);max-width:760px;margin:0 0 26px}
.feat-head{display:flex;gap:20px;justify-content:space-between;align-items:flex-end;flex-wrap:wrap;margin-bottom:24px}
.feat-head h2{margin:0}.feat-head .sub{margin:6px 0 0}
.feat-pills{display:flex;gap:8px;flex-wrap:wrap}
.feat-pill{border:1.5px solid var(--line);background:#fff;color:var(--dark);padding:8px 18px;border-radius:999px;font-weight:700;font-size:14px;cursor:pointer;transition:all .2s ease}
.feat-pill.active{background:var(--green);border-color:var(--green);color:#fff}
.feat-pill:hover{border-color:var(--green);color:var(--green)}
.feat-pill.active:hover{color:#fff}
.filters{display:flex;gap:12px;flex-wrap:wrap;background:#fff;border:1px solid var(--line);padding:16px;border-radius:var(--radius);margin-bottom:26px}.filters label{font-weight:700;font-size:14px;display:flex;flex-direction:column;gap:6px;flex:1;min-width:170px}.filters input,.filters select{padding:11px 12px;border:1px solid var(--line);border-radius:9px;font-size:15px;background:#fff}
.grid{display:grid;grid-template-columns:repeat(4,1fr);gap:20px}
.card{background:var(--card);border:1px solid #E7EFEA;border-radius:20px;overflow:hidden;display:flex;flex-direction:column;box-shadow:0 2px 12px rgba(20,32,27,.06);transition:transform .25s ease,box-shadow .25s ease}
.card:hover{transform:translateY(-5px);box-shadow:0 20px 38px rgba(20,32,27,.14)}
.card-cover{position:relative;background:#F1F5F2}
.card-cover img{display:block;width:100%;height:auto;aspect-ratio:400/300;object-fit:cover}
/* 3D book (real cover on the front face + spine + page edges) */
.book-stage{position:relative;display:flex;align-items:center;justify-content:center;padding:30px 10px 34px;background:radial-gradient(120% 110% at 50% 0%,#FFFFFF 0%,#EDF5F0 55%,#DCEBE1 100%);overflow:hidden}
.book-stage::before{content:"";position:absolute;width:230px;height:230px;border-radius:50%;background:rgba(255,255,255,.6);top:-80px;right:-50px}
.book-stage::after{content:"";position:absolute;width:170px;height:170px;border-radius:50%;background:rgba(14,138,95,.10);bottom:-70px;left:-40px}
.book3d{position:relative;width:148px;height:198px;flex-shrink:0;transform-style:preserve-3d;transform:perspective(1000px) rotateY(-22deg) rotateX(2deg);transition:transform .45s cubic-bezier(.22,.8,.32,1),filter .45s ease;filter:drop-shadow(12px 16px 18px rgba(20,32,27,.30))}
.card:hover .book3d,.modal .book3d:hover{transform:perspective(1000px) rotateY(-11deg) rotateX(1deg) translateY(-6px);filter:drop-shadow(16px 24px 26px rgba(20,32,27,.34))}
.book3d-front{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center;border-radius:2px 7px 7px 2px;box-shadow:inset 0 0 0 1px rgba(0,0,0,.10);transform:translateZ(10px)}
.book3d-back{position:absolute;inset:0;background:#0B3D2B;border-radius:2px 7px 7px 2px;transform:translateZ(-10px)}
.book3d-spine{position:absolute;left:-10px;top:0;width:20px;height:100%;transform:rotateY(-90deg);background:linear-gradient(90deg,#053A28,#0B6B4A 55%,#0E8A5F);border-radius:2px 0 0 2px}
.book3d-pages{position:absolute;right:-10px;top:3px;width:20px;height:calc(100% - 6px);transform:rotateY(90deg);background:repeating-linear-gradient(90deg,#FFFDF4 0 2px,#E9E2C8 2px 3px);border-radius:0 2px 2px 0}
.book3d-shade{position:absolute;inset:0;transform:translateZ(11px);background:linear-gradient(90deg,rgba(0,0,0,.30),rgba(0,0,0,0) 20%,rgba(255,255,255,.14) 32%,rgba(0,0,0,0) 48%);border-radius:2px 7px 7px 2px;pointer-events:none}
.modal-book{border-radius:14px;margin-bottom:16px}
.modal-book .book3d{width:132px;height:176px}
@media(max-width:760px){.book3d{width:120px;height:160px}.book-stage{padding:24px 8px 28px}}
.live-badge{position:absolute;top:12px;left:12px;background:rgba(255,255,255,.94);color:#0B6B4A;font-size:12px;font-weight:800;padding:5px 11px;border-radius:999px;display:inline-flex;align-items:center;gap:5px;box-shadow:0 2px 8px rgba(0,0,0,.12)}
.live-badge i{width:7px;height:7px;border-radius:50%;background:#22C55E;display:inline-block;font-style:normal}
.live-badge.soon{color:#8A5A00}.live-badge.soon i{background:#F59E0B}
.card-body{padding:18px;display:flex;flex-direction:column;gap:10px;flex:1}
.subj-tag{display:inline-flex;align-items:center;gap:6px;font-size:13px;font-weight:800;padding:5px 11px;border-radius:8px;width:fit-content;background:#EAF4EF;color:#0B6B4A}
.subj-tag.sindhi{background:#F3E8FF;color:#7C3AED}.subj-tag.urdu{background:#E9F9EC;color:#0B6B4A}.subj-tag.english{background:#FDE8EF;color:#BE185D}.subj-tag.arabic{background:#E0F2FE;color:#1D4ED8}.subj-tag.math{background:#FFF7CC;color:#92400E}.subj-tag.science{background:#E0F7FA;color:#0E7490}.subj-tag.social-studies{background:#E8EAF6;color:#4338CA}.subj-tag.islamiat{background:#DBEAFE;color:#1E40AF}.subj-tag.mazhabi-taleemat{background:#E0F2F1;color:#00695C}.subj-tag.computer{background:#EDE9FE;color:#5B21B6}.subj-tag.physics{background:#FFEDD5;color:#C2410C}.subj-tag.chemistry{background:#FCE7F3;color:#9D174D}.subj-tag.biology{background:#DCFCE7;color:#15803D}.subj-tag.pakistan-studies{background:#D1FAE5;color:#065F46}
.card-body h3{margin:0;font-size:17.5px;line-height:1.35}
.card-meta{display:flex;gap:6px;flex-wrap:wrap;margin:0}
.card-desc{margin:0;color:var(--muted);font-size:14px;line-height:1.55}
.card-body .actions{margin-top:auto;padding-top:4px}
.btn-open{display:inline-flex;align-items:center;gap:7px;background:linear-gradient(135deg,#0E8A5F,#065F46);color:#fff!important;text-decoration:none;padding:10px 20px;border-radius:999px;font-weight:700;font-size:14.5px;box-shadow:0 6px 14px rgba(11,107,74,.24);transition:transform .2s ease,box-shadow .2s ease}.btn-open:hover{background:linear-gradient(135deg,#12A06E,#065F46);transform:translateY(-1px);box-shadow:0 10px 20px rgba(11,107,74,.30)}
.modal-cover{width:100%;max-height:260px;object-fit:contain;background:#F1F5F2;border-radius:8px;margin-bottom:12px}
.chip{display:inline-block;background:#EAF4EF;color:var(--green);padding:4px 10px;border-radius:999px;font-size:12.5px;font-weight:700}.chip.soon{background:#FFF4DE;color:#8A5A00}.chip.live{background:#E3F7EC;color:#0B6B4A}
.pdf-banner{display:flex;align-items:center;gap:18px;background:#EAF6EF;border:1px solid #D3EBDC;border-radius:18px;padding:22px 26px;flex-wrap:wrap;margin-top:10px}
.pdf-banner-icon{width:56px;height:56px;border-radius:50%;background:var(--green);color:#fff;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.pdf-banner h3{margin:0;font-size:19px}.pdf-banner p{margin:2px 0 0;color:var(--muted);font-size:14.5px}
.pdf-banner .btn.whatsapp{margin-left:auto}
.steps-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:18px}.step{background:#fff;border:1px solid var(--line);border-radius:var(--radius);padding:24px}.step .num{width:44px;height:44px;border-radius:50%;background:var(--green);color:#fff;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:20px;margin-bottom:12px}
.subject-strip{display:flex;gap:10px;flex-wrap:wrap}.subject-strip a{background:#fff;border:1px solid var(--line);padding:9px 16px;border-radius:999px;text-decoration:none;color:var(--dark);font-weight:600}
.testimonials{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:18px}.testi{background:#fff;border:1px solid var(--line);border-radius:var(--radius);padding:22px}.testi p{font-style:italic}.testi b{display:block;margin-top:10px}
.faq details{background:#fff;border:1px solid var(--line);border-radius:10px;padding:14px 18px;margin-bottom:10px}.faq summary{cursor:pointer;font-weight:700}
.newsletter{background:var(--dark);color:#fff;border-radius:18px;padding:34px;text-align:center}.newsletter h2{color:#fff}.newsletter input{padding:13px 16px;border-radius:10px;border:0;min-width:260px;font-size:15px}.newsletter form{display:flex;gap:10px;justify-content:center;flex-wrap:wrap;margin-top:16px}
.post{max-width:820px;margin:0 auto;background:#fff;border:1px solid var(--line);border-radius:16px;padding:32px}.post h1{font-size:32px;line-height:1.25}.post h2{font-size:24px;margin-top:34px}.post-meta{color:var(--muted)}.post-hero{background:var(--green);color:#fff;border-radius:12px;padding:34px 26px;display:flex;justify-content:space-between;align-items:flex-end;margin:20px 0}.post-hero-num{font-size:52px;font-weight:800}.lead{font-size:18px}
.post-thumb{width:100%;height:auto;border-radius:12px;margin:20px 0;display:block}
figure.diagram{margin:22px 0 8px;border:1px solid var(--line);border-radius:12px;padding:14px;background:#F7FAF8}figure.diagram img{width:100%;height:auto;display:block;border-radius:8px}figure.diagram figcaption{font-size:14px;color:var(--muted);text-align:center;margin-top:10px}
.key-points li{margin-bottom:10px}.steps li{margin-bottom:12px}.related{background:#F7FAF8;border:1px solid var(--line);border-radius:12px;padding:20px;margin-top:30px}
.crumbs{padding:18px 0 6px;color:var(--muted);font-size:14px}.crumbs a{color:var(--muted)}
.modal-backdrop{position:fixed;inset:0;background:rgba(0,0,0,.55);display:none;align-items:center;justify-content:center;z-index:100;padding:16px}.modal-backdrop.open{display:flex}.modal{background:#fff;border-radius:16px;max-width:640px;width:100%;max-height:88vh;overflow:auto;padding:26px}.modal .close{float:right;background:none;border:0;font-size:24px;cursor:pointer}
.site-footer{background:#fff;border-top:1px solid var(--line);margin-top:50px;padding:36px 0 20px}.footer-grid{display:grid;grid-template-columns:2fr 1fr 1fr;gap:24px}.site-footer ul{list-style:none;padding:0}.site-footer li{margin-bottom:8px}.site-footer a{text-decoration:none;color:var(--muted)}.copyright{text-align:center;color:var(--muted);font-size:13.5px;border-top:1px solid var(--line);padding-top:16px}
.pagination{display:flex;gap:12px;align-items:center;justify-content:center;margin:30px 0}.form-box{max-width:640px;background:#fff;border:1px solid var(--line);border-radius:14px;padding:26px}.form-box label{display:block;font-weight:700;margin:14px 0 6px}.form-box input,.form-box textarea,.form-box select{width:100%;padding:12px;border:1px solid var(--line);border-radius:9px;font-size:15px}
.notice{background:#FFF4DE;border:1px solid #F2D492;border-radius:10px;padding:14px 18px}
@media(max-width:1020px){.grid{grid-template-columns:repeat(3,1fr)}.trust-grid{grid-template-columns:repeat(2,1fr)}}
@media(max-width:760px){.logo{white-space:normal}.logo-text{white-space:normal}.main-nav{display:none;width:100%;flex-direction:column;align-items:stretch}.main-nav.open{display:flex}.nav-toggle{display:block}.footer-grid{grid-template-columns:1fr}.post{padding:20px}.hero{padding:24px 0 20px}.section{padding:32px 0}.grid{grid-template-columns:repeat(2,1fr)}.trust-grid{grid-template-columns:1fr 1fr}.pdf-banner{flex-direction:column;align-items:flex-start}.pdf-banner .btn.whatsapp{margin-left:0}.feat-head{flex-direction:column;align-items:flex-start}}
@media(max-width:520px){.hero h1{font-size:22px}.grid{grid-template-columns:1fr}.hero-search{flex-direction:column;background:transparent;padding:0;box-shadow:none;gap:10px}.hero-search input{background:#fff;border-radius:999px;padding:13px 18px;width:100%}.hero-search .btn{width:100%}}
.pdf-frame{width:100%;height:78vh;border:1px solid var(--line);border-radius:12px;background:#fff}.btn.whatsapp{background:#25D366;border-color:#25D366;color:#fff!important}.btn.whatsapp:hover{background:#1FB857;border-color:#1FB857}.preview-meta{display:flex;gap:8px;flex-wrap:wrap;margin:12px 0}
@media(max-width:760px){.pdf-frame{height:68vh}}

/* ---- Responsive hardening (mobile / tablet) ---- */
/* Global media containment: no image, svg, video or iframe may ever exceed its container */
img,svg,video,iframe{max-width:100%}
img{height:auto}
/* Long words / URLs in article bodies must wrap instead of overflowing narrow screens */
.post{overflow-wrap:break-word}
.post a{overflow-wrap:anywhere}
.crumbs{overflow-wrap:break-word}
/* Pagination links may wrap on small screens instead of clipping */
.pagination{flex-wrap:wrap}
/* Keep the header on one line a little longer on small tablets */
@media(max-width:900px){.main-nav a{padding:8px 11px;font-size:14px}.logo-text{font-size:15px}}
/* Article hero: stack title + number on mobile */
@media(max-width:760px){.post-hero{flex-direction:column;align-items:flex-start;gap:6px;padding:26px 20px}.post-hero-num{font-size:36px;line-height:1}}
/* Small phones: smaller headings, single-column trust grid, full-width newsletter form */
@media(max-width:520px){.section h2{font-size:24px}.post h1{font-size:26px}.post h2{font-size:21px}.trust-grid{grid-template-columns:1fr}.newsletter{padding:24px 18px}.newsletter input{min-width:0;width:100%}.newsletter form{flex-direction:column}.newsletter .btn{width:100%}}
"""

JS = r"""
// Solved Sindh Textbook Board Books — search, filters, FAQ, detail modal
// NOTE: website is English-only. No language switcher, no RTL: the whole
// document always stays LTR so English content is always left-sided.
document.addEventListener('DOMContentLoaded', ()=>{
  const navBtn = document.getElementById('nav-toggle');
  const nav = document.getElementById('main-nav');
  if(navBtn && nav){ navBtn.addEventListener('click', ()=>{ nav.classList.toggle('open'); navBtn.setAttribute('aria-expanded', nav.classList.contains('open')); }); }
  // Catalogue render
  const grid = document.getElementById('books-grid');
  if(grid){ renderBooks(); ['q','f-class','f-medium','f-subject','f-status'].forEach(id=>{ const el=document.getElementById(id); if(el) el.addEventListener('input', renderBooks); }); }
  const blogSearch = document.getElementById('blog-search');
  if(blogSearch){ const cat=document.getElementById('blog-cat'); const fn=()=>{ const q=blogSearch.value.toLowerCase(); const c=cat?cat.value:''; document.querySelectorAll('#blog-grid .blog-card').forEach(card=>{ const txt=card.textContent.toLowerCase(); const okQ=!q||txt.includes(q); const okC=!c||txt.includes(c.toLowerCase()); card.style.display=(okQ&&okC)?'':'none'; }); }; blogSearch.addEventListener('input',fn); if(cat) cat.addEventListener('change',fn); }
  // Featured class-filter pills (index featured grid + solved page)
  document.querySelectorAll('.feat-pills').forEach(pills=>{
    pills.addEventListener('click', e=>{
      const btn = e.target.closest('.feat-pill'); if(!btn) return;
      pills.querySelectorAll('.feat-pill').forEach(p=>p.classList.remove('active'));
      btn.classList.add('active');
      const grid = document.getElementById(pills.dataset.grid); if(!grid) return;
      const f = btn.dataset.filter;
      grid.querySelectorAll('.card').forEach(card=>{ card.style.display = (f==='all' || card.dataset.class===f) ? '' : 'none'; });
    });
  });
  // Hero search -> books page
  const heroForm = document.getElementById('hero-search-form');
  if(heroForm){ heroForm.addEventListener('submit', e=>{ e.preventDefault(); const q=document.getElementById('hero-search').value; window.location.href='/books.html?q='+encodeURIComponent(q); }); }
  // Newsletter (no backend — mailto fallback + success message)
  document.querySelectorAll('.newsletter form').forEach(f=>f.addEventListener('submit', e=>{ e.preventDefault(); const msg=f.parentElement.querySelector('.nl-msg'); if(msg){ msg.textContent='Thanks! You are on the list. New solved notes will be shared here first.'; } f.reset(); }));
});
let BOOKS = [];
async function loadBooks(){
  if(BOOKS.length) return BOOKS;
  try{ const r = await fetch('/assets/data/books.json'); BOOKS = await r.json(); }catch(e){ BOOKS = []; }
  return BOOKS;
}
function subjSlug(subject){
  const map = {'Sindhi':'sindhi','Urdu':'urdu','English':'english','Arabic':'arabic','Math':'math','Science':'science','Social Studies':'social-studies','Islamiat':'islamiat','Mazhabi Taleemat':'mazhabi-taleemat','Computer':'computer','Physics':'physics','Chemistry':'chemistry','Biology':'biology','Pakistan Studies':'pakistan-studies','Mathematics':'math'};
  return map[subject] || 'science';
}
function subjectCover(b){
  if(b.cover) return b.cover;
  return 'assets/images/covers/subjects/' + subjSlug(b.subject) + '.svg';
}
const BOOK_IC = '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2 4h6a4 4 0 0 1 4 4v12a3 3 0 0 0-3-3H2z"/><path d="M22 4h-6a4 4 0 0 0-4 4v12a3 3 0 0 1 3-3h7z"/></svg>';
function cardHTML(b){
  const live = b.status==='live';
  const slug = subjSlug(b.subject);
  const cover = subjectCover(b);
  const badge = live ? '<span class="live-badge"><i></i>Live Preview</span>' : '<span class="live-badge soon"><i></i>Coming Soon</span>';
  const btn = live ? `<a class="btn-open" href="/preview.html?id=${b.id}">${BOOK_IC} Open &rarr;</a>` : `<button class="btn-open" onclick="openBook('${b.id}')">Notify me</button>`;
  const coverEl = live
    ? `<div class="book-stage"><div class="book3d"><div class="book3d-back"></div><div class="book3d-spine"></div><img class="book3d-front" src="/${cover}" alt="${b.title} — official book cover" loading="lazy"><div class="book3d-pages"></div><div class="book3d-shade"></div></div>${badge}</div>`
    : `<div class="card-cover"><img src="/${cover}" alt="${b.title} — illustrated cover" loading="lazy">${badge}</div>`;
  return `<article class="card" data-id="${b.id}" data-class="${b.cls}">${coverEl}<div class="card-body"><span class="subj-tag ${slug}">${BOOK_IC} ${b.subject}</span><h3>${b.title}</h3><p class="card-meta"><span class="chip">Class ${b.cls}</span> <span class="chip">${b.subject}</span> <span class="chip">${b.medium} Medium</span></p><p class="card-desc">${b.desc}</p><div class="actions">${btn}</div></div></article>`;
}
async function renderBooks(){
  const grid = document.getElementById('books-grid'); if(!grid) return;
  const books = await loadBooks();
  const params = new URLSearchParams(location.search);
  const q = (document.getElementById('q')?.value || params.get('q') || '').toLowerCase();
  const qc = document.getElementById('q'); if(qc && !qc.value && q) qc.value = q;
  const fcEl = document.getElementById('f-class'); if(fcEl && !fcEl.value && params.get('f-class')) fcEl.value = params.get('f-class');
  const fmEl = document.getElementById('f-medium'); if(fmEl && !fmEl.value && params.get('f-medium')) fmEl.value = params.get('f-medium');
  const fsEl = document.getElementById('f-subject'); if(fsEl && !fsEl.value && params.get('f-subject')) fsEl.value = params.get('f-subject');
  const fc = fcEl?.value || '';
  const fm = fmEl?.value || '';
  const fs = fsEl?.value || '';
  const fst = document.getElementById('f-status')?.value || '';
  const filtered = books.filter(b=>{
    if(fc && String(b.cls)!==fc) return false;
    if(fm && b.medium!==fm) return false;
    if(fs && b.subject!==fs) return false;
    if(fst && b.status!==fst) return false;
    if(q && !(b.title+' '+b.subject+' '+b.medium+' Class '+b.cls).toLowerCase().includes(q)) return false;
    return true;
  });
  const count = document.getElementById('books-count'); if(count) count.textContent = filtered.length + ' solved notes found';
  grid.innerHTML = filtered.length ? filtered.map(cardHTML).join('') : '<p>No solved notes match your filters. Try clearing the search or choose another class/medium.</p>';
}
async function openBook(id){
  const books = await loadBooks();
  const b = books.find(x=>x.id===id); if(!b) return;
  const modal = document.getElementById('book-modal'); const body = document.getElementById('modal-body');
  const chapters = (b.chapters||[]).length ? '<h3>Chapters covered</h3><ul>'+b.chapters.map(c=>'<li>'+c+'</li>').join('')+'</ul>' : '<p>This book is being prepared. Join the list below and we will share it as soon as it is ready.</p>';
  const dl = b.pdf ? `<p><a class="btn" href="/preview.html?id=${b.id}"><svg class="ic" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg> Open Preview</a></p>` : '<p><a class="btn outline" href="/contact.html">Request this book</a></p>';
  const coverImg = b.cover ? `<div class="book-stage modal-book"><div class="book3d"><div class="book3d-back"></div><div class="book3d-spine"></div><img class="book3d-front" src="/${b.cover}" alt="${b.title} — official book cover"><div class="book3d-pages"></div><div class="book3d-shade"></div></div></div>` : '';
  body.innerHTML = `${coverImg}<h2>${b.title}</h2><p><span class="chip">Class ${b.cls}</span> <span class="chip">${b.subject}</span> <span class="chip">${b.medium} Medium</span> ${b.status==='live'?'<span class="chip live">Live</span>':'<span class="chip soon">Coming Soon</span>'}</p><p>${b.desc}</p>${chapters}${dl}<p><a href="/books.html">← Back to solved notes</a></p>`;
  modal.classList.add('open');
}
function closeModal(){ document.getElementById('book-modal')?.classList.remove('open'); }
document.addEventListener('click', e=>{ if(e.target && e.target.id==='book-modal') closeModal(); });
document.addEventListener('keydown', e=>{ if(e.key==='Escape') closeModal(); });
"""


# ---------------- Templates ----------------
def head(title, desc, path, keywords="", extra=""):
    return f"""<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{BASE}{path}">
<meta name="robots" content="index, follow">
{f'<meta name="keywords" content="{keywords}">' if keywords else ''}
<meta property="og:type" content="website"><meta property="og:site_name" content="Solved Sindh Textbook Board Books">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<meta property="og:url" content="{BASE}{path}"><meta property="og:image" content="{BASE}/assets/images/og.svg">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{title}"><meta name="twitter:description" content="{desc}"><meta name="twitter:image" content="{BASE}/assets/images/og.svg">
<link rel="icon" type="image/svg+xml" href="/favicon.svg"><link rel="manifest" href="/manifest.webmanifest">
<meta name="theme-color" content="#0B6B4A"><link rel="stylesheet" href="/assets/css/style.css?v=4">
{extra}</head>
<body>
<a class="skip-link" href="#main">Skip to main content</a>
"""

def header(active=""):
    def a(href, label):
        return f'<a href="{href}" class="{"active" if href==active else ""}">{label}</a>'
    return f"""<header class="site-header"><div class="container header-inner">
<a class="logo" href="/"><span class="logo-mark">S</span><span class="logo-text">Solved Sindh Textbook Board Books</span></a>
<button class="nav-toggle" id="nav-toggle" aria-label="Toggle menu" aria-expanded="false">☰</button>
<nav class="main-nav" id="main-nav" aria-label="Main navigation">
{a('/', 'Home')}{a('/books.html', 'Solved Books')}{a('/blog/', 'Blog')}{a('/about.html', 'About')}{a('/contact.html', 'Contact')}
</nav></div></header>
"""

FOOTER = """<footer class="site-footer"><div class="container footer-grid">
<div><a class="logo" href="/"><span class="logo-mark">S</span> Solved Sindh Textbook Board Books</a><p>Preview solved Sindh Textbook Board books and exercises free on this website — Sindhi, Urdu and English medium. Prepared by teachers, for students.</p></div>
<div><h3>Explore</h3><ul><li><a href="/books.html">Solved Books</a></li><li><a href="/blog/">Blog</a></li><li><a href="/about.html">About</a></li></ul></div>
<div><h3>Help</h3><ul><li><a href="/contact.html">Contact</a></li><li><a href="/privacy.html">Privacy Policy</a></li><li><a href="/terms.html">Terms</a></li></ul></div>
</div><p class="copyright">© 2026 Solved Sindh Textbook Board Books. Preview free on this website. Textbooks are the property of the Sindh Textbook Board.</p></footer>
<script src="/assets/js/main.js"></script>
</body></html>"""

MODAL = """<div class="modal-backdrop" id="book-modal" role="dialog" aria-modal="true" aria-label="Book details"><div class="modal"><button class="close" onclick="closeModal()" aria-label="Close">×</button><div id="modal-body"></div></div></div>"""

ORG_LD = json.dumps({"@context":"https://schema.org","@type":"Organization","name":"Solved Sindh Textbook Board Books","url":BASE,"logo":BASE+"/assets/images/og.svg","description":"Free solved Sindh Textbook Board books and exercises for Sindh Board students in Sindhi, Urdu and English medium."}, ensure_ascii=False)
SITE_LD = json.dumps({"@context":"https://schema.org","@type":"WebSite","name":"Solved Sindh Textbook Board Books","url":BASE,"inLanguage":["en","sd","ur"],"publisher":{"@type":"Organization","name":"Solved Sindh Textbook Board Books"},"potentialAction":{"@type":"SearchAction","target":BASE+"/books.html?q={search_term_string}","query-input":"required name=search_term_string"}}, ensure_ascii=False)

BOOK_ICON = '<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2 4h6a4 4 0 0 1 4 4v12a3 3 0 0 0-3-3H2z"/><path d="M22 4h-6a4 4 0 0 0-4 4v12a3 3 0 0 1 3-3h7z"/></svg>'
HERO_ART = '<svg viewBox="0 0 520 420" width="460" height="372" role="img" aria-label="Stack of Sindh Textbook Board books">\n<path d="M448 36l4 12 12 4-12 4-4 12-4-12-12-4 12-4z" fill="#FDE047"/>\n<path d="M52 52l3 9 9 3-9 3-3 9-3-9-9-3 9-3z" fill="#ffffff" opacity="0.85"/>\n<path d="M492 250l3 8 8 3-8 3-3 8-3-8-8-3 8-3z" fill="#FDE047" opacity="0.9"/>\n<g transform="translate(396,52) rotate(12)">\n<polygon points="0,16 48,0 96,16 48,32" fill="#0B6B4A" stroke="#ffffff" stroke-width="2"/>\n<polygon points="24,28 24,52 48,62 72,52 72,28 48,38" fill="#065F46"/>\n<line x1="72" y1="28" x2="72" y2="62" stroke="#FDE047" stroke-width="2"/><circle cx="72" cy="66" r="4" fill="#FDE047"/>\n</g>\n<text x="398" y="146" font-family="cursive" font-size="30" fill="#FDE047" text-anchor="middle" transform="rotate(4 398 146)">Learn</text>\n<text x="400" y="178" font-family="cursive" font-size="30" fill="#ffffff" text-anchor="middle" transform="rotate(4 400 178)">Grow</text>\n<text x="402" y="210" font-family="cursive" font-size="30" fill="#FDE047" text-anchor="middle" transform="rotate(4 402 210)">Succeed</text>\n<g transform="rotate(-8 150 300)">\n<rect x="58" y="122" width="54" height="238" rx="6" fill="#2563EB"/>\n<rect x="116" y="112" width="54" height="248" rx="6" fill="#F59E0B"/>\n<rect x="174" y="120" width="54" height="240" rx="6" fill="#0E7490"/>\n</g>\n<g transform="rotate(3 330 250)">\n<ellipse cx="330" cy="370" rx="152" ry="12" fill="#000000" opacity="0.18"/>\n<rect x="212" y="96" width="236" height="272" rx="10" fill="#FFF8E7" stroke="#E8A020" stroke-width="3"/>\n<rect x="212" y="96" width="26" height="272" rx="6" fill="#0E8A5F"/>\n<circle cx="330" cy="160" r="34" fill="#ffffff" stroke="#0B6B4A" stroke-width="2.5"/>\n<circle cx="330" cy="160" r="26" fill="none" stroke="#0B6B4A" stroke-width="1.5"/>\n<path d="M338 142a20 20 0 1 0 12 22 15 15 0 1 1-12-22z" fill="#0B6B4A"/>\n<path d="M348 138l1.6 4 4 1.6-4 1.6-1.6 4-1.6-4-4-1.6 4-1.6z" fill="#0B6B4A"/>\n<text x="330" y="228" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#0B6B4A" text-anchor="middle">Sindh Textbook Board</text>\n<text x="330" y="280" font-family="Arial, sans-serif" font-size="44" font-weight="bold" fill="#1F2937" text-anchor="middle">سنده</text>\n<text x="330" y="320" font-family="Arial, sans-serif" font-size="24" fill="#4B5563" text-anchor="middle">کتاب نصاب</text>\n</g>\n<g transform="translate(26,302)"><path d="M0 20c14-8 28-10 44-8v34c-16-2-30 0-44 8z" fill="#ffffff"/><path d="M44 12c16-2 30 0 44 8v34c-14-8-28-10-44-8z" fill="#FDE047"/></g>\n</svg>'
PDF_BANNER = ''
PILLS = '<div class="feat-pills" data-grid="{grid}"><button class="feat-pill active" data-filter="all">All</button><button class="feat-pill" data-filter="6">Class 6</button><button class="feat-pill" data-filter="7">Class 7</button><button class="feat-pill" data-filter="8">Class 8</button><button class="feat-pill" data-filter="9">Class 9</button><button class="feat-pill" data-filter="10">Class 10</button></div>'

def featured_cards(limit=None):
    out = ""
    for b in (REAL[:limit] if limit else REAL):
        slug = SUBJ_SLUG[b['subject']]
        out += f"""<article class="card" data-class="{b['cls']}"><div class="book-stage"><div class="book3d"><div class="book3d-back"></div><div class="book3d-spine"></div><img class="book3d-front" src="/{b['cover']}" alt="{b['title']} — official book cover" loading="lazy"><div class="book3d-pages"></div><div class="book3d-shade"></div></div><span class="live-badge"><i></i>Live Preview</span></div><div class="card-body"><span class="subj-tag {slug}">{BOOK_ICON} {b['subject']}</span><h3>{b['title']}</h3><p class="card-meta"><span class="chip">Class {b['cls']}</span> <span class="chip">{b['subject']}</span> <span class="chip">{b['medium']} Medium</span></p><p class="card-desc">{b['desc']}</p><div class="actions"><a class="btn-open" href="/preview.html?id={b['id']}">{BOOK_ICON} Open &rarr;</a></div></div></article>\n"""
    return out

# ---------------- Pages ----------------
def build():
    os.makedirs(os.path.join(SITE, "assets/data"), exist_ok=True)
    with open(os.path.join(SITE, "assets/data/books.json"), "w", encoding="utf-8") as f:
        json.dump(BOOKS, f, ensure_ascii=False, indent=2)
    w("assets/css/style.css", CSS.strip() + "\n")
    w("assets/js/main.js", JS.strip() + "\n")

    # INDEX
    faq_ld = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
        {"@type":"Question","name":"Are the solved notes really free?","acceptedAnswer":{"@type":"Answer","text":"Yes — completely free. Every solved note is free to read on this website. No download needed, no payment, no sign-up. Just open a book and start reading — come back any time to revise."}},
        {"@type":"Question","name":"Which mediums are available?","acceptedAnswer":{"@type":"Answer","text":"Solved notes are available in Sindhi, Urdu, English and Arabic medium for Classes 6–10 — 119 books are live now."}},
        {"@type":"Question","name":"Do the solved notes follow the Sindh Textbook Board textbook?","acceptedAnswer":{"@type":"Answer","text":"Yes. Every solved exercise follows the official Sindh Textbook Board textbook chapter by chapter, in the book's own format."}},
        {"@type":"Question","name":"Can I request a book that is not listed?","acceptedAnswer":{"@type":"Answer","text":"Yes. Use the contact page to request any Sindh Textbook Board class, subject or medium. Requested books are prepared first."}},
    ]}
    index = head("Solved Sindh Textbook Board Books — Solved Exercises Sindhi, Urdu & English Medium, Free Preview | Sindh Board",
        "Preview solved Sindh Textbook Board books & exercises free on this website. 119 solved books live for Classes 6–10 in Sindhi, Urdu, English & Arabic medium. Free to read, no sign-up.",
        "/", "Sindh Textbook Board solved books, Sindh Textbook Board solved exercises, Class 9 Islamiat solved Sindhi",
        f'<script type="application/ld+json">{ORG_LD}</script><script type="application/ld+json">{SITE_LD}</script><script type="application/ld+json">{json.dumps(faq_ld, ensure_ascii=False)}</script>')
    index += header("/") + f"""
<main id="main">
<section class="hero"><div class="container">
<div class="hero-copy">
<span class="hero-badge">★ Free Preview · Sindh Textbook Board</span>
<h1>Free Solved Sindh<br>Textbook Board Books<br><span class="hero-yellow">Sindhi, Urdu &amp; English Medium</span></h1>
<p class="hero-lead">Preview solved exercises for Sindh Textbook Board books. Classes 6–10 solved notes are live now — free to read on this website, any time.</p>
<form class="hero-search" id="hero-search-form" role="search"><svg class="search-ic" width="19" height="19" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><line x1="21" y1="21" x2="16.5" y2="16.5"/></svg><label class="sr-only" for="hero-search" style="position:absolute;left:-9999px">Search books</label><input type="search" id="hero-search" placeholder="Search by class, subject or medium… e.g. Class 9 Islamiat Sindhi"><button class="btn" type="submit">Search</button></form>
<div class="hero-cta"><a class="btn btn-white" href="/books.html">Browse Solved Books</a> <a class="btn amber" href="/books.html">Solved Books</a></div>
</div>
</div></section>
<section class="trust-bar"><div class="container trust-grid">
<div class="trust-item"><span class="trust-ic"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><rect x="4" y="11" width="16" height="9" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/></svg></span><div><b>100% Free Preview</b><small>Free to read on this site</small></div></div>
<div class="trust-item"><span class="trust-ic"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 4h6a4 4 0 0 1 4 4v12a3 3 0 0 0-3-3H2z"/><path d="M22 4h-6a4 4 0 0 0-4 4v12a3 3 0 0 1 3-3h7z"/></svg></span><div><b>All Classes &amp; Subjects</b><small>Classes 6–10 (Sindh Textbook Board)</small></div></div>
<div class="trust-item"><span class="trust-ic"><svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor"><path d="M13 2 4 14h6l-1 8 9-12h-6z"/></svg></span><div><b>Fast &amp; Easy Access</b><small>No registration needed</small></div></div>
<div class="trust-item"><span class="trust-ic"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2 4 5v6c0 5 3.4 9.4 8 11 4.6-1.6 8-6 8-11V5z"/><path d="m9 12 2 2 4-4"/></svg></span><div><b>Trusted &amp; Official</b><small>Sindh Textbook Board</small></div></div>
</div></section>
<section class="section container"><div class="feat-head"><div><h2>Featured solved notes — free preview</h2><p class="sub">Real solved exercises, prepared from the Sindh Textbook Board textbook. Click Open to preview free on this website.</p></div>{PILLS.format(grid="featured-grid")}</div><div class="grid featured-grid" id="featured-grid">{featured_cards()}</div>{PDF_BANNER}</section>
<section class="section container"><h2>How it works</h2><div class="steps-grid">
<div class="step"><div class="num">1</div><h3>Find your book</h3><p>Search by class, subject or medium — or browse the catalogue.</p></div>
<div class="step"><div class="num">2</div><h3>Preview free</h3><p>Open the preview on this website. Free to read — come back any time to revise.</p></div>
<div class="step"><div class="num">3</div><h3>Learn &amp; write</h3><p>Study the solved answers, then write them from memory. That is how marks are made.</p></div></div></section>
<section class="section container"><h2>Browse by subject</h2><div class="subject-strip">
<a href="/books.html?f-subject=Islamiat">Islamiat</a><a href="/books.html?f-subject=Urdu">Urdu</a><a href="/books.html?f-subject=Sindhi">Sindhi</a><a href="/books.html?f-subject=English">English</a><a href="/books.html?f-subject=Math">Math</a><a href="/books.html?f-subject=Science">Science</a><a href="/books.html?f-subject=Physics">Physics</a><a href="/books.html?f-subject=Chemistry">Chemistry</a><a href="/books.html?f-subject=Biology">Biology</a><a href="/books.html?f-subject=Pakistan Studies">Pakistan Studies</a><a href="/books.html?f-subject=Social Studies">Social Studies</a><a href="/books.html?f-subject=Arabic">Arabic</a><a href="/books.html?f-subject=Computer">Computer</a><a href="/books.html?f-subject=Mazhabi Taleemat">Mazhabi Taleemat</a></div></section>
<section class="section container"><h2>Why students love it</h2><div class="steps-grid">
<div class="step"><h3>📖 Follows the textbook</h3><p>Every answer follows the Sindh Textbook Board book chapter by chapter — nothing extra, nothing missing.</p></div>
<div class="step"><h3>✍️ Exam-ready answers</h3><p>Answers are written the way examiners want: translation, explanation, example.</p></div>
<div class="step"><h3>🌍 Four mediums</h3><p>Sindhi, Urdu, English and Arabic — study in the medium you write your exam in.</p></div>
<div class="step"><h3>📱 Works on any phone</h3><p>Fast, mobile-first pages and PDFs that open on any phone.</p></div></div></section>
<section class="section container"><h2>What students say</h2><div class="testimonials">
<div class="testi"><p>“Class 9 Islamiat ke solved notes ne meri tayyari aasan kar di. Har jawab kitab ke mutabiq hai.”</p><b>— Class 9 Student, Hyderabad</b></div>
<div class="testi"><p>“Sindhi medium notes milna mushkil tha. Yahan sab kuch free aur saaf likha hua mila.”</p><b>— Class 8 Student, Larkana</b></div>
<div class="testi"><p>“Main apni class ko isi se parhata hoon. Solved exercises ka format board ke liye behtareen hai.”</p><b>— School Teacher, Sukkur</b></div></div></section>
<section class="section container"><h2>Frequently asked questions</h2><div class="faq">
<details open><summary>Are the solved notes really free?</summary><p>Yes — completely free. Every solved note is free to read on this website. No download needed, no payment, no sign-up. Just open a book and start reading — come back any time to revise.</p></details>
<details><summary>Which mediums are available?</summary><p>Sindhi, Urdu, English and Arabic. 119 solved books for Classes 6–10 are live now.</p></details>
<details><summary>Do the solved notes follow the Sindh Textbook Board textbook?</summary><p>Yes. Every solved exercise follows the official Sindh Textbook Board textbook chapter by chapter.</p></details>
<details><summary>Can I request a book that is not listed?</summary><p>Yes — use the <a href="/contact.html">contact page</a>. Requested books are prepared first.</p></details>
</div></section>
<section class="section container"><div class="newsletter"><h2>Get new solved notes first</h2><p>One email when a new book is added. No spam, unsubscribe anytime.</p><form><label class="sr-only" for="nl-email" style="position:absolute;left:-9999px">Email</label><input id="nl-email" type="email" required placeholder="Your email address"><button class="btn amber" type="submit">Join free</button></form><p class="nl-msg"></p><p>Or join on WhatsApp: <a href="https://wa.me/923018981055" style="color:#fff">+92 301 8981055</a></p></div></section>
</main>
""" + MODAL + FOOTER
    w("index.html", index)

    # BOOKS
    books_page = head("Solved Books — Sindh Textbook Board Solved Exercises by Class, Subject & Medium | Solved Sindh Textbook Board Books",
        "Browse all Sindh Textbook Board solved notes by class, subject and medium (Sindhi, Urdu, English, Arabic). Free to read on this website, live search and filters.",
        "/books.html", "Sindh Textbook Board books catalogue, solved exercises by class, Sindh Board books")
    books_page += header("/books.html") + """
<main id="main" class="container"><h1>Solved Books — Sindh Textbook Board Solved Exercises</h1>
<p class="lead">Search and filter the full catalogue. All live notes are free to read on this website. Coming-soon notes can be requested.</p>
<div class="filters">
<label>Search <input type="search" id="q" placeholder="e.g. Class 9 Islamiat Sindhi"></label>
<label>Class <select id="f-class"><option value="">All classes</option><option>1</option><option>2</option><option>3</option><option>4</option><option>5</option><option>6</option><option>7</option><option>8</option><option>9</option><option>10</option><option>11</option><option>12</option></select></label>
<label>Medium <select id="f-medium"><option value="">All mediums</option><option>Sindhi</option><option>Urdu</option><option>English</option><option>Arabic</option></select></label>
<label>Subject <select id="f-subject"><option value="">All subjects</option><option>Islamiat</option><option>Urdu</option><option>Sindhi</option><option>English</option><option>Math</option><option>Science</option><option>Social Studies</option><option>Physics</option><option>Chemistry</option><option>Biology</option><option>Pakistan Studies</option><option>Mathematics</option><option>Computer</option><option>Arabic</option><option>Mazhabi Taleemat</option></select></label>
<label>Status <select id="f-status"><option value="">All</option><option value="live">Live — Free to Read</option><option value="coming-soon">Coming Soon</option></select></label>
</div><p id="books-count"></p><div class="grid" id="books-grid"><p>Loading books…</p></div>
<p class="notice">Tip: click <strong>Open</strong> on any card to preview it free on this website. Cannot find your book? <a href="/contact.html">Request it here</a>.</p>
</main>
""" + MODAL + FOOTER
    w("books.html", books_page)


    # ABOUT / CONTACT / LEGAL
    about = head("About — Solved Sindh Textbook Board Books", "About Solved Sindh Textbook Board Books: free solved Sindh Textbook Board exercises for Sindh Board students in Sindhi, Urdu and English medium, prepared by teachers.", "/about.html")
    about += header("/about.html") + """<main id="main" class="container"><h1>About Solved Sindh Textbook Board Books</h1><p class="lead">We are teachers from Sindh. We saw students struggling to find solved exercises in their own medium — especially Sindhi medium — so we started preparing them, chapter by chapter, from the official Sindh Textbook Board textbooks.</p><h2>What we do</h2><ul><li>Solve every exercise from the Sindh Textbook Board textbook in the book's own format.</li><li>Write answers the way board examiners want: translation, explanation, example.</li><li>Publish everything free to read on this website.</li></ul><h2>What we do not do</h2><p>We do not replace the textbook. Solved notes are for learning and revision — always study with your Sindh Textbook Board book open. Textbooks are the property of the Sindh Textbook Board; solved notes here are original explanations of those exercises.</p><p><a class="btn" href="/books.html">Browse solved notes →</a></p></main>""" + FOOTER
    w("about.html", about)
    contact = head("Contact — Request a Book | Solved Sindh Textbook Board Books", "Contact Solved Sindh Textbook Board Books to request a solved book, report an error, or suggest a new guide.", "/contact.html")
    contact += header("/contact.html") + """<main id="main" class="container"><h1>Contact &amp; Request a Book</h1><p class="lead">Tell us which book you need — class, subject and medium — and we will prepare it first.</p><div class="form-box"><form action="mailto:hello@stbbsolved.pk" method="post" enctype="text/plain"><label>Your name <input name="name" required></label><label>Email <input name="email" type="email" required></label><label>Request <select name="type"><option>Request a solved book</option><option>Report an error</option><option>Suggest a guide</option><option>Other</option></select></label><label>Class <input name="class" placeholder="e.g. Class 10"></label><label>Subject &amp; Medium <input name="subject" placeholder="e.g. Physics, English medium"></label><label>Message <textarea name="message" rows="5" required placeholder="Which book do you need?"></textarea></label><button class="btn" type="submit">Send request</button></form></div><p>WhatsApp: <a href="https://wa.me/923018981055">+92 301 8981055</a></p></main>""" + FOOTER
    w("contact.html", contact)
    privacy = head("Privacy Policy | Solved Sindh Textbook Board Books", "Privacy policy for Solved Sindh Textbook Board Books. No accounts, no tracking beyond basic analytics.", "/privacy.html")
    privacy += header("") + """<main id="main" class="container"><h1>Privacy Policy</h1><p>This site does not require accounts. We do not sell personal data. If you email us, we use your message only to reply. Preview uses the on-page viewer. No personal data is needed to read.</p><p>Basic anonymous visit counts may be used to see which books students need most. No advertising profiles are built from this site.</p></main>""" + FOOTER
    w("privacy.html", privacy)
    terms = head("Terms | Solved Sindh Textbook Board Books", "Terms of use for Solved Sindh Textbook Board Books. Free solved notes for study; always verify against your Sindh Textbook Board textbook.", "/terms.html")
    terms += header("") + """<main id="main" class="container"><h1>Terms of Use</h1><p>Solved notes are free to read on this website for study and revision. Always verify answers against your official Sindh Textbook Board textbook and your teacher. We aim for accuracy but accept no liability for exam outcomes. Textbooks remain the property of the Sindh Textbook Board.</p></main>""" + FOOTER
    w("terms.html", terms)

    # PREVIEW — PDF viewer page. View-only: no download, no purchase.
    preview = head("Preview Solved PDF | Solved Sindh Textbook Board Books",
        "Preview a solved Sindh Textbook Board PDF free on this website. Free to read, no download needed.",
        "/preview.html", "preview solved PDF, Sindh Textbook Board solved notes preview")
    preview += header("") + """<main id="main" class="container">
<p id="preview-loading">Loading book…</p>
<div id="preview-content" style="display:none">
<h1 id="preview-title"></h1>
<div class="preview-meta" id="preview-chips"></div>
<p class="lead" id="preview-desc"></p>
<p>Free to read on this website. No download needed — just read it here, any time.</p>
<div oncontextmenu="return false"><iframe id="pdf-frame" class="pdf-frame" title="Solved PDF preview" src=""></iframe></div>
<p style="margin-top:18px"><a class="btn outline" href="/books.html">← Back to solved notes</a></p>
</div>
<div id="preview-notfound" style="display:none"><h1>Book not found</h1><p>This book is not live yet. Browse the catalogue or request it on the contact page.</p><p><a class="btn" href="/books.html">Browse solved notes →</a> <a class="btn outline" href="/contact.html">Request this book</a></p></div>
</main>

<script>
async function initPreview(){
  const id = new URLSearchParams(location.search).get('id');
  let books = [];
  try{ books = await (await fetch('/assets/data/books.json')).json(); }catch(e){}
  const b = books.find(x=>x.id===id);
  document.getElementById('preview-loading').style.display = 'none';
  if(!b || !b.pdf){
    document.getElementById('preview-notfound').style.display = 'block';
    return;
  }
  document.getElementById('preview-content').style.display = 'block';
  document.getElementById('preview-title').textContent = b.title;
  document.title = 'Preview — ' + b.title + ' | Solved Sindh Textbook Board Books';
  document.getElementById('preview-chips').innerHTML = '<span class="chip">Class ' + b.cls + '</span> <span class="chip">' + b.subject + '</span> <span class="chip">' + b.medium + ' Medium</span> <span class="chip live">Preview Free</span>';
  document.getElementById('preview-desc').textContent = b.desc || '';
  document.getElementById('pdf-frame').src = '/' + b.pdf + '#toolbar=0&navpanes=0&scrollbar=0';
}
document.addEventListener('DOMContentLoaded', initPreview);
</script>
""" + FOOTER
    w("preview.html", preview)

    # SEO files
    import sys
    sys.path.insert(0, SITE)
    from build_blog import POSTS
    urls = ["", "/books.html", "/about.html", "/contact.html", "/privacy.html", "/terms.html", "/preview.html", "/blog/"]
    urls += [f"/blog/{p['slug']}.html" for p in POSTS]
    import math as _math
    _total_pages = max(1, _math.ceil(len(POSTS) / 30))
    urls += [f"/blog/page-{n}.html" for n in range(2, _total_pages + 1)]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for u in urls:
        sm += f'  <url><loc>{BASE}{u if u else "/"}</loc><lastmod>{TODAY}</lastmod></url>\n'
    sm += "</urlset>\n"
    w("sitemap.xml", sm)
    w("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n")
    w("manifest.webmanifest", json.dumps({"name":"Solved Sindh Textbook Board Books","short_name":"Sindh Textbook Board Solved","start_url":"/","display":"standalone","background_color":"#ffffff","theme_color":"#0B6B4A","icons":[{"src":"/favicon.svg","sizes":"512x512","type":"image/svg+xml"}]}, indent=2))
    w("favicon.svg", '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#0B6B4A"/><text x="32" y="44" font-family="Arial" font-size="34" font-weight="bold" fill="#fff" text-anchor="middle">S</text></svg>\n')
    w("assets/images/og.svg", '<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630"><rect width="1200" height="630" fill="#0B6B4A"/><text x="60" y="200" font-family="Arial" font-size="64" font-weight="bold" fill="#fff">Solved Sindh Textbook Board Books</text><text x="60" y="280" font-family="Arial" font-size="32" fill="#DCE8E0">Preview solved exercises free — Sindhi · Urdu · English</text><text x="60" y="340" font-family="Arial" font-size="28" fill="#fff">119 solved books live — Classes 6–10</text></svg>\n')
    # README
    readme = f"""# Solved Sindh Textbook Board Books — Static Website

Free solved Sindh Textbook Board books & exercises for Sindh Board students (Sindhi, Urdu, English medium).
Pure static HTML/CSS/JS — no backend, no build step. Deploy anywhere (Vercel, GitHub Pages, Netlify).

## Live content
- **119 solved-notes PDFs live**: Classes 6–10 × all subjects × Sindhi / Urdu / English / Arabic (in `assets/pdfs/`).
- **{len(BOOKS)} catalogue entries** in `assets/data/books.json` (119 live + rest coming-soon).
- **{len(POSTS)} SEO blog posts** in `blog/` (generated by `build_blog.py`; daily engine in `gen/`).

## Preview locally
```bash
cd stbb-solved-website
python3 -m http.server 8000
# open http://localhost:8000
```

## Add a new book
1. Drop the PDF into `assets/pdfs/` (e.g. `Class10-Physics-SolvedExercises-English.pdf`).
2. Edit `assets/data/books.json` — copy a live entry, set `status: "live"`, `pdf: "assets/pdfs/<file>.pdf"`, `pages`, `desc`, `chapters`.
3. Or: add the entry to `BOOKS` in `build_site.py` and re-run `python3 build_site.py`.
4. The book appears automatically on Home and Solved Books pages (JS renders from books.json).

## Add a blog post
Daily engine (15/day, from 2026-10-16): write a `gen/batch_XXX.py` batch file, run `python3 gen/build_batch.py batch_XXX BATCH_XXX` (validates, appends to `gen/extra_posts.json`, rebuilds blog + sitemap), then `python3 gen/push_batch.py "Day N" <files>` to push.
Manual single post: append a dict to `POSTS` in `build_blog.py` (slug, title, cat, desc, kw, intro, points).
2. Run `python3 build_blog.py` — it regenerates `blog/*.html`, `blog/index.html`, `blog/page-N.html`.
3. Run `python3 build_site.py` to refresh `sitemap.xml`.

## Deploy to Vercel
1. Push this folder to a GitHub repo (e.g. `stbb-solved-website`).
2. Vercel → New Project → import repo → Framework: **Other** → Deploy. No build command needed.
3. After deploy, replace `{BASE}` with your real domain in `build_site.py` / `build_blog.py`, re-run both scripts, and re-deploy.
4. Submit `https://YOUR-DOMAIN/sitemap.xml` in Google Search Console.

## Files
- `index.html`, `books.html`, `about.html`, `contact.html`, `privacy.html`, `terms.html`
- `blog/` — 50 posts + index + page-2
- `assets/css/style.css`, `assets/js/main.js`, `assets/data/books.json`, `assets/pdfs/`
- `sitemap.xml`, `robots.txt`, `manifest.webmanifest`, `favicon.svg`
- `build_site.py`, `build_blog.py` — generators (source of truth for pages/blogs)

## Domain suggestions (check availability before registering)
1. **stbbsolved.pk** — exact-match, best for SEO in Pakistan
2. **solvedstbb.com** — global, easy to say
3. **stbbnotes.pk** — short, memorable, brandable
"""
    w("README.md", readme)
    print(f"Built core site: {len(BOOKS)} books ({len(REAL)} live), sitemap {len(urls)} URLs")

if __name__ == "__main__":
    build()
