import pandas as pd
import argparse

def main():
    parser = argparse.ArgumentParser(description='Convert the BrainSwipes CSV results file to a TSV file following HBCD specs.')
    parser.add_argument('input_csv', type=str, help='Path to the input CSV file')
    args = parser.parse_args()

    df = pd.read_csv(args.input_csv)
    df_tsv = pd.DataFrame()

    df_tsv['ID'] = df['sample'].str.split('_').str[0]
    df_tsv['visit'] = df['sample'].str.split('_').str[1]
    df_tsv['file'] = df['sample']
    df_tsv['average_vote'] = df['aveVote']
    df_tsv['nrev'] = df['count']

    df_tsv.to_csv('img_swipes_qc.tsv', index=None, sep='\t')

if __name__ == "__main__":
    main()
