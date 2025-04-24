# OmegaT Translation Memory Project  
**Patrik Hrabánek**  
**27/03/2025**

## 1. Introduction  
The present project focuses on improving the performance of OmegaT’s TM (Translation Memory) performance and ease of use as a CAT (Computer-Assisted-Translation) tool for heavily specific use cases. Presently, the focus is on translations of academic abstracts within the field of Technology. The languages involved are Czech and English, with the direction of translation being Czech → English. The idea is that if a translation model is trained on highly specific data, the MT within OmegaT will be more accurate than other APIs (e.g., Google Translate v2) and using OmegaT will become easier and more effective in these contexts. Additionally, the TM of OmegaT will improve based on these already improved machine translations.

### 1.1. Corpus  
The corpus chosen to facilitate the present project was the Czech and English abstracts of ÚFAL papers (Rosa, 2016) corpus. A corpus with a high degree of specificity was needed, as training a model on highly specific data was likely to increase performance in translation tasks involving that same highly specific type of data. In this case, the data used were academic abstracts from the Institute of Formal and Applied Linguistics of Charles University. These abstracts often focus on topics within Machine Translation, creation and administration of language corpora, Text Processing, Machine Learning etc. Consequently, many abstracts share a common structure and contain highly specific technical jargon. This makes the data ideal for specializing a Machine Translation model through learning.

### 1.2. Machine Translation Model  
The model picked for additional training had to be a pre-trained model that can handle at least basic Czech to English translation on its own. After careful considerations of various possible Neural Machine Translation models, it was decided to select MarianMT, specifically the HelsinkiNLP-/opus-mt-cs-en version. It’s part of the Helsinki-NLP model family on Hugging Face, which has been specifically trained on a variety of language combinations. For Czech-to-English, the present model has already been trained on substantial parallel corpora (such as the OPUS corpus), providing strong out-of-the-box performance for translation between these two languages. Because it’s based on transformer architecture, it allows MarianMT to handle long-range dependencies in sentences, making it well-suited for translations which require careful focus on word order, grammatical structure (e. g., the case system in Czech), and context. MarianMT is also open-source, allowing for modifications or fine-tuning within specific domains to improve performance. Therefore, the choice to use this translation model made most sense.

## 2. Training  
In order to train the model, pairs of text from the chosen corpus were imported as a .csv file with original Czech text in column ‘cs’ and translated English text in column ‘en’. The first half of the abstracts in our corpus (n=1216 pairs of Czech abstracts with corresponding English translations) were used to train the model, while the second half (n=1435) was used for performance evaluation. Next, the correct tokenizer and model were loaded from transformers. Finally, the training arguments were set (e. g., learning rate, weight decay, number of epochs). Google Colab was used for training, as it provides easy and free access to GPUs for ML purposes.

## 3. Performance Evaluation  
Several metrics were used to assess whether performance improved post-training (e.g., ROUGE, ChrF, BLEU). However, the main focus was on the BLEU metric as it provides a strong indication of how well the translation retains the meaning and structure of the original text through measuring how many n-grams in the machine-translated output overlap with n-grams in reference translations. The BLEU scores can be seen below:

**CORRECT ANALYSIS:**  
- Untrained BLEU Score: 18.93076293683068  
- Trained BLEU Score: 25.48179861663984  

Even though the difference in BLEU scores does not seem to be large, the performance of the model improved by 34.61%, which is a significant result.

## 4. Integration into OmegaT  
In the next step, our trained model needed to be usable within the OmegaT environment. Natively, OmegaT allows for the use of MT via APIs (e. g., Google Translate v2, DeepL…), therefore creation of our own API was necessary. This was easily done using the Flask package. As this project’s goal was to simply test whether our trained model performs better within OmegaT, a locally run API was chosen. However, there was no direct way to access this API, as OmegaT only contained native options. Therefore, a workaround which would allow for addition of non-native MT pipelines was needed. Thankfully, this could be solved with the OmegaT FakeMT plugin, installed in the program’s directory. Lastly, the API needed to be run on a separate port within Python.

## 5. Performance in OmegaT  
The trained model works flawlessly within OmegaT, suggesting automatic translations immediately after selecting a new line of text to be translated. Translations make sense and the whole process works seamlessly.

### 5.1. Comparison with Google Translate API  
OmegaT allows for running multiple MT options through APIs. When compared to the Google Translate v2 API, the output is generally slightly less accurate, and the style is less ‘academic’. Furthermore, there is a noticeable delay between the appearance of Google Translate’s suggested translation and the locally run translation, especially with longer text. It should be noted that this might be subjected to individual performance depending on the machine used. Most importantly though, the trained model can be run locally and for free.

Below some improvements and drawbacks as compared to Google Translate v2 are shown:

**Improvements:**  
- **Voice – passive vs. active**  
  - *Podúloha 1 byla zaměřená na rozdělování 5 miliónů slov v 9 jazycích (čeština, angličtina, španělština, maďarština, francouzština, italština, ruština, latina, mongolština).*  
    - Sub-task 1 was focused on splitting 5 million words in 9 languages (Czech, English, Spanish, Hungarian, French, Italian, Russian, Latin, Mongolian).  
    - **Fake MT:** Subtask 1 focused on segmenting 5 million words in 9 languages (Czech, English, Spanish, Hungarian, French, Italian, Russian, Latin, Mongolian).  

**Drawbacks:**  
- **Problems with identifying the subject**  
  - *Zúčastnilo se 13 systémů od 7 týmů, přičemž nejlepší systém dosáhl průměrné úspěšnosti 97.29% F1, s rozsahem hodnot od 93.84% pro angličtinu po 99.38% pro latinu.*  
    - It participated in 13 systems from 7 teams, with the best system reaching an average accuracy of 97.29% F1 ranging from 93.84% for English to 99.38% for Latin.  
    - **Fake MT:** 13 systems from 7 teams participated, with the best system achieving an average success rate of 97.29% F1, with a range of values from 93.84% for English to 99.38% for Latin.  

- **Problems with word order, especially in short sentences**  
  - *Zúčastnilo se 10 systémů od 3 týmů.*  
    - Ten systems participated from three teams.  
    - **Fake MT:** 10 systems from 3 teams participated.  

- **Minor spelling errors**  
  - *Prezentace* translated as *Prezentation*  

- **Problems with capital letters**  
  - FakeMT assumes that everything is a full sentence  

- **Over-reliance on the modal verb ‘can’**

## 6. References  
Rosa, R. (2016). Czech and English abstracts of ÚFAL papers. LINDAT/CLARIAH-CZ digital library at the Institute of Formal and Applied Linguistics (ÚFAL), Faculty of Mathematics and Physics, Charles University, http://hdl.handle.net/11234/1-1731.
