PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE transactions (
transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
cust_name TEXT NOT NULL,
date text DEFAULT CURRENT_DATE,
network TEXT NOT NULL,
data_or_airtime TEXT NOT NULL,
payment_method TEXT NOT NULL,
plan TEXT NOT NULL,
amount INTEGER NOT NULL,
remark TEXT);
INSERT INTO transactions VALUES(7,'Bro Bola','2025-01-16','Mtn','Data','Cash','1gb',350,'First O''man telecoms Customer');
INSERT INTO transactions VALUES(8,'Alfa Value','2025-01-16','Mtn','Data','on account','10gb',3000,'');
INSERT INTO transactions VALUES(9,'Bro Bola','2025-01-16','Mtn','Data','on account','1gb',350,'');
INSERT INTO transactions VALUES(10,'Anita','2025-01-16','Mtn','Data','on account','500mb',200,'');
INSERT INTO sqlite_sequence VALUES('transactions',11);
CREATE INDEX idx_name_date ON transactions (cust_name, date);
CREATE INDEX idx_transactionID ON transactions (transaction_id);
COMMIT;
