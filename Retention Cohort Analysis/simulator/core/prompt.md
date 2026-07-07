Buatkan full Python code untuk generate synthetic dataset untuk project portfolio Data Analytics dengan studi kasus:
"Retention & Cohort Analysis for a SaaS Product"
Dataset ini akan digunakan untuk latihan SQL, Tableau/dashboarding, cohort analysis, retention analysis, churn analysis, feature usage analysis, dan business insight.
Tujuan utama:
Membuat event-level SaaS dataset yang realistis untuk menganalisis user retention berdasarkan weekly signup cohort, melihat user churn, membandingkan retention antar segment, dan memahami faktor yang memengaruhi user tetap aktif atau berhenti menggunakan produk.
PENTING:
Raw dataset harus terlihat seperti production event data, bukan dataset yang sudah penuh dengan metric turunan.
Jangan masukkan kolom turunan seperti:
•	signup_date
•	signup_week
•	cohort_start_date
•	event_week
•	cohort_index
•	max_observable_week
•	churned
•	churn_status
•	churn_week
•	is_core_feature
•	reached_aha_moment
•	final_plan_type
•	last_activity_date
•	total_events
•	total_core_feature_events
•	session_id
•	active_day
•	session_depth
•	user_pattern
Kolom-kolom tersebut nanti akan dihitung saat analisis menggunakan SQL.
JANGAN buat validation table terpisah.
JANGAN export file validation user-level.
JANGAN export file session-level.
Output hanya raw event dataset CSV.
Gunakan:
•	pandas
•	numpy
•	random
•	datetime
•	np.random.seed(42)
Jangan gunakan external API.
Jangan gunakan library yang sulit di-install.
==================================================
BUSINESS CONTEXT
Sebuah SaaS company berhasil mendapatkan banyak user baru, tetapi belum tahu apakah user tersebut tetap aktif setelah signup.
Tim ingin menjawab beberapa pertanyaan:
1.	Berapa retention user per weekly signup cohort?
2.	Pada minggu keberapa user paling banyak churn?
3.	Source mana yang menghasilkan user dengan retention terbaik?
4.	Apakah paid users lebih retain dibanding free users?
5.	Apakah early feature usage berhubungan dengan retention yang lebih tinggi?
6.	Segment mana yang harus diprioritaskan untuk retention improvement?
7.	Apakah user yang mencapai "aha moment" lebih mungkin bertahan?
8.	Apakah user dengan session activity yang lebih dalam lebih mungkin retain?
9.	Apakah user yang membuat report atau mengundang tim punya retention lebih tinggi?
Dataset harus dibuat agar bisa mendukung analisis tersebut menggunakan SQL dan Tableau.
==================================================
OUTPUT FILE
Buat 1 file output saja:
saas_retention_events_raw.csv
Ini adalah raw event dataset utama yang akan dianalisis di SQL.
Jangan buat file output lain.
==================================================
RAW EVENT DATASET FORMAT
Raw dataset harus berbentuk event-level data.
Setiap baris merepresentasikan satu user event.
Kolom raw dataset yang wajib ada:
1.	event_id
o	Unique identifier untuk setiap event.
o	Format: E000001, E000002, dst.
o	event_id harus tetap unique, termasuk untuk duplicate tracking rows.
2.	user_id
o	Unique identifier untuk setiap user.
o	Format: U00001, U00002, dst.
3.	event_time
o	Timestamp event.
o	Range tanggal: 2026-01-01 sampai 2026-06-30.
o	Event_time untuk user yang sama harus masuk akal secara kronologis.
o	Tidak boleh ada event sebelum signup event.
o	Event_time harus bisa diparse sebagai datetime.
o	Format output disarankan: YYYY-MM-DD HH:MM:SS.
4.	event_name
o	Event aktivitas user.
o	Gunakan event berikut:
	signup
	login
	dashboard_view
	feature_used
	report_created
	invite_team_member
	trial_started
	subscription_started
	subscription_cancelled
5.	source
o	Acquisition source.
o	Value utama:
	ads
	organic
	referral
	social
6.	device
o	Device type.
o	Value utama:
	mobile
	desktop
	tablet
7.	country
o	Value utama:
	US
	UK
	France
	Indonesia
	India
	Australia
	Germany
8.	plan_type
o	Value utama:
	free
	trial
	basic
	pro
