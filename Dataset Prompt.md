```
Buatkan full Python code untuk generate synthetic dataset untuk project portfolio Data Analytics dengan studi kasus:

"Retention & Cohort Analysis for a SaaS Product"

Dataset ini akan digunakan untuk latihan SQL, Tableau/dashboarding, cohort analysis, retention analysis, churn analysis, feature usage analysis, dan business insight.

Tujuan utama:
Membuat event-level SaaS dataset yang realistis untuk menganalisis user retention berdasarkan weekly signup cohort, melihat user churn, membandingkan retention antar segment, dan memahami faktor yang memengaruhi user tetap aktif atau berhenti menggunakan produk.

PENTING:
Raw dataset harus terlihat seperti production event data, bukan dataset yang sudah penuh dengan metric turunan.

Jangan masukkan kolom turunan seperti:
- signup_date
- signup_week
- cohort_start_date
- event_week
- cohort_index
- max_observable_week
- churned
- churn_status
- churn_week
- is_core_feature
- reached_aha_moment
- final_plan_type
- last_activity_date
- total_events
- total_core_feature_events

Kolom-kolom tersebut nanti akan dihitung saat analisis menggunakan SQL.

JANGAN buat validation table terpisah.
JANGAN export file validation user-level.
Output hanya raw event dataset CSV.

Gunakan:
- pandas
- numpy
- random
- datetime
- np.random.seed(42)

Jangan gunakan external API.
Jangan gunakan library yang sulit di-install.

==================================================
BUSINESS CONTEXT
==================================================

Sebuah SaaS company berhasil mendapatkan banyak user baru, tetapi belum tahu apakah user tersebut tetap aktif setelah signup.

Tim ingin menjawab beberapa pertanyaan:

1. Berapa retention user per weekly signup cohort?
2. Pada minggu keberapa user paling banyak churn?
3. Source mana yang menghasilkan user dengan retention terbaik?
4. Apakah paid users lebih retain dibanding free users?
5. Apakah early feature usage berhubungan dengan retention yang lebih tinggi?
6. Segment mana yang harus diprioritaskan untuk retention improvement?
7. Apakah user yang mencapai "aha moment" lebih mungkin bertahan?

Dataset harus dibuat agar bisa mendukung analisis tersebut menggunakan SQL dan Tableau.

==================================================
OUTPUT FILE
==================================================

Buat 1 file output saja:

saas_retention_events_raw.csv

Ini adalah raw event dataset utama yang akan dianalisis di SQL.

Jangan buat file output lain.

==================================================
RAW EVENT DATASET FORMAT
==================================================

Raw dataset harus berbentuk event-level data.

Setiap baris merepresentasikan satu user event.

Kolom raw dataset yang wajib ada:

1. event_id
   - Unique identifier untuk setiap event.
   - Format: E000001, E000002, dst.
   - event_id harus tetap unique, termasuk untuk duplicate tracking rows.

2. user_id
   - Unique identifier untuk setiap user.
   - Format: U00001, U00002, dst.

3. event_time
   - Timestamp event.
   - Range tanggal: 2026-01-01 sampai 2026-06-30.
   - Event_time untuk user yang sama harus masuk akal secara kronologis.
   - Tidak boleh ada event sebelum signup event.

4. event_name
   - Event aktivitas user.
   - Gunakan event berikut:
     - signup
     - login
     - dashboard_view
     - feature_used
     - report_created
     - invite_team_member
     - trial_started
     - subscription_started
     - subscription_cancelled

5. source
   - Acquisition source.
   - Value utama:
     - ads
     - organic
     - referral
     - social

6. device
   - Device type.
   - Value utama:
     - mobile
     - desktop
     - tablet

7. country
   - Value utama:
     - US
     - UK
     - France
     - Indonesia
     - India
     - Australia
     - Germany

8. plan_type
   - Value utama:
     - free
     - trial
     - basic
     - pro

   PENTING:
   plan_type harus merepresentasikan user plan pada saat event terjadi, bukan final plan user.

   Contoh benar:
   - signup event: plan_type = free
   - login sebelum trial: plan_type = free
   - trial_started: plan_type = trial
   - subscription_started: plan_type = basic/pro
   - activity setelah subscription_started: plan_type = basic/pro

   Jangan broadcast final paid status ke semua event historis.

9. subscription_status
   - Value:
     - free
     - trial
     - active
     - cancelled

   PENTING:
   subscription_status harus merepresentasikan status pada saat event terjadi, bukan final status user.

10. revenue
    - Revenue hanya muncul untuk event subscription_started.
    - Jika plan basic, revenue sekitar 30.
    - Jika plan pro, revenue sekitar 100.
    - Untuk event lain, revenue = 0.

Jangan masukkan kolom turunan ke raw dataset seperti:
- signup_date
- signup_week
- cohort_index
- max_observable_week
- churned
- churn_status
- is_core_feature
- reached_aha_moment

signup_date nanti harus bisa dihitung di SQL dari event signup pertama milik setiap user.

==================================================
DATA SIZE
==================================================

Target raw dataset:
- Total event rows sekitar 100,000 rows.
- Unique users boleh menyesuaikan agar total event rows mendekati 100,000.
- Target approximate unique users bisa berada di kisaran 8,000 sampai 15,000 users.
- Jangan paksa jumlah rows tepat 100,000 jika merusak logic data.
- Lebih penting menjaga realistic behavior daripada angka rows yang terlalu presisi.

Setelah dataset dibuat, print:
- total rows
- total unique users
- average events per user
- date range
- event count by event_name
- user count by source
- count by plan_type
- count by subscription_status

==================================================
ANALYTICAL DEFINITIONS
==================================================

Definisi ini jangan dimasukkan sebagai kolom turunan di raw dataset.
Definisi ini dipakai untuk membangun logic data dan nanti dihitung ulang di SQL.

Active user:
User dianggap active pada suatu minggu jika memiliki minimal satu activity event.

Activity events:
- login
- dashboard_view
- feature_used
- report_created
- invite_team_member

Event berikut tidak dihitung sebagai active usage:
- signup
- trial_started
- subscription_started
- subscription_cancelled

Retention rate:
retained_users / cohort_size

Churn definition:
User dianggap churn jika setelah pernah aktif, user tidak memiliki activity event lagi selama minimal 3 minggu berturut-turut.

Namun churn harus memperhatikan observation window.
User hanya boleh dianggap churn jika masih ada minimal 3 full observable weeks setelah last activity week.

Aha moment definition:
User mencapai aha moment jika dalam 7 hari pertama setelah signup melakukan minimal 2 core feature events.

Core feature events:
- feature_used
- report_created
- invite_team_member

Aha moment harus bisa dihitung ulang dari raw event dataset menggunakan SQL.

==================================================
CRITICAL ANALYTICAL RULES
==================================================

1. Churn must respect observation window.

A user can only be considered churned if there are at least 3 full observable weeks after the user's last activity week.

Logic:
last_activity_cohort_index + 3 <= max_observable_week

Namun jangan masukkan churned atau churn_status ke raw dataset.
Logic ini hanya digunakan untuk membuat data behavior lebih realistis dan nanti dihitung ulang di SQL.

2. plan_type and subscription_status must be event-level snapshots.

For each event row, plan_type and subscription_status must reflect the user's status at the time of the event.

Do not use final plan_type for all historical events.

3. event_id must remain unique.

Duplicate or near-duplicate tracking rows should receive a new event_id.

Duplicate tracking row logic:
- same user_id
- same or similar event_name
- same or very close event_time
- same source/device/country
- new unique event_id

This simulates double tracking without breaking event_id uniqueness.

4. Every user must have exactly one recoverable signup event.

Signup is required for cohort analysis.
Dirty data can affect event_name slightly, such as "sign_up", but it must be recoverable during cleaning.

Do not create users without signup event.
Do not create missing user_id.
Do not create missing event_time.

5. Retention calculations should exclude non-observable cohort periods.

Do not calculate Week N retention if that cohort has not had enough time to be observed.

This should be handled later in SQL using logic similar to:
cohort_index <= max_observable_week

Do not add max_observable_week to raw dataset.

==================================================
USER BEHAVIOR LOGIC
==================================================

Jangan generate data secara random total.

Dataset harus mengikuti realistic retention behavior.

Rules:

1. Setiap user wajib memiliki event signup.
2. Signup event harus menjadi event pertama user.
3. Setelah signup, sebagian user akan aktif lagi pada minggu-minggu berikutnya.
4. Sebagian user hanya aktif di minggu pertama lalu churn.
5. Sebagian user retain lebih lama.
6. Retention secara umum harus menurun dari waktu ke waktu.
7. User yang retained bisa memiliki beberapa event dalam satu minggu.
8. User yang churn harus berhenti menghasilkan activity event setelah churn.
9. Paid users bisa tetap aktif lebih lama dibanding free users.
10. Event_time untuk user yang sama harus logis dan tidak mundur.

Retention should be controlled by weekly survival probability so the final validation table is close to the target retention curve.
Avoid generating too many users who are active in Week 1 but disappear immediately after, because that creates an unrealistic curve shape.

==================================================
RETENTION BOTTLENECK LOGIC
==================================================

Tambahkan bottleneck utama yang jelas dan bisa dianalisis.

Main bottleneck:
Retention turun tajam dari Week 0 ke Week 1, lalu terus turun signifikan sampai Week 3.

Business reasoning:
Banyak user signup dan mencoba produk pada Week 0, tetapi tidak semua kembali pada Week 1.
Sebagian user yang kembali di Week 1 juga gagal mencapai "aha moment" atau tidak cukup menggunakan core feature, sehingga churn meningkat antara Week 1 dan Week 3.

Expected overall retention pattern kira-kira:
- Week 0: 100%
- Week 1: sekitar 60% - 65%
- Week 2: sekitar 40% - 45%
- Week 3: sekitar 28% - 33%
- Week 4: sekitar 21% - 25%
- Week 5: sekitar 16% - 21%
- Week 6: sekitar 13% - 17%
- Week 7: sekitar 10% - 13%
- Week 8: sekitar 8% - 10%

Important:
Week 1 retention should NOT be too high.
Avoid Week 1 retention above 70% overall.

After Week 4, the retention curve should decline more slowly.
Do not make long-term retention drop too aggressively.

Bottleneck harus lebih kuat untuk:
- ads users
- social users
- free users
- users without aha moment

Bottleneck harus lebih ringan untuk:
- referral users
- organic users
- paid users
- users who reached aha moment

Tambahkan noise kecil per user dan per cohort agar pattern tidak terlalu sempurna.

==================================================
RETENTION CURVE SHAPE CONTROL
==================================================

Pastikan bentuk retention curve mengikuti pola yang realistis:

1. Week 0 harus 100% karena semua user signup.
2. Week 1 harus menunjukkan drop awal yang jelas.
   Target Week 1 overall retention sekitar 60% - 65%.
   Jangan sampai Week 1 retention mendekati 75% atau lebih.
3. Week 2 dan Week 3 harus menjadi periode bottleneck utama.
   Banyak user yang belum mencapai aha moment harus churn pada periode ini.
4. Setelah Week 4, retention harus turun lebih lambat.
   User yang masih aktif setelah Week 4 cenderung lebih engaged.
5. Long-term retention tidak boleh terlalu rendah.
   Target Week 8 overall retention sekitar 8% - 10%.
6. Retention curve tidak boleh terlalu sempurna.
   Tambahkan noise kecil per source, plan, dan cohort.

Gunakan retention probability yang mengontrol survival user per week, bukan hanya memilih last_active_week secara random tanpa mempertahankan bentuk curve.

Target approximate retention overall:
- Week 1: 60% - 65%
- Week 2: 40% - 45%
- Week 3: 28% - 33%
- Week 4: 21% - 25%
- Week 8: 8% - 10%

Jika hasil validation menunjukkan:
- Week 1 > 70%, turunkan early retention probability.
- Week 4 < 20%, naikkan mid-term retention probability.
- Week 8 < 7%, naikkan long-term retention floor.

==================================================
SOURCE RETENTION LOGIC
==================================================

Source harus memengaruhi retention, tetapi tidak boleh menentukan hasil secara mutlak.

Distribusi source:
- ads: 40%
- organic: 30%
- referral: 20%
- social: 10%

Logic:

1. Referral
   - Retention paling tinggi.
   - User lebih mungkin menggunakan core feature.
   - User lebih mungkin mencapai aha moment.
   - User lebih mungkin convert ke paid plan.

2. Organic
   - Retention cukup kuat.
   - Behavior stabil.
   - Conversion ke paid sedang sampai baik.
   - Core feature usage cukup tinggi.

3. Ads
   - Volume user paling besar.
   - Retention lebih rendah.
   - Banyak user signup tapi cepat churn.
   - Banyak user tidak mencapai aha moment.
   - Paid conversion lebih rendah dibanding organic/referral.

4. Social
   - Volume paling kecil.
   - Retention paling lemah atau mirip ads.
   - Banyak user hanya aktif di minggu awal.
   - Core feature usage lebih rendah.

Realism guardrail:
- Tidak semua ads users buruk.
- Tidak semua referral users bagus.
- Beberapa free users tetap retain.
- Beberapa paid users tetap churn.
- Beberapa users without aha moment tetap aktif.
- Beberapa users with aha moment tetap churn.

Source, plan, dan feature usage harus memengaruhi probabilitas, bukan menentukan hasil secara absolut.

==================================================
PLAN TYPE AND SUBSCRIPTION LOGIC
==================================================

Plan type harus memengaruhi retention.

Rules:

1. Free users
   - Retention paling rendah.
   - Banyak churn setelah week 1 atau week 2.
   - Lebih sedikit menggunakan core feature.

2. Trial users
   - Retention sedang.
   - Sebagian convert ke basic/pro.
   - trial_started harus terjadi setelah signup dan setelah user melakukan beberapa activity event.

3. Basic users
   - Retention lebih tinggi.
   - Revenue sekitar 30 saat subscription_started.

4. Pro users
   - Retention paling tinggi.
   - Revenue sekitar 100 saat subscription_started.
   - Lebih mungkin menggunakan core feature dan invite_team_member.

Rules tambahan:
- Tidak semua user mulai trial.
- Tidak semua trial users convert ke paid subscription.
- subscription_started hanya boleh terjadi setelah trial_started atau setelah beberapa core feature activity.
- subscription_cancelled dapat terjadi beberapa minggu setelah subscription_started.
- Setelah subscription_cancelled, user tidak boleh memiliki subscription_started lagi, kecuali edge case sangat kecil jika ingin dibuat.
- Setelah subscription_cancelled, subscription_status pada event setelahnya harus "cancelled" jika ada event non-activity administratif.
- Setelah churn/cancelled, jangan generate activity event reguler lagi kecuali edge case kecil yang realistis.

==================================================
FEATURE USAGE AND AHA MOMENT LOGIC
==================================================

Feature usage harus menjadi faktor penting dalam retention.

Core feature events:
- feature_used
- report_created
- invite_team_member

Aha moment:
User dianggap mencapai aha moment jika dalam 7 hari pertama setelah signup melakukan minimal 2 core feature events.

Logic:
1. Users who reach aha moment have significantly higher retention after week 2.
2. Users who do not reach aha moment are more likely to churn between week 1 and week 3.
3. Referral and organic users are more likely to reach aha moment.
4. Ads and social users are less likely to reach aha moment.
5. Paid users usually have higher aha moment rate than free users.
6. Users who invite team members tend to retain better than users who only login.

Do not export reached_aha_moment in raw dataset.
Do not export is_core_feature in raw dataset.
Both must be calculated later in SQL from event_name and event_time.

==================================================
EVENT FREQUENCY LOGIC
==================================================

Untuk user yang retained:
- Mereka bisa punya beberapa event dalam satu minggu.
- Activity event bisa berupa login, dashboard_view, feature_used, report_created, invite_team_member.
- Semakin engaged user, semakin banyak event per minggu.

Untuk user yang churn:
- Mereka berhenti menghasilkan activity event setelah churn.
- Mereka boleh memiliki subscription_cancelled jika paid user.

Frequency pattern:
- Week 0 biasanya lebih banyak activity karena user baru mencoba produk.
- User yang mencapai aha moment punya event frequency lebih tinggi.
- Paid users punya event frequency lebih stabil.
- Free users lebih cepat menurun activity-nya.

==================================================
REVENUE LOGIC
==================================================

Untuk versi pertama, revenue dibuat sederhana.

Revenue muncul pada event subscription_started:
- basic: sekitar 30
- pro: sekitar 100

Non-revenue events:
- revenue = 0

Rules:
- subscription_started hanya muncul untuk user yang convert ke paid.
- subscription_started harus terjadi setelah trial_started atau setelah cukup core feature activity.
- plan_type berubah secara logis:
  - free → trial → basic/pro
  - atau free → basic/pro untuk sebagian kecil user
- subscription_status berubah secara logis:
  - free
  - trial
  - active
  - cancelled

Jangan tambahkan invoice_paid untuk versi pertama agar dataset tidak terlalu kompleks.
Revenue analysis akan dianggap simple subscription-start revenue, bukan full recurring revenue.

==================================================
OBSERVATION WINDOW LOGIC
==================================================

Dataset date range:
- Start date: 2026-01-01
- End date: 2026-06-30

Pastikan data generation memperhitungkan observation window.

Rules:
- User yang signup dekat akhir periode dataset tidak boleh dipaksa memiliki event sampai Week 8.
- User cohort akhir tidak boleh dibuat seolah-olah churn hanya karena belum cukup waktu observasi.
- Jangan masukkan max_observable_week ke raw dataset.
- max_observable_week nanti harus dihitung di SQL.

==================================================
DIRTY DATA / DATA QUALITY ISSUES
==================================================

Tambahkan sedikit data kotor secara realistis, tapi jangan sampai merusak retention logic utama.

Tambahkan:

1. Typo / inconsistent values:
   - event_name: "log_in" sebagai typo dari "login" sekitar 1%
   - event_name: "sign_up" sebagai typo dari "signup" sekitar 0.5%
   - country: "USA" sebagai inconsistent dari "US" sekitar 1%
   - country: "Indnesia" sebagai typo dari "Indonesia" sekitar 0.5%
   - device: "Mobile" sebagai inconsistent dari "mobile" sekitar 2%
   - plan_type: "Basic" sebagai inconsistent dari "basic" sekitar 1%

2. Missing values:
   - beberapa country = None
   - beberapa device = None
   - beberapa source = None
   - Jangan terlalu banyak missing values.

3. Duplicate events:
   - sekitar 300–700 rows duplicate atau near-duplicate.
   - Duplicate harus punya event_id baru.
   - Duplicate bisa punya user_id, event_name, event_time yang sama atau mirip.
   - Duplicate jangan terlalu banyak sampai merusak retention table.

4. Multi-source user:
   - sekitar 50–100 user memiliki lebih dari satu source karena tracking/attribution issue.
   - First-touch source nantinya bisa dihitung di SQL berdasarkan event_time pertama.

5. Jangan membuat data terlalu rusak.
   - Dirty data harus cukup untuk latihan cleaning, bukan membuat analisis tidak bisa dipakai.

Dirty data guardrails:
- Jangan buat user_id missing.
- Jangan buat event_time missing.
- Setiap user harus tetap memiliki minimal satu signup event yang bisa dipulihkan melalui cleaning.
- Dirty data hanya boleh terjadi pada categorical fields dan sebagian duplicate events.

==================================================
PYTHON VALIDATION SUMMARY
==================================================

Setelah generate dataset, tambahkan Python validation summary dengan print saja.

Jangan export validation table.

Print untuk raw dataset:

1. Total rows
2. Total unique users
3. Average events per user
4. Date range
5. Signup users harus sama dengan total unique users setelah memperbaiki sign_up menjadi signup secara internal
6. Unique event_name values
7. Count by event_name
8. Count by source
9. Count by plan_type
10. Count by subscription_status
11. Basic duplicate count
12. event_id duplicate count harus 0
13. Missing values per column
14. Check apakah ada event sebelum signup
15. Check apakah signup event adalah event pertama user
16. Check apakah raw dataset tidak memiliki kolom turunan yang dilarang

Tambahkan juga printed validation summary internal, tanpa export file:

1. Approximate overall retention by cohort_index:
   - cohort_index
   - retained_users
   - cohort_size
   - retention_rate

2. Retention by source summary:
   - source
   - week_1_retention
   - week_2_retention
   - week_4_retention
   - week_8_retention

3. Retention by plan_type summary:
   - plan_type
   - week_1_retention
   - week_4_retention
   - week_8_retention

4. Aha moment validation:
   - users who reached aha moment
   - users who did not reach aha moment
   - week 4 retention for both groups

5. Churn summary:
   - estimated churned users
   - estimated churn rate
   - estimated churned users by source
   - estimated churned users by plan_type
   - estimated churn_week distribution

Catatan:
Validation summary boleh menggunakan internal calculations di Python, tetapi raw dataset tetap tidak boleh berisi kolom cohort/churn/aha turunan.

==================================================
EXPECTED SQL ANALYSIS USE CASE
==================================================

Dataset raw ini nantinya akan dianalisis menggunakan SQL untuk menghitung:

1. Data cleaning:
   - fix log_in → login
   - fix sign_up → signup
   - fix USA → US
   - fix Indnesia → Indonesia
   - fix Mobile → mobile
   - fix Basic → basic
   - handle null source/country/device
   - remove duplicate tracking events

2. Cohort fields:
   - signup_date
   - signup_week
   - cohort_start_date
   - event_week
   - cohort_index
   - max_observable_week

3. Retention:
   - weekly retention
   - cohort retention heatmap
   - retention curve

4. Churn:
   - churned
   - churn_status
   - churn_week

5. Aha moment:
   - core feature usage in first 7 days
   - reached_aha_moment

6. Segment analysis:
   - retention by source
   - retention by plan_type
   - retention by country/device
   - retention by aha moment

7. Business recommendations.

==================================================
CODE QUALITY REQUIREMENTS
==================================================

1. Kode harus rapi dan mudah dibaca.
2. Tambahkan komentar untuk setiap logic besar.
3. Gunakan function jika diperlukan agar kode tidak berantakan.
4. Gunakan np.random.seed(42) agar reproducible.
5. Pastikan event_time bertipe datetime.
6. Pastikan tidak ada event sebelum signup event.
7. Pastikan signup event adalah event pertama user.
8. Pastikan user progression masuk akal.
9. Pastikan retention curve menurun secara natural tapi tidak terlalu sempurna.
10. Pastikan source effect, plan effect, dan aha moment effect terlihat tetapi tidak terlalu deterministik.
11. Pastikan total rows mendekati 100,000.
12. Jangan membuat dataset terlalu kecil.
13. Jangan membuat dirty data merusak core retention logic.
14. Raw dataset harus tetap terlihat seperti event-level production data.
15. Analytical derived fields harus dihitung di SQL, bukan disimpan di raw dataset.
16. Jangan export validation table.
17. Output hanya satu CSV raw dataset.
18. Jangan gunakan external API.
19. Jangan gunakan library selain pandas, numpy, random, datetime jika tidak perlu.

Tolong buatkan full Python code berdasarkan semua spesifikasi di atas.
```
