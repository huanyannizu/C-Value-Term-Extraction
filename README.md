# C-Value-Term-Extraction

The original file 'Turku.txt' was tagged by Stanford CoreNLP to Part of Speech, which gave out 'Turku-tagged.txt'

#### To extract terms from a tagged file, run the following command in the terminal:
>python3 Main.py path to /Turku-tagged.txt ligui_filter L freq_threshold C-Value_threshld

#### Parameters in the above command:
- ligui_filter: the linguistic filter, can be Noun or AdjNoun or AdjPrepNoun
- L: the expected maximum length of a term
- freq_threshold: the frequency threshold 
- C-Value_threshld: the C-value threshold

The program will print out terms with the top-10 C-value.

#### Example of running using Noun filter
<img width="789" alt="screen shot 2017-12-24 at 6 54 32 pm" src="https://user-images.githubusercontent.com/18735754/34328005-148f3c08-e8dc-11e7-99df-9b2d7167da9c.png">

#### Example of running using AdjNoun filter
<img width="808" alt="screen shot 2017-12-24 at 6 54 51 pm" src="https://user-images.githubusercontent.com/18735754/34328125-b5880426-e8de-11e7-9650-a994dc978fc1.png">

#### Example of running using AdjPrepNoun filter
<img width="832" alt="screen shot 2017-12-24 at 7 22 29 pm" src="https://user-images.githubusercontent.com/18735754/34328165-d57e5b30-e8df-11e7-9cc5-26b0dd0dc8aa.png">