PENTING:
plan_type harus merepresentasikan user plan pada saat event terjadi, bukan final plan user.
Contoh benar:
o	signup event: plan_type = free
o	login sebelum trial: plan_type = free
o	dashboard_view sebelum trial: plan_type = free
o	trial_started: plan_type = trial
o	activity setelah trial_started: plan_type = trial
o	subscription_started: plan_type = basic/pro
o	activity setelah subscription_started: plan_type = basic/pro
Jangan broadcast final paid status ke semua event historis.
9.	subscription_status
o	Value:
	free
	trial
	active
	cancelled
PENTING:
subscription_status harus merepresentasikan status pada saat event terjadi, bukan final status user.
10.	revenue
o	Revenue hanya muncul untuk event subscription_started.
o	Jika plan basic, revenue sekitar 30.
o	Jika plan pro, revenue sekitar 100.
o	Untuk event lain, revenue = 0.
Jangan masukkan kolom turunan ke raw dataset seperti:
•	signup_date
•	signup_week
•	cohort_index
•	max_observable_week
•	churned
•	churn_status
•	is_core_feature
•	reached_aha_moment
•	session_id
•	user_pattern
signup_date nanti harus bisa dihitung di SQL dari event signup pertama milik setiap user.
==================================================
DATA SIZE
Target raw dataset:
•	Total event rows sekitar 100,000 sampai 130,000 rows.
•	Unique users boleh menyesuaikan agar total event rows mendekati target.
•	Target approximate unique users bisa berada di kisaran 10,000 sampai 13,500 users.
•	Average events per user kira-kira 8 sampai 12 events.
•	Jangan paksa jumlah rows tepat 100,000 jika merusak logic data.
•	Lebih penting menjaga realistic behavior daripada angka rows yang terlalu presisi.
Catatan penting:
Karena dataset harus menggunakan session-based activity behavior, total rows boleh sedikit lebih tinggi dari 100,000. Range 100,000–130,000 rows masih aman dan realistis untuk project portfolio SQL/Tableau.
Setelah dataset dibuat, print:
•	total rows
•	total unique users
•	average events per user
•	date range
•	event count by event_name
•	user count by source
•	count by plan_type
•	count by subscription_status
==================================================
ANALYTICAL DEFINITIONS
Definisi ini jangan dimasukkan sebagai kolom turunan di raw dataset.
Definisi ini dipakai untuk membangun logic data dan nanti dihitung ulang di SQL.
Active user:
User dianggap active pada suatu minggu jika memiliki minimal satu activity event.
Activity events:
•	login
•	dashboard_view
•	feature_used
•	report_created
•	invite_team_member
Event berikut tidak dihitung sebagai active usage:
•	signup
•	trial_started
•	subscription_started
•	subscription_cancelled
Retention rate:
retained_users / cohort_size
Churn definition:
User dianggap churn jika setelah pernah aktif, user tidak memiliki activity event lagi selama minimal 3 minggu berturut-turut.
Namun churn harus memperhatikan observation window.
User hanya boleh dianggap churn jika masih ada minimal 3 full observable weeks setelah last activity week.
Aha moment definition:
User mencapai aha moment jika dalam 7 hari pertama setelah signup melakukan minimal 2 core feature events.
Core feature events:
•	feature_used
•	report_created
•	invite_team_member
Aha moment harus bisa dihitung ulang dari raw event dataset menggunakan SQL.
Session-based behavior:
Session tidak perlu diekspor sebagai kolom.
Session hanya digunakan sebagai internal data generation logic agar event tidak terlihat random dan isolated.
==================================================
CRITICAL ANALYTICAL RULES
1.	Churn must respect observation window.
A user can only be considered churned if there are at least 3 full observable weeks after the user's last activity week.
Logic:
last_activity_cohort_index + 3 <= max_observable_week
Namun jangan masukkan churned atau churn_status ke raw dataset.
Logic ini hanya digunakan untuk membuat data behavior lebih realistis dan nanti dihitung ulang di SQL.
2.	plan_type and subscription_status must be event-level snapshots.
For each event row, plan_type and subscription_status must reflect the user's status at the time of the event.
Do not use final plan_type for all historical events.
3.	event_id must remain unique.
Duplicate or near-duplicate tracking rows should receive a new event_id.
Duplicate tracking row logic:
•	same user_id
•	same or similar event_name
•	same or very close event_time
•	same source/device/country
•	new unique event_id
This simulates double tracking without breaking event_id uniqueness.
4.	Every user must have exactly one recoverable signup event.
Signup is required for cohort analysis.
Dirty data can affect event_name slightly, such as "sign_up", but it must be recoverable during cleaning.
Do not create users without signup event.
Do not create missing user_id.
Do not create missing event_time.
5.	Retention calculations should exclude non-observable cohort periods.
Do not calculate Week N retention if that cohort has not had enough time to be observed.
This should be handled later in SQL using logic similar to:
cohort_index <= max_observable_week
Do not add max_observable_week to raw dataset.
6.	Session-based behavior is required.
Do not generate activity events as fully random isolated events.
For active users, activity should usually appear as realistic session-like sequences.
==================================================
USER BEHAVIOR LOGIC
Jangan generate data secara random total.
Dataset harus mengikuti realistic retention behavior dan session-based user activity.
Rules:
1.	Setiap user wajib memiliki event signup.
2.	Signup event harus menjadi event pertama user.
3.	Setelah signup, sebagian user akan aktif lagi pada minggu-minggu berikutnya.
4.	Sebagian user hanya aktif di minggu pertama lalu churn.
5.	Sebagian user retain lebih lama.
6.	Retention secara umum harus menurun dari waktu ke waktu.
7.	User yang retained bisa memiliki beberapa active days dalam satu minggu.
8.	User yang retained harus menghasilkan session-like activity, bukan hanya isolated random events.
9.	User yang churn harus berhenti menghasilkan regular activity event setelah churn.
10.	Paid users bisa tetap aktif lebih lama dibanding free users.
11.	Event_time untuk user yang sama harus logis dan tidak mundur.
12.	Activity events dalam satu session harus memiliki timestamp yang berdekatan.
13.	Tidak semua activity session harus dimulai dengan login, karena user bisa masih authenticated atau langsung masuk ke dashboard.
14.	Login tidak wajib muncul setiap hari, tetapi harus tetap muncul secara realistis di sebagian session.
15.	dashboard_view harus muncul di sebagian besar activity session.
16.	feature_used biasanya muncul setelah dashboard_view.
17.	report_created biasanya muncul setelah feature_used atau setelah user punya feature activity sebelumnya.
18.	invite_team_member harus lebih jarang dan lebih sering muncul pada user yang lebih engaged.
Retention should be controlled by weekly survival probability so the final validation table is close to the target retention curve.
Avoid generating too many isolated single events.
Most active user-days should contain at least 2 events.
==================================================
RETENTION BOTTLENECK LOGIC
Tambahkan bottleneck utama yang jelas dan bisa dianalisis.
Main bottleneck:
Retention turun tajam dari Week 0 ke Week 1, lalu terus turun signifikan sampai Week 3.
Business reasoning:
Banyak user signup dan mencoba produk pada Week 0, tetapi tidak semua kembali pada Week 1.
Sebagian user yang kembali di Week 1 juga gagal mencapai "aha moment" atau tidak cukup menggunakan core feature, sehingga churn meningkat antara Week 1 dan Week 3.
Expected overall retention pattern kira-kira:
•	Week 0: 100%
•	Week 1: sekitar 60% - 65%
•	Week 2: sekitar 40% - 45%
•	Week 3: sekitar 28% - 33%
•	Week 4: sekitar 21% - 25%
•	Week 5: sekitar 16% - 21%
•	Week 6: sekitar 13% - 17%
•	Week 7: sekitar 10% - 13%
•	Week 8: sekitar 8% - 10%
Important:
Week 1 retention should NOT be too high.
Avoid Week 1 retention above 70% overall.
After Week 4, the retention curve should decline more slowly.
Do not make long-term retention drop too aggressively.
Bottleneck harus lebih kuat untuk:
•	ads users
•	social users
•	free users
•	users without aha moment
•	users with shallow signup behavior
•	users with low session depth
•	users who only login or view dashboard without core feature usage
Bottleneck harus lebih ringan untuk:
•	referral users
•	organic users
•	paid users
•	users who reached aha moment
•	users with deeper session activity
•	users who created reports
•	users who invited team members
Tambahkan noise kecil per user dan per cohort agar pattern tidak terlalu sempurna.
==================================================
RETENTION CURVE SHAPE CONTROL
Pastikan bentuk retention curve mengikuti pola yang realistis:
1.	Week 0 harus 100% karena semua user signup.
2.	Week 1 harus menunjukkan drop awal yang jelas.
Target Week 1 overall retention sekitar 60% - 65%.
Jangan sampai Week 1 retention mendekati 75% atau lebih.
3.	Week 2 dan Week 3 harus menjadi periode bottleneck utama.
Banyak user yang belum mencapai aha moment harus churn pada periode ini.
4.	Setelah Week 4, retention harus turun lebih lambat.
User yang masih aktif setelah Week 4 cenderung lebih engaged.
5.	Long-term retention tidak boleh terlalu rendah.
Target Week 8 overall retention sekitar 8% - 10%.
6.	Retention curve tidak boleh terlalu sempurna.
Tambahkan noise kecil per source, plan, cohort, dan engagement pattern.
Gunakan retention probability yang mengontrol survival user per week, bukan hanya memilih last_active_week secara random tanpa mempertahankan bentuk curve.
Target approximate retention overall:
•	Week 1: 60% - 65%
•	Week 2: 40% - 45%
•	Week 3: 28% - 33%
•	Week 4: 21% - 25%
•	Week 8: 8% - 10%
Jika hasil validation menunjukkan:
•	Week 1 > 70%, turunkan early retention probability.
•	Week 4 < 20%, naikkan mid-term retention probability.
•	Week 8 < 7%, naikkan long-term retention floor.
==================================================
SESSION-BASED ACTIVITY LOGIC
Generate user activity menggunakan session-based behavior.
Jangan membuat activity events sebagai event random yang berdiri sendiri.
Untuk setiap retained user-week:
1.	Generate 1 sampai 3 active days dalam minggu tersebut.
2.	Untuk setiap active day, generate 1 session-like sequence.
3.	Setiap session biasanya berisi 2 sampai 5 events.
4.	Event dalam satu session harus memiliki timestamp yang berdekatan, biasanya dalam rentang 1 sampai 45 menit.
5.	Jangan terlalu sering membuat active day yang hanya punya 1 event.
6.	Tidak semua session harus dimulai dengan login.
7.	Sebagian session bisa dimulai langsung dari dashboard_view karena user bisa masih authenticated.
8.	dashboard_view harus muncul di sebagian besar session.
9.	feature_used biasanya muncul setelah dashboard_view.
10.	report_created biasanya muncul setelah feature_used.
11.	invite_team_member harus lebih jarang dan biasanya muncul pada user yang lebih engaged.
12.	trial_started dan subscription_started adalah lifecycle events, bukan activity session events.
13.	subscription_cancelled adalah lifecycle event dan biasanya terjadi setelah subscription_started.
Contoh session ringan:
•	login
•	dashboard_view
Contoh session normal:
•	login
•	dashboard_view
•	feature_used
Contoh session product-value:
•	dashboard_view
•	feature_used
•	report_created
Contoh session advanced/team adoption:
•	login
•	dashboard_view
•	feature_used
•	report_created
•	invite_team_member
Contoh session tanpa login yang masih realistis:
•	dashboard_view
•	feature_used
•	report_created
Jangan paksa login muncul setiap hari.
Login should appear in some sessions, not all sessions.
Approximate session login probability:
•	Week 0: login appears in around 60% - 80% of sessions.
•	Week 1 and after: login appears in around 30% - 55% of sessions.
•	Returning users after long inactivity are more likely to have login events.
•	Paid users may have more dashboard_view sessions without login due to persistent authentication.
Approximate active days per retained week:
•	Low-engagement users: 1 active day per retained week.
•	Medium-engagement users: 1 to 2 active days per retained week.
•	High-engagement users: 2 to 3 active days per retained week.
•	Paid/pro users may have more stable active days, but they do not need to be active every day.
==================================================
USER ACTIVITY PATTERN LOGIC
Tambahkan beberapa pola perilaku user agar dataset tidak terasa random.
1.	Shallow Signup Pattern
User signup, login atau dashboard_view sebentar, lalu churn cepat.
Contoh:
•	signup
•	login
•	dashboard_view
Cocok untuk:
•	ads users
•	social users
•	free users
•	users without aha moment
2.	New User Exploration Pattern
User mencoba produk di awal tetapi belum tentu mencapai value utama.
Contoh:
•	signup
•	login
•	dashboard_view
•	feature_used
•	dashboard_view
Cocok untuk:
•	free users
•	early week activity
•	users who may or may not retain
3.	Aha Moment Pattern
User cepat menggunakan core feature dalam 7 hari pertama.
Contoh:
•	signup
•	login
•	dashboard_view
•	feature_used
•	report_created
Atau:
•	signup
•	dashboard_view
•	feature_used
•	report_created
•	feature_used
User dengan pattern ini harus punya retention probability lebih tinggi setelah Week 2.
4.	Trial Evaluation Pattern
User mencoba fitur dulu, lalu mulai trial.
Contoh:
•	signup
•	login
•	dashboard_view
•	feature_used
•	report_created
•	trial_started
5.	Paid Conversion Pattern
User dari trial lanjut menjadi paid.
Contoh:
•	signup
•	login
•	dashboard_view
•	feature_used
•	report_created
•	trial_started
•	feature_used
•	subscription_started
Setelah subscription_started, plan_type berubah menjadi basic atau pro untuk event setelahnya.
6.	Team Adoption Pattern
User mulai menggunakan produk bersama tim.
Contoh:
•	signup
•	login
•	dashboard_view
•	feature_used
•	report_created
•	invite_team_member
User yang melakukan invite_team_member harus cenderung punya retention lebih tinggi, tetapi tidak boleh 100% pasti retain.
7.	Churn After Trial Pattern
User mulai trial tetapi tidak lanjut paid dan berhenti aktif.
Contoh:
•	signup
•	login
•	dashboard_view
•	trial_started
•	dashboard_view
•	feature_used
•	inactive
8.	Paid Churn Pattern
User sempat bayar tetapi akhirnya cancel.
Contoh:
•	signup
•	feature_used
•	report_created
•	trial_started
•	subscription_started
•	dashboard_view
•	feature_used
•	subscription_cancelled
Setelah subscription_cancelled, jangan generate regular activity lagi kecuali edge case kecil.
9.	Comeback User Pattern
Sebagian kecil user sempat inactive lalu kembali aktif.
Contoh:
•	Week 0 active
•	Week 1 inactive
•	Week 2 inactive
•	Week 3 active again
Comeback user boleh ada, tapi jangan terlalu banyak agar churn analysis tetap jelas.
Approximate pattern distribution:
•	Shallow signup: 25% - 35%
•	New user exploration: 20% - 30%
•	Aha moment users: 20% - 30%
•	Trial evaluators: 10% - 20%
•	Paid conversion users: 7% - 12%
•	Team adoption users: 3% - 8%
•	Comeback users: 3% - 7%
•	Paid churn users: 1% - 3%
Pattern distribution tidak harus presisi.
Gunakan probabilistic assignment dan tambahkan noise agar dataset tidak terlalu kaku.
==================================================
SOURCE RETENTION LOGIC
Source harus memengaruhi retention, tetapi tidak boleh menentukan hasil secara mutlak.
Distribusi source:
•	ads: 40%
•	organic: 30%
•	referral: 20%
•	social: 10%
Logic:
1.	Referral
o	Retention paling tinggi.
o	User lebih mungkin menggunakan core feature.
o	User lebih mungkin mencapai aha moment.
o	User lebih mungkin convert ke paid plan.
o	User lebih mungkin punya session yang lebih dalam.
o	User lebih mungkin membuat report atau invite team member.
2.	Organic
o	Retention cukup kuat.
o	Behavior stabil.
o	Conversion ke paid sedang sampai baik.
o	Core feature usage cukup tinggi.
o	Session depth cukup baik.
3.	Ads
o	Volume user paling besar.
o	Retention lebih rendah.
o	Banyak user signup tapi cepat churn.
o	Banyak user tidak mencapai aha moment.
o	Paid conversion lebih rendah dibanding organic/referral.
o	Banyak session dangkal seperti login + dashboard_view saja.
4.	Social
o	Volume paling kecil.
o	Retention paling lemah atau mirip ads.
o	Banyak user hanya aktif di minggu awal.
o	Core feature usage lebih rendah.
o	Session depth cenderung rendah.
Realism guardrail:
•	Tidak semua ads users buruk.
•	Tidak semua referral users bagus.
•	Beberapa free users tetap retain.
•	Beberapa paid users tetap churn.
•	Beberapa users without aha moment tetap aktif.
•	Beberapa users with aha moment tetap churn.
•	Beberapa ads users bisa mencapai aha moment.
•	Beberapa referral users bisa churn cepat.
Source, plan, feature usage, dan session depth harus memengaruhi probabilitas, bukan menentukan hasil secara absolut.
==================================================
PLAN TYPE AND SUBSCRIPTION LOGIC
Plan type harus memengaruhi retention.
Rules:
1.	Free users
o	Retention paling rendah.
o	Banyak churn setelah week 1 atau week 2.
o	Lebih sedikit menggunakan core feature.
o	Lebih banyak shallow session.
2.	Trial users
o	Retention sedang.
o	Sebagian convert ke basic/pro.
o	trial_started harus terjadi setelah signup dan setelah user melakukan beberapa activity event.
3.	Basic users
o	Retention lebih tinggi.
o	Revenue sekitar 30 saat subscription_started.
o	Session lebih stabil dibanding free users.
o	Lebih mungkin membuat report.
4.	Pro users
o	Retention paling tinggi.
o	Revenue sekitar 100 saat subscription_started.
o	Lebih mungkin menggunakan core feature dan invite_team_member.
o	Lebih mungkin punya session advanced/team adoption.
Rules tambahan:
•	Tidak semua user mulai trial.
•	Tidak semua trial users convert ke paid subscription.
•	subscription_started hanya boleh terjadi setelah trial_started atau setelah beberapa core feature activity.
•	subscription_cancelled dapat terjadi beberapa minggu setelah subscription_started.
•	Setelah subscription_cancelled, user tidak boleh memiliki subscription_started lagi, kecuali edge case sangat kecil jika ingin dibuat.
•	Setelah subscription_cancelled, subscription_status pada event setelahnya harus "cancelled" jika ada event non-activity administratif.
•	Setelah churn/cancelled, jangan generate activity event reguler lagi kecuali edge case kecil yang realistis.
==================================================
FEATURE USAGE AND AHA MOMENT LOGIC
Feature usage harus menjadi faktor penting dalam retention.
Core feature events:
•	feature_used
•	report_created
•	invite_team_member
Aha moment:
User dianggap mencapai aha moment jika dalam 7 hari pertama setelah signup melakukan minimal 2 core feature events.
Logic:
1.	Users who reach aha moment have significantly higher retention after Week 2.
2.	Users who do not reach aha moment are more likely to churn between Week 1 and Week 3.
3.	Referral and organic users are more likely to reach aha moment.
4.	Ads and social users are less likely to reach aha moment.
5.	Paid users usually have higher aha moment rate than free users.
6.	Users who invite team members tend to retain better than users who only login.
7.	report_created should usually happen after feature_used within the same session or after previous feature usage.
8.	invite_team_member should be less frequent and mostly appear for users with stronger engagement.
9.	Aha moment should emerge from event behavior, not be directly inserted as a raw column.
10.	Users with deeper sessions should be more likely to reach aha moment.
11.	Users with only login/dashboard_view sessions should be less likely to retain long term.
Do not export reached_aha_moment in raw dataset.
Do not export is_core_feature in raw dataset.
Both must be calculated later in SQL from event_name and event_time.
==================================================
EVENT FREQUENCY LOGIC
Untuk user yang retained:
•	Mereka bisa punya beberapa active days dalam satu minggu.
•	Setiap active day sebaiknya punya 1 session-like event sequence.
•	Activity event bisa berupa login, dashboard_view, feature_used, report_created, invite_team_member.
•	Semakin engaged user, semakin banyak active days dan semakin dalam event sequence-nya.
•	User dengan aha moment punya event frequency lebih tinggi.
•	Paid users punya event frequency lebih stabil.
•	Free users lebih cepat menurun activity-nya.
Untuk user yang churn:
•	Mereka berhenti menghasilkan regular activity event setelah churn.
•	Mereka boleh memiliki subscription_cancelled jika paid user.
•	Jangan generate activity event reguler setelah churn kecuali edge case kecil seperti comeback user.
Frequency pattern:
•	Week 0 biasanya lebih banyak activity karena user baru mencoba produk.
•	Week 1 sampai Week 3 adalah periode penting untuk melihat apakah user kembali dan mencapai value.
•	Week 4 dan seterusnya lebih banyak diisi oleh user yang lebih engaged.
•	Long-term retained users tidak harus aktif setiap hari.
•	Long-term retained users biasanya punya session yang lebih berkualitas, bukan sekadar banyak login.
•	Avoid generating too many isolated single events.
•	Most active days should contain at least 2 events.
•	Most sessions should contain 2 to 5 events.
•	Activity sessions should usually have event timestamps close together.
==================================================
REVENUE LOGIC
Untuk versi pertama, revenue dibuat sederhana.
Revenue muncul pada event subscription_started:
•	basic: sekitar 30
•	pro: sekitar 100
Non-revenue events:
•	revenue = 0
Rules:
•	subscription_started hanya muncul untuk user yang convert ke paid.
•	subscription_started harus terjadi setelah trial_started atau setelah cukup core feature activity.
•	plan_type berubah secara logis:
o	free → trial → basic/pro
o	atau free → basic/pro untuk sebagian kecil user
•	subscription_status berubah secara logis:
o	free
o	trial
o	active
o	cancelled
Jangan tambahkan invoice_paid untuk versi pertama agar dataset tidak terlalu kompleks.
Revenue analysis akan dianggap simple subscription-start revenue, bukan full recurring revenue.
==================================================
OBSERVATION WINDOW LOGIC
Dataset date range:
•	Start date: 2026-01-01
•	End date: 2026-06-30
Pastikan data generation memperhitungkan observation window.
Rules:
•	User yang signup dekat akhir periode dataset tidak boleh dipaksa memiliki event sampai Week 8.
•	User cohort akhir tidak boleh dibuat seolah-olah churn hanya karena belum cukup waktu observasi.
•	Jangan masukkan max_observable_week ke raw dataset.
•	max_observable_week nanti harus dihitung di SQL.
==================================================
DIRTY DATA / DATA QUALITY ISSUES
Tambahkan sedikit data kotor secara realistis, tapi jangan sampai merusak retention logic utama.
Tambahkan:
1.	Typo / inconsistent values:
o	event_name: "log_in" sebagai typo dari "login" sekitar 1%
o	event_name: "sign_up" sebagai typo dari "signup" sekitar 0.5%
o	country: "USA" sebagai inconsistent dari "US" sekitar 1%
o	country: "Indnesia" sebagai typo dari "Indonesia" sekitar 0.5%
o	device: "Mobile" sebagai inconsistent dari "mobile" sekitar 2%
o	plan_type: "Basic" sebagai inconsistent dari "basic" sekitar 1%
2.	Missing values:
o	beberapa country = None
o	beberapa device = None
o	beberapa source = None
o	Jangan terlalu banyak missing values.
3.	Duplicate events:
o	sekitar 300–700 rows duplicate atau near-duplicate.
o	Duplicate harus punya event_id baru.
o	Duplicate bisa punya user_id, event_name, event_time yang sama atau mirip.
o	Duplicate jangan terlalu banyak sampai merusak retention table.
4.	Multi-source user:
o	sekitar 50–100 user memiliki lebih dari satu source karena tracking/attribution issue.
o	First-touch source nantinya bisa dihitung di SQL berdasarkan event_time pertama.
5.	Jangan membuat data terlalu rusak.
o	Dirty data harus cukup untuk latihan cleaning, bukan membuat analisis tidak bisa dipakai.
Dirty data guardrails:
•	Jangan buat user_id missing.
•	Jangan buat event_time missing.
•	Setiap user harus tetap memiliki minimal satu signup event yang bisa dipulihkan melalui cleaning.
•	Dirty data hanya boleh terjadi pada categorical fields dan sebagian duplicate events.
•	Dirty data tidak boleh merusak urutan utama user journey.
•	Dirty data tidak boleh membuat signup hilang total untuk user.
==================================================
PYTHON VALIDATION SUMMARY
Setelah generate dataset, tambahkan Python validation summary dengan print saja.
Jangan export validation table.
Print untuk raw dataset:
1.	Total rows
2.	Total unique users
3.	Average events per user
4.	Date range
5.	Signup users harus sama dengan total unique users setelah memperbaiki sign_up menjadi signup secara internal
6.	Unique event_name values
7.	Count by event_name
8.	Count by source
9.	Count by plan_type
10.	Count by subscription_status
11.	Basic duplicate count
12.	event_id duplicate count harus 0
13.	Missing values per column
14.	Check apakah ada event sebelum signup
15.	Check apakah signup event adalah event pertama user
16.	Check apakah raw dataset tidak memiliki kolom turunan yang dilarang
17.	Check apakah revenue hanya muncul pada subscription_started
18.	Check apakah event_time bisa diparse sebagai datetime
Tambahkan juga printed validation summary internal, tanpa export file:
1.	Approximate overall retention by cohort_index:
o	cohort_index
o	retained_users
o	cohort_size
o	retention_rate
2.	Retention by source summary:
o	source
o	week_1_retention
o	week_2_retention
o	week_4_retention
o	week_8_retention
3.	Retention by plan_type summary:
o	plan_type
o	week_1_retention
o	week_4_retention
o	week_8_retention
4.	Aha moment validation:
o	users who reached aha moment
o	users who did not reach aha moment
o	week 4 retention for both groups
5.	Churn summary:
o	estimated churned users
o	estimated churn rate
o	estimated churned users by source
o	estimated churned users by plan_type
o	estimated churn_week distribution
6.	Session realism validation:
o	average events per active day
o	percentage of active days with only 1 event
o	percentage of active days with 2 or more events
o	percentage of activity sessions containing dashboard_view
o	percentage of activity sessions containing login
o	percentage of sessions with core feature events
o	average time gap between events inside session-like sequences
o	event sequence examples for several users
Catatan:
Validation summary boleh menggunakan internal calculations di Python, tetapi raw dataset tetap tidak boleh berisi kolom cohort/churn/aha/session turunan.
==================================================
EXPECTED SQL ANALYSIS USE CASE
Dataset raw ini nantinya akan dianalisis menggunakan SQL untuk menghitung:
1.	Data cleaning:
o	fix log_in → login
o	fix sign_up → signup
o	fix USA → US
o	fix Indnesia → Indonesia
o	fix Mobile → mobile
o	fix Basic → basic
o	handle null source/country/device
o	remove duplicate tracking events
2.	Cohort fields:
o	signup_date
o	signup_week
o	cohort_start_date
o	event_week
o	cohort_index
o	max_observable_week
3.	Retention:
o	weekly retention
o	cohort retention heatmap
o	retention curve
4.	Churn:
o	churned
o	churn_status
o	churn_week
5.	Aha moment:
o	core feature usage in first 7 days
o	reached_aha_moment
6.	Segment analysis:
o	retention by source
o	retention by plan_type
o	retention by country/device
o	retention by aha moment
o	retention by feature usage
7.	Session and engagement analysis:
o	approximate session depth from event sequence
o	active days per week
o	event frequency per retained user
o	deeper engagement behavior such as report_created and invite_team_member
8.	Business recommendations.
==================================================
CODE QUALITY REQUIREMENTS
1.	Kode harus rapi dan mudah dibaca.
2.	Tambahkan komentar untuk setiap logic besar.
3.	Gunakan function jika diperlukan agar kode tidak berantakan.
4.	Gunakan np.random.seed(42) agar reproducible.
5.	Pastikan event_time bertipe datetime.
6.	Pastikan tidak ada event sebelum signup event.
7.	Pastikan signup event adalah event pertama user.
8.	Pastikan user progression masuk akal.
9.	Pastikan retention curve menurun secara natural tapi tidak terlalu sempurna.
10.	Pastikan source effect, plan effect, aha moment effect, dan session depth effect terlihat tetapi tidak terlalu deterministik.
11.	Pastikan total rows mendekati 100,000 sampai 130,000.
12.	Jangan membuat dataset terlalu kecil.
13.	Jangan membuat dirty data merusak core retention logic.
14.	Raw dataset harus tetap terlihat seperti event-level production data.
15.	Analytical derived fields harus dihitung di SQL, bukan disimpan di raw dataset.
16.	Jangan export validation table.
17.	Output hanya satu CSV raw dataset.
18.	Jangan gunakan external API.
19.	Jangan gunakan library selain pandas, numpy, random, datetime jika tidak perlu.
20.	Generate activity using retained week → active day → session → event sequence.
21.	Jangan generate terlalu banyak isolated single events.
22.	Jangan paksa login muncul sebelum setiap activity.
23.	dashboard_view harus muncul secara realistis sebagai bagian dari sebagian besar usage sessions.
24.	report_created dan invite_team_member harus muncul sebagai deeper engagement behavior, bukan random event tanpa konteks.
25.	Pastikan plan_type dan subscription_status tetap event-level snapshot, bukan final user status.
26.	Pastikan lifecycle events seperti trial_started, subscription_started, dan subscription_cancelled terjadi secara kronologis.
27.	Pastikan duplicate tracking rows tetap punya event_id unique.
28.	Pastikan output CSV hanya berisi raw columns yang diminta.
Tolong buatkan full Python code berdasarkan semua spesifikasi di atas.

