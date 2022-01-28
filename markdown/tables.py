import pandas as pd 


def df_to_md(df, output_md, mode='w', caption=' '):

    """
    
    function
    ---------
    Converts a Pandas DataFrame to a formated Markdown table

    parameters
    ---------
    df (required): Pandas DataFrame table
    ouput_md (required): ouput filname (eg. 'mymarkdown.md')
    mode (optional): 'w' to create/overwrite output_md (default), or 'a' to append to output_md
    caption (optional): string to caption the table as

    """

    f = open(output_md, mode)
    rows, cols = df.shape

    # Create caption 
    if caption != ' ':
        f.write("\n### " + caption + "\n")

    # Create header
    f.write('| ')
    for head in df.columns:
        f.write(head + ' | ')
    f.write('\n| :--- ')
    for _ in range(cols-2):
        f.write('| :----: ')
    f.write('| ---: |\n')

    # Enter contents
    for i in range(rows):
        f.write('| ')
        for j in range(cols):
            f.write(str(df.iloc[i, j]) + ' | ')
        f.write('\n')


def csv_to_md(input_csv, output_md, mode='w', caption=' '):
    
    """

    function
    ---------
    Converts a csv to a formated Markdown table

    parameters
    ---------
    input_csv (required): input filename (eg. 'results.csv')
    ouput_md (required): ouput filname (eg. 'mymarkdown.md')
    mode (optional): 'w' to create/overwrite output_md (default), or 'a' to append to output_md
    caption (optional): string to caption the table as

    """

    df = pd.read_csv(input_csv)
    df_to_md(df, output_md, mode=mode, caption=caption)
