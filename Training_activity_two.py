import argparse
import logging

logging.basicConfig(filename='TA2.log', 
                    encoding='utf-8', 
                    level=logging.DEBUG,
                    format='[%(asctime)s]%(levelname)s- %(message)s',
                    datefmt='%H:%M:%S'
                    )
console = logging.StreamHandler()                   
console.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(levelname)-8s %(message)s')
console.setFormatter(formatter) 
logging.getLogger('').addHandler(console) 
logger = logging.getLogger(__name__)

bases = ["A","T","G","C","a","t","g","c"]

def main(file):
    dna_sequence = open_dna_sequence(file)

def open_dna_sequence(file):

    dna_sequence = []
    
    for count, base in enumerate(file.read(), start=1):
        if base not in bases:
            logging.error(f"Invalid base in file at pos {count}")
            exit(1)
        else:
            dna_sequence.append(base) 
    
    logging.info(f"The number of bases in the sequence is {len(dna_sequence)}")    
    
    if (len(dna_sequence)/3).is_integer():
        logging.info("File contains appropriate number of bases")
    else:
        logging.error("Incorrect number of bases in sequence file")

    return dna_sequence

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert DNA sequence to protein sequence\n')
    parser.add_argument('-f', '--file', help='Insert file here', required=True)
    args = vars(parser.parse_args())
    file = open(args['file'])
    main_runner = main(file)
