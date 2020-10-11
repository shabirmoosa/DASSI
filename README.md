# DASSI

DASSI: Differential Architecture Search for Splice Identification in genomic DNA



Model Testing:

cd testing/

python test.py --typ <acc,don> --test_file <path to test seq file> --data <hs,athaliana,celegans,dmelanogaster>

for example : testing on donor sites for homo sapiens

python test.py --typ don --test_file ../data/asp/test_hs_don_seq.txt --data hs
