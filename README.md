# abstracts
Training a pre-trained MarianMT model on data from academic abstracts in order to improve translation ease and performance within OmegaT

# Introduction

The project aims to enhance OmegaT’s performance by integrating a custom-trained neural machine translation model. The focus is on improving translations in Czech → English academic abstracts related to Technology, particularly in the fields of Machine Translation, Text Processing, and Machine Learning. By training a model on highly specific data, we expect the MT model to provide more accurate translations in this academic domain, leading to improved performance and usability in OmegaT.

# Corpus

The chosen corpus for training and testing this model is the Czech and English abstracts of ÚFAL papers (Rosa, 2016). This corpus consists of academic abstracts from the Institute of Formal and Applied Linguistics (ÚFAL) at Charles University, focusing on topics such as Machine Translation, language corpora, and Text Processing. These abstracts often contain highly specific technical jargon, making them ideal for training a domain-specific MT model.

# Machine Translation Model

The machine translation model selected for this project is MarianMT, specifically the Helsinki-NLP/opus-mt-cs-en version, which was pre-trained on a wide range of language pairs, including Czech and English. This model is based on the transformer architecture, which allows for better handling of sentence structure, word order, and grammatical intricacies (e.g., the Czech case system).

Key Benefits of MarianMT:
Multilingual capabilities with existing pre-trained models.
Transformer-based architecture for improved translation quality.
Open-source for easy customization and fine-tuning.
MarianMT's ability to be fine-tuned with domain-specific data makes it an ideal choice for this project.

# Training

To train the model, pairs of text from the ÚFAL corpus were imported as a .csv file, with the Czech text in the cs column and the corresponding English text in the en column. The training dataset consisted of the first half of the abstracts (1216 pairs), while the second half (1435 pairs) was used for performance evaluation.

The training process involved:

Loading the appropriate tokenizer and model from the transformers library.
Setting training arguments (e.g., learning rate, weight decay, epochs).
Using Google Colab for training, providing free access to GPUs.

# Performance Evaluation

To evaluate the trained model's performance, several metrics were used, with a particular focus on the BLEU score. The BLEU score measures the overlap of n-grams between the machine-translated text and reference translations. The following BLEU scores were recorded:

Untrained Model BLEU Score: 18.93
Trained Model BLEU Score: 25.48
This indicates an improvement of 34.61%, a significant enhancement in translation quality after fine-tuning the model on domain-specific data.

# Integration into OmegaT

The next step was integrating the trained model into the OmegaT environment. OmegaT natively supports MT via APIs (e.g., Google Translate, DeepL), but custom models require an additional setup.

A local Flask API was created to serve the trained model, which was then integrated into OmegaT using the FakeMT plugin. This plugin allows non-native MT systems to be used in OmegaT, making the locally trained model accessible for real-time translation tasks.

The trained model runs on a separate port within Python, providing local, free, and efficient translations.
Performance in OmegaT

Once integrated, the trained model performs seamlessly within OmegaT, suggesting translations immediately after a line of text is selected for translation. The translations are relevant and contextually accurate, showing how the domain-specific training improved the model’s output.

# Comparison with Google Translate API
When compared to the Google Translate v2 API, the trained model shows:

Slightly improved accuracy, especially for academic text.
Better handling of grammatical structures (e.g., voice: passive vs. active).
Faster processing time with no noticeable delay, as the model runs locally.

## Improvements:

The model correctly handles passive vs. active voice and more complex syntactic structures typical in academic abstracts.


## Drawbacks:

Some word order issues can still arise, especially in short sentences.
Spelling and capitalization errors occasionally occur.
Over-reliance on certain modal verbs (e.g., 'can').

# References

Rosa, R. (2016). Czech and English abstracts of ÚFAL papers. LINDAT/CLARIAH-CZ digital library at the Institute of Formal and Applied Linguistics (ÚFAL), Faculty of Mathematics and Physics, Charles University, http://hdl.handle.net/11234/1-1731.
