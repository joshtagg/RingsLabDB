CREATE DATABASE RingOccultations;
USE RingOccultations;

SET autocommit=0 ; source C:\Users\joshu\Desktop\FixedRawData\10kSQLfixed\3CEN040_UVIS_Egress10km.sql ; COMMIT ;

SET autocommit=0 ; source C:\Users\joshu\Desktop\FixedRawData\10kAnd1kCombined\OneFile1k.sql ; COMMIT ;

SET autocommit=0 ; source C:\Users\joshu\Desktop\FixedRawData\10kAnd1kCombined\OneFile10kFixed.sql ; COMMIT ;

/*

Problems with current sql occultations:
numbers with decimal places do not import properly



*/

DROP TABLE 3CEN040_UVIS_Egress10km;

DROP DATABASE ringoccultations;


SET autocommit=0 ; source C:\Users\joshu\Desktop\FixedRawData\1kSQLfixed\ALPARA098_UVIS_Ingress1km.sql ; COMMIT ;