from seqbio.calculation.SeqCal import countBase,gcContent,atContent,countBasesDict
from seqbio.pattern.SeqPattern import cpgSearch,enzTargetsScan
from seqbio.seqMan.dnaconvert import complementSeq, reverseComplementSeq,dna2rna,dna2protein,loadCodons

def argparserLocal():
    from argparse import ArgumentParser
    parser = ArgumentParser(prog='myseq', description='Work with sequence')

    subparsers = parser.add_subparsers(
        title='commands', description='Please choose command below:',
        dest='command'
    )
    subparsers.required = True

    # Transcription command
    parser_transcription = subparsers.add_parser('transcription', help="Convert DNA->RNA")
    parser_transcription.add_argument('--seq', '-s', required=True, help="Provide sequence")
    parser_transcription.add_argument('--revcomp', '-r', action='store_true', help="Use reverse complement")
 

    # Translation command
    parser_translation = subparsers.add_parser('translation', help="Convert DNA->Protein")
    parser_translation.add_argument('--seq', '-s', required=True, help="Provide sequence")
    parser_translation.add_argument('--revcomp', '-r', action='store_true', help="Use reverse complement")


    # GC Content command
    parser_gccontent = subparsers.add_parser('gcContent', help="Calculate GC content")
    parser_gccontent.add_argument('--seq', '-s', required=True, help="Provide sequence")


    # Count Bases command
    parser_countbases = subparsers.add_parser('countBases', help="Count number of each base")
    parser_countbases.add_argument('--seq', '-s', required=True, help="Provide sequence")
    parser_countbases.add_argument('--revcomp', '-r', action='store_true', help="Use reverse complement")

    # Enzyme Targets Scan command
    parser_enzscan = subparsers.add_parser('enzTargetsScan', help="Find restriction enzyme")
    parser_enzscan.add_argument('--seq', '-s', required=True, help="Provide sequence")
    parser_enzscan.add_argument('--enzyme', '-e', required=True, help="Enzyme name")
    parser_enzscan.add_argument('--revcomp', '-r', action='store_true', help="Use reverse complement")

    return parser

def main():
    parser = argparserLocal()
    args = parser.parse_args()

    if args.seq == None:
        print("------\nError: You do not provide -s or --seq\n------\n")
    else:
        seq = args.seq.upper()
    # Input
    # seq = 'ATGGGccGTAGAATTCTTGCaaGCCCGT'

    if args.command == 'gcContent':
        if args.seq == None:
            exit(parser.parse_args(['gcContent','-h']))
        print("Input",args.seq,"\nGC content =", gcContent(seq) )

    elif args.command == 'countBases':
        if args.seq is None:
            exit(parser.parse_args(['countBases', '-h']))

        if args.revcomp:
            rev_seq = reverseComplementSeq(seq)  
            print("Input", seq, "\ncountBases =", countBasesDict(rev_seq))  
        else:
            print("Input", seq, "\ncountBases =", countBasesDict(seq)) 

    elif args.command == 'cpgScan':
        if args.seq == None:
            exit(parser.parse_args(['cpgScan','-h']))
        print("Input",args.seq,"\ncpgScan =", cpgSearch(seq) )    

    elif args.command == 'enzTargetsScan':
        if args.seq is None:
            exit(parser.parse_args(['enzTargetsScan','-h']))
        if args.revcomp:
            seq = reverseComplementSeq(seq)
        ecoRI_sites = enzTargetsScan(seq, args.enzyme)
        print("Input", args.seq, "\nEcoRI sites =", ecoRI_sites)
        
    elif args.command == 'transcription':
        if args.seq is None:
            exit(parser.parse_args(['transcription', '-h']))

        if args.revcomp:
            seq = reverseComplementSeq(seq) 
            print("Input", args.seq, "\nTranscription-revcomp =", dna2rna(seq)) 
        else:
            print("Input", args.seq, "\nTranscription =", dna2rna(seq))

    elif args.command == 'translation':
        if args.seq is None:
            exit(parser.parse_args(['translation', '-h']))

        if args.revcomp:
            seq = reverseComplementSeq(seq) 
            print("Input", args.seq, "\nTranslation-revcomp =", dna2protein(seq)) 
        else:
            print("Input", args.seq, "\nTranslation =", dna2protein(seq))

    else:
        parser.print_help()

if __name__ == '__main__':
    main()

# # Input
# seq = 'ATGGGccGTAGAATTCTTGCaaGCCCGT'
# seq = seq.upper()
# print("Transcription: ", dna2rna(seq))
# print("Transcription-revcomp: ", dna2rna(reverseComplementSeq(seq)))
# print("Translation: ", dna2protein(seq))
# print("Translation-revcomp: ", dna2protein(reverseComplementSeq(seq)))
# print("GC Content:", gcContent(seq))
# print("Count Bases: ", countBasesDict(seq))
# print("Count Bases-revcomp: ", countBasesDict(reverseComplementSeq(seq)))
# print("Search EcoRI: ", enzTargetsScan(seq, 'EcoRI'))
# print("Search EcoRI-revcomp: ", enzTargetsScan(reverseComplementSeq(seq), 'EcoRI'))