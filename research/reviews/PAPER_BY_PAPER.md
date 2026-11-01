# Paper-by-paper first-pass evidence

This dossier records abstracts and algorithmically selected body passages that were inspected. Passage selectors are heuristic: a method-oriented passage can come from introductory context, and an evaluation-oriented passage can be a table caption or setup rather than an experimental result. The dossier does not assert that all methods, tables, appendices, or every sentence were read. Core architectural claims rely on the additional scoped checks in CORE_FINDINGS.md. Author-reported results are not reproduced results. Excluded records do not count toward the retained corpus.

The HTML-fallback STAG method entry is a reviewer paraphrase; its conclusion passage is extracted. Other excerpt fields below are extracted text, possibly truncated.

## 1. Auto Spell Suggestion for High Quality Speech Synthesis in Hindi

ID: `1402.3648` | Theme: Evaluation/reliability | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/1402.3648

Snapshot SHA-256: `c4f891725fdb0925bb68ed707721d4dadead01aed3093daee80fb3b1a1fac6c2`

Abstract extract: The goal of Text-to-Speech (TTS) synthesis in a particular language is to convert arbitrary input text to intelligible and natural sounding speech. However, for a particular language like Hindi, which is a highly confusing language (due to very close spellings), it is not an easy task to identify errors/mistakes in input text and an incorrect text degrade the quality of output speech hence this paper is a contribution to the development of high quality speech synthesis with the involvement of Spellchecker which generates spell suggestions for misspelled words automatically. Involvement of spellchecker would increase the efficiency of speech synthesis by providing spell suggestions for incorr

**Method-oriented passage (PDF p. 2)**

3.2 Spellchecker A Spellchecker is a program to locate misspelled word and notify user about the misspellings. Depending on the spellchecker, the feature may either auto correct the word or allow the user to select from list of predicted suggestions of misspelled word. Approach we have used for implementing spellchecker is Dictionary based where we compared every word with list of thousands of properly spelled words to determine most approximated words of misspelled word. For example:

**Results-oriented passage (PDF p. 2)**

In above example, Hindi text input has some incorrect words like and and can be corrected by using Dictionary based spellchecker. Now corrected text is further processed and synthesised which results in high quality speech.

**Caveat-oriented passage (PDF p. 3)**

3.4 Grapheme to Phoneme Conversion (G2P Conversion) Grapheme is smallest unit in script similarly phoneme is smallest unit in speech. In [8] Hindi, words are not pronounced in the same way as it is scripted so to provide naturalness in speech it is required to convert grapheme into phoneme to generate phonetic information. But the greatest challeng

## 2. DNN-based Speech Synthesis for Indian Languages from ASCII text

ID: `1608.05374` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/1608.05374

Snapshot SHA-256: `0213683f149322c41b3b2af04c213ac8bb195bdfab2df6258a0247344c5b7727`

Abstract extract: Text-to-Speech synthesis in Indian languages has a seen lot of progress over the decade partly due to the annual Blizzard challenges. These systems assume the text to be written in Devanagari or Dravidian scripts which are nearly phonemic orthography scripts. However, the most common form of computer interaction among Indians is ASCII written transliterated text. Such text is generally noisy with many variations in spelling for the same word. In this paper we evaluate three approaches to synthesize speech from such noisy ASCII text: a naive Uni-Grapheme approach, a Multi-Grapheme approach, and a supervised Grapheme-to-Phoneme (G2P) approach. These methods first convert the ASCII text to a ph

**Method-oriented passage (PDF p. 3)**

Duration Model: For duration modeling, the input com- prises binary features (xp) derived from a subset of the ques- tions used by the decision-tree clustering in the standard HTS synthesiser. Similar to [20, 21], frame-aligned data for DNN training is created by forced alignment using the HMM sys- tem. The output is an eight-dimensional vector (yp) of durations for every phone, comprising ﬁve sub-state durations, the over- all phone duration, syllable duration and whole word duration. We use this form of multi-task learning to improve the model; the three additional features (phone, syllable, and word dura- tions) act as a secondary task to 

**Results-oriented passage (PDF p. 4)**

Table 3: Objective results of the proposed techniques versus the benchmark approach. MCD and BAP are Mel-Cepstral Distortion and Band Aperiodicity distortion, respectively. V/UV error means frame-level voiced/unvoiced prediction error. Root Mean Squared Error (RMSE) of F0 was calculated on a linear frequency scale.

**Caveat-oriented passage (PDF p. 3)**

Our languages of interest are Hindi, Tamil and Telugu, all of which are widely-spoken Indian languages. We train and test on the 2015 Blizzard Challenge data which contains about four hours of speech and corresponding text for each language. The data-set contains 1710 utterances for Hindi, 1462 utterances for Tamil, and 2481 utterances for Telugu, 

## 3. Active Learning for Speech Recognition: the Power of Gradients

ID: `1612.03226` | Theme: Loop/data selection | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/1612.03226

Snapshot SHA-256: `8475795b62187d16625ed7ea7d73203d5039ef345e25ddfafe78c7a2f5f4e0c8`

Abstract extract: In training speech recognition systems, labeling audio clips can be expensive, and not all data is equally valuable. Active learning aims to label only the most informative samples to reduce cost. For speech recognition, confidence scores and other likelihood-based active learning methods have been shown to be effective. Gradient-based active learning methods, however, are still not well-understood. This work investigates the Expected Gradient Length (EGL) approach in active learning for end-to-end speech recognition. We justify EGL from a variance reduction perspective, and observe that EGL's measure of informativeness picks novel samples uncorrelated with confidence scores. Experimentally,

**Method-oriented passage (PDF p. 2)**

In [4], EGL was applied to active learning on sequence labeling tasks, but our work is the ﬁrst we know of to apply EGL to speech recognition in particular. Gradient-based methods have also found applications outside active learning. For example, [9] suggests that in stochastic gradient descent, sampling training instances with probabilities proportional to their gradient lengths can speed up convergence. From the perspective of variance reduction, this importance sampling problem shares many similarities to problems found in active learning.

**Results-oriented passage (PDF p. 4)**

We implement EGL by marginalizing over the most likely 100 labels, and compare it with: 1) a random selection baseline, 2) entropy, and 3) pCTC. Using the same base model, each method queries a variable percentage of the unlabeled dataset. The queries are then included into training set, and the model continues training until convergence. Fig. 1 reports the metrics (Exact values are reported in Table 1 in the Appendix) on the test set as the query percentage varies. All the active learning methods outperform the random baseline. Moreover, EGL shows a steeper, more rapid reduction in error than all other approaches. Speciﬁcally, when querying 

**Caveat-oriented passage (PDF p. 1)**

In training speech recognition systems, labeling audio clips can be expensive, and not all data is equally valuable. Active learning aims to label only the most in- formative samples to reduce cost. For speech recognition, conﬁdence scores and other likelihood-based active learning methods have been shown to be effective. Gradient-based active lear

## 4. On Calibration of Modern Neural Networks

ID: `1706.04599` | Theme: Evaluation/reliability | Status: `selected_fulltext_review_plus_scoped_core_crosscheck`

Source: https://arxiv.org/pdf/1706.04599

Snapshot SHA-256: `cb654a65acb785ed4387d6c2db1301d065075dddc2d363676836a2f2a14bc50d`

Abstract extract: Confidence calibration -- the problem of predicting probability estimates representative of the true correctness likelihood -- is important for classification models in many applications. We discover that modern neural networks, unlike those from a decade ago, are poorly calibrated. Through extensive experiments, we observe that depth, width, weight decay, and Batch Normalization are important factors influencing calibration. We evaluate the performance of various post-processing calibration methods on state-of-the-art architectures with image and document classification datasets. Our analysis and experiments not only offer insights into neural network learning, but also provide a simple and

**Method-oriented passage (PDF p. 5)**

Platt scaling (Platt et al., 1999) is a parametric approach to calibration, unlike the other approaches. The non- probabilistic predictions of a classiﬁer are used as features for a logistic regression model, which is trained on the val- idation set to return probabilities. More speciﬁcally, in the context of neural networks (Niculescu-Mizil & Caruana, 2005), Platt scaling learns scalar parameters a, b ∈R and outputs ˆqi = σ(azi + b) as the calibrated probability. Pa- rameters a and b can be optimized using the NLL loss over the validation set. It is important to note that the neural network’s parameters are ﬁxed during this stage.

**Results-oriented passage (PDF p. 7)**

Calibration Results. Table 1 displays model calibration, as measured by ECE (with M = 15 bins), before and af- ter applying the various methods (see Section S3 for MCE, NLL, and error tables). It is worth noting that most datasets and models experience some degree of miscalibration, with ECE typically between 4 to 10%. This is not architecture speciﬁc: we observe miscalibration on convolutional net- works (with and without skip connections), recurrent net- works, and deep averaging networks. The two notable ex- ceptions are SVHN and Reuters, both of which experience ECE values below 1%. Both of these datasets have very low error (1.98% and 2.

**Caveat-oriented passage (PDF p. 4)**

Weight decay, which used to be the predominant regu- larization mechanism for neural networks, is decreasingly utilized when training modern neural networks. Learning theory suggests that regularization is necessary to prevent overﬁtting, especially as model capacity increases (Vapnik, 1998). However, due to the apparent regularization effects of B

Additional interpretation and limitations: [core findings](CORE_FINDINGS.md).

## 5. Automated Audio Captioning with Recurrent Neural Networks

ID: `1706.10006` | Theme: Captioning/grounding | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/1706.10006

Snapshot SHA-256: `ac79b31b5a7122e39e6718e24d6f4b0a4afc35c6c32be31938c96cb8825ac38d`

Abstract extract: We present the first approach to automated audio captioning. We employ an encoder-decoder scheme with an alignment model in between. The input to the encoder is a sequence of log mel-band energies calculated from an audio file, while the output is a sequence of words, i.e. a caption. The encoder is a multi-layered, bi-directional gated recurrent unit (GRU) and the decoder a multi-layered GRU with a classification layer connected to the last GRU of the decoder. The classification layer and the alignment model are fully connected layers with shared weights between timesteps. The proposed method is evaluated using data drawn from a commercial sound effects library, ProSound Effects. The resulti

**Method-oriented passage (PDF p. 2)**

bits sample width) and creates a textual description (i.e. cap- tion) for it. At ﬁrst a matrix of features, X ∈RT ×Nfeats, is extracted from the audio ﬁle. Each row of the matrix X con- tains the extracted features from the input audio ﬁle in frame t. The matrix X is used as an input to a neural network, which outputs a matrix Y ∈RI×Nwords. Each each row of the out- put matrix Y contains the probability distribution over unique words. Then, we pick the most probable word according to each row of the output matrix, creating a sequence of words. The resulting sequence of words is the caption of the input audio ﬁle. For feature extraction, the i

**Results-oriented passage (PDF p. 3)**

In order to evaluate our method, we employ the audio data and their corresponding captions from PSE library [3]. This library consists of 175,000 sound recordings distributed over 501 categories in total, e.g. ambience, audience, foley, na- ture, wildlife, sports, transportation and weather. The audio recordings in the PSE library are inconsistent in terms of sam- pling rate, number of channels, and sample width. In order to have consistency in the data we used recordings with sam- pling rate of at least 44.1 kHz, maximum two channels, and sample width of at least 16 bits. This resulted in 153 220 recordings. All 153 220 recordings were proce

**Caveat-oriented passage (PDF p. 4)**

In the present work, we proposed the ﬁrst method for auto- mated audio captioning. The method is based on an encoder- decoder scheme with an attentional layer in between them. The method was evaluated using a commercial dataset of recordings, each of which is associated with a textual de- scription (caption) within the dataset. The evaluation of th

## 6. Natural TTS Synthesis by Conditioning WaveNet on Mel Spectrogram Predictions

ID: `1712.05884` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/1712.05884

Snapshot SHA-256: `7609c6af1f6cf7649747a0b28d4fc50e7bf523cd6c9b756bb6791635d5c9c029`

Abstract extract: This paper describes Tacotron 2, a neural network architecture for speech synthesis directly from text. The system is composed of a recurrent sequence-to-sequence feature prediction network that maps character embeddings to mel-scale spectrograms, followed by a modified WaveNet model acting as a vocoder to synthesize timedomain waveforms from those spectrograms. Our model achieves a mean opinion score (MOS) of $4.53$ comparable to a MOS of $4.58$ for professionally recorded speech. To validate our design choices, we present ablation studies of key components of our system and evaluate the impact of using mel spectrograms as the input to WaveNet instead of linguistic, duration, and $F_0$ feat

**Method-oriented passage (PDF p. 2)**

While linear spectrograms discard phase information (and are therefore lossy), algorithms such as Grifﬁn-Lim [14] are capable of estimating this discarded information, which enables time-domain conversion via the inverse short-time Fourier transform. Mel spectro- grams discard even more information, presenting a challenging in- verse problem. However, in comparison to the linguistic and acoustic features used in WaveNet, the mel spectrogram is a simpler, lower- level acoustic representation of audio signals. It should therefore be straightforward for a similar WaveNet model conditioned on mel spectrograms to generate audio, essentially as a n

**Results-oriented passage (PDF p. 3)**

When generating speech in inference mode, the ground truth targets are not known. Therefore, the predicted outputs from the previous step are fed in during decoding, in contrast to the teacher-forcing conﬁguration used for training. We randomly selected 100 ﬁxed examples from the test set of our internal dataset as the evaluation set. Audio generated on this set are sent to a human rating service similar to Amazon’s Mechanical Turk where each sample is rated by at least 8 raters on a scale from 1 to 5 with 0.5 point increments, from which a subjective mean opinion score (MOS) is calculated. Each evaluation is conducted independently from each

**Caveat-oriented passage (PDF p. 4)**

results by 0.142 ± 0.338. Examination of rater comments shows that our neural system tends to generate speech that feels more natural and human-like, but it sometimes runs into pronunciation difﬁculties, e.g., when handling names. This result points to a challenge for end-to-end approaches – they require training on data that cover intended usage.

## 7. Style Tokens: Unsupervised Style Modeling, Control and Transfer in End-to-End Speech Synthesis

ID: `1803.09017` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/1803.09017

Snapshot SHA-256: `a5c7640e71c1ec6a69b78c8ece44c6954c24b419c10b148b79d36b3ce4960b9a`

Abstract extract: In this work, we propose "global style tokens" (GSTs), a bank of embeddings that are jointly trained within Tacotron, a state-of-the-art end-to-end speech synthesis system. The embeddings are trained with no explicit labels, yet learn to model a large range of acoustic expressiveness. GSTs lead to a rich set of significant results. The soft interpretable "labels" they generate can be used to control synthesis in novel ways, such as varying speed and speaking style - independently of the text content. They can also be used for style transfer, replicating the speaking style of a single audio clip across an entire long-form text corpus. When trained on noisy, unlabeled found data, GSTs learn to

**Method-oriented passage (PDF p. 1)**

In this work, we propose “global style tokens” (GSTs), a bank of embeddings that are jointly trained within Tacotron, a state-of-the-art end-to- end speech synthesis system. The embeddings are trained with no explicit labels, yet learn to model a large range of acoustic expressiveness. GSTs lead to a rich set of signiﬁcant results. The soft interpretable “labels” they generate can be used to control synthesis in novel ways, such as varying speed and speaking style – independently of the text content. They can also be used for style transfer, replicating the speaking style of a single audio clip across an entire long-form text corpus. When tra

**Results-oriented passage (PDF p. 7)**

To demonstrate this, we run inference using a manually- identiﬁed clean style token (scaled to 0.3), and then evaluate the output using MOS naturalness tests. We use the same 100-phrase evaluation set as (Wang et al., 2017a), collecting 8 ratings each from crowdsourced native speakers. Table 2 shows MOS results for both a baseline Tacotron and a “clean-token” GST model. While the baseline Tacotron achieves a 4.0 MOS when the dataset is 100% clean, MOS decreases as interference increases, dropping to a low score of 1.353. Because the model has no prior knowledge of speech or noise, it blindly models all statistics in the train- ing set, result

**Caveat-oriented passage (PDF p. 3)**

While we use content-based attention as a similarity mea- sure in this work, it is trivial to substitute alternatives. Dot- product attention, location-based attention, or even combi- nations of attention mechanisms may learn different types of style tokens. In our experiments, we found that using multi- head attention (Vaswani et al., 2017) signiﬁ

## 8. Neural Speech Synthesis with Transformer Network

ID: `1809.08895` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/1809.08895

Snapshot SHA-256: `55212e20379ee183e470627b718cf0c4932b08efbedb9c673cd26efc73602624`

Abstract extract: Although end-to-end neural text-to-speech (TTS) methods (such as Tacotron2) are proposed and achieve state-of-the-art performance, they still suffer from two problems: 1) low efficiency during training and inference; 2) hard to model long dependency using current recurrent neural networks (RNNs). Inspired by the success of Transformer network in neural machine translation (NMT), in this paper, we introduce and adapt the multi-head attention mechanism to replace the RNN structures and also the original attention mechanism in Tacotron2. With the help of multi-head self-attention, the hidden states in the encoder and decoder are constructed in parallel, which improves the training efficiency. M

**Method-oriented passage (PDF p. 2)**

sequence of input is ﬁrstly processed with a 3-layer CNN to extract a longer-term context, and then fed into the encoder, which is a bi-directional LSTM. The previous mel spectro- gram frame (the predicted one in inference, or the golden one in training time), is ﬁrst processed with a 2-layer fully connected network (decoder pre-net), whose output is con- catenated with the previous context vector, followed by a 2- layer LSTM. The output is used to calculate the new context vector at this time step, which is concatenated with the out- put of the 2-layer LSTM to predict the mel spectrogram and stop token with two different linear projections r

**Results-oriented passage (PDF p. 5)**

model and one group of recordings. Those MOS tests are rigorous and reliable, as each audio is listened to by at least 20 testers, who are all native English speakers (compar- ing to Tacotron2’s 8 testers in Shen et al. (2017)), and each tester listens less than 30 audios. We train a Tacotron2 model with our internal US English female dataset as the baseline (also use phonemes as input), and gain equal MOS with our model. Therefore we test the comparison mean option score (CMOS) between samples generated by Tacotron2 and our model for a ﬁner contrast. In the comparison mean option score (CMOS) test, testers listen to two audios (generated by 

**Caveat-oriented passage (PDF p. 2)**

where f(·) is a fully connected layer. For translation tasks, this softmax function is among all dimensions of f(st) and calculates the probability of each word in the vocabulary. However, in the TTS task, the softmax function is not re- quired and the hidden states s calculated by decoder are con- sumed directly by a linear projection to obtain th

## 9. Limitations of Source-Filter Coupling In Phonation

ID: `1811.07435` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/1811.07435

Snapshot SHA-256: `b355a0b7b3c46d9169b8cc1e5446a176734e51c5713476b06bdf54dfe153ac74`

Abstract extract: The coupling of vocal fold (source) and vocal tract (filter) is one of the most critical factors in source-filter articulation theory. The traditional linear source-filter theory has been challenged by current research which clearly shows the impact of acoustic loading on the dynamic behavior of the vocal fold vibration as well as the variations in the glottal flow pulses shape. This paper outlines the underlying mechanism of source-filter interactions; demonstrates the design and working principles of coupling for the various existing vocal cord and vocal tract biomechanical models. For our study, we have considered self-oscillating lumped-element models of the acoustic source and computati

**Method-oriented passage (PDF p. 2)**

literature which could produce this favourable condition. The Kelly-Lochbaum model of the vocal tract is traditionally con- structed by approximating the cross-sectional area of the vo- cal tract by cascading multiple cylindrical tube sections [6]. The resulting tube system then could be interpreted as a dig- ital waveguide or digital wave model of the vocal tract. But the severe pitfalls in this model are: 1) length of each of the cylindrical tube section has to be equal. 2) the junction of two tube section is not smooth. These limitations affect the formant frequencies of the articulatory model which in turn prevent to achieve the exact mat

**Results-oriented passage (PDF p. 2)**

Unlike the one-mass model, the two mass model of vo- cal fold [5] has successfully demonstrated the self-oscillating characteristics of the vocal fold. And the oscillation sustains for both the inductive and capacitive load of the vocal tract. Two mass model uses two mass elements per vocal cord and provides the necessary degree-of-freedom to introduce the vertical phase difference in vocal fold edges during oscilla- tion. However, the main disadvantage of both of these models is that their tissue discretization in a coronal plane does not capture the layered structure of the vocal folds. And there is no immediate correlation between the spri

**Caveat-oriented passage (PDF p. 2)**

The limitation in source-ﬁlter interaction for various mod- els has been discussed. One of the signiﬁcant challenges in designing a speech synthesizer model is to address the de- gree of interaction between the vocal fold and vocal tract which varies based on the types of articulatory gestures like singing; breathy voice; male or female voice; high

## 10. Audio Caption: Listen and Tell

ID: `1902.09254` | Theme: Captioning/grounding | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/1902.09254

Snapshot SHA-256: `ff57e7ce1fb1c55360d8a6aea5c9fd407ed0a46141d6decd5a38810f92894333`

Abstract extract: Increasing amount of research has shed light on machine perception of audio events, most of which concerns detection and classification tasks. However, human-like perception of audio scenes involves not only detecting and classifying audio sounds, but also summarizing the relationship between different audio events. Comparable research such as image caption has been conducted, yet the audio field is still quite barren. This paper introduces a manually-annotated dataset for audio caption. The purpose is to automatically generate natural sentences for audio scene description and to bridge the gap between machine perception of audio and image. The whole dataset is labelled in Mandarin and we al

**Method-oriented passage (PDF p. 2)**

labels in our dataset after merging, collected from the answers to Question 1. Most frequent sound belongings and scenes can be seen in Table 2. All labelling results were then translated into English by Baidu Translation to increase the accessibility of the dataset. The collected dataset was divided into a training and develop- ment subset such that the average number of tokens (words) within each subset was roughly equal (see Table 3 and Figure 1).

**Results-oriented passage (PDF p. 3)**

Evaluation Since this dataset uses Chinese labels, the choice of evaluation metrics is limited to language agnostic methods such as BLEU [21]. BLEU can be regarded as a weighted N-gram. In this work, we provide scores up to 4-gram. As seen in Table 3, some utterances contain less than four tokens, which leads to an unstable BLEU score. In cases the system generates a hypothesis < N, we use method 1 of chancherry smoothing [22]. The results in Table 5 are evaluated on the held out development set.

**Caveat-oriented passage (PDF p. 2)**

Source As audio-only information is not sufﬁcient for determin- ing a sound event, we included video clips with sound. All video data were extracted from Youku, Iqiyi and Tencent movies which are video websites equivalent to Youtube. They also have exclu- sive authorization of TV shows, thus some of the video clips were from TV shows and interviews

## 11. LibriTTS: A Corpus Derived from LibriSpeech for Text-to-Speech

ID: `1904.02882` | Theme: Data/Indic speech | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/1904.02882

Snapshot SHA-256: `e6096a735f6bb16edf24cbaf3ce7b20eaa3f1e9b04292ba1c3e27c1c0cfb557d`

Abstract extract: This paper introduces a new speech corpus called "LibriTTS" designed for text-to-speech use. It is derived from the original audio and text materials of the LibriSpeech corpus, which has been used for training and evaluating automatic speech recognition systems. The new corpus inherits desired properties of the LibriSpeech corpus while addressing a number of issues which make LibriSpeech less than ideal for text-to-speech work. The released corpus consists of 585 hours of speech data at 24kHz sampling rate from 2,456 speakers and the corresponding texts. Experimental results show that neural end-to-end TTS models trained from the LibriTTS corpus achieved above 4.0 in mean opinion scores in n

**Method-oriented passage (PDF p. 2)**

3. Non-standard words (e.g., abbreviations, numbers and currency expressions) and semiotic classes [36] (text to- kens and token sequences that represent particular enti- ties that are semantically constrained, such as measure phrases, addresses and dates) in the sentences are de-

**Results-oriented passage (PDF p. 4)**

Table 4 shows the experimental results. It can be seen from the table that LibriTTS (24kHz) achieved the best subjective scores with all speakers. The gaps in MOS between LibriTTS (16kHz) and LibriTTS (24kHz) for female and male speakers were 0.175 and 0.133, respectively. It clearly shows the beneﬁt

**Caveat-oriented passage (PDF p. 2)**

Having appropriate data facilitates exploration of new tasks and research ideas. Table 1 lists publicly available English speech corpora which are used in recent TTS research papers. The CMU ARCTIC corpus [19] has been used for many years in statistical parametric speech synthesis research [28]. However, it is too small to train neural end-to-end T

## 12. VoiceID Loss: Speech Enhancement for Speaker Verification

ID: `1904.03601` | Theme: Evaluation/reliability | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/1904.03601

Snapshot SHA-256: `39a49dc1102e80ca54b34d807bbcb5dbf6a77571bf8e090eaf458e2750381dd0`

Abstract extract: In this paper, we propose VoiceID loss, a novel loss function for training a speech enhancement model to improve the robustness of speaker verification. In contrast to the commonly used loss functions for speech enhancement such as the L2 loss, the VoiceID loss is based on the feedback from a speaker verification model to generate a ratio mask. The generated ratio mask is multiplied pointwise with the original spectrogram to filter out unnecessary components for speaker verification. In the experiments, we observed that the enhancement network, after training with the VoiceID loss, is able to ignore a substantial amount of time-frequency bins, such as those dominated by noise, for verificati

**Method-oriented passage (PDF p. 1)**

In this paper, we propose VoiceID loss, a novel loss function for training a speech enhancement model to improve the ro- bustness of speaker veriﬁcation. In contrast to the commonly used loss functions for speech enhancement such as the L2 loss, the VoiceID loss is based on the feedback from a speaker ver- iﬁcation model to generate a ratio mask. The generated ratio mask is multiplied pointwise with the original spectrogram to ﬁlter out unnecessary components for speaker veriﬁcation. In the experiments, we observed that the enhancement network, after training with the VoiceID loss, is able to ignore a substan- tial amount of time-frequency bi

**Results-oriented passage (PDF p. 3)**

The performance (as shown in Table 2) is based on two types of veriﬁcation model, a model trained using the clean dataset D and a model trained using the augmented dataset D + DN . In the clean setting, both the proposed masking approach and the DAE approach show signiﬁcant improvement. The proposed masking approach shows improvement in all SNR settings con- sistently, but the DAE is only effective under low SNR settings. The relative improvement become marginal if we use the aug- mented model, as shown is the right part of the ﬁgure, but still, the proposed masking approach is effective in almost all cases. We also observe that the proposed 

**Caveat-oriented passage (PDF p. 4)**

ity matrix, as shown in Figure 5. The analysis approach of us- ing frame-level matrix is ﬁrst introduced in [15]. We follow the same approach to compute the matrix before and after enhance- ment using two utterances from the same speaker in the TIMIT dataset, a clean and studio-level dataset. In Figure 5 (a), we see low scores between the different

## 13. Crowdsourcing a Dataset of Audio Captions

ID: `1907.09238` | Theme: Data/Indic speech | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/1907.09238

Snapshot SHA-256: `3ee498065a534a58610293da538799beb11d8de5c25f0eea81cf2b1de923dca0`

Abstract extract: Audio captioning is a novel field of multi-modal translation and it is the task of creating a textual description of the content of an audio signal (e.g. "people talking in a big room"). The creation of a dataset for this task requires a considerable amount of work, rendering the crowdsourcing a very attractive option. In this paper we present a three steps based framework for crowdsourcing an audio captioning dataset, based on concepts and practises followed for the creation of widely used image captioning and machine translations datasets. During the first step initial captions are gathered. A grammatically corrected and/or rephrased version of each initial caption is obtained in second st

**Method-oriented passage (PDF p. 2)**

hampering the diversity of the captions. In both datasets, the di- versity is hampered by the lack of a minimum amount of words in a caption, while in the case of AudioCaps the diversity is further hampered by removing informative sounds about spatial relation- ships (e.g. “inside small room”), and giving the labels from Au- dioSet to the annotators to guide the caption. Additionally, Audio Caption is created by annotators who are not located in an English speaking area, increasing the chance for ﬂaws in the acquired En- glish captions. Finally, in the AudioCaps the assessment of the au- dio captioning methods is hindered by having only one c

**Results-oriented passage (PDF p. 4)**

than that of the initial captions, high frequencies of similarities in the high range might be a result of annotators ﬁxing these errors and therefore not rephrasing the caption. Figure 4 displays a box plot of the cross-similarity values for the Nc selected (i.e. the ﬁnal), the other (i.e. the rest Nc not selected at the third step), and the Nc initial captions. The cross-similarity values for the selected, other, and initial captions are 0.24, 0.20, and 0.14 respectively. From the results it can be inferred that from the ﬁrst step of our framework we indeed get a diverse set of initial captions. Moreover, the results in Figure 4 show that t

**Caveat-oriented passage (PDF p. 2)**

Our proposed framework consists of three serially executed steps, inspired by practices followed in the creation of image captioning and machine translation datasets [8, 7, 17], and which is imple- mented on an online crowdsourcing platform. We employ as poten- tial annotators the registered users of the platform (the total amount of registered use

## 14. Self-Training for End-to-End Speech Recognition

ID: `1909.09116` | Theme: Loop/data selection | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/1909.09116

Snapshot SHA-256: `0d3465efd7953b32c27a2cd2ceaade6f913e440d98cdabdc7e421d70a4177c42`

Abstract extract: We revisit self-training in the context of end-to-end speech recognition. We demonstrate that training with pseudo-labels can substantially improve the accuracy of a baseline model. Key to our approach are a strong baseline acoustic and language model used to generate the pseudo-labels, filtering mechanisms tailored to common errors from sequence-to-sequence models, and a novel ensemble approach to increase pseudo-label diversity. Experiments on the LibriSpeech corpus show that with an ensemble of four models and label filtering, self-training yields a 33.9% relative improvement in WER compared with a baseline trained on 100 hours of labelled data in the noisy speech setting. In the clean sp

**Method-oriented passage (PDF p. 2)**

Model combination often helps reduce word error rates in ASR. One way to utilize multiple models in self-training is to combine the model scores during inference to generate a single pseudo-labelled set with higher quality. However, as M increases, the decoding process becomes heavyweight. Instead, we propose sample ensemble. Given M boot- strapped acoustic models, we generate a pseudo-labelled data set, ¯Dm, for each model in parallel. We then combine all M sets of pseudo-labels with uniform weights and optimize the following objective during training

**Results-oriented passage (PDF p. 3)**

model performance. Label quality is deﬁned as the WER of the ﬁltered pseudo-labels as compared to the ground truth. We apply our heuristic ﬁltering, i.e. “no EOS + n-gram” ﬁlters, with c = 2 and n = 4 and then add conﬁdence-based ﬁltering on top of the ﬁltered data set. We can see that ﬁltering indeed improves the pseudo-label quality as we adjust the threshold on the conﬁdence score. In the clean setting, the heuristic ﬁlter removes 1.8% of the data, and further removal of the worst 10% of the pseudo- labels based on conﬁdence scores results in a 5.2% relative improvement in WER on the dev clean set compared with a baseline without ﬁltering.

**Caveat-oriented passage (PDF p. 4)**

When decoded with an external LM, our best model achieves a WRR over 50% in both clean and noisy speech settings. Table 2 compares our approach with other semi-supervised learning methods with sequence-to-sequence models that use the same audio data setup. We see that our conventional pseudo-labelling approach together with ﬁltering and ensem- ble 

## 15. Clotho: An Audio Captioning Dataset

ID: `1910.09387` | Theme: Data/Indic speech | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/1910.09387

Snapshot SHA-256: `fcd2c0e5577a7e16fd9270b52c9e45d26fbbf122f2bc38dd71f7f690a4a47347`

Abstract extract: Audio captioning is the novel task of general audio content description using free text. It is an intermodal translation task (not speech-to-text), where a system accepts as an input an audio signal and outputs the textual description (i.e. the caption) of that signal. In this paper we present Clotho, a dataset for audio captioning consisting of 4981 audio samples of 15 to 30 seconds duration and 24 905 captions of eight to 20 words length, and a baseline method to provide initial results. Clotho is built with focus on audio content and caption diversity, and the splits of the data are not hampering the training or evaluation of methods. All sounds are from the Freesound platform, and captio

**Method-oriented passage (PDF p. 2)**

nying videos of the audio samples. The perceptual ambiguity of sounds can be ham- pered by providing contextual information (e.g. word labels) to annotators, making them aware of the ac- tual source and not letting them describe their own perceived information. Using visual stimuli (e.g. video) introduces a bias, since annotators may de- scribe what they see and not what they hear. Also, a single caption per ﬁle impedes the learning and evaluation of diverse descriptions of information, and domain-speciﬁc data of previous audio captioning datasets have an observed signiﬁcant impact on the performance of methods [6]. Finally, unique words (i.e

**Results-oriented passage (PDF p. 4)**

The tolerance means, for example, that we can tol- erate a word appearing a total of 3 times in the whole Clotho dataset D, to appear 2 times in the de- velopment split (appearing 0 times in development split results in the rejection of the split set). This will result to this word appearing in either evalua- tion or testing split, but still this word will not ap- pear only in one split. To pick the best set of splits, we count the amount of words that have a frequency f d w /∈[f Dev w −δw, f Dev w +δw]. We score, in an ascending fashion, the sets of splits according to that amount of words and we pick the top 50 ones. For each of the 50 sets

**Caveat-oriented passage (PDF p. 4)**

where αd = 1/f Dev w and αe = 1/0.5f Ev w . We sort all 50 000 sets of splits according to Γ and in ascending fash- ion, and we pick the top one. This set of splits is the ﬁnal split for the Clotho dataset, containing 2893 au- dio samples and 14465 captions in development split, 1045 audio samples and 5225 captions in evaluation split, and 1043 aud

## 16. Indian EmoSpeech Command Dataset: A dataset for emotion based speech recognition in the wild

ID: `1910.13801` | Theme: Evaluation/reliability | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/1910.13801

Snapshot SHA-256: `dcf05b89db98e54e1bffeae8cefc4a748fb66e3a8e39c3814a6845372b1bef52`

Abstract extract: Speech emotion analysis is an important task which further enables several application use cases. The non-verbal sounds within speech utterances also play a pivotal role in emotion analysis in speech. Due to the widespread use of smartphones, it becomes viable to analyze speech commands captured using microphones for emotion understanding by utilizing on-device machine learning models. The non-verbal information includes the environment background sounds describing the type of surroundings, current situation and activities being performed. In this work, we consider both verbal (speech commands) and non-verbal sounds (background noises) within an utterance for emotion analysis in real-life sc

**Method-oriented passage (PDF p. 5)**

Then to get a balanced training set we augmented the keywords with background sound. In the absence of an adequate volume of training data, it is possible to increase the effective size of existing data through the process of data augmentation, which has con- tributed to signiﬁcantly improving the performance of deep networks in the domain of image classiﬁcation. In the case of speech recognition, augmentation traditionally involves deforming the audio waveform used for training in some fashion (e.g., by speeding it up or slowing it down), or adding background noise. This has the effect of making the dataset effectively larger, as multiple au

**Results-oriented passage (PDF p. 2)**

• We perform a comprehensive analysis on keyword detection in varying conditions such as with the presence of background noise, varying emotions and varying environmental conditions. We compare the results with benchmark Speech Command dataset and show a signiﬁcant performance gain of 3.3% in top-one score for keyword spotting.

**Caveat-oriented passage (PDF p. 2)**

The paper is organized as follows. In Sec. 2, we provide the motivation behind this attempt of Indian EmoSpeech dataset curation. In Sec. 3, we deﬁne the characteristic properties associated with the dataset. In Sec. 4, we describe the details related to the dataset collection. In Sec. 5, we provide relevant details on other contemporary datasets i

## 17. Common Voice: A Massively-Multilingual Speech Corpus

ID: `1912.06670` | Theme: Data/Indic speech | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/1912.06670

Snapshot SHA-256: `abda109167628b721e63a61a76f6701dd52a12b19a70cc1f8b3d66108b2dc03c`

Abstract extract: The Common Voice corpus is a massively-multilingual collection of transcribed speech intended for speech technology research and development. Common Voice is designed for Automatic Speech Recognition purposes but can be useful in other domains (e.g. language identification). To achieve scale and sustainability, the Common Voice project employs crowdsourcing for both data collection and data validation. The most recent release includes 29 languages, and as of November 2019 there are a total of 38 languages collecting data. Over 50,000 individuals have participated so far, resulting in 2,500 hours of collected audio. To our knowledge this is the largest audio corpus in the public domain for sp

**Method-oriented passage (PDF p. 2)**

any given speaker may appear in only one. This ensures that contributors seen at train time are not seen at test time, which would skew results. Additionally, repetitions of text sentences are removed from the train, test, and development sets of the corpus.4

**Results-oriented passage (PDF p. 3)**

5.1. Data We made dataset splits (c.f. Table (2)) such that one speaker’s recordings are only present in one data split. This allows us to make a fair evaluation of speaker generaliza- tion, but as a result some training sets have very few speak- ers, making this an even more challenging scenario. The splits per language were made as close as possible to 80% train, 10% development, and 10% test.10

**Caveat-oriented passage (PDF p. 1)**

multilingual (17 languages), and released under an open li- cense (GNU General Public License). However, the Vox- Forge does not have a sustainable data collection pipeline compared to Common Voice, and there is no data valida- tion step in place. M-AILABS data contains 9 language varieties with a modiﬁed BSD 3-Clause License, however there is no c

## 18. PANNs: Large-Scale Pretrained Audio Neural Networks for Audio Pattern Recognition

ID: `1912.10211` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/1912.10211

Snapshot SHA-256: `d9160fa1a23a8609fe9b346897828283981d4640f17a2d79f399094f78dd80a1`

Abstract extract: Audio pattern recognition is an important research topic in the machine learning area, and includes several tasks such as audio tagging, acoustic scene classification, music classification, speech emotion classification and sound event detection. Recently, neural networks have been applied to tackle audio pattern recognition problems. However, previous systems are built on specific datasets with limited durations. Recently, in computer vision and natural language processing, systems pretrained on large-scale datasets have generalized well to several tasks. However, there is limited research on pretraining systems on large-scale datasets for audio pattern recognition. In this paper, we propos

**Method-oriented passage (PDF p. 4)**

In this section, we propose architectures which we call Wavegram-CNN and Wavegram-Logmel-CNN for AudioSet tagging. The Wavegram-CNN we propose is a time-domain audio tagging system. Wavegram is a feature we propose that is similar to log mel spectrogram, but is learnt using a neural network. A Wavegram is designed to learn a time- frequency representation that is a modiﬁcation of the Fourier transform. A Wavegram has a time axis and a frequency axis. Frequency patterns are important for audio pattern recognition, for example, sounds with different pitch shifts belong to the same class. A Wavegram is designed to learn frequency information tha

**Results-oriented passage (PDF p. 5)**

To investigate the generalization ability of PANNs, we transfer PANNs to a range of audio pattern recognition tasks. Previous works on audio transfer learning [21][14][22][25][23] mainly focused on music tagging, and were limited to smaller datasets than AudioSet. To begin with, we demonstrate the training of a PANN in Fig. 2(a). Here, DAudioSet is the AudioSet dataset, and x0, y0 are training input and target, respectively. FCAudioSet is the fully connected layer for AudioSet tagging. In this article, we propose to compare the following transfer learning strategies. 1) Train a system from scratch. All parameters are randomly initialized. Sys

**Caveat-oriented passage (PDF p. 2)**

Audio tagging is an essential task of audio pattern recog- nition, with the goal of predicting the presence or absence of audio tags in an audio clip. Early work on audio tag- ging included using manually-designed features as input, such as audio energy, zero-crossing rate, and mel-frequency cepstrum coefﬁcients (MFCCs) [27]. Generative models, in-

## 19. Audio Codec Enhancement with Generative Adversarial Networks

ID: `2001.09653` | Theme: Representations/codecs | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2001.09653

Snapshot SHA-256: `6f0cb7cc96ac2ad3a7e9787be6fceba7cd55889250247c96df07832cb9479469`

Abstract extract: Audio codecs are typically transform-domain based and efficiently code stationary audio signals, but they struggle with speech and signals containing dense transient events such as applause. Specifically, with these two classes of signals as examples, we demonstrate a technique for restoring audio from coding noise based on generative adversarial networks (GAN). A primary advantage of the proposed GAN-based coded audio enhancer is that the method operates end-to-end directly on decoded audio samples, eliminating the need to design any manually-crafted frontend. Furthermore, the enhancement approach described in this paper can improve the sound quality of low-bit rate coded audio without any 

**Method-oriented passage (PDF p. 2)**

To the best of our knowledge, GANs have not yet been applied to any coded audio enhancement task, so this is the first contribution to demonstrate an adversarial framework to enhance coded audio. Furthermore, we are not aware of any deep learning based coded applause restoration technique. Unlike previous approaches based on generative models, our method works entirely end-to-end, directly on decoded audio samples. Therefore, no manually-crafted features are extracted and, with that, no explicit assumptions about decoded audio are done (i.e. our method is codec-agnostic). The generator architecture is fully 1D-convolutional, thus providing a 

**Results-oriented passage (PDF p. 4)**

We attribute the improvements with our enhancer due to the following. First, the model performs spectral and temporal noise shaping. Second, due to the generative nature of the model, it can perform spectral gap filling (compare spectrograms in Fig. 4). For applause, we did not observe any effect of noise shaping; rather our model performed a transient-to-noise ratio restoration. Specifically, transients and noise were very slightly (between 0 and 1 dB) amplified and attenuated, respectively. This is in line with the manually-crafted method proposed in [6] followed by transient and noise classification. The advantage of our proposed method is

**Caveat-oriented passage (PDF p. 2)**

intelligent gap filling). Recently, autoregressive generative models are being adopted for the purpose. In [10], the authors attempted to reduce artifacts in mp3 using a dilated convolution based Wavenet [16] as the generative model. However, results indicate that white noise is superimposed on the output, indicating that the method does not guaran

## 20. Study of human phonation in a full body domain

ID: `2005.02168` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2005.02168

Snapshot SHA-256: `a8411e8d879bd5fa9b9a232812adf9a15ce23aa76422f6d7d90c4d9eb7d9eec8`

Abstract extract: The Generation and propagation of the human voice is studied in two-dimensions using a full-body domain, using direct numerical simulation. The fluid/air in the vocal tract is modeled as a compressible and viscous fluid interacting with the non-linear, viscoelastic vocal folds (VF). The VF tissue material properties are multi-layered, with varying stiffness, and a finite-strain model is utilized and implemented in a quadratic finite element code. The fluid-solid domains are coupled through a boundary-fitted interface and utilize a Poisson equation-based mesh deformation method. The full-body domain includes the near VF region, the vocal tract, a simplified model of the soft palate and mouth,

**Method-oriented passage (PDF p. 1)**

The Generation and propagation of the human voice is studied in two-dimensions using a full-body domain, using direct numerical sim- ulation. The ﬂuid/air in the vocal tract is modeled as a compressible and viscous ﬂuid interacting with the non-linear, viscoelastic vocal folds (VF). The VF tissue material properties are multi-layered, with varying stiﬀness, and a ﬁnite-strain model is utilized and implemented in a quadratic ﬁnite element code. The ﬂuid-solid domains are coupled through a boundary-ﬁtted interface and utilize a Poisson equation- based mesh deformation method. The full-body domain includes the near VF region, the vocal tract, a 

**Results-oriented passage (PDF p. 5)**

Following the simulation of the adult and child phonation, the eﬀect of changing the material properties of the VF layers on phonation characteristics like sound intensity and pitch was analyzed. Three diﬀerent cases for this analysis was undertaken. Table 4 provides the parameters for each of these cases and also comparing to the already completed adult simulation. The cover layer elasticity was varied by ∓20% for the ﬁrst two cases and the ligament layer was made considerably softer for the third case, while the other properties were kept unchanged. Varying one property at a time, will give an insight on the eﬀect of each of these variation

**Caveat-oriented passage (PDF p. 2)**

challenged by the uncertainty in determining accurate material properties and the internal layering of the VFs. This was overcome in a recent study [1], which has provided quantitative estimates to the above problems. Initial investigations using CFD assumed rigid VFs [2, 3, 4] or with a pre- scribed motion [5, 6, 7, 8, 9]. Only a small subset allo

## 21. From Speaker Verification to Multispeaker Speech Synthesis, Deep Transfer with Feedback Constraint

ID: `2005.04587` | Theme: Evaluation/reliability | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2005.04587

Snapshot SHA-256: `ef4552dd0914ba60d7f405cf3f6c3f558422c81cb5d0afdce064552089090eb6`

Abstract extract: High-fidelity speech can be synthesized by end-to-end text-to-speech models in recent years. However, accessing and controlling speech attributes such as speaker identity, prosody, and emotion in a text-to-speech system remains a challenge. This paper presents a system involving feedback constraint for multispeaker speech synthesis. We manage to enhance the knowledge transfer from the speaker verification to the speech synthesis by engaging the speaker verification network. The constraint is taken by an added loss related to the speaker identity, which is centralized to improve the speaker similarity between the synthesized speech and its natural reference audio. The model is trained and eva

**Method-oriented passage (PDF p. 1)**

embedding to characterize the expected voice and speaking style in the multispeaker TTS system [10, 11, 12], while speaker adaptation can also be used for speaker transfer TTS model- ing [13]. Voice cloning by speaker adaptation acquires more data and computational resource for the target voice and usu- ally is less robust compared with cloning by speaker embedding [14]. The speaker veriﬁcation system plays an essential role in the multispeaker TTS system for cloning unseen voices. Eliya Nachmani et al. has proposed an approach where the speaker veriﬁcation system and the synthesizer are jointly trained [15]. However, the knowledge for discri

**Results-oriented passage (PDF p. 4)**

We asked 12 people to choose their preferable speech for pairs that contain speech synthesized by both systems. Audios in each pair are synthesized with the same text content and the conditioned embedding from the same reference audio. Each person chose their preference concerning speaker similarity and naturalness from 38 pairs, which are randomly selected from the VCTK test set, the VCTK validation set, and the Librispeech set. Preference results are shown in ﬁgure 3. For subjective evaluation, the FC system outperforms the baseline system on all three evaluation sets. For seen speakers in the training data, the speech synthesized by both s

**Caveat-oriented passage (PDF p. 2)**

might be because the datasets collected for speech synthesis have limited speakers, and the datasets collected for speaker analysis have no transcriptions for TTS training. Jia Ye et al. chose to train the two models individually, where the TTS model learns the speaker representation knowledge by the em- bedding extracted from the speaker veriﬁcati

## 22. Self-Training for End-to-End Speech Translation

ID: `2006.02490` | Theme: Loop/data selection | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2006.02490

Snapshot SHA-256: `91bea23ffaef9d76041c2da5105d29044cb50f7f35d28affee9e9e15ac43fa42`

Abstract extract: One of the main challenges for end-to-end speech translation is data scarcity. We leverage pseudo-labels generated from unlabeled audio by a cascade and an end-to-end speech translation model. This provides 8.3 and 5.7 BLEU gains over a strong semi-supervised baseline on the MuST-C English-French and English-German datasets, reaching state-of-the art performance. The effect of the quality of the pseudo-labels is investigated. Our approach is shown to be more effective than simply pre-training the encoder on the speech recognition task. Finally, we demonstrate the effectiveness of self-training by directly generating pseudo-labels with an end-to-end model instead of a cascade model.

**Method-oriented passage (PDF p. 4)**

We have shown the effectiveness of pseudo-labels for end-to- end ST in low- and high-resource data conditions, across two domains and 3 language pairs. In the high-resource setting, ﬁne-tuning and larger architectures were found to be critical for obtaining improvements over the baseline. Larger amounts of pseudo-labels allow to increase the model size further. By doing so, we obtained state-of-the-art results on the MuST-C English- French and English-German datasets. Our approach was shown empirically to be more effective than encoder pre-training, high- lighting the importance of pre-training the decoder. Finally, pseudo-labeling may be fur

**Results-oriented passage (PDF p. 3)**

In §3.2, substantial improvements over the baseline were ob- tained by training a larger model. In Table 3, the capacity of the model is further increased in order to verify to what extent pseudo-labels can beneﬁt training. When adding 17,607 h of unlabeled data, VGGT and VGGTLARGE obtain similar per- formance but with 35,217 h of additional data, VGGTLARGE obtains 1 BLEU improvement on the En-De MuST-C dev set.

**Caveat-oriented passage (PDF p. 3)**

We ﬁrst study the effect of simply adding pseudo-labels to the baseline training data and retraining with the LSTM model, where the baseline is either lower resource (MuST-C) or higher resource (MuST-C + LS). In Figure 1, with this simple method, the low resource baseline can be improved by up to 2.4 BLEU on the En-De MuST-C dev set. Above a certai

## 23. Audio Captioning using Gated Recurrent Units

ID: `2006.03391` | Theme: Captioning/grounding | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2006.03391

Snapshot SHA-256: `8b1c84ec04b946141f857760849cb38395a0243269f971e32ffd58265c181414`

Abstract extract: Audio captioning is a recently proposed task for automatically generating a textual description of a given audio clip. In this study, a novel deep network architecture with audio embeddings is presented to predict audio captions. Within the aim of extracting audio features in addition to log Mel energies, VGGish audio embedding model is used to explore the usability of audio embeddings in the audio captioning task. The proposed architecture encodes audio and text input modalities separately and combines them before the decoding stage. Audio encoding is conducted through Bi-directional Gated Recurrent Unit (BiGRU) while GRU is used for the text encoding phase. Following this, we evaluate our 

**Method-oriented passage (PDF p. 2)**

• We propose a novel model speciﬁcally designed for the audio captioning task, which encodes audio and text separately. We combine these features and decode them in the GRU layer.

**Results-oriented passage (PDF p. 2)**

The organization of the paper is as follows. Section 2 in- troduces our proposed method. We present our experimental results and evaluations in Section 3. Finally, we give conclud- ing remarks and possible future directions in Section 4.

**Caveat-oriented passage (PDF p. 1)**

occurring in the audio clip along with their starting and end- ing times. The audio tagging task assigns predeﬁned labels to a given audio segment, whereas the acoustic scene recogni- tion task concerns the understanding of the acoustics of the environment and assign labels to it. However, audio cap- tioning is quite a higher level of abstraction o

## 24. FastSpeech 2: Fast and High-Quality End-to-End Text to Speech

ID: `2006.04558` | Theme: Evaluation/reliability | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2006.04558

Snapshot SHA-256: `cc63cbd90dbc90107603cd064969f23a9b6b00b986c3bda3c27dc63613147e2a`

Abstract extract: Non-autoregressive text to speech (TTS) models such as FastSpeech can synthesize speech significantly faster than previous autoregressive models with comparable quality. The training of FastSpeech model relies on an autoregressive teacher model for duration prediction (to provide more information as input) and knowledge distillation (to simplify the data distribution in output), which can ease the one-to-many mapping problem (i.e., multiple speech variations correspond to the same text) in TTS. However, FastSpeech has several disadvantages: 1) the teacher-student distillation pipeline is complicated and time-consuming, 2) the duration extracted from the teacher model is not accurate enough, 

**Method-oriented passage (PDF p. 2)**

In this work, we propose FastSpeech 2 to address the issues in FastSpeech and better handle the one-to-many mapping problem in non-autoregressive TTS. To simplify the training pipeline and avoid the information loss due to data simpliﬁcation in teacher-student distillation, we directly train the FastSpeech 2 model with ground-truth target instead of the simpliﬁed output from a teacher. To reduce the information gap (input does not contain all the information to predict the target) be- tween the input (text sequence) and target output (mel-spectrograms) and alleviate the one-to-many mapping problem for non-autoregressive TTS model training, we

**Results-oriented passage (PDF p. 7)**

Training and Inference Speedup FastSpeech 2 simpliﬁes the training pipeline of FastSpeech by removing the teacher-student distillation process, and thus reduces the training time. We list the total training time of Transformer TTS (the autoregressive teacher model), FastSpeech (including the training of Transformer TTS teacher model and FastSpeech student model) and FastSpeech 2 in Table 2. It can be seen that FastSpeech 2 reduces the total training time by 3.12× compared with FastSpeech. Note that training time here only includes acoustic model training, without considering the vocoder training. Therefore, we do not compare the training time

**Caveat-oriented passage (PDF p. 4)**

The variance adaptor aims to add variance information (e.g., duration, pitch, energy, etc.) to the phoneme hidden sequence, which can provide enough information to predict variant speech for the one-to-many mapping problem in TTS. We brieﬂy introduce the variance information as follows: 1) phoneme duration, which represents how long the speech voic

## 25. Generic Indic Text-to-speech Synthesisers with Rapid Adaptation in an End-to-end Framework

ID: `2006.06971` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2006.06971

Snapshot SHA-256: `92ebe508e381dfbed043e74da3ff9630897bf8191c377707af9f864d9de73819`

Abstract extract: Building text-to-speech (TTS) synthesisers for Indian languages is a difficult task owing to a large number of active languages. Indian languages can be classified into a finite set of families, prominent among them, Indo-Aryan and Dravidian. The proposed work exploits this property to build a generic TTS system using multiple languages from the same family in an end-to-end framework. Generic systems are quite robust as they are capable of capturing a variety of phonotactics across languages. These systems are then adapted to a new language in the same family using small amounts of adaptation data. Experiments indicate that good quality TTS systems can be built using only 7 minutes of adapta

**Method-oriented passage (PDF p. 2)**

3.1. Tacotron2 Tacotron2 learns the mapping between linguistic and acous- tic features during training. The basic architecture is a recur- rent neural network (RNN) based sequence-to-sequence model [2]. It consists of an encoder and an attention-based decoder. The encoder encodes the character embeddings extracted from the text. The attention module then summarises this variable- length encoded representation as a ﬁxed-length context vector and feeds it to the decoder at each step. The decoder then pre- dicts mel-spectrograms corresponding to frame(s) at each de- coder step. A location-sensitive attention is used in the decoder [20]. Addition

**Results-oriented passage (PDF p. 3)**

4.3. Generic voices with speaker-embedding x-vectors are used as speaker embedding in the generic TTSes. The incorporation of x-vectors is shown with dashed modules in Figure 1. 512-dimensional x-vectors are extracted from the audio ﬁles using a pre-trained x-vector [22] provided by Kaldi. Experiments with speaker embedding in generic voices are pre- sented here. Languages/speakers present in the pooled data are referred to as seen languages/speakers. (a) Seen language, seen speaker (without speaker switch- ing): Monolingual sentences are synthesised using the x-vector of the corresponding monolingual speaker. For example, Hindi sentences are

**Caveat-oriented passage (PDF p. 2)**

4.1. Datasets The datasets used in this work are part of the IndicTTS database [24]. For generic voices, constituent monolingual data of 5 hours each is used. Only one male speaker per language is con- sidered due to the unavailability of multiple speakers for each language. Totally 9 languages spanning 8 different scripts are used in the experimen

## 26. Boosting Active Learning for Speech Recognition with Noisy Pseudo-labeled Samples

ID: `2006.11021` | Theme: Loop/data selection | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2006.11021

Snapshot SHA-256: `4b04f6e14fb7e04b030e10b01db7107f83c3f389cefd756adc8575deb96a8159`

Abstract extract: The cost of annotating transcriptions for large speech corpora becomes a bottleneck to maximally enjoy the potential capacity of deep neural network-based automatic speech recognition models. In this paper, we present a new training pipeline boosting the conventional active learning approach targeting label-efficient learning to resolve the mentioned problem. Existing active learning methods only focus on selecting a set of informative samples under a labeling budget. One step further, we suggest that the training efficiency can be further improved by utilizing the unlabeled samples, exceeding the labeling budget, by introducing sophisticatedly configured unsupervised loss complementing supe

**Method-oriented passage (PDF p. 2)**

overcome the limitations of both AL and SSL.To this end, we introduce Consistency Regularization (CR) [7, 8, 9] technique which regularizes the side-effect of noisy pseudo-labels by forcing a model to predict consistently on both of genuine and distorted versions of a sample. The experimental results suggest that our new training pipeline can fully utilize PLS in training. The overview of the training pipeline proposed in this paper is depicted in Figure 1.

**Results-oriented passage (PDF p. 5)**

tional samples (i.e. PLS) during training. It explains our hy- pothesis mentioned in section 4.1 that noisy pseudo-labeled samples rather hinders the model training. To resolve such a problem, we try adopting the preliminary ﬁltering men- tioned at section 4.3 to ﬁlter out the samples having too noisy pseudo-labels, so +PLS-τ with τ = −0.5 achieves the better CERs, but it still is worse than those of our proposed +CR-Xs utilizing the noisy samples effectively other than abandoning them. We discuss this observation in the following subsection. The gains of +CR-Xs over the other pipelines are impres- sive as the labeling budget is smaller. For 

**Caveat-oriented passage (PDF p. 2)**

CR is mostly applied in computer vision tasks [7, 8, 9] and CR has not been actively considered in ASR task because of its incompatibility to distortions (i.e., augmentations), which has been reported to be effective for vision tasks. However, we show that appropriate augmentations, which do not corrupt essential linguistic information, can enable 

## 27. wav2vec 2.0: A Framework for Self-Supervised Learning of Speech Representations

ID: `2006.11477` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2006.11477

Snapshot SHA-256: `4a881708378143547a5c053f62090104afb49782a4c71d78441dde0a818758ff`

Abstract extract: We show for the first time that learning powerful representations from speech audio alone followed by fine-tuning on transcribed speech can outperform the best semi-supervised methods while being conceptually simpler. wav2vec 2.0 masks the speech input in the latent space and solves a contrastive task defined over a quantization of the latent representations which are jointly learned. Experiments using all labeled data of Librispeech achieve 1.8/3.3 WER on the clean/other test sets. When lowering the amount of labeled data to one hour, wav2vec 2.0 outperforms the previous state of the art on the 100 hour subset while using 100 times less labeled data. Using just ten minutes of labeled data a

**Method-oriented passage (PDF p. 2)**

Previous work learned a quantization of the data followed by a contextualized representations with a self-attention model [5, 4], whereas our approach solves both problems end-to-end. Masking parts of the input with Transformer networks for speech has been explored [4, 26], but prior work relies either on a two-step pipeline or their model is trained by reconstructing the ﬁlter bank input features. Other related work includes learning representations from auto-encoding the input data [52, 11] or directly predicting future timesteps [8].

**Results-oriented passage (PDF p. 7)**

Table 2 shows that our approach achieves WER 1.8/3.3 on test-clean/other on the full Librispeech benchmark. This is despite a weaker baseline architecture: supervised training of our architecture achieves WER 2.1/4.6 (LARGE - from scratch) compared to WER 1.9/4.1 for ContextNet [17], the baseline architecture of the state of the art [42]. We use a simple Transformer with CTC which does not perform as well as seq2seq models [51].

**Caveat-oriented passage (PDF p. 4)**

As unlabeled data we consider the Librispeech corpus [40] without transcriptions containing 960 hours of audio (LS-960) or the audio data from LibriVox (LV-60k). For the latter we follow the pre- processing of [27] resulting in 53.2k hours of audio. We ﬁne-tune on ﬁve labeled data settings: 960 hours of transcribed Librispeech, the train-clean-100 

## 28. Shouted Speech Compensation for Speaker Verification Robust to Vocal Effort Conditions

ID: `2008.02487` | Theme: Evaluation/reliability | Status: `selected_fulltext_review_plus_scoped_core_crosscheck`

Source: https://arxiv.org/pdf/2008.02487

Snapshot SHA-256: `ce550a2073def177156e6f5171b5da448e80a347b84abe61f02d6f6b1968a59f`

Abstract extract: The performance of speaker verification systems degrades when vocal effort conditions between enrollment and test (e.g., shouted vs. normal speech) are different. This is a potential situation in non-cooperative speaker verification tasks. In this paper, we present a study on different methods for linear compensation of embeddings making use of Gaussian mixture models to cluster shouted and normal speech domains. These compensation techniques are borrowed from the area of robustness for automatic speech recognition and, in this work, we apply them to compensate the mismatch between shouted and normal conditions in speaker verification. Before compensation, shouted condition is automatically 

**Method-oriented passage (PDF p. 1)**

and demonstrate that the accuracy is negatively affected in the presence of vocal effort mismatch. High vocal effort mode is used by speakers to produce a louder acoustic signal in order to increase the signal-to-noise ratio usually in noisy environments, distant communication or in emergency situations. There are some works that address the issue of how to detect high vocal effort [4–6]. In [5], spectral characteristics of shouted speech are studied in order to demon- strate that many acoustic properties of the voice change in high vocal effort situations. In this paper, we focus on detecting shouted speech as a previous step to alleviate th

**Results-oriented passage (PDF p. 4)**

Condition Baseline MEMLIN RATZ SPLICE A-A 24.76 21.09 22.16 21.24 N-N 12.93 12.93 12.93 12.93 S-S 16.37 13.73 15.00 13.60 N-S 27.73 26.60 28.06 26.95 Table 1: Speaker veriﬁcation results in terms of EER, in per- centages, when using oracle shouted speech detection.

**Caveat-oriented passage (PDF p. 4)**

In this work, we have shown the need for vocal effort mismatch compensation in the context of speaker veriﬁcation. Moreover, we have also shown the potential of several linear compensation techniques intended to mitigate the mismatch between speaker embeddings extracted from shouted and normal speech utter- ances. These techniques have worked on to

Additional interpretation and limitations: [core findings](CORE_FINDINGS.md).

## 29. Controllable Neural Prosody Synthesis

ID: `2008.03388` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2008.03388

Snapshot SHA-256: `5b09bedf65adbbbd2e81ea2069c94e51972eae3e7d8ab1b62bfe176f61fce11d`

Abstract extract: Speech synthesis has recently seen significant improvements in fidelity, driven by the advent of neural vocoders and neural prosody generators. However, these systems lack intuitive user controls over prosody, making them unable to rectify prosody errors (e.g., misplaced emphases and contextually inappropriate emotions) or generate prosodies with diverse speaker excitement levels and emotions. We address these limitations with a user-controllable, context-aware neural prosody generator. Given a real or synthesized speech recording, our model allows a user to input prosody constraints for certain time frames and generates the remaining time frames from input text and contextual prosody. We al

**Method-oriented passage (PDF p. 2)**

A signiﬁcant advantage of working with an F0 contour, as op- posed to jointly predicting all prosodic features, is that users may explicitly create, modify, and constrain the F0 contour to realize a creative goal. We propose three techniques designed to facilitate control of a DAR-based model for F0 generation: (1) if available, the preceding and following speech content is summarized and used to condition the model, (2) random seg- ments of the ground truth F0 are provided to the model during training, and (3) the model predicts F0 values in reverse order. The preceding and following speech content provides use- ful indicators for placing em

**Results-oriented passage (PDF p. 4)**

such as our proposed low-pass evaluation method. We present our repunctuation experiment results in Table 4. Relative to DAR, using C-DAR with short, user-speciﬁed F0 contours improves the adherence of the generated F0 contour to high-level semantic concepts (e.g., questions and statements). We ﬁnd this to be especially true when the target punctuation is a question mark. We believe this is because statements are heav- ily over-represented in the dataset, leading to class-imbalance and mode collapse. Our results indicate that simple user inputs make for an effective mode selector for prosody generation.

**Caveat-oriented passage (PDF p. 1)**

Speech synthesis has recently seen signiﬁcant improvements in ﬁdelity, driven by the advent of neural vocoders and neural prosody generators. However, these systems lack intuitive user controls over prosody, making them unable to rectify prosody errors (e.g., misplaced emphases and contextually inappropri- ate emotions) or generate prosodies with d

## 30. Self-training and Pre-training are Complementary for Speech Recognition

ID: `2010.11430` | Theme: Loop/data selection | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2010.11430

Snapshot SHA-256: `b81792c717fab0d9f3c725fa4817b94c6b8e0244a1e3cc753e18b7d429ce7945`

Abstract extract: Self-training and unsupervised pre-training have emerged as effective approaches to improve speech recognition systems using unlabeled data. However, it is not clear whether they learn similar patterns or if they can be effectively combined. In this paper, we show that pseudo-labeling and pre-training with wav2vec 2.0 are complementary in a variety of labeled data setups. Using just 10 minutes of labeled data from Libri-light as well as 53k hours of unlabeled data from LibriVox achieves WERs of 3.0%/5.2% on the clean and other test sets of Librispeech - rivaling the best published systems trained on 960 hours of labeled data only a year ago. Training on all labeled data of Librispeech achiev

**Method-oriented passage (PDF p. 2)**

relative WER reduction of 25% and 40% over recent work in pre-training alone [24]. Using just the acoustic model without a language model achieves WER 3.7%/6.5% - supporting the hypothesis that self-training distills the language model used for pseudo-labeling into the ﬁnal model. When all 960 hours of labeled training data are used we achieve 1.5%/3.1% WER on Librispeech.

**Results-oriented passage (PDF p. 4)**

Next, we evaluate performance with more labeled data. We consider the 100h clean subset of Librispeech as well as all 960h of labeled data in Librispeech. Table 2 shows that LS-960 as unlabeled data is not enough to outperform the baseline when 100h of labeled data is available. However, performance improves when using the much larger LV-60k, achieving a 10% relative WER reduction on test-other over wav2vec 2.0.

**Caveat-oriented passage (PDF p. 2)**

Previous work considered multiple rounds of pseudo-labeling where the labeling step is repeated with each new model to train another model [14]. While iterative pseudo-labeling is more accurate, we opt for a single iteration which is computationally less demanding while still enabling us to reason about whether unsupervised pre-training and pseudo-

## 31. DNSMOS: A Non-Intrusive Perceptual Objective Speech Quality metric to evaluate Noise Suppressors

ID: `2010.15258` | Theme: Evaluation/reliability | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2010.15258

Snapshot SHA-256: `2e5975d615e5348d35d82bd34f4cc4d277d571a429c160eaa27305e22442f2ef`

Abstract extract: Human subjective evaluation is the gold standard to evaluate speech quality optimized for human perception. Perceptual objective metrics serve as a proxy for subjective scores. The conventional and widely used metrics require a reference clean speech signal, which is unavailable in real recordings. The no-reference approaches correlate poorly with human ratings and are not widely adopted in the research community. One of the biggest use cases of these perceptual objective metrics is to evaluate noise suppression algorithms. This paper introduces a multi-stage self-teaching based perceptual objective metric that is designed to evaluate noise suppressors. The proposed method generalizes well i

**Method-oriented passage (PDF p. 2)**

life long learning [13] to learn in the presence of noisy labels. We show that the multi-stage training signiﬁcantly improves the correlation and generalizes remarkably well to other im- pairment types that are very different from what was used in the training set. We found the DNSMOS very useful in our audio/speech research as it generalizes well to a variety of speech impairments. Hence, we are providing the DNS- MOS as an Azure service for other researchers to use. The details of the API are at www.microsoft.com/en-us/ research/dns-challenge/dnsmos.

**Results-oriented passage (PDF p. 4)**

We initially analyzed the effect of α0 on M1 to understand the weightage given to the teacher model M0 vs human rat- ings. Figure. 3 shows the SRCC between MOS and M1 for different values of α0 computed on one of the P.808 runs with 12 closely stack ranked models. We see in Figure. 3 that the SRCC is higher for α0 = 0.8. The noisy and the processed clips comprised of a similar distribution as that of the training set. In order to test the generalization capability of training multiple stages of self- teaching models, we evaluated on the ICASSP 2021 DNS Challenge 2 ﬁnal submissions [20], which comprised of the blind test set processed by 18 di

**Caveat-oriented passage (PDF p. 2)**

clips processed by a given model. However, the absolute val- ues of the scores vary between P.808 runs as the raters differ and humans tend to be inconsistent in perceptual tasks due to various biases.

## 32. Unsupervised Domain Adaptation for Speech Recognition via Uncertainty Driven Self-Training

ID: `2011.13439` | Theme: Loop/data selection | Status: `selected_fulltext_review_plus_scoped_core_crosscheck`

Source: https://arxiv.org/pdf/2011.13439

Snapshot SHA-256: `70727f954b5569eff46cc3806b342a68ba188fc9ca576ceedcc3dba549af93a4`

Abstract extract: The performance of automatic speech recognition (ASR) systems typically degrades significantly when the training and test data domains are mismatched. In this paper, we show that self-training (ST) combined with an uncertainty-based pseudo-label filtering approach can be effectively used for domain adaptation. We propose DUST, a dropout-based uncertainty-driven self-training technique which uses agreement between multiple predictions of an ASR system obtained for different dropout settings to measure the model's uncertainty about its prediction. DUST excludes pseudo-labeled data with high uncertainties from the training, which leads to substantially improved ASR results compared to ST withou

**Method-oriented passage (PDF p. 4)**

In this work, we proposed DUST, a dropout-based uncertainty- driven self-training method for unsupervised domain adaptation. Through several experiments transferring from WSJ to TED- LIUM 3 and SWITCHBOARD, we show that DUST signiﬁcantly improves performance over the baseline model trained only on the labeled source domain data, and is able to recover 60% to 80% of the WER on the target domain by using only unlabeled speech from that domain. Future work includes performing a thorough investi- gation of the combination of DUST with self-supervised represen- tation learning approaches for low-resource semi-supervised speech recognition and doma

**Results-oriented passage (PDF p. 3)**

while using approximately one-third of the pseudo-labeled data (38k vs 100k). When comparing the downstream task performance for different ﬁltering thresholds, the following two observations can be made: ﬁrst, the downstream task performance is substantially better than the baseline regardless of the ﬁltering threshold; second, best results are obtained when the ﬁltering threshold τ is set to mid-range values, with the optimal setting being 0.3 based on the TED develop- ment set. From here on, we ﬁx the threshold value τ to 0.3. We next perform multiple iterations of self-training, where an LM trained on the source domain text is used for dec

**Caveat-oriented passage (PDF p. 4)**

without the use of an LM for the pseudo-label generation process. First, here again DUST1 performs on par with classic self-training (ST1), while using only a fraction of pseudo-labeled utterances (see |P| in Table 3). Compared with the baseline, we are able to recover 80% of the WERs when using no LM for decoding the test data, 79% when using a so

Additional interpretation and limitations: [core findings](CORE_FINDINGS.md).

## 33. Whispered and Lombard Neural Speech Synthesis

ID: `2101.05313` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2101.05313

Snapshot SHA-256: `a3f160ae526932a945f2c06f083f84950294687e97c69ac3f5794e1bd90e27c1`

Abstract extract: It is desirable for a text-to-speech system to take into account the environment where synthetic speech is presented, and provide appropriate context-dependent output to the user. In this paper, we present and compare various approaches for generating different speaking styles, namely, normal, Lombard, and whisper speech, using only limited data. The following systems are proposed and assessed: 1) Pre-training and fine-tuning a model for each style. 2) Lombard and whisper speech conversion through a signal processing based approach. 3) Multi-style generation using a single model based on a speaker verification model. Our mean opinion score and AB preference listening tests show that 1) we ca

**Method-oriented passage (PDF p. 2)**

The multi-style speech corpus used in this work was cre- ated in a professional recording studio over the course of three days. Normal, Lombard, and whisper style speech was recorded by an American, non-professional, male tal- ent. Each style was collected through a 4-hour session (one style per day), yielding around 40 minutes of usable audio per session. The talent read out the same 600 sentences per style, most of which were selected from VCTK [21] and voice assistant scripts. The complete dataset consisted of 2 hours (3 × 40 min) of audio sampled at a frequency of 24 kHz. In this preliminary investigation, the text and lexicon were not cl

**Results-oriented passage (PDF p. 4)**

The input for the baseline Tacotron model is a sequence of phonemes, punctuations, and word boundaries, which is converted to 512-dimensional embeddings through a text encoder. The output is a sequence of Mel-spectrograms, computed from 25 ms frames with 10 ms shift. A stepwise monotonic attention [35] is adopted for better alignment be- tween the input and output features. For evaluation of the naturalness, we use a mean opinion score (MOS) on a scale from 1 to 5. AB listening tests are conducted to assess which system sounds more natural or more preferred in terms of speech quality or intelligibility (A: ﬁrst sample, B: second sample, C: no

**Caveat-oriented passage (PDF p. 3)**

Although the PF model can generate the target voice from a limited amount of data, the current architecture requires training a separate model for each style. [27, 28, 29] have proposed extending the Tacotron to a multi-speaker model by conditioning the synthesis on a speaker representation in addi- tion to the phoneme sequence. [30] further extend

## 34. Target Speaker Verification with Selective Auditory Attention for Single and Multi-talker Speech

ID: `2103.16269` | Theme: Evaluation/reliability | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2103.16269

Snapshot SHA-256: `1f66a4c4306732a1d9aa0b585f7e689dd18c1850f3274a0d1fc203733dd6f0e4`

Abstract extract: Speaker verification has been studied mostly under the single-talker condition. It is adversely affected in the presence of interference speakers. Inspired by the study on target speaker extraction, e.g., SpEx, we propose a unified speaker verification framework for both single- and multi-talker speech, that is able to pay selective auditory attention to the target speaker. This target speaker verification (tSV) framework jointly optimizes a speaker attention module and a speaker representation module via multi-task learning. We study four different target speaker embedding schemes under the tSV framework. The experimental results show that all four target speaker embedding schemes significa

**Method-oriented passage (PDF p. 2)**

1) We propose a uniﬁed network architecture that performs target speaker veriﬁcation (tSV) for both single- and multi-talker speech. 2) We propose a multi-task learning algorithm for the pro- posed tSV framework, which jointly optimize the target speaker attention module and the speaker representation module. 3) We perform comprehensive studies on each individual network modules as well as at the system level. We successfully show that the proposed tSV framework not only works well under the multi-talker condition, but also performs as competitively as traditional SV under the single-talker condition. The remainder of the paper is organized a

**Results-oriented passage (PDF p. 9)**

counterpart (SV-T). This suggests that the time-domain SV system is sensitive to the mismatch between speaker veriﬁca- tion module trained with single talker speech, and the extracted speech from speaker extraction module. The difference between the target speaker extraction- veriﬁcation pipeline [31] and the proposed tSV system mainly lies in their training schemes. The former trains the extraction module and veriﬁcation module separately, while the latter enables a multi-task joint training between speaker attention and speaker representation modules. Next we summarize the results for the four target speaker embedding schemes under multi-ta

**Caveat-oriented passage (PDF p. 8)**

In Figure 1, to keep the same processing procedures for both eref and etest during inference, we pass the enrollment utterance and the test utterance through the shared speaker attention module in the same way. We note an alternative implementation to Path B is bypassing the speaker attention module and directly feeding the enrollment utterance int

## 35. Expressive Text-to-Speech using Style Tag

ID: `2104.00436` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2104.00436

Snapshot SHA-256: `6504affdf8314d4b3c954c914a31c13498c2cd5be9778b0e547dfd6cb8def2ce`

Abstract extract: As recent text-to-speech (TTS) systems have been rapidly improved in speech quality and generation speed, many researchers now focus on a more challenging issue: expressive TTS. To control speaking styles, existing expressive TTS models use categorical style index or reference speech as style input. In this work, we propose StyleTagging-TTS (ST-TTS), a novel expressive TTS model that utilizes a style tag written in natural language. Using a style-tagged TTS dataset and a pre-trained language model, we modeled the relationship between linguistic embedding and speaking style domain, which enables our model to work even with style tags unseen during training. As style tag is written in natural 

**Method-oriented passage (PDF p. 2)**

In this section, we introduce the ST-TTS architecture. Our pro- posed model takes grapheme sequence and style tag as input and returns log mel-spectrogram. Reference speech is addition- ally used for training and optionally used for inference. The en- tire structure is based on non-autoregressive feedforward TTS models [3, 4, 8], and end-to-end trainable by jointly optimizing duration information with the entire system. The entire archi- tecture is shown in Figure 1, and described as follows.

**Results-oriented passage (PDF p. 4)**

We measure the 5 scale Mean Opinion Score (MOS) to esti- mate the speech quality of the proposed model. Since ST-TTS is the ﬁrst TTS model which can control style with the unde- ﬁned label or reference speech, we chose Tacotron2-GST [12] as a baseline. The result of ﬁve groups: ground truth (GT), GT with vocoder reconstruction, Tacotron2-GST, ST-TTS (ref- erence speech), ST-TTS (style tag) is shown in Table 2. ST- TTS (reference speech) and ST-TTS (style tag) mean ST-TTS using reference speech and style tag for style input respectively. The reference speech used for Tacotron2-GST and ST-TTS (ref- erence speech) is the target speech itself bec

**Caveat-oriented passage (PDF p. 1)**

Recently, end-to-end (e2e) speech synthesis systems have achieved signiﬁcant improvement and now show almost human- like speech quality. Among e2e speech synthesis systems, au- toregressive (AR) models such as Tacotron2 [1] and Trans- former TTS [2] ﬁrst showed state-of-the-art performance by ex- ploiting the attention mechanism. However, as AR mod

## 36. AST: Audio Spectrogram Transformer

ID: `2104.01778` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2104.01778

Snapshot SHA-256: `c237e981755e9ba5047e7290ffcb7d38d8292e166730ae3cd180b7833f184303`

Abstract extract: In the past decade, convolutional neural networks (CNNs) have been widely adopted as the main building block for end-to-end audio classification models, which aim to learn a direct mapping from audio spectrograms to corresponding labels. To better capture long-range global context, a recent trend is to add a self-attention mechanism on top of the CNN, forming a CNN-attention hybrid model. However, it is unclear whether the reliance on a CNN is necessary, and if neural networks purely based on attention are sufficient to obtain good performance in audio classification. In this paper, we answer the question by introducing the Audio Spectrogram Transformer (AST), the first convolution-free, pur

**Method-oriented passage (PDF p. 2)**

shelf pretrained Vision Transformer (ViT) to AST. While ViT and AST have similar architectures (e.g., both use a standard Transformer, same patch size, same embedding size), they are not same. Therefore, a few modiﬁcations need to make for the adaptation. First, the input of ViT is a 3-channel image while the input to the AST is a single-channel spectro- gram, we average the weights corresponding to each of the three input channels of the ViT patch embedding layer and use them as the weights of the AST patch embedding layer. This is equivalent to expanding a single-channel spectrogram to 3- channels with the same content, but is computational

**Results-oriented passage (PDF p. 3)**

We repeat each experiment three times with the same setup but different random seeds and report the mean and standard devi- ation. When AST is trained with the full AudioSet, the mAP at the last epoch is 0.448±0.001. As in [8], we also use weight averaging [30] and ensemble [31] strategies to further improve the performance of AST. Speciﬁcally, for weight averaging, we average all weights of the model checkpoints from the ﬁrst to the last epoch. The weight-averaged model achieves an mAP of 0.459±0.000, which is our best single model (weight averag- ing does not increase the model size). For ensemble, we eval- uate two settings: 1) Ensemble-S:

**Caveat-oriented passage (PDF p. 2)**

Figure 1 illustrates the proposed Audio Spectrogram Trans- former (AST) architecture. First, the input audio waveform of t seconds is converted into a sequence of 128-dimensional log Mel ﬁlterbank (fbank) features computed with a 25ms Ham- ming window every 10ms. This results in a 128×100t spectro- gram as input to the AST. We then split the spectr

## 37. NISQA: A Deep CNN-Self-Attention Model for Multidimensional Speech Quality Prediction with Crowdsourced Datasets

ID: `2104.09494` | Theme: Evaluation/reliability | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2104.09494

Snapshot SHA-256: `adeb58a0197bb9bf22e93d37c8b7e637938e4a040f642d19c6b533aa12a647ac`

Abstract extract: In this paper, we present an update to the NISQA speech quality prediction model that is focused on distortions that occur in communication networks. In contrast to the previous version, the model is trained end-to-end and the time-dependency modelling and time-pooling is achieved through a Self-Attention mechanism. Besides overall speech quality, the model also predicts the four speech quality dimensions Noisiness, Coloration, Discontinuity, and Loudness, and in this way gives more insight into the cause of a quality degradation. Furthermore, new datasets with over 13,000 speech files were created for training and validation of the model. The model was finally tested on a new, live-talking 

**Method-oriented passage (PDF p. 2)**

In this stage, the individual time steps of the feature sequence can interact with each other to improve the prediction perfor- mance. To this end, a Self-Attention network is applied, which is based on the Transformer encoder [20]. Because the Self- Attention only models temporal dependencies of framewise fea- tures that are already computed by a deep framewise network, a relatively low complexity of the Transformer is sufﬁcient. Moreover, in practice, it was noted that the multi-head mech- anism did not improve the results. Therefore, the block is im- plemented with a single head, a depth of 2 blocks, a model dimensionality of dtf = 64, and

**Results-oriented passage (PDF p. 4)**

The ﬁnal model was trained on a set of 59 training and 18 vali- dation datasets with a batch size of 160, learning rate of 0.001, Adam optimiser and bias-aware loss according to [35]. After each epoch, the model weights were stored, and the results on the training and validation set were calculated as average PCC across all datasets. The training was stopped after the valida- tion PCC did not increase for more than 10 epochs. The model weights with the best performance on the validation set were selected as the ﬁnal model. This model was then evaluated on the four independent test sets, which were not considered for training, hyper-parameter 

**Caveat-oriented passage (PDF p. 2)**

The input to the model are Mel-spec segments with 48 Mel- bands. The FFT window length is 20 ms with a hop size of 10 ms. The maximum frequency was chosen to be 20 kHz to be able to predict speech quality for up to fullband (FB). The Mel-specs are divided into segments with a width of 15 (i.e. 150 ms) and a height of 48. The hop size between the se

## 38. VQCPC-GAN: Variable-Length Adversarial Audio Synthesis Using Vector-Quantized Contrastive Predictive Coding

ID: `2105.01531` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2105.01531

Snapshot SHA-256: `3168701dd62ba1589f5ab11b53dba3ca7fce6066f7b04045656013df09bcf3cf`

Abstract extract: Influenced by the field of Computer Vision, Generative Adversarial Networks (GANs) are often adopted for the audio domain using fixed-size two-dimensional spectrogram representations as the "image data". However, in the (musical) audio domain, it is often desired to generate output of variable duration. This paper presents VQCPC-GAN, an adversarial framework for synthesizing variable-length audio by exploiting Vector-Quantized Contrastive Predictive Coding (VQCPC). A sequence of VQCPC tokens extracted from real audio data serves as conditional input to a GAN architecture, providing step-wise time-dependent features of the generated content. The input noise z (characteristic in adversarial ar

**Method-oriented passage (PDF p. 4)**

In this work, we presented VQCPC-GAN, an adversarial model capable of performing variable-length sound synthesis of tonal sounds. We adapted the WGAN architecture found in previous works [4, 5] to a sequential setting by conducting two major ar- chitectural changes. First, we condition G on dynamic and static information captured, respectively, by a sequence of discrete tokens learned through VQCPC, and a global noise z. Additionally, we introduce a secondary fully-convolutional D that discriminates be- tween real and fake data distributions at a frame level and predicts the VQCPC token associated with each frame. Results showed that VQCPC-GA

**Results-oriented passage (PDF p. 4)**

Table 5.2 presents the metrics scored by our proposed VQCPC- GAN and the baselines. Overall, our WGANs score closest to those of real data in most metrics, or even better in the case of the PIS. GANSynth follows closely and VQCPC-GAN obtains slightly worse results. VQCPC-GAN performs particularly good in terms of PIS, which suggests that the generated examples have an identi- ﬁable pitch content and that the distribution of pitch classes follows that of the training data. This is not surprising given that the model has explicit pitch conditioning, making it trivial to learn the speciﬁc mapping between the pitch class and the respective tonal 

**Caveat-oriented passage (PDF p. 1)**

In recent years, Generative Adversarial Networks (GANs) [1] have shown outstanding results in image and audio synthesis tasks [2, 3, 4, 5, 6]. As most (initial) studies on GANs focused on gener- ating images, the resulting architectures are now often adopted for the musical audio domain, using ﬁxed-size two-dimensional spec- trogram representations

## 39. HuBERT: Self-Supervised Speech Representation Learning by Masked Prediction of Hidden Units

ID: `2106.07447` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2106.07447

Snapshot SHA-256: `3a919c3ede82b15c3c28f648ea8c8ef7417bab533b04f9b2b97a324c9be688d9`

Abstract extract: Self-supervised approaches for speech representation learning are challenged by three unique problems: (1) there are multiple sound units in each input utterance, (2) there is no lexicon of input sound units during the pre-training phase, and (3) sound units have variable lengths with no explicit segmentation. To deal with these three problems, we propose the Hidden-Unit BERT (HuBERT) approach for self-supervised speech representation learning, which utilizes an offline clustering step to provide aligned target labels for a BERT-like prediction loss. A key ingredient of our approach is applying the prediction loss over the masked regions only, which forces the model to learn a combined acous

**Method-oriented passage (PDF p. 2)**

inputs, such as in Computer Vision (CV) applications, repre- sentations are often learned through instance classiﬁcation, in which each image and its augmentations are treated as a single output class to be pulled together [14], [15] or contrasted against other negative samples [22]. Speech signals differ from text and images in that they are continuous-valued sequences. Self-supervised learning for the speech recognition domain faces unique challenges from those in CV and NLP. Firstly, the presence of multiple sounds in each input utterance breaks the instance classiﬁcation as- sumption used in many CV pre-training approaches. Secondly, duri

**Results-oriented passage (PDF p. 1)**

Abstract—Self-supervised approaches for speech representa- tion learning are challenged by three unique problems: (1) there are multiple sound units in each input utterance, (2) there is no lexicon of input sound units during the pre-training phase, and (3) sound units have variable lengths with no explicit segmentation. To deal with these three problems, we propose the Hidden-Unit BERT (HuBERT) approach for self-supervised speech representation learning, which utilizes an ofﬂine clustering step to provide aligned target labels for a BERT-like prediction loss. A key ingredient of our approach is applying the prediction loss over the masked re

**Caveat-oriented passage (PDF p. 3)**

where A is the projection matrix, ec is the embedding for codeword c, sim(·, ·) computes the cosine similarity between two vectors, and τ scales the logit, which is set to 0.1. When cluster ensembles are used, one projection matrix A(k) is applied for each clustering model k. After HuBERT pre-training, We use the connectionist tem- poral classiﬁcat

## 40. LoRA: Low-Rank Adaptation of Large Language Models

ID: `2106.09685` | Theme: Efficiency/adaptation | Status: `selected_fulltext_review_plus_scoped_core_crosscheck`

Source: https://arxiv.org/pdf/2106.09685

Snapshot SHA-256: `e9a0d3128767db616085dc0f4e6e455e672e89af823e8ed1282793682787395a`

Abstract extract: An important paradigm of natural language processing consists of large-scale pre-training on general domain data and adaptation to particular tasks or domains. As we pre-train larger models, full fine-tuning, which retrains all model parameters, becomes less feasible. Using GPT-3 175B as an example -- deploying independent instances of fine-tuned models, each with 175B parameters, is prohibitively expensive. We propose Low-Rank Adaptation, or LoRA, which freezes the pre-trained model weights and injects trainable rank decomposition matrices into each layer of the Transformer architecture, greatly reducing the number of trainable parameters for downstream tasks. Compared to GPT-3 175B fine-tu

**Method-oriented passage (PDF p. 2)**

While our proposal is agnostic to training objective, we focus on language modeling as our motivat- ing use case. Below is a brief description of the language modeling problem and, in particular, the maximization of conditional probabilities given a task-speciﬁc prompt.

**Results-oriented passage (PDF p. 7)**

Table 3: GPT-2 medium (M) and large (L) with different adaptation methods on the E2E NLG Challenge. For all metrics, higher is better. LoRA outperforms several baselines with comparable or fewer trainable parameters. Conﬁdence intervals are shown for experiments we ran. * indicates numbers published in prior works.

**Caveat-oriented passage (PDF p. 3)**

The problem we set out to tackle is by no means new. Since the inception of transfer learning, dozens of works have sought to make model adaptation more parameter- and compute-efﬁcient. See Sec- tion 6 for a survey of some of the well-known works. Using language modeling as an example, there are two prominent strategies when it comes to efﬁcient ad

Additional interpretation and limitations: [core findings](CORE_FINDINGS.md).

## 41. Loss Prediction: End-to-End Active Learning Approach For Speech Recognition

ID: `2107.04289` | Theme: Loop/data selection | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2107.04289

Snapshot SHA-256: `2eef6f993feb7b500c29a8ebe384424c35cfea0733a372575bc4c76eef330369`

Abstract extract: End-to-end speech recognition systems usually require huge amounts of labeling resource, while annotating the speech data is complicated and expensive. Active learning is the solution by selecting the most valuable samples for annotation. In this paper, we proposed to use a predicted loss that estimates the uncertainty of the sample. The CTC (Connectionist Temporal Classification) and attention loss are informative for speech recognition since they are computed based on all decoding paths and alignments. We defined an end-to-end active learning pipeline, training an ASR/LP (Automatic Speech Recognition/Loss Prediction) joint model. The proposed approach was validated on an English and a Chin

**Method-oriented passage (PDF p. 2)**

In this paper, we propose an active training pipeline for end-to-end speech recognition. As Fig 1 depicts, the overall training pipeline is performed iteratively. It consists of two parts: (1) ASR/LP joint model training, (2) annotated data selection. The ASR/LP joint model contains ASR target task module θasr and loss prediction module θlp. Task module θasr conducts the ASR task ˜y = θasr(x), where x is the audio sample and ˜y is the predicted text sentence. Loss prediction module predicts the loss ˜L = θlp(h, g), where h and g are the hidden feature maps extracted from task module θasr.

**Results-oriented passage (PDF p. 5)**

The LP approach was training a ASR/LP joint model, while the RS and LC method only used the ASR model. Fig 3 illustrates Word Error Rate (WER) and Word Correct Rate(CORR) results on WSJ, and Fig 4 illustrates Character Error Rate (CER) and CORR results on AISHELL-1. To investigate the performance difference, all the models were evaluated without applying the language model. The results infer that our proposed LP approach has the best performance, compared with other uncertainty-based LC and EL methods.

**Caveat-oriented passage (PDF p. 2)**

In this paper, we explore the application of uncertainty- based active learning for end-to-end ASR models. For ASR tasks, predicting uncertainty and diversity of samples is dif- ﬁcult because text transcription is a sequence of labels. In recent studies, the probability-based least conﬁdent score was explored. The samples with the lowest decoding p

## 42. Federated Self-Training for Semi-Supervised Audio Recognition

ID: `2107.06877` | Theme: Loop/data selection | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2107.06877

Snapshot SHA-256: `a09f9b372c5dcc62152167e7d3cf22019d6953fe80ff6743a51befe98b182213`

Abstract extract: Federated Learning is a distributed machine learning paradigm dealing with decentralized and personal datasets. Since data reside on devices like smartphones and virtual assistants, labeling is entrusted to the clients, or labels are extracted in an automated way. Specifically, in the case of audio data, acquiring semantic annotations can be prohibitively expensive and time-consuming. As a result, an abundance of audio data remains unlabeled and unexploited on users' devices. Most existing federated learning approaches focus on supervised learning without harnessing the unlabeled data. In this work, we study the problem of semi-supervised learning of audio models via self-training in conjunc

**Method-oriented passage (PDF p. 3)**

perform various audio recognition tasks, which have recently attracted increasing interest from researchers. As a result, numerous audio recognition systems have been developed, such as for wildlife monitoring [28, 36] and surveillance [5]. In addition to monitoring applications, highly accurate acoustic models are utilized for keyword spotting for virtual assistants [23], anomaly detection for machine sounds [18], and in the development of health risk diagnosis systems, such as cardiac arrest detection [4]. However, in the majority of such applications, there is no straightforward manner for the annotation process. For instance, suppose that

**Results-oriented passage (PDF p. 4)**

• We study on the practical problem of semi-supervised federated learning for audio recognition tasks to address the lack of labeled data that presents a major challenge for learning on-device models. • We design a simple yet effective approach based on self-training, called FedSTAR. It exploits large-scale unlabeled distributed data in a federated setting with the help of a novel adaptive confidence thresholding mechanism for effectively generating pseudo-labels. • We exploit self-supervised models pre-trained on FSD-50K corpus [6] for significantly im- proving training convergence in federated settings. • We demonstrate through extensive ev

**Caveat-oriented passage (PDF p. 2)**

labeled datasets have brought tremendous advancements in several areas, including language modeling, audio understanding, object recognition, image synthesis, and more. Traditionally, developing machine learning models or performing analytics in a data center context requires the data from IoT devices to be pooled or aggregated in a centralized rep

## 43. CLSRIL-23: Cross Lingual Speech Representations for Indic Languages

ID: `2107.07402` | Theme: Data/Indic speech | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2107.07402

Snapshot SHA-256: `d3e328851c5f16d894cb13012aff12fa7dbdc7b9be5f2a7ff3922ef674aae215`

Abstract extract: We present a CLSRIL-23, a self supervised learning based audio pre-trained model which learns cross lingual speech representations from raw audio across 23 Indic languages. It is built on top of wav2vec 2.0 which is solved by training a contrastive task over masked latent speech representations and jointly learns the quantization of latents shared across all languages. We compare the language wise loss during pretraining to compare effects of monolingual and multilingual pretraining. Performance on some downstream fine-tuning tasks for speech recognition is also compared and our experiments show that multilingual pretraining outperforms monolingual training, in terms of learning speech repre

**Method-oriented passage (PDF p. 2)**

in this space as well has been in monolingual speech recognition [Chung and Glass, 2018, Tjandra et al., 2019, Jiang et al., 2019, Harwath et al., 2020]. Our approach is based on the wav2vec 2.0 [Baevski et al., 2020] the details of which are explained in the coming sections. An approach which uses multiple languages in pre-training and ﬁne-tuning is described in [Conneau et al., 2020]. It also shows that cross lingual pre-training outperforms monolingual pre-training. We extend the work by [Rivière et al., 2020] and [Conneau et al., 2020] by pretraining only on Indic languages so that speech recognition tasks have a better performance on Ind

**Results-oriented passage (PDF p. 5)**

We ﬁnetune on 4563.7 hours of Hindi data using checkpoints from monolingual and multilingual pretraining. We see that even the high resource language, in our case Hindi, beneﬁts from multilingual pretraining. On a separate 10 hour test we see a 5% decrease in WER and a 9.5% decrease in CER when decoding is done without a language model. It can be also seen from table 5.2 that the WER decrease by 3% and CER by 9% when using a language model while decoding. We also compared ﬁnetuning results on Gujarati, Tamil and Telugu using 40 hours of training data and 5 hours of test sets for each language. In each case we see that multilingual pretraining

**Caveat-oriented passage (PDF p. 1)**

We present a CLSRIL-23, a self supervised learning based audio pre-trained model which learns cross lingual speech representations from raw audio across 23 Indic languages. It is built on top of wav2vec 2.0 which is solved by training a contrastive task over masked latent speech representations and jointly learns the quantization of latents shared 

## 44. Audio Captioning Transformer

ID: `2107.09817` | Theme: Captioning/grounding | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2107.09817

Snapshot SHA-256: `2750d1c13e764b49ec57fe4a9052ff09095b412b8b19cfcf13a630ac9cde1f4a`

Abstract extract: Audio captioning aims to automatically generate a natural language description of an audio clip. Most captioning models follow an encoder-decoder architecture, where the decoder predicts words based on the audio features extracted by the encoder. Convolutional neural networks (CNNs) and recurrent neural networks (RNNs) are often used as the audio encoder. However, CNNs can be limited in modelling temporal relationships among the time frames in an audio signal, while RNNs can be limited in modelling the long-range dependencies among the time frames. In this paper, we propose an Audio Captioning Transformer (ACT), which is a full Transformer network based on an encoder-decoder architecture and

**Method-oriented passage (PDF p. 1)**

ABSTRACT Audio captioning aims to automatically generate a natural language description of an audio clip. Most captioning models follow an encoder-decoder architecture, where the decoder predicts words based on the audio features extracted by the encoder. Convolutional neural networks (CNNs) and recurrent neural networks (RNNs) are often used as the audio encoder. However, CNNs can be limited in modelling temporal relationships among the time frames in an audio signal, while RNNs can be limited in modelling the long-range dependencies among the time frames. In this paper, we propose an Audio Captioning Transformer (ACT), which is a full Trans

**Results-oriented passage (PDF p. 4)**

Table 2 presents the results on AudioCaps test set. We compare the proposed ACT model with three representative audio captioning mod- els, “RNN+RNN” [3], “CNN+RNN” [6] and “CNN+Transformer” [9]. In these models, CNNs are all pre-trained on upstream audio- related tasks. As can be seen in Table 2 that the ACT model outper- forms “RNN+RNN” model substantially in all evaluation metrics and achieves slightly higher scores than “CNN+RNN” model in most metrics. Compared with the state-of-the-art “CNN+Transformer” ap- proach, ACT model outperforms it in machine translation metrics but gives slightly lower scores in CIDEr. As machine translation metr

**Caveat-oriented passage (PDF p. 1)**

the Transformer model in natural language processing [7], the RNN decoder has been replaced by a Transformer decoder in captioning models, and the “CNN+Transformer” architecture has been shown to achieve state-of-the-art performance in this area [8, 9]. Description of an audio signal needs to capture temporal-spatial relationships between audio obj

## 45. CL4AC: A Contrastive Loss for Audio Captioning

ID: `2107.09990` | Theme: Captioning/grounding | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2107.09990

Snapshot SHA-256: `29b0e41c5d19a561010a324ed4089976fcc5b39249792340d58427ca09c7f28e`

Abstract extract: Automated Audio captioning (AAC) is a cross-modal translation task that aims to use natural language to describe the content of an audio clip. As shown in the submissions received for Task 6 of the DCASE 2021 Challenges, this problem has received increasing interest in the community. The existing AAC systems are usually based on an encoder-decoder architecture, where the audio signal is encoded into a latent representation, and aligned with its corresponding text descriptions, then a decoder is used to generate the captions. However, training of an AAC system often encounters the problem of data scarcity, which may lead to inaccurate representation and audio-text alignment. To address this p

**Method-oriented passage (PDF p. 2)**

is the log mel-spectrogram of an audio clip with H and W being its height and width, respectively, C = {wm}M m=1 is the token sequence of a caption where wm is the m-th token in the caption C having M tokens, an is the log mel-spectrogram of the n-th audio clip in the dataset, and Cn is the token sequence of the n-th caption in the dataset. The sequence-to-sequence architecture with Convolutional Neu- ral Network (CNN) encoder and Transformer decoder are used as the basis of our proposed framework, as shown in Figure 1. This archi- tecture was shown to offer the state-of-the-art performance [9, 10] in Task 6 of the DCASE 2021 challenge.

**Results-oriented passage (PDF p. 4)**

Table 2 shows the performance of our proposed method on the Clotho v2 evaluation set. By adopting the contrastive loss technique dur- ing the training process, all the metrics except METERO increased on the evaluation set. For BLEU1, BLEU2, BLEU3, BLEU4, the relative improvement percentages for contrastive loss are 0.55%, 1.16%, 1.80%, and 2.88%, respectively. The n in BLEUn means the n-grams matching between the predicted results and ground truths. The ascending increases of the relative improvement from BLEU1 to BLEU4 show that our proposed method generates more matching n-grams, demonstrating a more ﬂuent and better quality captioning

**Caveat-oriented passage (PDF p. 2)**

To obtain accurate audio-text representation R while the model is trained with limited data, we use the self-supervised signal derived from the audio-text training data by contrasting samples. First, we construct mismatched audio-text pairs as negative samples. Then, a contrasting auxiliary task is designed to maximize the difference between the re

## 46. Audio Captioning Using Sound Event Detection

ID: `2110.01210` | Theme: Captioning/grounding | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2110.01210

Snapshot SHA-256: `97843cf84a00343e72241c34576de7c60515805d7d76ee21ade4d779764d5869`

Abstract extract: This technical report proposes an audio captioning system for DCASE 2021 Task 6 audio captioning challenge. Our proposed model is based on an encoder-decoder architecture with bi-directional Gated Recurrent Units (BiGRU) using pretrained audio features and sound event detection. A pretrained neural network (PANN) is used to extract audio features and Word2Vec is selected with the aim of extracting word embeddings from the audio captions. To create semantically meaningful captions, we extract sound events from the audio clips and feed the encoder-decoder architecture with sound events in addition to PANNs features. Our experiments on the Clotho dataset show that our proposed method significan

**Method-oriented passage (PDF p. 2)**

system [6], therefore Word2Vec is used for representing the cap- tions in the training dataset. Each unique word in the dataset is represented by v = [v1, ..., vi], where vi ∈R256 and 256 is the dimension for word embeddings. Encoded partial captions are con- catenated to the encoded PANNs features and sound event vectors to feed the decoder part. The decoder contains one GRU layer that contains 128 cells. The Softmax function is used after the fully connected layer. The decoder predicts probabilities of the unique words in the dataset and selects the most probable word as the predicted word. After ﬁnding the <eos> token, the whole sentence i

**Results-oriented passage (PDF p. 2)**

For evaluation, BLUE-n [9], METEOR [10], ROUGEL [11], CIDEr [12], SPICE [13], and SPIDEr [14] metrics are used. The matching words in the actual and predicted captions are calculated for BLEU- n. It calculates the precision for n-grams. Recall and precision are calculated for METEOR. ROUGEL calculates Longest Common Subsequence. CIDEr presents more semantic results by calculat- ing cosine-similarity between actual and predicted captions. SPICE parses the actual and predicted captions and creates scene graph rep- resentation. SPIDEr is a linear combination of CIDEr and SPICE. The comparison of our proposed method and Clotho V2 is shown in Tabl

**Caveat-oriented passage (PDF p. 2)**

We use Clotho [3] audio captioning dataset for our experiments. The challenge presents a new version of the Clotho dataset that is called Clotho V2. Clotho V2 contains 3840 audio clips in the devel- opment split. There is a validation split that has 1046 audio ﬁles in the Clotho V2. There are 1045 audio ﬁles in the evaluation split and 1043 audio ﬁ

## 47. DNSMOS P.835: A Non-Intrusive Perceptual Objective Speech Quality Metric to Evaluate Noise Suppressors

ID: `2110.01763` | Theme: Evaluation/reliability | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2110.01763

Snapshot SHA-256: `11488d4c0d300f3118cd7bd1f04fe6931ca1e7434a6e5d0c6a1f0c3a477d7901`

Abstract extract: Human subjective evaluation is the gold standard to evaluate speech quality optimized for human perception. Perceptual objective metrics serve as a proxy for subjective scores. We have recently developed a non-intrusive speech quality metric called Deep Noise Suppression Mean Opinion Score (DNSMOS) using the scores from ITU-T Rec. P.808 subjective evaluation. The P.808 scores reflect the overall quality of the audio clip. ITU-T Rec. P.835 subjective evaluation framework gives the standalone quality scores of speech and background noise in addition to the overall quality. In this work, we train an objective metric based on P.835 human ratings that outputs 3 scores: i) speech quality (SIG), ii

**Method-oriented passage (PDF p. 2)**

the quantity and diversity of the audio clips. A comparison of some common DNN-based non-intrusive speech quality assessment (NI-SQA) methods is given in Table 1. ACR is Absolute Catagorgy Rating [7]. DNSMOS P.835 is the ﬁrst P.835 based NI-SQA model we are aware of. In [16], we show that the NI-SQA metric called DNSMOS trained using subjective quality labels is more robust and re- liable than some of the other popular intrusive metrics. DNS- MOS is used to do model training and model selection during noise suppression development. DNSMOS is also used for doing ablation studies for noise suppressors [22, 23]. DNS- MOS has been quite popular, 

**Results-oriented passage (PDF p. 3)**

For predicting the MOS scores, we explored different conﬁg- urations of CNN-based models. The architecture for the best performing model is shown in Table 2. The input to the model is log power spectrogram with a 320 FFT size computed over a clip of length 9 seconds sampled at 16 kHz with a frame size of 20 ms and hop length of 10 ms. This results in an input di- mension of 900 x 161. We trained two different models with almost the same architecture except for the last layer. One model is trained to predict all 3 outputs (SIG, BAK, OVRL) and the other model is trained to predict only SIG. The rea- son is we found the prediction of SIG is a mu

**Caveat-oriented passage (PDF p. 2)**

We used the labeled data from the DNS Challenge V3 [10] to train DNSMOS P.835. The DNS Challenge V3 test set comprised of 600 noisy speech clips processed by about 40 different noise suppression models. The real recordings in the test set were captured in a variety of noise types and Sig- nal to Noise Ratio (SNR) and target levels. The test set is 

## 48. LaughNet: synthesizing laughter utterances from waveform silhouettes and a single laughter example

ID: `2110.04946` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2110.04946

Snapshot SHA-256: `32091d5bee95e32ac32f3f3097bc0b83c193c1882c70a23bfe65a8badf67c64d`

Abstract extract: Emotional and controllable speech synthesis is a topic that has received much attention. However, most studies focused on improving the expressiveness and controllability in the context of linguistic content, even though natural verbal human communication is inseparable from spontaneous non-speech expressions such as laughter, crying, or grunting. We propose a model called LaughNet for synthesizing laughter by using waveform silhouettes as inputs. The motivation is not simply synthesizing new laughter utterances, but testing a novel synthesis-control paradigm that uses an abstract representation of the waveform. We conducted basic listening test experiments, and the results showed that Laugh

**Method-oriented passage (PDF p. 1)**

same methodology as TTS. Speciﬁcally, laughter is treated as an extension of speech, thus presented by the same sym- bolic phonemes [6, 7] with additional speciﬁed contexts [8]. This setup is convenient but inadequate, as a linguistic inter- face cannot fully express the dynamic of laughter. Different approaches include training auto-encoder (AE) or variational autoencoder (VAE) [9] models that generate laughter from a latent vector, or assuming non-speech vocalizations are real- izations of emotions [10]. Most of these approaches lack the ability to control due to the highly abstract input. The text in TTS can be seen as the control interfac

**Results-oriented passage (PDF p. 4)**

the synthesis models and asked to judge quality. Figure 3a shows the results in which all of the models received low score with MU016 scoring slightly better than the other two. For the similarity evaluation, listeners were presented with two samples, one from a target and the other from one of the evaluated models. These included natural samples of the same target (NAT) and the natural laughter sample of a ran- dom speaker with a different sex than the target (CROSS). Figure 3b shows the results of the similarity evaluation, in which all three LaughNet models had lower scores than NAT but higher than CROSS. Out of all three LaughNet models, 

**Caveat-oriented passage (PDF p. 4)**

We proposed a model for synthesizing laughter utterances us- ing waveform silhouettes as input. The experimental results indicate that LaughNet can not only synthesize laughter with moderate quality and characteristics of the target speaker with just a single training example, but also have a reliable control interface that can dictate the shape of

## 49. Diverse Audio Captioning via Adversarial Training

ID: `2110.06691` | Theme: Captioning/grounding | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2110.06691

Snapshot SHA-256: `b8e8bcc675ae9c4b2fd121ba5709bd4770ae4526edd31fbae66248c40a818dcb`

Abstract extract: Audio captioning aims at generating natural language descriptions for audio clips automatically. Existing audio captioning models have shown promising improvement in recent years. However, these models are mostly trained via maximum likelihood estimation (MLE),which tends to make captions generic, simple and deterministic. As different people may describe an audio clip from different aspects using distinct words and grammars, we argue that an audio captioning system should have the ability to generate diverse captions for a fixed audio clip and across similar audio clips. To address this problem, we propose an adversarial training framework for audio captioning based on a conditional generat

**Method-oriented passage (PDF p. 1)**

Audio captioning aims at generating natural language descriptions for audio clips automatically. Existing audio captioning models have shown promising improvement in recent years. However, these models are mostly trained via maximum likelihood estimation (MLE), which tends to make captions generic, simple and deterministic. As different people may describe an audio clip from different aspects using distinct words and grammars, we argue that an audio captioning system should have the ability to generate diverse captions for a ﬁxed audio clip and across similar audio clips. To address this problem, we propose an adversarial training framework f

**Results-oriented passage (PDF p. 4)**

We conduct experiments to study the contribution of discriminator and evaluators in our proposed framework. The results are shown in Table 2. When only using the naturalness discriminator, the generated captions can be very diverse but get low scores on the n-gram based evaluation metrics. This is because the model would generate ran- dom captions which are irrelevant to the given audio clip, thus these captions would be diverse but were not semantically faithful to the audio clip. When only using the evaluators, the proposed framework degenerates to a conventional RL optimization method. When only

**Caveat-oriented passage (PDF p. 2)**

similar caption retrieval to guide the caption generation. Liu et al [16] proposed a contrastive loss to improve the quality of latent rep- resentation and the alignment between audio and texts. Audio captioning models are generally trained via MLE with ‘teacher-forcing’ strategy, where the model is trained to maximize the conditional log-likelihoo

## 50. SpeechT5: Unified-Modal Encoder-Decoder Pre-Training for Spoken Language Processing

ID: `2110.07205` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2110.07205

Snapshot SHA-256: `7f56b9cbd2c090f7431f34447dc43259f25f0a566cd17cc6a3fca808d573e299`

Abstract extract: Motivated by the success of T5 (Text-To-Text Transfer Transformer) in pre-trained natural language processing models, we propose a unified-modal SpeechT5 framework that explores the encoder-decoder pre-training for self-supervised speech/text representation learning. The SpeechT5 framework consists of a shared encoder-decoder network and six modal-specific (speech/text) pre/post-nets. After preprocessing the input speech/text through the pre-nets, the shared encoder-decoder network models the sequence-to-sequence transformation, and then the post-nets generate the output in the speech/text modality based on the output of the decoder. Leveraging large-scale unlabeled speech and text data, we 

**Method-oriented passage (PDF p. 2)**

we attempt to formulate each spoken language pro- cessing task as a speech/text to speech/text prob- lem via an encoder-decoder framework, which en- ables us to use the same pre-trained model with bimodal data across diverse tasks, as shown in Figure 1. To achieve this, we propose a uniﬁed- modal pre-training framework, SpeechT5, contain- ing an encoder-decoder backbone network and modal-speciﬁc pre/post-nets. With the pre-nets, the input speech/text is embedded in a shared space, and the encoder-decoder backbone net- work models the sequence-to-sequence conversion, from which the model-speciﬁc post-nets generate the speech/text output. Parti

**Results-oriented passage (PDF p. 5)**

Table 1: Results of ASR (speech to text) on the LibriSpeech dev and test sets when training on the 100 hours subset of LibriSpeech. † indicates that results are not reported in the corresponding paper and evaluated by ourselves.

**Caveat-oriented passage (PDF p. 9)**

In this paper, we have proposed SpeechT5 as a pre- trained encoder-decoder model for various spoken language processing tasks. We convert all spo- ken language processing tasks into a speech/text to speech/text format and propose a novel joint pre- training method to utilize cross-modal information by leveraging the unlabeled speech and text data. 

## 51. Continual self-training with bootstrapped remixing for speech enhancement

ID: `2110.10103` | Theme: Loop/data selection | Status: `excluded_after_screening`

Source: https://arxiv.org/pdf/2110.10103

Snapshot SHA-256: `17bf5e81f13a53369bd3da7e9661050caeea34dbace544e57626cc84653d656c`

Excluded: Related earlier RemixIT version; count the later 2202.08862 work once

Abstract extract: We propose RemixIT, a simple and novel self-supervised training method for speech enhancement. The proposed method is based on a continuously self-training scheme that overcomes limitations from previous studies including assumptions for the in-domain noise distribution and having access to clean target signals. Specifically, a separation teacher model is pre-trained on an out-of-domain dataset and is used to infer estimated target signals for a batch of in-domain mixtures. Next, we bootstrap the mixing process by generating artificial mixtures using permuted estimated clean and noise signals. Finally, the student model is trained using the permuted estimated sources as targets while we peri

**Method-oriented passage (PDF p. 1)**

which enables unsupervised training of separation models by gener- ating artiﬁcial mixtures of mixtures (MoMs) and letting the separa- tion model estimate and reassign the sources back to the ground-truth mixtures. MixIT has been experimentally shown to provide a robust unsupervised solution for speech enhancement under a variety of se- tups [6, 7, 8]. However, MixIT assumes access to in-domain noise samples and slightly alters the input SNR distribution by training on artiﬁcial MoMs with more than one noise sources [9]. On the other hand, teacher-student setups have shown signiﬁcant improvements in several audio processing tasks [10]. In [11

**Results-oriented passage (PDF p. 4)**

The speech enhancement results of the proposed method alongside supervised and unsupervised baselines are summarized in Table 1. The percentage of the available data denotes the portion of each dis- joint splits from the DNS or the LFSD paired data collections. For instance, the unsupervised RemixIT teacher pre-training requires un- supervised MixIT using 80% of the LFSD data pairs to simulate the noisy recordings D′ m and the other 20% for the clean OOD noise recordings D′ n, whilst the regular student training leverages the whole noisy DNS dataset. Notice that unsupervised and semi-supervised RemixIT does not depend on clean in-domain noise

**Caveat-oriented passage (PDF p. 2)**

where π ∈{(2, 3), (3, 2)} is the set of permutations of the output noise slots. However, MixIT depends on in-domain isolated noise recordings which makes it impractical for real-world settings. In most of the cases, matching the real noise distribution with the avail- able noise set Dn is a strenuous task. The data augmentation pro- posed in [9] sh

## 52. Synt++: Utilizing Imperfect Synthetic Data to Improve Speech Recognition

ID: `2110.11479` | Theme: Loop/data selection | Status: `selected_fulltext_review_plus_scoped_core_crosscheck`

Source: https://arxiv.org/pdf/2110.11479

Snapshot SHA-256: `66981e16185995c2e2c995438307dbe94d3c14eb29a2c79e1018b175d6bdd621`

Abstract extract: With recent advances in speech synthesis, synthetic data is becoming a viable alternative to real data for training speech recognition models. However, machine learning with synthetic data is not trivial due to the gap between the synthetic and the real data distributions. Synthetic datasets may contain artifacts that do not exist in real data such as structured noise, content errors, or unrealistic speaking styles. Moreover, the synthesis process may introduce a bias due to uneven sampling of the data manifold. We propose two novel techniques during training to mitigate the problems due to the distribution gap: (i) a rejection sampling algorithm and (ii) using separate batch normalization s

**Method-oriented passage (PDF p. 2)**

Let x be a speech signal and y be the corresponding token label, and pd(x,y), pg(x,y) denote the joint true and syn- thetic data distributions, respectively. We use the synthesizer as proposal distribution and use rejection sampling to make it closer to the true distribution. Following standard rejec- tion sampling [8], a synthetic data (x,y) is accepted with probability pd(x,y) Mpg(x,y), where scalar M > 0 is selected such that Mpg(x,y) > pd(x,y),∀(x,y) in domain of pd, i.e., M = maxx,y pd(x,y) pg(x,y). Azadi et. al. [9] proposed a rejection sampling method to match the distribution of the images from a genera- tive adversarial network to th

**Results-oriented passage (PDF p. 4)**

The WERs of the recognition models are reported in Ta- ble 1 on the two ofﬁcial test sets (test-clean and test-other). Synt++ gives signiﬁcant improvement over naively adding synthetic data to the training (Synt). Synthetic data with extended corpus: We study the effect of synthesizing speech from an extended text corpus in Table 2. In addition to LibriSpeech 960h, we also report the results when we have a smaller real dataset (LibriSpeech 100h). For LibriSpeech 100h, we use the text corpus of Lib- riSpeech 960h and synthesize 960 hours of synthetic data. For LibriSpeech 960h dataset, we double its text corpus by adding the text from the lang

**Caveat-oriented passage (PDF p. 2)**

State-of-the-art neural Text-to-Speech (TTS) architectures, such as Tacotron 2 [11] and FastSpeech 2 [12], are capable of generating speech indistinguishable from human speech. Controllable speech synthesis extends the TTS models beyond modeling the voice of a single or a few speakers to the entire style space of speech [5–7,13]. Using controllable

Additional interpretation and limitations: [core findings](CORE_FINDINGS.md).

## 53. WavLM: Large-Scale Self-Supervised Pre-Training for Full Stack Speech Processing

ID: `2110.13900` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2110.13900

Snapshot SHA-256: `0ca8836ebdf8236e610187738217d4c91c5ead13873472e476423f1561e9238e`

Abstract extract: Self-supervised learning (SSL) achieves great success in speech recognition, while limited exploration has been attempted for other speech processing tasks. As speech signal contains multi-faceted information including speaker identity, paralinguistics, spoken content, etc., learning universal representations for all speech tasks is challenging. To tackle the problem, we propose a new pre-trained model, WavLM, to solve full-stack downstream speech tasks. WavLM jointly learns masked speech prediction and denoising in pre-training. By this means, WavLM does not only keep the speech content modeling capability by the masked speech prediction, but also improves the potential to non-ASR tasks by 

**Method-oriented passage (PDF p. 2)**

setting. WavLM shows comparable performance to the wav2vec 2.0 and HuBERT, which achieves 1.8% and 3.2% WER on the test-clean and test-other sets, respectively. The contribution of the paper can be summarized as follows: 1) WavLM sheds light on a general pre-trained model for full stack speech processing tasks, in contrast to the previous SSL works focusing on a group of similar tasks. 2) We propose simple but effective modiﬁcations to the existing pre-trained models, which show general and consistent improvements across downstream tasks. 3) We scale-up self-supervised speech pre-training with more unlabeled data and longer training steps. 4)

**Results-oriented passage (PDF p. 2)**

• Speech separation is a classic multi-speaker task, which is the key to solving the cocktail party problem. The task can evaluate the model’s capability of extracting multiple speech signals from a mixture of sounds. WavLM achieves SOTA performance on the speech separation LibriCSS benchmark [21], and signiﬁcantly outperforms the previous Conformer model [22] by a 27.7% relative word error rate (WER) reduction.

**Caveat-oriented passage (PDF p. 8)**

push the limit of the speaker veriﬁcation system, we introduce the large margin ﬁne-tuning and quality-aware score calibration strategies [58] into our best systems and the corresponding results are listed at the bottom of Table II. With these two strategies, our best system exceeds the winner system [57] (Vox1-O: 0.461, Vox1-E: 0.634, Vox1-H: 0.99

## 54. Generating Diverse Realistic Laughter for Interactive Art

ID: `2111.03146` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2111.03146

Snapshot SHA-256: `9e2289ae951aee0cfe9e31cf91d604b74ab0ba5f0065b59862b74bb434de3a64`

Abstract extract: We propose an interactive art project to make those rendered invisible by the COVID-19 crisis and its concomitant solitude reappear through the welcome melody of laughter, and connections created and explored through advanced laughter synthesis approaches. However, the unconditional generation of the diversity of human emotional responses in high-quality auditory synthesis remains an open problem, with important implications for the application of these approaches in artistic settings. We developed LaughGANter, an approach to reproduce the diversity of human laughter using generative adversarial networks (GANs). When trained on a dataset of diverse laughter samples, LaughGANter generates div

**Method-oriented passage (PDF p. 1)**

We propose an interactive art project to make those rendered invisible by the COVID-19 crisis and its concomitant solitude reappear through the welcome melody of laughter and connections created and explored through advanced laughter synthesis approaches. However, the unconditional generation of the diversity of human emotional responses in high-quality auditory synthesis remains an open problem with important implications for applying these approaches in artistic settings. We developed LaughGANter, an approach to reproduce the diversity of human laughter using generative adversarial networks (GANs). When trained on a dataset of diverse laugh

**Results-oriented passage (PDF p. 2)**

Setup. Our model is implemented in PyTorch. We use a dataset containing 2145 laughter samples collected by the National Film Board of Canada. Samples are 1-8s long (22.05kHz mono) and were organized (and labeled) from subjects of different ages and genders (55% male, 45% female; 93% adult, 6% child, 1% teen). The audio data is augmented using a random combination of additive noise, shifting, and changing pitch and duration (using pyrubberband). Then, this data is converted to Mel spectrograms and fed into the model. In addition to qualitative evaluation, i.e., listening to generated samples, we have used Fréchet inception distance (FID) [23] 

**Caveat-oriented passage (PDF p. 2)**

Related work. Previous work in the ﬁeld of laughter generation involves [12] the use of oscillatory system [13], formant synthesis [14], articulatory speech synthesis [15], and hidden Markov models (HMM) [16]. Recently, some researchers have also used deep learning [12, 17] methods for laughter synthesis. However, GANs are advantageous in learning 

## 55. JTubeSpeech: corpus of Japanese speech collected from YouTube for speech recognition and speaker verification

ID: `2112.09323` | Theme: Evaluation/reliability | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2112.09323

Snapshot SHA-256: `9feea347fd194e1a2af55157e4cf94062e319ec93bb5a7ddbfef1f2060ac2495`

Abstract extract: In this paper, we construct a new Japanese speech corpus called "JTubeSpeech." Although recent end-to-end learning requires large-size speech corpora, open-sourced such corpora for languages other than English have not yet been established. In this paper, we describe the construction of a corpus from YouTube videos and subtitles for speech recognition and speaker verification. Our method can automatically filter the videos and subtitles with almost no language-dependent processes. We consistently employ Connectionist Temporal Classification (CTC)-based techniques for automatic speech recognition (ASR) and a speaker variation-based method for automatic speaker verification (ASV). We build 1) 

**Method-oriented passage (PDF p. 2)**

Unlike an ASR corpus, ASV requires high-quality speaker labels. Therefore, we propose an unsupervised method for only extracting monologue videos (i.e., single-speaker videos) from the obtained videos. Furthermore, we remove videos with text-to-speech (TTS) voices, which have different characteristics from natural speech. Removing non-speech and too-short videos. First, we delete videos without speech. Unlike the corpus for ASR, there is no need to align subtitle and speech. Therefore, we simply use voice activ- ity detection (VAD) here. We applied VAD to sections trimmed out based on the subtitles and used only sections mainly consisting of 

**Results-oriented passage (PDF p. 4)**

Figure 4 shows the ASR performance for various amounts of training data by changing the score threshold θ. We conﬁrmed that the normal test set was more difﬁcult than the easy test set. This result validates our design of the test set by controlling the difﬁculties based on the score. As regards the amounts of train- ing data, if we increase the amount of training data by reducing θ, the training data may contain more noisy transcriptions or dis- torted audio segments. Nevertheless, the ASR performance was improved, and the ﬁnal CERs were 5.2% in eval easy jun21 and 10.7% in eval normal jun21. These CER ranges are similar to other Japanese AS

**Caveat-oriented passage (PDF p. 2)**

of our experiments, can be interpreted as a production probability of at least 75% each second. Inference of long audio ﬁles. Alignment requires inference of the audio using the encoder and the CTC layer of a pre-trained ASR model. We found that many audio ﬁles are longer than three hours and their inference reaches a practical limitation: The memo

## 56. Joint Speech Recognition and Audio Captioning

ID: `2202.01405` | Theme: Captioning/grounding | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2202.01405

Snapshot SHA-256: `7a106936882dfa0cc0c5e5631f8bb540cf281e568ab30220e6bdd905f96743e9`

Abstract extract: Speech samples recorded in both indoor and outdoor environments are often contaminated with secondary audio sources. Most end-to-end monaural speech recognition systems either remove these background sounds using speech enhancement or train noise-robust models. For better model interpretability and holistic understanding, we aim to bring together the growing field of automated audio captioning (AAC) and the thoroughly studied automatic speech recognition (ASR). The goal of AAC is to generate natural language descriptions of contents in audio samples. We propose several approaches for end-to-end joint modeling of ASR and AAC tasks and demonstrate their advantages over traditional approaches, 

**Method-oriented passage (PDF p. 2)**

The independent ASR and AAC modeling frameworks discussed in Section 2 inherently follow a similar structure: acoustic feature en- coding and word sequence decoding. Exploiting this similarity and the serialized output training proposed in [22], we propose an intu- itive approach to our multi-task modeling: concatenating the word sequences WASR and WAAC as follows:

**Results-oriented passage (PDF p. 3)**

Following the synthetic multi-task dataset preparation procedure de- tailed in Section 3, we randomly mix the 37k speech samples from WSJ with 26k non-speech AudioCaps samples using mixing weight γ. To mix the 836 total samples in development and evaluation splits of WSJ, we proportionately select 600 samples at random from Au- dioCaps that are not seen during training. We choose 5 discrete val- ues for γ ∈{0.1, 0.2, 0.4, 0.6, 0.8} to perform the above mixing process, aiming to evaluate our proposed methods at different lev- els of background sounds. This process results in 37k × 5 ≈187k training samples and roughly 4k dev and eval samples.

**Caveat-oriented passage (PDF p. 2)**

The inter-dependency of ASR and AAC tasks, in addition to their similar modeling techniques, motivates us to explore models that can be trained jointly on these two tasks. However an important chal- lenge in realizing this joint modeling is the dearth of labeled real- world recordings with both a speech transcript and an audio caption. We overcome 

## 57. RemixIT: Continual self-training of speech enhancement models via bootstrapped remixing

ID: `2202.08862` | Theme: Loop/data selection | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2202.08862

Snapshot SHA-256: `1680f810cc283dae171e59cfec559aafe9c97cb6d5188e28b57fdebda29c7a9c`

Abstract extract: We present RemixIT, a simple yet effective self-supervised method for training speech enhancement without the need of a single isolated in-domain speech nor a noise waveform. Our approach overcomes limitations of previous methods which make them dependent on clean in-domain target signals and thus, sensitive to any domain mismatch between train and test samples. RemixIT is based on a continuous self-training scheme in which a pre-trained teacher model on out-of-domain data infers estimated pseudo-target signals for in-domain mixtures. Then, by permuting the estimated clean and noise signals and remixing them together, we generate a new set of bootstrapped mixtures and corresponding pseudo-ta

**Method-oriented passage (PDF p. 2)**

In this work, we propose RemixIT which is based on several aforementioned state-of-the-art SSL strategies for pseudo- labeling and continual training while also providing a novel technique for training speech enhancement models with OOD data. Our method trains a student model using self-augmented mixtures generated by permuting and remixing the teacher’s estimates and using them as pseudo-targets for regular re- gression. Moreover, RemixIT treats self-training as a lifelong process while continually updating the teacher model using the student’s weights that consequently leads to faster and more

**Results-oriented passage (PDF p. 7)**

B. Self-supervised and semi-supervised speech enhancement Table I summarizes the mean speech enhancement per- formance of RemixIT against in-domain and cross-domain supervised and SSL baselines with the same architecture on the DNS test set. Notice that in both semi-supervised and unsupervised cases, the learned RemixIT’s student does not assume access to in-domain clean speech nor to noise samples like the previous state-of-the-art SSL speech enhancement algorithms. For instance, SSL RemixIT’s teacher pre-training is performed with OOD MixIT by using 80% of the LFSD noisy recordings D′ m and rest 20% to simulate the isolated noise recordings

**Caveat-oriented passage (PDF p. 2)**

a subset of outputs of a pre-trained MixIT model to solve the input SNR distribution mismatch. Furthermore, a student model could also perform test-time adaptation by using the teacher’s estimated waveforms as targets [36]. However, those approaches enforce only the consistency of the student’s pre- dictions over a frozen teacher’s output pseudo-ta

## 58. Leveraging Pre-trained BERT for Audio Captioning

ID: `2203.02838` | Theme: Captioning/grounding | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2203.02838

Snapshot SHA-256: `6d2b2e70a19dfaf5e5d574cdb824508bcf6dba94f5d6c7519dade84be30f5ec7`

Abstract extract: Audio captioning aims at using natural language to describe the content of an audio clip. Existing audio captioning systems are generally based on an encoder-decoder architecture, in which acoustic information is extracted by an audio encoder and then a language decoder is used to generate the captions. Training an audio captioning system often encounters the problem of data scarcity. Transferring knowledge from pre-trained audio models such as Pre-trained Audio Neural Networks (PANNs) have recently emerged as a useful method to mitigate this issue. However, there is less attention on exploiting pre-trained language models for the decoder, compared with the encoder. BERT is a pre-trained lan

**Method-oriented passage (PDF p. 1)**

widely investigated. Xu et al. [11] propose an approach that uses transfer learning to exploit local and global information from audio tagging and acoustic scene classiﬁcation, respectively. Pre-trained Audio Neural Networks (PANNs) [12] are the models pre-trained on AudioSet [13], which have achieved great success as the encoder [5]–[7], [14] in the audio captioning system. Nevertheless, compared with the audio encoder, there is less attention on exploiting pre-trained NLP models for the language decoder in the audio captioning model. Koizumi et al. [15] used a frozen Generative Pre-Training model (GPT-2) [16] with the retrieval of similar c

**Results-oriented passage (PDF p. 3)**

A. Comparison with baseline methods We compare our proposed approach with ﬁve baseline methods, namely, the TopDown-AlignedAtt [8] model, the CNN10-AT model [11] which uses pre-trained Audio Tagging model as the encoder, the Audio Captioning Transformer (ACT) [3], which is the ﬁrst convolution-free architecture, the model in [15] that uses frozen GPT-2 and audio-based similar caption retrieval, and ﬁnally the current state-of-the-art model [17] on AudioCaps based on BART and AudioSet tags. We report the performance of the ﬁrst four baseline methods in the upper part of Table II. It can be observed that the ﬁnal method [17] cannot generalize w

**Caveat-oriented passage (PDF p. 3)**

During the inference stage, the mel-spectrogram along with the token “<soc>” are fed into the encoder and decoder separately to generate the ﬁrst token. Then, the following tokens are predicted based on the previously generated tokens until the token “<eoc>” or the maximum length (50 tokens in our experiments) is reached. The beam search strategy [

## 59. Detection of AI Synthesized Hindi Speech

ID: `2203.03706` | Theme: Speech/audio generation and control | Status: `excluded_after_screening`

Source: https://arxiv.org/pdf/2203.03706

Snapshot SHA-256: `d101503f9e577cdea65e0d5c051bda2f289141fc25b9692008e8fe137d4436c4`

Excluded: Synthetic Hindi detection; peripheral to captioning/generation objectives

Abstract extract: The recent advancements in generative artificial speech models have made possible the generation of highly realistic speech signals. At first, it seems exciting to obtain these artificially synthesized signals such as speech clones or deep fakes but if left unchecked, it may lead us to digital dystopia. One of the primary focus in audio forensics is validating the authenticity of a speech. Though some solutions are proposed for English speeches but the detection of synthetic Hindi speeches have not gained much attention. Here, we propose an approach for discrimination of AI synthesized Hindi speech from an actual human speech. We have exploited the Bicoherence Phase, Bicoherence Magnitude, M

**Method-oriented passage (PDF p. 1)**

Abstract—The recent advancements in generative artiﬁcial speech models have made possible the generation of highly realistic speech signals. At ﬁrst, it seems exciting to obtain these artiﬁcially synthesized signals such as speech clones or deep fakes but if left unchecked, it may lead us to digital dystopia. One of the primary focus in audio forensics is validating the authenticity of a speech. Though some solutions are proposed for English speeches but the detection of synthetic Hindi speeches have not gained much attention. Here, we propose an approach for discrimination of AI synthesized Hindi speech from an actual human speech. We have e

**Results-oriented passage (PDF p. 3)**

and ‘AI Synthesized speech’, the Bagged Trees classiﬁer pro- vided the highest accuracy of 98.9%. Next, we experimented for a more ﬁner multi-class classiﬁcation, considering the ﬁves classes as ‘Amazon Polly’, ‘Hearling’, ‘Human Speech’, ‘IITM TTS’, and ‘Voice Maker’. Here, four classes ‘Amazon Polly’, ‘Hearling’, ‘IITM TTS’, and ‘Voice Maker’ represent the ‘AI Synthesized speech’. Here again, the Bagged Trees classiﬁer gave us the highest accuracy of 93.4%. The confusion matrix for both the binary-class and mutli-class classiﬁcation for the Bagged Trees classiﬁer is shown in Fig. 1 and Fig. 2 respectively. Based on the confusion matrix, we 

**Caveat-oriented passage (PDF p. 1)**

∗Dhirubhai Ambani Institute of Information and Communication Technology Gandhinagar, Gujarat, India Email: {201801417,201801110,Priyanka Singh}@daiict.ac.in † Indian Institute of Technology Jammu, Jammu, India Email: singh.arun.kumar@ieee.org

## 60. ConferencingSpeech 2022 Challenge: Non-intrusive Objective Speech Quality Assessment (NISQA) Challenge for Online Conferencing Applications

ID: `2203.16032` | Theme: Evaluation/reliability | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2203.16032

Snapshot SHA-256: `fc98cabca3f6258a194202e5d4b5f29820f0cb133594e09e30b177b5fb27c2fb`

Abstract extract: With the advances in speech communication systems such as online conferencing applications, we can seamlessly work with people regardless of where they are. However, during online meetings, speech quality can be significantly affected by background noise, reverberation, packet loss, network jitter, etc. Because of its nature, speech quality is traditionally assessed in subjective tests in laboratories and lately also in crowdsourcing following the international standards from ITU-T Rec. P.800 series. However, those approaches are costly and cannot be applied to customer data. Therefore, an effective objective assessment approach is needed to evaluate or monitor the speech quality of the ongo

**Method-oriented passage (PDF p. 2)**

ulate the voice impairment scenario that may be encountered in the online meeting scene. In order to prevent the possible speaker-dependent behavior of the trained model, the original speech data was selected from three publicly available datasets Magic data [17], ST Mandarin [18] and AIshell 100h [19]. Each speech clip in the source data was processed with one type of impairment and only one type. The different impairment types and the corresponding percentage of the speech clips ap- plied with each impairment type are listed in Table 1. Based on the speech clips processed in the above step, we applied another speech processing step includin

**Results-oriented passage (PDF p. 3)**

The OR represents the number of outlier-points to the to- tal number of speech utterances. An outlier is deﬁned as a point for which the prediction error is larger than the 95% con- ﬁdence interval of the MOS value. PCC, on the other hand, measures the linear relationship between a model’s estimation and the subjective data. Meanwhile, due to bias or offsets, dif- ferent gradients and different qualitative rank orders are always present in subjective evaluations. The statistical uncertainty al- ways exists in the collected MOS. Therefore, a mapping func- tion is recommended to compensate for the possible variance between several subjective ex

**Caveat-oriented passage (PDF p. 2)**

In this challenge, comprehensive training datasets with ground truth MOS were provided to each registered team. It is antici- pated that the participating teams use only the impaired speech signals to design corresponding algorithms or models, so that the output prediction scores are close to the real MOS. The ﬁnal ranking of this challenge will be

## 61. Deep Speech Based End-to-End Automated Speech Recognition (ASR) for Indian-English Accents

ID: `2204.00977` | Theme: Speech/audio generation and control | Status: `excluded_after_screening`

Source: https://arxiv.org/pdf/2204.00977

Snapshot SHA-256: `9753868d3ded0a21e42773e00673b740e6a1dc57915f9ee8af53857d3527b6a6`

Excluded: Weakly relevant Indian-English ASR overview; excluded from architecture evidence

Abstract extract: Automated Speech Recognition (ASR) is an interdisciplinary application of computer science and linguistics that enable us to derive the transcription from the uttered speech waveform. It finds several applications in Military like High-performance fighter aircraft, helicopters, air-traffic controller. Other than military speech recognition is used in healthcare, persons with disabilities and many more. ASR has been an active research area. Several models and algorithms for speech to text (STT) have been proposed. One of the most recent is Mozilla Deep Speech, it is based on the Deep Speech research paper by Baidu. Deep Speech is a state-of-art speech recognition system is developed using end

**Method-oriented passage (PDF p. 2)**

In 2017 Deep Speech model, a state-of-the-art speech recognition system developed using end-to-end deep learning was presented. It is based on Baidu Research Lab’s research paper. Deep Speech tend to perform in challenging noisy environments better than widely used, state-of-the-art commercial speech systems. As it is based on deep learning, the training datasets used to train are mostly comprised of American-English accents. Hence, it performs poorly for all other English accents. India has always been known as a country with vast diversity. India houses over 19,500 languages or dialects being spoken as a mother tongue (Chandramouli and Gene

**Results-oriented passage (PDF p. 3)**

Automated Speech Recognition. DL impacted many Machines Learning (ML) fields that completely rely on domain knowledge. DL can replace decades of research of modeling with its DL models, which have higher accuracy and require less manual labor. There are some most commonly used methods for speech recognition listed below- Hidden Markov Models (HMMs): Hidden Markov Models are statistical model based on the Markov process with unknown parameters, where the probability of the current state solely depends on current state and is independent of previous states. It is a type of Acoustic Model (AM) of speech recognition. In HMM, the states are not di

**Caveat-oriented passage (PDF p. 4)**

the time varying information like time-varying spectra of speech sounds. This limitation is tackled by Recurrent Neural Networks (RNNs), which have ability of incorporating feedback structure by having connection between units of different layers and memorizing the time-varying information. Classification and recognition of static patterns is the m

## 62. UTMOS: UTokyo-SaruLab System for VoiceMOS Challenge 2022

ID: `2204.02152` | Theme: Evaluation/reliability | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2204.02152

Snapshot SHA-256: `fe2afa1b8106d59019e54e69f87a10af7af4408e01ea3f6fa458f8dc1925636f`

Abstract extract: We present the UTokyo-SaruLab mean opinion score (MOS) prediction system submitted to VoiceMOS Challenge 2022. The challenge is to predict the MOS values of speech samples collected from previous Blizzard Challenges and Voice Conversion Challenges for two tracks: a main track for in-domain prediction and an out-of-domain (OOD) track for which there is less labeled data from different listening tests. Our system is based on ensemble learning of strong and weak learners. Strong learners incorporate several improvements to the previous fine-tuning models of self-supervised learning (SSL) models, while weak learners use basic machine-learning methods to predict scores from SSL features. In the C

**Method-oriented passage (PDF p. 3)**

We use an ensemble of models for prediction robustness. Speciﬁcally, we use the stacking method [15, 16] illustrated in Fig. 2 as the ensemble method. We use not only ﬁne-tuned SSL models but also simple regression models using utterance-level features. We refer to the former and latter models as “strong learners” and “weak learners,” respectively. The weak learners are a combination of feature extractions and regression methods. We propose using pretrained-SSL- model-based mean embeddings for feature extraction. Specif- ically, we extract embeddings of input utterances and compute the mean for all frames, taking as inspiration the structure 

**Results-oriented passage (PDF p. 4)**

4.3. Ablation study on SSL-based models We conducted ablation studies for each of the methods de- scribed in Section 3.1. We denote a strong learner using all the methods in Section 3.1 as “UTMOS strong.” A method based on ﬁne-tuning of the SSL model [8], which is a baseline method of the challenge, was designated as “SSL-MOS.” Table 2 lists the results. The best results are shown in bold, while the worst ones are underlined except for UTMOS strong and SSL-MOS. We can see that all of our methods outperformed SSL-MOS in almost all indices. Furthermore, in the main track, the method that excluded data augmentation or phoneme encoder from UT- MO

**Caveat-oriented passage (PDF p. 2)**

Table 1: Datasets used in VoiceMOS Challenge 2022: “closed/open” indicates that system used to synthesize speech is in- cluded/excluded in training data; “labeled/unlabeled” indicates that corresponding MOS score is included/excluded.

## 63. Aggression in Hindi and English Speech: Acoustic Correlates and Automatic Identification

ID: `2204.02814` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2204.02814

Snapshot SHA-256: `89abfb84ba31ac14c180d612f1f79fcdce97f851db8bc0725bb9626985496c70`

Abstract extract: In the present paper, we will present the results of an acoustic analysis of political discourse in Hindi and discuss some of the conventionalised acoustic features of aggressive speech regularly employed by the speakers of Hindi and English. The study is based on a corpus of slightly over 10 hours of political discourse and includes debates on news channel and political speeches. Using this study, we develop two automatic classification systems for identifying aggression in English and Hindi speech, based solely on an acoustic model. The Hindi classifier, trained using 50 hours of annotated speech, and English classifier, trained using 40 hours of annotated speech, achieve a respectable acc

**Method-oriented passage (PDF p. 2)**

In addition to this, audio of the complete data was also extracted in .wav format and stored separately as the speech corpus. It was done for two reasons – it is comparatively easier to store, maintain, process and share speech data than multimodal data and more importantly, for the current purposes, we only needed speech data as we would be training the system based only on speech (more specifically prosodic) and textual features. Moreover, it would not be a mammoth task to integrate the video with this annotated and transcribed speech data at a later stage if we need to use the video features as well.

**Results-oriented passage (PDF p. 4)**

4. Classification Experiments and Results We used a total dataset of approximately 50 hours in Hindi and 40 hours in English to train two classifiers – one each for English and Hindi – for automatic identification of aggression in speech. The distribution of each class in the dataset is given in Table 2 below

**Caveat-oriented passage (PDF p. 2)**

2. Political Speeches – In addition to the political debates, political speeches available on the web are also included in the corpus. However, unlike the debates these are monologues and are largely aggressive. These make up around 80 hours of total data in Hindi and English each. These speeches were downloaded using the same methods as above and 

## 64. Caption Feature Space Regularization for Audio Captioning

ID: `2204.08409` | Theme: Captioning/grounding | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2204.08409

Snapshot SHA-256: `64533e6be35b2c8210e160f71ec8780707c6d68d47a39e39b0eff6e561635d54`

Abstract extract: Audio captioning aims at describing the content of audio clips with human language. Due to the ambiguity of audio, different people may perceive the same audio differently, resulting in caption disparities (i.e., one audio may correlate to several captions with diverse semantics). For that, general audio captioning models achieve the one-to-many training by randomly selecting a correlated caption as the ground truth for each audio. However, it leads to a significant variation in the optimization directions and weakens the model stability. To eliminate this negative effect, in this paper, we propose a two-stage framework for audio captioning: (i) in the first stage, via the contrastive learni

**Method-oriented passage (PDF p. 2)**

For the audio captioning task, an audio clip has multiple captions to describe how different annotators feel about it. Different perceptions cause the disparity of the captions in semantics, however, for each audio, only one caption will be randomly selected as the ground truth for each training to generate the description of the audio, and this training strategy can easily affect the performance of the model and make it unstable. To solve the above problem, we propose a proxy feature optimization method to regularize the training of the caption generation, the key module is shown in Block B of Fig. 2. Our method is a two-stage audio captioni

**Results-oriented passage (PDF p. 4)**

We use the same metrics used in the DCASE Challenge to evaluate the performance of our proposed method, including machine translation metrics: BLEU𝑛[24], ROUGE𝐿[25], ME- TEOR [26] and captioning metrics: CIDEr [27], SPICE [28], SPIDEr [29]. And the 𝑛in BLEU means 𝑛−gram. The machine translation metrics are used to measure the word accuracy and recall of generated text compared to the ground truth. The captioning metrics are customized to the captioning task, taking into consideration the scene graph contained within the generated caption as well as the 𝑛-gram’s frequency-inverse document frequency (TF-IDF). The seman- tic ﬁdelity and syntacti

**Caveat-oriented passage (PDF p. 4)**

The Clotho dataset [2] and the Audiocaps dataset [12] are two datasets that are commonly used for audio captioning tasks. There are two versions of the Clotho dataset, Clotho-v1 and Clotho-v2 respectively. Each audio clip has ﬁve captions describing the audio contents, and the annotator uses only the audio signal for annotation. However, the Audioc

## 65. Automated Audio Captioning using Audio Event Clues

ID: `2204.08567` | Theme: Captioning/grounding | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2204.08567

Snapshot SHA-256: `1021795d4bfa375d3042b3e8950a463c65a0cefac4b9d6834ed9aee3f956ad18`

Abstract extract: Audio captioning is an important research area that aims to generate meaningful descriptions for audio clips. Most of the existing research extracts acoustic features of audio clips as input to encoder-decoder and transformer architectures to produce the captions in a sequence-to-sequence manner. Due to data insufficiency and the architecture's inadequate learning capacity, additional information is needed to generate natural language sentences, as well as acoustic features. To address these problems, an encoder-decoder architecture is proposed that learns from both acoustic features and extracted audio event labels as inputs. The proposed model is based on pre-trained acoustic features and 

**Method-oriented passage (PDF p. 1)**

model is presented with gated recurrent units (GRU) using a new Chinese audio captioning dataset [9]. To solve infrequent classes problems in the captions, an encoder-decoder model with caption decoder and content word decoder is presented in [7]. Pre-trained audio and text embeddings increase the performance of audio captioning in the studies [6], [10]. Recent studies propose transformer models to generate captions. A transformer model with keyword estimation is proposed in [11]. Another transformer model is presented in [12] using temporal and time-frequency information in audio clips. Previous studies state the data insufﬁciency problem on

**Results-oriented passage (PDF p. 5)**

In order to obtain acoustic features, Log Mel energy features are extracted in the same way as [3] using 96 ms Hamming window and 50% overlap. 64 log Mel energies are calculated for each audio frame as A ∈RT ×M, where M is the number of Mel bins and T is the number of windows in the audio clip. In the encoder-decoder architecture, the ﬁrst BiGRU layer contains 32 cells and the second BiGRU layer contains 64 cells in the acoustic encoder, empirically. There is one GRU layer that contains 128 cells for encoding partial captions in the linguistic encoder. For the encoding words, we experiment with both GRU and BiGRU layers. Since using the BiGRU

**Caveat-oriented passage (PDF p. 2)**

Most previous studies are focused on encoder-decoder mod- els on audio captioning. AAC is presented with an encoder- decoder model in [1]. This architecture contains an encoder with three Bi-directional GRU layers and a decoder with two GRU layers with an attention mechanism between encoder and decoder. [3] uses the same encoder-decoder architectur

## 66. FLEURS: Few-shot Learning Evaluation of Universal Representations of Speech

ID: `2205.12446` | Theme: Evaluation/reliability | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2205.12446

Snapshot SHA-256: `670824d0dfaa98f56b7f774116d5d70bdeb7990ce031ebe690e9c86c6053283f`

Abstract extract: We introduce FLEURS, the Few-shot Learning Evaluation of Universal Representations of Speech benchmark. FLEURS is an n-way parallel speech dataset in 102 languages built on top of the machine translation FLoRes-101 benchmark, with approximately 12 hours of speech supervision per language. FLEURS can be used for a variety of speech tasks, including Automatic Speech Recognition (ASR), Speech Language Identification (Speech LangID), Translation and Retrieval. In this paper, we provide baselines for the tasks based on multilingual pre-trained models like mSLAM. The goal of FLEURS is to enable speech technology in more languages and catalyze research in low-resource speech understanding.

**Method-oriented passage (PDF p. 2)**

train speech hours 231h 134h 116h 237h 124h 112h 32h 987h dev speech hours 29h 18h 14h 24h 16h 14h 4h 120h test speech hours 68h 43h 33h 58h 37h 35h 9h 283h train transcript tokens 1475k 772k 630k 1072k 699k 525k 405k 5578k dev transcript tokens 184k 107k 75k 116k 93k 65k 51k 692k test transcript tokens 443k 260k 181k 272k 210k 158k 116k 1640k

**Results-oriented passage (PDF p. 3)**

We add two LSTM[28] layer to ﬁne-tune our pre-trained mod- els for ASR, using a CTC [29] loss. The baselines use a 6100- character vocabulary built from SRC NORM. We do not include meta information of language identiﬁcation labels in modeling, and there is no language model used for hypothesis scoring. We ﬁne-tune on all 102 locales, and report results for multilingual ﬁne-tuning from both speech-only pre-trained and speech-text pre-trained models. Our ﬁnetuning parameters follow [10]. We evaluate ﬁne-tuned ASR models for all locales in terms of % character error rate (CER). Experiments show that ﬁne-tuning from multimodal pre-training is sli

**Caveat-oriented passage (PDF p. 3)**

FLEURS enables evaluations for several core speech tasks. In this paper, we focus on speech recognition, speech language identiﬁcation and speech-text retrieval. Training a giant model from scratch on the FLEURS dataset will easily overﬁt. Fine- tuning on limited supervised data from a model pre-trained on a vast amount of (unsupervised) data has a

## 67. CLAP: Learning Audio Concepts From Natural Language Supervision

ID: `2206.04769` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2206.04769

Snapshot SHA-256: `4850b5a6e5c00187b38e914513136c5277e9480f31e946e9a79def48ed606416`

Abstract extract: Mainstream Audio Analytics models are trained to learn under the paradigm of one class label to many recordings focusing on one task. Learning under such restricted supervision limits the flexibility of models because they require labeled audio for training and can only predict the predefined categories. Instead, we propose to learn audio concepts from natural language supervision. We call our approach Contrastive Language-Audio Pretraining (CLAP), which learns to connect language and audio by using two encoders and a contrastive learning to bring audio and text descriptions into a joint multimodal space. We trained CLAP with 128k audio and text pairs and evaluated it on 16 downstream tasks 

**Method-oriented passage (PDF p. 4)**

We introduced CLAP for learning audio concepts from nat- ural language supervision. CLAP does not require gold stan- dard class labels for training, enables ﬂexible class predic- tion, and generalizes to multiple downstream tasks. The train- ing data consists of 128k audio-text pairs which is at least 0.001% smaller than what similar Computer Vision models used. Nonetheless, CLAP establishes SoTA in Zero-Shot per- formance and SoTA in supervised performance for 5 tasks. Hence, CLAP shows potential for building an audio founda- tion model that can learn by natural language supervision and can generalize to a wide range of tasks while achieving

**Results-oriented passage (PDF p. 3)**

Table 1. CLAP (ZS) Zero-Shot outperforms the literature. CLAP (Best) is the best performance among our supervised setups. Higher is better for all numbers, DCASE17 employs F1, FSD50K and AudioSet employs mAP, everything else uses accuracy.

**Caveat-oriented passage (PDF p. 3)**

Pre-processing. We used log Mel spectrogram representa- tions of audio with a sampling rate of 44.1 KHz, hop size of 320 secs, window size 1024 secs, and 64 Mel bins in the range of 50-8000 Hz. During training, each audio clip is ran- domly truncated to a continuous segment of 5 secs, or padded if shorter. The captions were not altered. The batches

## 68. Learnable Frequency Filters for Speech Feature Extraction in Speaker Verification

ID: `2206.07563` | Theme: Evaluation/reliability | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2206.07563

Snapshot SHA-256: `2a2e82aa185cf500e0175f4c5c4e0330c2bb457850cb8f8ed9d98d4311e1825d`

Abstract extract: Mel-scale spectrum features are used in various recognition and classification tasks on speech signals. There is no reason to expect that these features are optimal for all different tasks, including speaker verification (SV). This paper describes a learnable front-end feature extraction model. The model comprises a group of filters to transform the Fourier spectrum. Model parameters that define these filters are trained end-to-end and optimized specifically for the task of speaker verification. Compared to the standard Mel-scale filter-bank, the filters' bandwidths and center frequencies are adjustable. Experimental results show that applying the learnable acoustic front-end improves speake

**Method-oriented passage (PDF p. 2)**

Data-driven harmonic ﬁlters were proposed in [23], where learnable ﬁlters, instead of the commonly used Mel-scale ﬁl- ters, were applied to the STFT output. H triangular ﬁlters and F harmonics of each ﬁlter are learned in order to produce a 3-dimensional feature with shape F × H × T, represent- ing Harmonic×Frequency×Time as in the harmonic constant- Q transform (HCQT). State-of-the-art results across various tasks, like automatic music tagging and keyword spotting, were achieved with this trainable front-end. The learnable ﬁlters proposed in this paper can be viewed as a simpliﬁed version of these harmonic ﬁlters by omitting the harmonic ter

**Results-oriented passage (PDF p. 3)**

The number of frequency bins (N in Eq. 1) in STFT is set to 512, and the number of band-pass ﬁlters in both LFF and MF- BANK is 64. The Equal Error Rate (EER%) results on the Vox- celeb1 test sets are summarized in Table 1. We can see that LFF outperforms MFBANK on all test sets, and that T-type and B- type learnable ﬁlters do not show signiﬁcant differences in the model performance. To understand what the ﬁlters have learned in the training, we analyzed their parameters. The bandwidths and center fre- quencies are plotted in Fig. 3. The x-axis of (a) and (b) repre- sents the index of the ﬁlter, ranging from 0 to 63 (i.e. there are 64 ﬁlters 

**Caveat-oriented passage (PDF p. 2)**

In [22], it was shown that, without constraint on the ﬁlter weights, the frequency responses of the learned ﬁlters may ex- hibit spiky shapes and spread over a wide range, even to the negative frequency region, which do not appeal to our intuition. In view of these undesirable outcomes, Gabor ﬁlters were pro- posed to parameterize the convolution w

## 69. Analysis of Self-Supervised Learning and Dimensionality Reduction Methods in Clustering-Based Active Learning for Speech Emotion Recognition

ID: `2206.10188` | Theme: Loop/data selection | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2206.10188

Snapshot SHA-256: `f75ef93020783f5b3d3f6f5d0d561686ac8c9957b179798ecd4b60aca3c2ec82`

Abstract extract: When domain experts are needed to perform data annotation for complex machine-learning tasks, reducing annotation effort is crucial in order to cut down time and expenses. For cases when there are no annotations available, one approach is to utilize the structure of the feature space for clustering-based active learning (AL) methods. However, these methods are heavily dependent on how the samples are organized in the feature space and what distance metric is used. Unsupervised methods such as contrastive predictive coding (CPC) can potentially be used to learn organized feature spaces, but these methods typically create high-dimensional features which might be challenging for estimating data

**Method-oriented passage (PDF p. 2)**

Fig. 2 depicts a block diagram of the present experiments. First, a standard acoustic feature (log-mel) representation is obtained from an input signal. Then, an SSRL algorithm called contrastive predictive coding (CPC) [17] is applied to the data. CPC aims to produce linearly separable features that can be used to predict signal evolution over time [20, 21]. CPC has already been suc- cessfully used with clustering-based approaches (e.g. [21–23]) and also produces features that separate suprasegmental proper- ties such as speaker identities [17]. However, to the best of our knowledge, [24] is the only study so far using CPC for AL. Next, an a

**Results-oriented passage (PDF p. 4)**

higher labeling budgets are also included in the analyses. Each cross-fold experiment was repeated ﬁve times to account for the minor variability in the results due to t-SNE and MAL random initialization. We use Matthew’s correlation coefﬁcient (MCC) [42] as our primary evaluation metric. As argued by e.g. [43], MCC can be considered as one of the most informative quality measures for binary classiﬁers since it requires good results from all four confusion matrix categories to output a high score. After obtaining a set of labeled data from MAL, an SVM with an RBF kernel was trained with the labeled training data and tested on the test data. T

**Caveat-oriented passage (PDF p. 3)**

features, the mean over the time dimension of the encoder out- puts zt was computed to get 256-dimensional utterance features (ignoring potential zero padding). The context latent represen- tations ct were also tested but resulted in slightly worse results than using zt, and hence are not separately reported. In addition to the mean, we also tested

## 70. Annotated Speech Corpus for Low Resource Indian Languages: Awadhi, Bhojpuri, Braj and Magahi

ID: `2206.12931` | Theme: Data/Indic speech | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2206.12931

Snapshot SHA-256: `0580ddd053410299c655b6fae3f0cf5c159310a91ad806c1031e4df7eee4d632`

Abstract extract: In this paper we discuss an in-progress work on the development of a speech corpus for four low-resource Indo-Aryan languages -- Awadhi, Bhojpuri, Braj and Magahi using the field methods of linguistic data collection. The total size of the corpus currently stands at approximately 18 hours (approx. 4-5 hours each language) and it is transcribed and annotated with grammatical information such as part-of-speech tags, morphological features and Universal dependency relationships. We discuss our methodology for data collection in these languages, most of which was done in the middle of the COVID-19 pandemic, with one of the aims being to generate some additional income for low-income groups speak

**Method-oriented passage (PDF p. 3)**

• Training from scratch: We used Kaldi recipes [18] pro- vided by [19]3 to train the ASR models for these lan- guages from scratch. We experimented with four differ- ent models - monophone model (mono), triphone model (tri1), triphones with Delta feature augmentation (tri2b) and triphones with both delta feature augmentation and speaker normalisation (tri3b). • Transfer learning: We ﬁne-tuned wav2vec-large-xlsr-53 [20] model using the complete, multilingual dataset and evaluated the performance of the model for the whole test set.

**Results-oriented passage (PDF p. 3)**

For both the approaches. we used two kinds of setups for training and evaluation. In the ﬁrst setup, we trained monolin- gual models of each of the languages and calculated average WER of these. In the second setup, we trained a multilingual model and evaluated all the languages together. This was also meant to test if a single multilingual model gives a performance improvement over multiple monolingual models even with this small dataset or not. We report the WER for each of these mod- els for each language in Table 3. As is evident, WER obtained on at least one of the Hindi models for all the languages is better than the models trained for 

**Caveat-oriented passage (PDF p. 2)**

Although Automatic Speech Recognition (ASR) has done remarkable progress in last few years because of the availability of speech corpora of various kinds for “ofﬁcial” and relatively richer languages, it is still an extremely challenging tasks for non-scheduled, extremely low-resourced languages, generally spoken by people with low income because o

## 71. Automated Audio Captioning and Language-Based Audio Retrieval

ID: `2207.04156` | Theme: Captioning/grounding | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2207.04156

Snapshot SHA-256: `ac78d10aa2512c9cb3549fdfe4d325b9c960b884e6300df24c3778bffb37632e`

Abstract extract: This project involved participation in the DCASE 2022 Competition (Task 6) which had two subtasks: (1) Automated Audio Captioning and (2) Language-Based Audio Retrieval. The first subtask involved the generation of a textual description for audio samples, while the goal of the second was to find audio samples within a fixed dataset that match a given description. For both subtasks, the Clotho dataset was used. The models were evaluated on BLEU1, BLEU2, BLEU3, ROUGEL, METEOR, CIDEr, SPICE, and SPIDEr scores for audio captioning and R1, R5, R10 and mARP10 scores for audio retrieval. We have conducted a handful of experiments that modify the baseline models for these tasks. Our final architectu

**Method-oriented passage (PDF p. 2)**

Among works that build an audio-captioning model from the ground up, key variations include choice of architecture for the encoder and decoder, various feature extraction techniques, using overlapping versus non-overlapping time segments and the use of regularization. The approach of Wu et al. [2020] during the 2020 DCASE Challenge involved the use of a 10-layer CNN encoder with a Transformer as the decoder. Xu et al. [2021b] modiﬁed this architecture and used a single-layer GRU with temporal attention in place of the Transformer. More recent studies (Mei et al. [2021], Labbé and Pellegrini [2021]) have attempted to use a fully recurrent enco

**Results-oriented passage (PDF p. 5)**

The baseline model was trained using the Adam optimizer and a ReduceLROnPlateau schedulder for 50 epochs. Performance was measured in terms of recall at R1, R5, R10 and mAP10 (mean average precision). For the developement-evaluation split in Clotho dataset (4), the results of our baseline model can be seen in Table 3. As can be seen, our baseline results were lower than what the original reference (*Add reference) listed. This could be due to various reasons: (1) the model was not trained long enough; (2) the hyperparameters used were not the best; (3) more regularization was needed to reduce overﬁtting; and so on. Nonetheless, we used the me

**Caveat-oriented passage (PDF p. 2)**

The task of Audio Retrieval has received limited attention in literature. As such, only a handful of papers on this topic have been published. One such work is the study by Koepke et al. [2022] which proposed two new benchmarks for text-based audio retrieval on the AudioCaps and Clotho datasets. These benchmarks were used to build baselines, and th

## 72. LLM.int8(): 8-bit Matrix Multiplication for Transformers at Scale

ID: `2208.07339` | Theme: Efficiency/adaptation | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2208.07339

Snapshot SHA-256: `40da3ce2d38eb3baa8b638cab093bd048178205c1eb4d0671e79c108f72906bf`

Abstract extract: Large language models have been widely adopted but require significant GPU memory for inference. We develop a procedure for Int8 matrix multiplication for feed-forward and attention projection layers in transformers, which cut the memory needed for inference by half while retaining full precision performance. With our method, a 175B parameter 16/32-bit checkpoint can be loaded, converted to Int8, and used immediately without performance degradation. This is made possible by understanding and working around properties of highly systematic emergent features in transformer language models that dominate attention and transformer predictive performance. To cope with these features, we develop a t

**Method-oriented passage (PDF p. 5)**

We ﬁnd that given input matrix Xf16 ∈Rs×h, these outliers occur systematically for almost all sequence dimensions s but are limited to speciﬁc feature/hidden dimensions h. As such, we propose mixed-precision decomposition for matrix multiplication where we separate outlier feature dimensions into the set O = {i|i ∈Z, 0 ≤i ≤h}, which contains all dimensions of h which have at least one outlier with a magnitude larger than the threshold α. In our work, we ﬁnd that α = 6.0 is sufﬁcient to reduce transformer performance degradation close to zero. Using Einstein notation where all indices are superscripts, given the weight matrix Wf16 ∈Rh×o, mixed

**Results-oriented passage (PDF p. 5)**

The main language modeling perplexity results on the 125M to 13B Int8 models evaluated on the C4 corpus can be seen in Table 1. We see that absmax, row-wise, and zeropoint quantization fail as we scale, where models after 2.7B parameters perform worse than smaller models. Zeropoint quantization fails instead beyond 6.7B parameters. Our method, LLM.int8(), is the only method that preserves perplexity. As such, LLM.int8() is the only method with a favorable scaling trend.

**Caveat-oriented passage (PDF p. 10)**

The main limitation of our work is that our analysis is solely on the Int8 data type, and we do not study 8-bit ﬂoating-point (FP8) data types. Since current GPUs and TPUs do not support this data type, we believe this is best left for future work. However, we also believe many insights from Int8 data types will directly translate to FP8 data types

## 73. IndicSUPERB: A Speech Processing Universal Performance Benchmark for Indian languages

ID: `2208.11761` | Theme: Evaluation/reliability | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2208.11761

Snapshot SHA-256: `5b24c33a9a3522ca69d6ba424142acaf5afefe815100207ab1ac1536af909880`

Abstract extract: A cornerstone in AI research has been the creation and adoption of standardized training and test datasets to earmark the progress of state-of-the-art models. A particularly successful example is the GLUE dataset for training and evaluating Natural Language Understanding (NLU) models for English. The large body of research around self-supervised BERT-based language models revolved around performance improvements on NLU tasks in GLUE. To evaluate language models in other languages, several language-specific GLUE datasets were created. The area of speech language understanding (SLU) has followed a similar trajectory. The success of large self-supervised models such as wav2vec2 enable creation 

**Method-oriented passage (PDF p. 2)**

languages covering 6 speech tasks: Automatic Speech Recognition, Speaker Veriﬁcation, Speaker Identiﬁcation (mono/multi), Language Identiﬁca- tion, Query By Example, and Keyword Spotting. In this work, our ﬁrst main contribution is to build a large dataset for automatic speech recogni- tion containing read speech across 12 Indian lan- guages from 1,218 speakers spanning 203 districts (see Figure 1). This is a one of its kind open source effort resulting in a very large dataset con- taining 1,684 hours of labelled speech recognition data. The data was collected with the help of paid speakers using a maker-checker ﬂow. Every spo- ken utterance 

**Results-oriented passage (PDF p. 9)**

The results of our experiments are summarised in Tables 6 to 11. Based on these results, we try to answer the following questions: Does Kathbath help in improving ASR for Indian languages? To assess the usefulness of Kathbath, we compare the performance of two IndicWav2Vec models. The ﬁrst model is trained on all existing data from publicly avail- able benchmarks, i.e., MUCS(Diwan et al., 2021), MSR(Srivastava et al., 2018) and a subset of OpenSLR(Kjartansson et al., 2018b) obtained from the authors of Shetty and Umesh (2021). The training data contained 40 hours each for Gujarati, Tamil and Telugu and 95 hours each for Hindi, Marathi and Odi

**Caveat-oriented passage (PDF p. 3)**

2https://github.com/AI4Bharat/indicSUPERB 3https://sites.google.com/view/gramvaaniasrchallenge/dataset 4https://www.openslr.org/122/ 5https://commonvoice.mozilla.org/en/datasets 6https://sites.google.com/view/indian-language- asrchallenge/home 7https://asr.iiit.ac.in/cstd/ 8https://blog.smc.org.in/malayalam-speech-corpus/

## 74. AudioLM: a Language Modeling Approach to Audio Generation

ID: `2209.03143` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2209.03143

Snapshot SHA-256: `16c8389ed725758ec76091137e98acdcab479ce84a40a11db5a82ccb65b054a2`

Abstract extract: We introduce AudioLM, a framework for high-quality audio generation with long-term consistency. AudioLM maps the input audio to a sequence of discrete tokens and casts audio generation as a language modeling task in this representation space. We show how existing audio tokenizers provide different trade-offs between reconstruction quality and long-term structure, and we propose a hybrid tokenization scheme to achieve both objectives. Namely, we leverage the discretized activations of a masked language model pre-trained on audio to capture long-term structure and the discrete codes produced by a neural audio codec to achieve high-quality synthesis. By training on large corpora of raw audio wa

**Method-oriented passage (PDF p. 5)**

• Piano continuation, where the model is expected to generate piano music, which is coherent with the prompt in terms of melody, harmony and rhythm. As the speech and piano prompts we use for evaluation are respectively from unseen speakers and unseen performances, generating consistent continuations requires AudioLM to generalize beyond training data. We furthermore conduct experiments that provide empirical support for our hierarchical approach and shed light on the properties of the semantic and acoustic tokens. In order to mitigate the potential misuse of our framework, we provide an effective method for detecting speech generated by Audi

**Results-oriented passage (PDF p. 7)**

In the second experiment, we verify the hypothesis that speaker identity and recording conditions are captured by the acoustic tokens. Qualitatively, one can listen to the samples produced by the previous experiment and observe that repeating the sampling of acoustic tokens conditioned on the same semantic tokens results in a wide variety of speakers and recording conditions. In order to perform a quantitative assessment of this obser- vation, we design the following experiment. We train a con- volutional network for speaker classification inspired by [58], which operates on the log-mel spectrogram of the inputs (25 ms window length, 10 ms ho

**Caveat-oriented passage (PDF p. 2)**

as the fact that they require exploiting long-term dependencies, allow learning representations that encode coarse, high-level information about the signal (e.g., phonemes and word identity when trained on speech [34]). These representations are thus particularly useful for discriminative downstream tasks such as speech recognition [33] or audio cl

## 75. AudioGen: Textually Guided Audio Generation

ID: `2209.15352` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2209.15352

Snapshot SHA-256: `42ea065e3ac2c08fc2916a908da51e9e8ccd34673d33cd0e7604f80b3e7dfc4b`

Abstract extract: We tackle the problem of generating audio samples conditioned on descriptive text captions. In this work, we propose AaudioGen, an auto-regressive generative model that generates audio samples conditioned on text inputs. AudioGen operates on a learnt discrete audio representation. The task of text-to-audio generation poses multiple challenges. Due to the way audio travels through a medium, differentiating ``objects'' can be a difficult task (e.g., separating multiple people simultaneously speaking). This is further complicated by real-world recording conditions (e.g., background noise, reverberation, etc.). Scarce text annotations impose another constraint, limiting the ability to scale mode

**Method-oriented passage (PDF p. 2)**

We propose AUDIOGEN, an autoregressive textually guided audio generation model. AUDIO- GEN consists of two main stages. The ﬁrst encodes raw audio to a discrete sequence of tokens using a neural audio compression model (e.g. Zeghidour et al. (2021)). This model is trained in an end-to-end fashion to reconstruct the input audio from the compressed representation, with an addition of a perceptual loss in the form of a set of discriminators. Such an audio representation is designed to generate high-ﬁdelity audio samples while still being compact. The second stage, leverages an autoregressive Transformer-decoder language-model that operates on th

**Results-oriented passage (PDF p. 2)**

Our contributions: (i) We propose a state-of-the-art auto-regressive audio generation model condi- tioned on textual descriptions or audio prompts, as evaluated with objective and subjective (human listeners) scores. Speciﬁcally we propose two model variations, one with 285M parameters and another one with 1B parameters; (ii) We improve text-to-audio generation in two axes. We im- prove text adherence by applying classiﬁer free guidance on top of the audio language model. We improve compositionality by performing on the ﬂy text and audio mixing; (iii) We show that the proposed approach can be extended to audio continuation conditioned on text

**Caveat-oriented passage (PDF p. 9)**

As we operate on audio tokens using relatively small down-sampling factor, the audio tokens se- quences can be extremely long. This impose two main limitations: (i) modeling long range se- quences; (ii) high inference time. In this work, we propose one possible relaxation to the ﬁrst limitation, however such an approach comes at the cost of produci

## 76. High Fidelity Neural Audio Compression

ID: `2210.13438` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2210.13438

Snapshot SHA-256: `f307ade111fdaad081ac8092f4ab7543b9c925192159de5a1816dcf26a5129f7`

Abstract extract: We introduce a state-of-the-art real-time, high-fidelity, audio codec leveraging neural networks. It consists in a streaming encoder-decoder architecture with quantized latent space trained in an end-to-end fashion. We simplify and speed-up the training by using a single multiscale spectrogram adversary that efficiently reduces artifacts and produce high-quality samples. We introduce a novel loss balancer mechanism to stabilize training: the weight of a loss now defines the fraction of the overall gradient it should represent, thus decoupling the choice of this hyper-parameter from the typical scale of the loss. Finally, we study how lightweight Transformer models can be used to further comp

**Method-oriented passage (PDF p. 3)**

Neural based audio codecs have been recently proposed and demonstrated promising results (Kleijn et al., 2018; Valin & Skoglund, 2019b; Lim et al., 2020; Kleijn et al., 2021; Zeghidour et al., 2021; Omran et al., 2022; Lin et al., 2022; Jayashankar et al., 2022; Li et al.; Jiang et al., 2022), where most methods are based on quantizing the latent space before feeding it to the decoder. In Valin & Skoglund (2019b), an LPCNet (Valin & Skoglund, 2019a) vocoder was conditioned on hand-crafted features and a uniform quantizer. Gârbacea et al. (2019) conditioned a WaveNet based model on discrete units obtained from a VQ-VAE (Van Den Oord et al., 20

**Results-oriented passage (PDF p. 8)**

We start with the results for EnCodec with a bandwidth in {1.5, 3, 6, 12} kbps and compare them to the baselines. Results for the streamable setup are reported in Figure 3 and a breakdown per category in Table 1. We additionally explored other quantizers such as Gumbel-Softmax and DiﬀQ (see details in Appendix A.2), however, we found in preliminary results that they provide similar or worse results, hence we do not report them.

**Caveat-oriented passage (PDF p. 2)**

Audio Codec. Low bitrate parametric speech and audio codecs have long been studied (Atal & Hanauer, 1971; Juang & Gray, 1982), but their quality has been severely limited. Despite some advances (Griﬃn & Lim, 1985; McCree et al., 1996), modeling the excitation signal has remained a challenging task. The current state-of-the-art traditional audio cod

## 77. GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers

ID: `2210.17323` | Theme: Efficiency/adaptation | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2210.17323

Snapshot SHA-256: `35e339171cd48bbf8dda246bd018b11aa33a5cda0c4a1587cdae574208f56396`

Abstract extract: Generative Pre-trained Transformer models, known as GPT or OPT, set themselves apart through breakthrough performance across complex language modelling tasks, but also by their extremely high computational and storage costs. Specifically, due to their massive size, even inference for large, highly-accurate GPT models may require multiple performant GPUs, which limits the usability of such models. While there is emerging work on relieving this pressure via model compression, the applicability and performance of existing compression techniques is limited by the scale and complexity of GPT models. In this paper, we address this challenge, and propose GPTQ, a new one-shot weight quantization met

**Method-oriented passage (PDF p. 2)**

2022). To date, only basic variants of round-to-nearest quantization (Yao et al., 2022; Dettmers et al., 2022) have been applied at the scale of GPT-175B; while this works well for low compression targets, e.g., 8-bit weights, they fail to preserve accuracy at higher rates. It therefore remains open whether one-shot post-training quantization to higher compression rates is generally-feasible.

**Results-oriented passage (PDF p. 6)**

Quantizing Small Models. As a ﬁrst ablation study, we compare GPTQ’s performance relative to state-of-the-art post-training quantization (PTQ) methods, on ResNet18 and ResNet50, which are standard PTQ benchmarks, in the same setup as (Frantar et al., 2022). As can be seen in Table 1, GPTQ performs on par at 4-bit, and slightly worse than the most accurate methods at 3-bit. At the same time, it signiﬁcantly outperforms AdaQuant, the fastest amongst prior PTQ methods. Further, we compare against the full greedy OBQ method on two smaller language models: BERT-base (De- vlin et al., 2019) and OPT-125M. The results are shown in Appendix Table 8. A

**Caveat-oriented passage (PDF p. 2)**

We hope that our work will stimulate further research in this area, and can be a further step towards making these models available to a wider audience. In terms of limitations, our method currently does not provide speedups for the actual multiplications, due to the lack of hardware support for mixed-precision operands (e.g. FP16 x INT4) on mainst

## 78. Active Learning of Non-semantic Speech Tasks with Pretrained Models

ID: `2211.00119` | Theme: Loop/data selection | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2211.00119

Snapshot SHA-256: `361533aa2397fcea0a1003dc48dacaca4af546e8f37bca7463f383bbc60d2b73`

Abstract extract: Pretraining neural networks with massive unlabeled datasets has become popular as it equips the deep models with a better prior to solve downstream tasks. However, this approach generally assumes that the downstream tasks have access to annotated data of sufficient size. In this work, we propose ALOE, a novel system for improving the data- and label-efficiency of non-semantic speech tasks with active learning. ALOE uses pretrained models in conjunction with active learning to label data incrementally and learn classifiers for downstream tasks, thereby mitigating the need to acquire labeled data beforehand. We demonstrate the effectiveness of ALOE on a wide range of tasks, uncertainty-based a

**Method-oriented passage (PDF p. 2)**

5, 6], to the best of our knowledge, ALOE is a ﬁrst attempt at improving label efﬁciency for non-semantic speech tasks with AL and pretrained models. In principle, AL provides a system- atic way to procure labels for the most informative instances, e.g., a class for which a model is highly uncertain [7, 8]. AL framework comprises three stages: a) acquisition—selecting relevant examples, b) annotation—getting ground-truth labels from a human annotator; and c) retraining—learning model on acquired and existing labeled instances. In practice, these steps are time-consuming and computationally expensive because a model has to be trained many time

**Results-oriented passage (PDF p. 3)**

Table 1: Comparison of test set accuracy (%) of our approach with other baselines on different end-tasks. ALOE achieves similar recognition rate with class-aware sampling, while using several folds less labeled examples. The baseline results are from [11], where available; else we train a linear classiﬁer on time-averaged representations using published models.

**Caveat-oriented passage (PDF p. 4)**

ALOE’s core strength is in its simplicity. Indeed, adding more layers or complexity to Gω may improve the classiﬁca- tion accuracy, but we wanted to show that even with a linear (i.e. single layer) model, optimal performance can be achieved. Also, it is standard protocol in self-supervised learning to eval- uate pretrained models with linear probes

## 79. Large-scale Contrastive Language-Audio Pretraining with Feature Fusion and Keyword-to-Caption Augmentation

ID: `2211.06687` | Theme: Captioning/grounding | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2211.06687

Snapshot SHA-256: `c223105503d6f5c173479b84bcc6648c0df9f12a8493492617616c75049e7d31`

Abstract extract: Contrastive learning has shown remarkable success in the field of multimodal representation learning. In this paper, we propose a pipeline of contrastive language-audio pretraining to develop an audio representation by combining audio data with natural language descriptions. To accomplish this target, we first release LAION-Audio-630K, a large collection of 633,526 audio-text pairs from different data sources. Second, we construct a contrastive language-audio pretraining model by considering different audio encoders and text encoders. We incorporate the feature fusion mechanism and keyword-to-caption augmentation into the model design to further enable the model to process audio inputs of va

**Method-oriented passage (PDF p. 5)**

In this paper, we propose a large-scale audio-text dataset and im- provements on current language-audio contrastive learning paradigm. We show that LAION-Audio-630, AudioSet with keyword-to- caption augmentation, and feature fusion effectively leads to better audio understanding, task performance, and enables effective learn- ings on variable-length data. Future works include collecting even larger dataset on training, applying representations into more down- stream tasks such as audio synthesis and separation.

**Results-oriented passage (PDF p. 4)**

Audio and Text Encoders We first conduct experiments to choose the best audio encoder and text encoder for the text-to-audio retrieval task. We combine two audio encoders with three text encoders in section 3.3 where both are loaded from pretrained checkpoints as the same to [5,7,8]. In this experiment, we only train on AudioCaps and Clotho datasets (∼55K data), and report the best mAP@10 on audio-to-text (A→T) and text-to-audio (T→A) perspectives. According to the results in Table 2, for audio encoder, HTSAT performs better than PANN combined with the RoBERTa or BERT text encoder. For the text encoder, RoBERTa achieves better per- formance t

**Caveat-oriented passage (PDF p. 3)**

Unlike RGB image data that can be resized to a unified resolution, audio has a nature of variable length. Conventionally, one would input the full audio into the audio encoder and take the average of per-frame or per-chunk audio embeddings as output (i.e., slice & vote). However, the conventional method is computationally ineffi- cient on long audi

## 80. Impact of visual assistance for automated audio captioning

ID: `2211.10539` | Theme: Captioning/grounding | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2211.10539

Snapshot SHA-256: `ee01f4405419cb3b8f3cc9c75c75ce3766429bb8b01d8abccef5adb657ad7070`

Abstract extract: We study the impact of visual assistance for automated audio captioning. Utilizing multi-encoder transformer architectures, which have previously been employed to introduce vision-related information in the context of sound event detection, we analyze the usefulness of incorporating a variety of pretrained features. We perform experiments on a YouTube-based audiovisual data set and investigate the effect of applying the considered transfer learning technique in terms of a variety of captioning metrics. We find that only one of the considered kinds of pretrained features provides consistent improvements, while the others do not provide any noteworthy gains at all. Interestingly, the outcomes 

**Method-oriented passage (PDF p. 2)**

the merit of vision-related information in the context of automated audio captioning, and not necessarily to achieve hyperoptimized per- formance. Hence, the encoder structure is kept relatively simple: It consists of a single feedforward layer with ReLU activation mapping the embeddings to 128-dimensional vectors. This choice is further justiﬁed by the fact that all of the considered features are already quite informative as they are all extracted from pretrained models. The component combining the outputs of the two encoders and utilizing them to generate captions of the provided clips is the multi- encoder transformer decoder [15, 16]. It 

**Results-oriented passage (PDF p. 3)**

In this section, we analyze the automated audio captioning scores listed in Section 3 obtained by the considered multi-encoder trans- formers using different types of auditory and visual features, as dis- cussed in Section 2. We report metrics which are averaged over 20 training runs with independent model parameter initialization in- stances to improve the reliability of the results. Table 1 contains the scores and associated standard deviations of the models incorporating different pretrained features. As mentioned in Section 2, the ﬁrst encoder always takes in auditory embeddings, while the other inputs are variable. The interpolation weig

**Caveat-oriented passage (PDF p. 3)**

As mentioned before, the goal of this project is to analyze the merit of including visual information in the context of automated audio captioning, and not to obtain ideal performance. Therefore, we only utilize a limited amount of data augmentation to prevent overﬁtting of models. More speciﬁcally, we solely employ SpecAugment [27]: Time and frequ

## 81. PromptTTS: Controllable Text-to-Speech with Text Descriptions

ID: `2211.12171` | Theme: Speech/audio generation and control | Status: `selected_fulltext_review_plus_scoped_core_crosscheck`

Source: https://arxiv.org/pdf/2211.12171

Snapshot SHA-256: `bcd921fc5d20ccc4ce5294987bce2869d80b3646fdfa0a990e23a3e340dac1bc`

Abstract extract: Using a text description as prompt to guide the generation of text or images (e.g., GPT-3 or DALLE-2) has drawn wide attention recently. Beyond text and image generation, in this work, we explore the possibility of utilizing text descriptions to guide speech synthesis. Thus, we develop a text-to-speech (TTS) system (dubbed as PromptTTS) that takes a prompt with both style and content descriptions as input to synthesize the corresponding speech. Specifically, PromptTTS consists of a style encoder and a content encoder to extract the corresponding representations from the prompt, and a speech decoder to synthesize speech according to the extracted style and content representations. Compared wi

**Method-oriented passage (PDF p. 2)**

As shown in Fig. 1, PromptTTS consists of a style encoder, a content encoder, and a speech decoder. The style encoder maps a style prompt to a semantic space to extract the style representation, which is used to guide the content encoder and the speech decoder. The content encoder takes a content prompt as input to extract the content representation. And the speech decoder concatenates the style representation and the content representation as input to produce the speech that is consistent with both style and content prompts. We introduce the above modules as follows.

**Results-oriented passage (PDF p. 3)**

Table 4 shows the accuracy of PromptTTS and the two-stage baseline system on 5 style factors. We have the following ob- servations: (1) PromptTTS outperforms the two-stage base- line system on all style factors on PromptSpeech since it could alleviate the cascaded error of the two-stage system, which is discussed in detail in 4.4.3; (2) PromptTTS achieves the av- erage accuracy of 90.31% on PromptSpeech, outperforming

**Caveat-oriented passage (PDF p. 4)**

To analyze the advantages of PromptTTS over the two-stage baseline system, we show the average accuracy of the two- stage baseline system at each stage in Table 6. Note that stage one corresponds to the explicit classiﬁcation on style fac- tors and stage two corresponds to the speech synthesis given ground-truth style factors. From the table, we ca

Additional interpretation and limitations: [core findings](CORE_FINDINGS.md).

## 82. Robust Speech Recognition via Large-Scale Weak Supervision

ID: `2212.04356` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2212.04356

Snapshot SHA-256: `6337bde031b2f237547a977b022f831169a7e05b4d9047f29501166d83594566`

Abstract extract: We study the capabilities of speech processing systems trained simply to predict large amounts of transcripts of audio on the internet. When scaled to 680,000 hours of multilingual and multitask supervision, the resulting models generalize well to standard benchmarks and are often competitive with prior fully supervised results but in a zero-shot transfer setting without the need for any fine-tuning. When compared to humans, the models approach their accuracy and robustness. We are releasing models and inference code to serve as a foundation for further work on robust speech processing.

**Method-oriented passage (PDF p. 2)**

Yet these new datasets are only a few times larger than the sum of existing high-quality datasets and still much smaller than prior unsupervised work. In this work we close that gap, scaling weakly supervised speech recognition the next order of magnitude to 680,000 hours of labeled audio data. We call our approach Whisper2. We demonstrate models trained at this scale transfer well to existing datasets zero- shot, removing the need for any dataset-speciﬁc ﬁne-tuning to achieve high-quality results.

**Results-oriented passage (PDF p. 6)**

the smallest zero-shot Whisper model, which has only 39 million parameters and a 6.7 WER on LibriSpeech test-clean is roughly competitive with the best supervised LibriSpeech model when evaluated on other datasets. When compared to a human in Figure 2, the best zero-shot Whisper models roughly match their accuracy and robustness. For a detailed breakdown of this large improvement in robustness, Table 2 compares the performance of the best zero-shot Whisper model with a supervised LibriSpeech model that has the closest performance to it on LibriSpeech test-clean. Despite their very close performance on the reference distribution, the zero-shot

**Caveat-oriented passage (PDF p. 2)**

Many transcripts on the internet are not actually human- generated but the output of existing ASR systems. Recent research has shown that training on datasets of mixed human and machine-generated data can signiﬁcantly impair the per- formance of translation systems (Ghorbani et al., 2021). In order to avoid learning “transcript-ese”, we developed m

## 83. BEATs: Audio Pre-Training with Acoustic Tokenizers

ID: `2212.09058` | Theme: Representations/codecs | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2212.09058

Snapshot SHA-256: `ca16a4100e27272cb220cf74b81b5ad30179d3a2a7cbd101157ea17ee1bc2bfc`

Abstract extract: The massive growth of self-supervised learning (SSL) has been witnessed in language, vision, speech, and audio domains over the past few years. While discrete label prediction is widely adopted for other modalities, the state-of-the-art audio SSL models still employ reconstruction loss for pre-training. Compared with reconstruction loss, semantic-rich discrete label prediction encourages the SSL model to abstract the high-level audio semantics and discard the redundant details as in human perception. However, a semantic-rich acoustic tokenizer for general audio pre-training is usually not straightforward to obtain, due to the continuous property of audio and unavailable phoneme sequences lik

**Method-oriented passage (PDF p. 2)**

To tackle these challenges, in this work we propose BEATS, short for Bidirectional Encoder representation from Audio Transformers, in which an acoustic tokenizer and an audio SSL model are optimized through an itera- tive audio pre-training framework. The training pipeline is illustrated in Figure 1. In each iteration, we ﬁrst use the acoustic tokenizer to generate the discrete labels of the unlabeled audio, and use them to optimize the audio SSL model with a mask and discrete label prediction loss. After convergence, the audio SSL model acts as a teacher to guide the acoustic tokenizer to learn audio semantics with knowledge distillation [Hi

**Results-oriented passage (PDF p. 9)**

Table 1: Comparing with the SOTA single models on audio and speech classiﬁcation tasks. IN, AS, and LS denote the ImageNet, AudioSet, and LibriSpeech datasets, respectively. TA and TI denote the 128K text-audio pairs and 400M text-image pairs for CLAP and CLIP pre-training, respectively. The evaluation metrics are mAP for AS-2M/AS-20K and accuracy for ESC-50/KS1/KS2/ER. We compared the best single models from each previous work. We gray-out the models and results with additional supervised training on the external datasets. ∗The results reported following the SUPERB policy [wen Yang et al., 2021], where pre-trained models are kept frozen duri

**Caveat-oriented passage (PDF p. 2)**

pre-training task as in SSL models of speech [Hsu et al., 2021, Chen et al., 2022b], vision [Bao et al., 2021, Peng et al., 2022, Wang et al., 2022b] and language [Devlin et al., 2019, Liu et al., 2019, Lan et al., 2019]. However, it was generally believed that the reconstruction loss only accounts for the correctness of low-level time-frequency fe

## 84. Skit-S2I: An Indian Accented Speech to Intent dataset

ID: `2212.13015` | Theme: Data/Indic speech | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2212.13015

Snapshot SHA-256: `d55624ffe4b9e86fb9da18ac9b059c43ce41014aa0d474e94ab59230d4e68488`

Abstract extract: Conventional conversation assistants extract text transcripts from the speech signal using automatic speech recognition (ASR) and then predict intent from the transcriptions. Using end-to-end spoken language understanding (SLU), the intents of the speaker are predicted directly from the speech signal without requiring intermediate text transcripts. As a result, the model can optimize directly for intent classification and avoid cascading errors from ASR. The end-to-end SLU system also helps in reducing the latency of the intent prediction model. Although many datasets are available publicly for text-to-intent tasks, the availability of labeled speech-to-intent datasets is limited, and there 

**Method-oriented passage (PDF p. 2)**

Table 3 shows the cascaded pipeline and end-to-end SLU base- line results. The XLMR NLU model trained on different ASR transcripts gives different test accuracy and F1 scores, as the er- ror in the ASR-predicted transcripts can affect the performance of the NLU model, and these models are not optimized together for intent classiﬁcation. The Hubert-based end-to-end SLU model performed better than the wav2vec2 model, and both the whisper models outper- formed Hubert and wav2vec models. In the pipeline and end- to-end SLU baselines, the whisper model outperforms the other baselines, as the whisper model is more robust and performs better in zero

**Results-oriented passage (PDF p. 2)**

A total of 11 speakers contributed to the dataset, including eight females and three males. The speakers are all native Indians with different native languages from different parts of the coun- try. There are 11845 samples in the dataset, and they are divided into train and test sets. The train set contains 10445 samples for training the model, while the test set contains 1400 samples for evaluation. Table 1 gives the data split of the Skit-S2I dataset. The train and test split have around 650 and 100 samples per in- tent, respectively, and each intent has data from all the speakers. The speakers are stratiﬁed across the train and test set in

**Caveat-oriented passage (PDF p. 1)**

Earlier intent classiﬁcation pipeline systems transcribe the speech signal with an ASR model and then train a Natual Lan- guage Understanding(NLU) model to predict the intents using the text transcripts. These pipeline methods are prone to er- ror propagation due to ASR transcript errors. The text-to-intent NLU models only make use of the semantic 

## 85. Neural Codec Language Models are Zero-Shot Text to Speech Synthesizers

ID: `2301.02111` | Theme: Representations/codecs | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2301.02111

Snapshot SHA-256: `3f4d4ddbb4cfb1682aa38a23ec9134eaccbda498e38af0013a69a8d7e8207fa1`

Abstract extract: We introduce a language modeling approach for text to speech synthesis (TTS). Specifically, we train a neural codec language model (called Vall-E) using discrete codes derived from an off-the-shelf neural audio codec model, and regard TTS as a conditional language modeling task rather than continuous signal regression as in previous work. During the pre-training stage, we scale up the TTS training data to 60K hours of English speech which is hundreds of times larger than existing systems. Vall-E emerges in-context learning capabilities and can be used to synthesize high-quality personalized speech with only a 3-second enrolled recording of an unseen speaker as an acoustic prompt. Experiment 

**Method-oriented passage (PDF p. 2)**

Instead of designing a complex and speciﬁc network for this problem, the ultimate solution is to train a model with large and diverse data as much as possible, motivated by success in the ﬁeld of text synthesis [Brown et al., 2020, Chowdhery et al., 2022]. Recent years have witnessed notable performance improvement for data increase in the text language model, from 16GB of uncompressed text [Devlin et al., 2019], to 160GB [Liu et al., 2019], to 570GB [Brown et al., 2020], and ﬁnally, around 1TB [Chowdhery et al., 2022]. Transferring this success to the ﬁeld of speech synthesis, we introduce VALL-E, the ﬁrst language model based TTS framework 

**Results-oriented passage (PDF p. 8)**

Table 2 shows the objective evaluation results. We ﬁrst compute the WER score and the speaker similarity score of the ground truth speech as the upper bound. To compare the speaker similarity, we use speech pairs from the same speaker in the test set. Compared with the YourTTS baseline, our

**Caveat-oriented passage (PDF p. 4)**

Since audio is typically stored as a sequence of 16-bit integer values, a generative model is required to output 216 = 65, 536 probabilities per timestep to synthesize the raw audio. In addition, the audio sample rate exceeding ten thousand leads to an extraordinarily long sequence length, making it more intractable for raw audio synthesis. To this

## 86. MusicLM: Generating Music From Text

ID: `2301.11325` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2301.11325

Snapshot SHA-256: `eed4bb48c6da86c176b157d0588ae9a2b3cced8d6fd7d267b3ecb35c9f5a2008`

Abstract extract: We introduce MusicLM, a model generating high-fidelity music from text descriptions such as "a calming violin melody backed by a distorted guitar riff". MusicLM casts the process of conditional music generation as a hierarchical sequence-to-sequence modeling task, and it generates music at 24 kHz that remains consistent over several minutes. Our experiments show that MusicLM outperforms previous systems both in audio quality and adherence to the text description. Moreover, we demonstrate that MusicLM can be conditioned on both text and a melody in that it can transform whistled and hummed melodies according to the style described in a text caption. To support future research, we publicly rel

**Method-oriented passage (PDF p. 2)**

When trained on a large dataset of unlabeled music, MusicLM learns to generate long and coherent music at 24 kHz, for text descriptions of signiﬁcant complexity, such as “enchanting jazz song with a memorable saxophone solo and a solo singer” or “Berlin 90s techno with a low bass and strong kick”. To address the lack of evaluation data for this task, we introduce MusicCaps, a new high-quality music caption dataset with 5.5k examples prepared by expert musi- cians, which we publicly release to support future research.

**Results-oriented passage (PDF p. 7)**

Table 1. Evaluation of generated samples using captions from the MusicCaps dataset. Models are compared in terms of audio quality, by means of Fr´echet Audio Distance (FAD), and faithfulness to the text description, using Kullback–Leibler Divergence (KLD) and MuLan Cycle Consistency (MCC), and counts of wins in pairwise human listening tests (Wins).

**Caveat-oriented passage (PDF p. 2)**

Despite the challenge of generating high-quality audio with long-term consistency, a series of approaches have recently tackled the problem with some success. Jukebox (Dhari- wal et al., 2020), for example, proposes a hierarchy of VQ- VAEs at various time resolutions to achieve high temporal

## 87. AudioLDM: Text-to-Audio Generation with Latent Diffusion Models

ID: `2301.12503` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2301.12503

Snapshot SHA-256: `3021560ca71a1100df38d7da4e4db5b8ff72e063e25e6dbf775013ab2020fb69`

Abstract extract: Text-to-audio (TTA) system has recently gained attention for its ability to synthesize general audio based on text descriptions. However, previous studies in TTA have limited generation quality with high computational costs. In this study, we propose AudioLDM, a TTA system that is built on a latent space to learn the continuous audio representations from contrastive language-audio pretraining (CLAP) latents. The pretrained CLAP models enable us to train LDMs with audio embedding while providing text embedding as a condition during sampling. By learning the latent representations of audio signals and their compositions without modeling the cross-modal relationship, AudioLDM is advantageous in

**Method-oriented passage (PDF p. 1)**

Text-to-audio (TTA) systems have recently gained attention for their ability to synthesize general au- dio based on text descriptions. However, previ- ous studies in TTA have limited generation qual- ity with high computational costs. In this study, we propose AudioLDM, a TTA system that is built on a latent space to learn continuous audio representations from contrastive language-audio pretraining (CLAP) embeddings. The pretrained CLAP models enable us to train LDMs with au- dio embeddings while providing text embeddings as the condition during sampling. By learning the latent representations of audio signals with- out modelling the cross-mo

**Results-oriented passage (PDF p. 6)**

Table 1. The comparison between AudioLDM and baseline TTA generation models. Evaluation is conducted on AudioCaps test set. The symbol † marks industry-level computation. DiffSound is trained on 32 V100 GPUs and AudioGen is trained on 64 A100 GPUs, while AudioLDM models are trained on a single GPU, RTX 3090 or A100. The AS and AC stand for AudioSet and AudioCaps datasets respectively. The results of AudioGen are employed from (Kreuk et al., 2022) since their implementation has been not publicly available.

**Caveat-oriented passage (PDF p. 1)**

For previous TTA works, a potential limitation for genera- tion quality is the requirement of large-scale high-quality audio-text data pairs, which are usually not readily avail- able, and where they are available, are of limited quality and quantity (Liu et al., 2022f). To better utilize the low-quality data, several methods for text preprocessing

## 88. Speak, Read and Prompt: High-Fidelity Text-to-Speech with Minimal Supervision

ID: `2302.03540` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2302.03540

Snapshot SHA-256: `afae678cd1c4ec6c47487e2bdfa72ef207f5d4e8069bf6b8117b759f675cd56d`

Abstract extract: We introduce SPEAR-TTS, a multi-speaker text-to-speech (TTS) system that can be trained with minimal supervision. By combining two types of discrete speech representations, we cast TTS as a composition of two sequence-to-sequence tasks: from text to high-level semantic tokens (akin to "reading") and from semantic tokens to low-level acoustic tokens ("speaking"). Decoupling these two tasks enables training of the "speaking" module using abundant audio-only data, and unlocks the highly efficient combination of pretraining and backtranslation to reduce the need for parallel data when training the "reading" component. To control the speaker identity, we adopt example prompting, which allows SPEA

**Method-oriented passage (PDF p. 12)**

In this work, we introduce SPEAR-TTS, a multi- speaker TTS system that has two features setting it apart. First, it only requires a minimal amount of parallel data to be trained, i.e. it can synthesize speech with high ﬁdelity and voice diversity when trained on as little as 15 minutes of parallel data coming from a single speaker. Second, SPEAR- TTS is able to synthesize speech maintaining voice characteristics of a previously unseen speaker using a 3-second long voice example. These capabilities originate from harnessing abundant audio-only data. The key component that unlocks the usage of such data is the hierarchical discrete representati

**Results-oriented passage (PDF p. 9)**

SPEAR-TTS is able to control the speaker voice via example prompting, as described in Section 8.3. We evaluate SPEAR-TTS in a zero-shot scenario, in which the voice used for prompting was never seen by S1 or S2 at training and S2 has to repro- duce its characteristics from a single prompt ex- ample. Speciﬁcally, we ﬁx S1, using the model trained on 15-minutes of LJSpeech and we con- sider all 40 speakers from LibriSpeech test-clean as target speakers. For each speaker, we randomly select 5 speech prompts with duration of 3 seconds each and transcripts from the same dataset. For each speech prompt and text transcript, we repeat synthesis 5 tim

**Caveat-oriented passage (PDF p. 13)**

While our motivation is to enable high-quality, di- verse, and controllable TTS for low-resource lan- guages, we started our investigations with English, which allowed us to address the problem using a collection of well-studied datasets. Next, we rely on LibriLight (Kahn et al., 2020) as our audio-only dataset which provides a sufﬁ- ciently divers

## 89. Fast and small footprint Hybrid HMM-HiFiGAN based system for speech synthesis in Indian languages

ID: `2302.06227` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2302.06227

Snapshot SHA-256: `a42bb46ffce1aca8a1c8cb686b428813b1aa4900acaef41c67f6daa9f1feefc3`

Abstract extract: Hidden-Markov-model (HMM) based text-to-speech (HTS) offers flexibility in speaking styles along with fast training and synthesis while being computationally less intense. HTS performs well even in low-resource scenarios. The primary drawback is that the voice quality is poor compared to that of E2E systems. A hybrid approach combining HMM-based feature generation and neural-network-based HiFi-GAN vocoder to improve HTS synthesis quality is proposed. HTS is trained on high-resolution mel-spectrograms instead of conventional mel generalized coefficients (MGC), and the output mel-spectrogram corresponding to the input text is used in a HiFi-GAN vocoder trained on Indic languages, to produce na

**Method-oriented passage (PDF p. 2)**

from the proposed hybrid system using either the USS units or the E2E units. [14] and [15] combine traditional methods with neural-network-based architectures like Tacotron2. [15] represents phones as vectors output by Tacotron encoder and uses Euclidean distance between them to perform unit se- lection, while [14] synthesizes extra phone-level units in the E2E context depending on selection cost. [13] uses a hidden semi-Markov model (HSMM) for latent representation of alignments to reduce the exposure bias, i.e., the mismatch be- tween training (teacher-forcing) and inference (free-running). [16] is a recent work on conversational speech syn

**Results-oriented passage (PDF p. 3)**

4.3. Evaluation A degradation mean opinion scores (DMOS) test is conducted to evaluate the performance of the various systems. In the DMOS test, native speakers of the language listen to the syn- thesized audio and rate utterances on a scale of 1-5, with 1 be- ing poor and 5 being human-like. GT utterances are included for reference. The utterances are presented to the evaluators in random order. The ﬁnal score is reported after normaliza- tion with respect to the scores of the GT utterances. A pair- wise comparison test (PC test) was also conducted between the proposed hybrid system and the HEQ hybrid system. In this measure, the evaluators 

**Caveat-oriented passage (PDF p. 3)**

4.2. Experiments The conventional HTS+HEQ system (as described in [10] is considered the baseline system. A Fastspeech system with a HiFi-GAN vocoder is also trained for comparison in terms of speech quality. The Fastspeech model is trained using ESPnet toolkit [30]. The alignments are obtained from tacotron2[4] teacher model. We also evaluate the 

## 90. Do Prosody Transfer Models Transfer Prosody?

ID: `2303.04289` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2303.04289

Snapshot SHA-256: `97d7b17865fc32c9adb789e89d4bbd4d5dffa38d3e5c6801bfbabe127a9e91e0`

Abstract extract: Some recent models for Text-to-Speech synthesis aim to transfer the prosody of a reference utterance to the generated target synthetic speech. This is done by using a learned embedding of the reference utterance, which is used to condition speech generation. During training, the reference utterance is identical to the target utterance. Yet, during synthesis, these models are often used to transfer prosody from a reference that differs from the text or speaker being synthesized. To address this inconsistency, we propose to use a different, but prosodically-related, utterance during training too. We believe this should encourage the model to learn to transfer only those characteristics that th

**Method-oriented passage (PDF p. 1)**

Some recent models for Text-to-Speech synthesis aim to transfer the prosody of a reference utterance to the generated target synthetic speech. This is done by using a learned embedding of the refer- ence utterance, which is used to condition speech generation. Dur- ing training, the reference utterance is identical to the target utter- ance. Yet, during synthesis, these models are often used to transfer prosody from a reference that differs from the text or speaker being synthesized. To address this inconsistency, we propose to use a different, but prosodically-related, utterance during training too. We believe this should encourage the model

**Results-oriented passage (PDF p. 3)**

For consistency with the PT literature, perceived naturalness of all methods and ground truth utterances was evaluated with a Mean Opinion Score (MOS) test. We evaluated each model’s synthesis of 30 of the test sentences, equal amounts of same-text and different- text, resulting in 120 evaluations across the four models. We also evaluated 30 ground truth utterances, both raw and vocoded, using HiFi-GAN to gauge possible reduction in perceived naturalness re- sulting from vocoding. This results in 180 MOS screens in total.

**Caveat-oriented passage (PDF p. 2)**

There is a correlation between the verbal and prosodic components of speech but predicting this similarity is not straightforward. Differ- ent renditions of the same text are, however, likely to have a similar prosodic structure. Therefore we consider the case where the refer- ence utterance is of the same text as the target utterance but read by a

## 91. WavCaps: A ChatGPT-Assisted Weakly-Labelled Audio Captioning Dataset for Audio-Language Multimodal Research

ID: `2303.17395` | Theme: Data/Indic speech | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2303.17395

Snapshot SHA-256: `1935de5dbecce6e387460d5153500643ce4a10eba7971d0c60c1b411bd184725`

Abstract extract: The advancement of audio-language (AL) multimodal learning tasks has been significant in recent years. However, researchers face challenges due to the costly and time-consuming collection process of existing audio-language datasets, which are limited in size. To address this data scarcity issue, we introduce WavCaps, the first large-scale weakly-labelled audio captioning dataset, comprising approximately 400k audio clips with paired captions. We sourced audio clips and their raw descriptions from web sources and a sound event detection dataset. However, the online-harvested raw descriptions are highly noisy and unsuitable for direct use in tasks such as automated audio captioning. To overcom

**Method-oriented passage (PDF p. 2)**

platforms—FreeSound1, BBC Sound Effects2, and Sound- Bible3—as well as from an audio tagging dataset, AudioSet. These comprehensive and varied sources are instrumental to enriching the depth and breadth of our dataset. Nevertheless, the harvested raw descriptions may range from complete sentences to fragmented phrases, lists of keywords or tags, and exhibit a high degree of noise. For instance, some de- scriptions do not represent the audio content at all, and certain descriptions contain extraneous information unrelated to the audio, such as recording devices, time, and locations. As a result, these unrefined raw descriptions hinder the lear

**Results-oriented passage (PDF p. 8)**

To ensure the robustness of our methodology, we incorpo- rated a human validation process for a subset of the WavCaps dataset. We randomly selected 160 samples from FreeSound, which are also included in the test set of Clotho. We recruited eight evaluators and engaged them in a two-stage process: initially, they were asked to listen to the audio samples and assessed the accuracy of the ChatGPT-augmented captions. The evaluators rated each caption on a Mean Opinion Score (MOS) scale from 1 to 5, where 1 means that the caption fails to correctly describe the audio clip at all, and 5 indicates a per- fect description of the audio clip without er

**Caveat-oriented passage (PDF p. 8)**

to note that if the original meta descriptions do not capture a particular aspect of the audio events or even do not accurately describe the audio content, the resulting captions tend to reflect these limitations, as we only processed the text metadata, but not the audio data. In addition, high-quality audio captions may include spatial-temporal in

## 92. Prefix tuning for automated audio captioning

ID: `2303.17489` | Theme: Captioning/grounding | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2303.17489

Snapshot SHA-256: `7025d58f8550dee1446f287b54bc5843a2ac816803b76b4a6e0ed0c10b6ffb2a`

Abstract extract: Audio captioning aims to generate text descriptions from environmental sounds. One challenge of audio captioning is the difficulty of the generalization due to the lack of audio-text paired training data. In this work, we propose a simple yet effective method of dealing with small-scaled datasets by leveraging a pre-trained language model. We keep the language model frozen to maintain the expressivity for text generation, and we only learn to extract global and temporal features from the input audio. To bridge a modality gap between the audio features and the language model, we employ mapping networks that translate audio features to the continuous vectors the language model can understand, 

**Method-oriented passage (PDF p. 1)**

ABSTRACT Audio captioning aims to generate text descriptions from environ- mental sounds. One challenge of audio captioning is the difﬁculty of the generalization due to the lack of audio-text paired training data. In this work, we propose a simple yet effective method of dealing with small-scaled datasets by leveraging a pre-trained lan- guage model. We keep the language model frozen to maintain the expressivity for text generation, and we only learn to extract global and temporal features from the input audio. To bridge a modality gap between the audio features and the language model, we employ map- ping networks that translate audio featur

**Results-oriented passage (PDF p. 3)**

We compare our proposed model with the competing methods ac- cording to the settings described in Sec. 3.1. As shown in (i) of both Table 1 and Table 2, our model shows favorable performance against the other methods. In setting (ii), where the test set distribution is different from the training one, the other methods show signiﬁcant performance drops in all the metrics, while our method favorably de- fends the drop. We postulate that the other methods may be ﬁtted to the target dataset by training the decoder with the target dataset. Fi- nally, we conduct an experiment (iii) to further evaluate whether the methods can be generalized to the 

**Caveat-oriented passage (PDF p. 4)**

We conduct ablation studies to evaluate our design choices; the ef- fectiveness of the mapping network, and the synergy of using both global and temporal features. The results are summarized in Table 4. We observe that using both global and temporal features may further enhance performance. However, using both features without map- ping networks ca

## 93. TorchAudio-Squim: Reference-less Speech Quality and Intelligibility measures in TorchAudio

ID: `2304.01448` | Theme: Evaluation/reliability | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2304.01448

Snapshot SHA-256: `48cf605756dc08812389b690fae92bd815bbbd0c4c7ce7ef54752fb455493c6c`

Abstract extract: Measuring quality and intelligibility of a speech signal is usually a critical step in development of speech processing systems. To enable this, a variety of metrics to measure quality and intelligibility under different assumptions have been developed. Through this paper, we introduce tools and a set of models to estimate such known metrics using deep neural networks. These models are made available in the well-established TorchAudio library, the core audio and speech processing library within the PyTorch deep learning framework. We refer to it as TorchAudio-Squim, TorchAudio-Speech QUality and Intelligibility Measures. More specifically, in the current version of TorchAudio-squim, we estab

**Method-oriented passage (PDF p. 2)**

We give a quick overview of the speech quality and intelligibility assessment tools currently provided through TorchAudio-Squim. As mentioned before, we are supporting both subjective and objective metrics in TorchAudio-Squim. Objective Metrics: In the current version, we are releasing a model to estimate 3 well-known objective metrics for speech assessment. These are Perceptual Evaluation of Speech Quality (PESQ) [19, 20], Short-Time Objective Intelligibility (STOI) [21] and Scale-Invariant Signal-to-Distortion Ratio (SI-SDR) [22]. Note that, we use Wideband-PESQ [20] and the term PESQ will refer to WB-PESQ throughout this paper. In this wor

**Results-oriented passage (PDF p. 4)**

We measure the performance of metric estimation using the mean absolute error (MAE), the Pearson correlation coefﬁcient (PCC) and the Spearman’s rank correlation coefﬁcient (SRCC). For both PCC and SRCC, higher scores correspond to better performance. Table 1 investigates different loss functions and weighting fac- tors. We observe that using the MAE loss as Ls yields a signiﬁcantly better performance than using the mean squared error (MSE) loss. In addition, different weighting factor values are compared, revealing that using w1 = 1, w2 = 2, w3 = 0.5, w0 = 2 with MTL achieves almost the best performance in terms of all the three scores. Tabl

**Caveat-oriented passage (PDF p. 5)**

[1] P. C. Loizou, “Speech quality assessment,” in Multimedia analysis and communications. Springer, 2011. [2] P. Gray, M. Hollier, and R. Massara, “Non-intrusive speech-quality assessment using vocal-tract models,” IEE Proceedings-Vision, Image and Signal Processing, vol. 147, no. 6, pp. 493–501, 2000. [3] W.-C. Huang, E. Cooper, Y. Tsao, H.-M. Wan

## 94. Margin-Mixup: A Method for Robust Speaker Verification in Multi-Speaker Audio

ID: `2304.03515` | Theme: Evaluation/reliability | Status: `selected_fulltext_review_plus_scoped_core_crosscheck`

Source: https://arxiv.org/pdf/2304.03515

Snapshot SHA-256: `0872f021a22f0f56cc207c98063d22a0c8460e2306c68754999f856ddc46ffc1`

Abstract extract: This paper is concerned with the task of speaker verification on audio with multiple overlapping speakers. Most speaker verification systems are designed with the assumption of a single speaker being present in a given audio segment. However, in a real-world setting this assumption does not always hold. In this paper, we demonstrate that current speaker verification systems are not robust against audio with noticeable speaker overlap. To alleviate this issue, we propose margin-mixup, a simple training strategy that can easily be adopted by existing speaker verification pipelines to make the resulting speaker embeddings robust against multi-speaker audio. In contrast to other methods, margin-

**Method-oriented passage (PDF p. 1)**

turns but are not designed to handle mixtures with signiﬁcant interference between speakers. In [7], target-speaker extrac- tion [8] is applied in a joint training scheme with speaker veriﬁcation to handle the signiﬁcant speaker overlap. An- other approach is used in [9], with an architecture injecting the target speaker embedding into the hidden frame-level features before the statistics pooling layer. However, these approaches use task-speciﬁc architectures or require signiﬁ- cant adaptations of existing speaker veriﬁcation pipelines. To alleviate this issue, we propose margin-mixup, a train- ing strategy based on mixup [10] to produce spea

**Results-oriented passage (PDF p. 3)**

Table 1 gives an overview of the impact of applying the proposed margin-mixup strategy on the baseline models de- scribed in Section 2. We notice a signiﬁcant performance degradation across all baseline models when mixing another speaker in the test trials as done in the Vox1-M test set. This supports our hypothesis that the single-speaker assumption held in most speaker veriﬁcation setups results in embed- dings unable to model signiﬁcant speaker overlap. However, while margin-mixup has a negligible performance impact on the single-speaker test set Vox1-O, the EER on Vox1-M improves on average with 44.4% relative over the baseline systems. T

**Caveat-oriented passage (PDF p. 2)**

Current state-of-the-art speaker veriﬁcation pipelines attain impressive performance on audio containing a single speaker. While those systems are generally robust against babble-like background noise, we argue they are not able to handle signif- icant interference of multiple speakers. This is mainly due to the emphasis of single-speaker audio in 

Additional interpretation and limitations: [core findings](CORE_FINDINGS.md).

## 95. Graph Attention for Automated Audio Captioning

ID: `2304.03586` | Theme: Captioning/grounding | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2304.03586

Snapshot SHA-256: `13fe3aa84920330e03a1e4c8aa046ddc0522e1a9dec2c8722b6116435a1f3644`

Abstract extract: State-of-the-art audio captioning methods typically use the encoder-decoder structure with pretrained audio neural networks (PANNs) as encoders for feature extraction. However, the convolution operation used in PANNs is limited in capturing the long-time dependencies within an audio signal, thereby leading to potential performance degradation in audio captioning. This letter presents a novel method using graph attention (GraphAC) for encoder-decoder based audio captioning. In the encoder, a graph attention module is introduced after the PANNs to learn contextual association (i.e. the dependency among the audio features over different time frames) through an adjacency graph, and a top-k mask 

**Method-oriented passage (PDF p. 2)**

The proposed GraphAC adopts P-Transformer [2] as the backbone, with the graph attention module added in the encoder to model the relations among the audio nodes (i.e., audio feature frames) extracted by PANNs, and to obtain an improved audio feature representation. Then, a Transformer decoder is employed to predict the caption from the audio fea- ture representation. Fig. 1 shows the framework of GraphAC.

**Results-oriented passage (PDF p. 3)**

In the graph attention module, k was empirically set as 25 in the top-k mask. Following P-Transformer [2], GraphAC applied SpecAugment and mix-up strategies to improve gen- eralisation. The cross-entropy loss with label smoothing [23] was used with Adam optimizer [24] to optimize the network. The batch size was 16, and the learning rate was 0.0001. The decoder used a teacher forcing strategy in training and a beam search strategy with a beam size of 5 in evaluation. Following DCASE Challenge, all the methods are evalu- ated by machine translation metrics (i.e., BLEUn, ROUGEl and METEOR) and captioning metrics (CIDEr, SPICE and SPIDEr). BLEUn 

**Caveat-oriented passage (PDF p. 3)**

Following Task 6 of the DCASE 2021 Challenge and related work, such as [2], we use the development and validation splits of the AudioCaps dataset [21] for pretraining, the development and validation splits of the Clotho-v2 dataset [1] for ﬁne- tuning, and the evaluation split of the Clotho-v2 dataset for evaluation. Speciﬁcally, AudioCaps has 44366

## 96. NaturalSpeech 2: Latent Diffusion Models are Natural and Zero-Shot Speech and Singing Synthesizers

ID: `2304.09116` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2304.09116

Snapshot SHA-256: `edfdf110918345ede9b82df372e6c04317cd28e71cabae96ed73dd30d812c698`

Abstract extract: Scaling text-to-speech (TTS) to large-scale, multi-speaker, and in-the-wild datasets is important to capture the diversity in human speech such as speaker identities, prosodies, and styles (e.g., singing). Current large TTS systems usually quantize speech into discrete tokens and use language models to generate these tokens one by one, which suffer from unstable prosody, word skipping/repeating issue, and poor voice quality. In this paper, we develop NaturalSpeech 2, a TTS system that leverages a neural audio codec with residual vector quantizers to get the quantized latent vectors and uses a diffusion model to generate these latent vectors conditioned on text input. To enhance the zero-shot

**Method-oriented passage (PDF p. 2)**

In this paper, we propose NaturalSpeech 2, a TTS system with latent diffusion models to achieve expressive prosody, good robustness, and most importantly strong zero-shot ability for speech synthesis. As shown in Figure 1, we first train a neural audio codec that converts a speech waveform into a sequence of latent vectors with a codec encoder, and reconstructs the speech waveform from these latent vectors with a codec decoder. After training the audio codec, we use the codec encoder to extract the latent vectors from the speech in the training set and use them as the target of the latent diffusion model, which is conditioned on prior vectors

**Results-oriented passage (PDF p. 11)**

We further evaluate the speaker similarity using SMOS test. We randomly select 10 utterances from LibriSpeech and VCTK datasets respectively, following the setting in the CMOS test. The length of the prompt speech is set to 3s. The results are shown in Table 5. NaturalSpeech 2 outperforms YourTTS by 1.25 and 0.77 SMOS scores for LibriSpeech and VCTK, respectively, which shows that NaturalSpeech 2 is significantly better in speaker similarity.

**Caveat-oriented passage (PDF p. 2)**

Previous speaker-limited recording-studio datasets are not enough to capture the diverse speaker identities, prosodies, and styles in human speech due to limited data diversity. Instead, we can train TTS models on a large-scale corpus to learn these diversities, and as a by-product, these trained models can generalize to the unlimited unseen scenar

## 97. Multi-Speaker Multi-Lingual VQTTS System for LIMMITS 2023 Challenge

ID: `2304.13121` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2304.13121

Snapshot SHA-256: `991e775ba3bb49883cd965eb4a5eb6b64bb15146a46312fff5c34b50c40c8eb0`

Abstract extract: In this paper, we describe the systems developed by the SJTU X-LANCE team for LIMMITS 2023 Challenge, and we mainly focus on the winning system on naturalness for track 1. The aim of this challenge is to build a multi-speaker multi-lingual text-to-speech (TTS) system for Marathi, Hindi and Telugu. Each of the languages has a male and a female speaker in the given dataset. In track 1, only 5 hours data from each speaker can be selected to train the TTS model. Our system is based on the recently proposed VQTTS that utilizes VQ acoustic feature rather than mel-spectrogram. We introduce additional speaker embeddings and language embeddings to VQTTS for controlling the speaker and language inform

**Method-oriented passage (PDF p. 2)**

Our TTS model is based on the recently proposed VQTTS [2], con- sisting of an acoustic model txt2vec and a vocoder vec2wav. It uses VQ acoustic feature extracted by vq-wav2vec [5] rather than mel-spectrogram as the acoustic feature. In this way, our acous- tic model txt2vec basically becomes a classification model rather than a traditional regression model. Instead of predicting the com- plicated mel-spectrogram with high correlation along both time and frequency axes, txt2vec only needs to consider the correlation along time axis in feature prediction, which narrows the gap between GT and predicted acoustic feature dramatically. Besides the 

**Results-oriented passage (PDF p. 2)**

There are evaluations on both mono-lingual and cross-lingual speech synthesis in this challenge. For mono-lingual speech synthesis, we just provide the specified speaker embedding and language embed- ding to the VQTTS. As for cross-lingual speech synthesis, we notice that giving unmatched speaker embedding and language embedding to the acoustic model txt2vec sometimes generates unstable results and mispronunciation in our preliminary experiments. Therefore, we provide a native speaker’s embedding to txt2vec for generating the proper articulation first. Then we provide the specified cross-lingual speaker’s embedding to the vec2wav for generati

**Caveat-oriented passage (PDF p. 2)**

Our proposed VQTTS system achieves the best naturalness among all the systems in track 1. We notice that the speaker similar- ity of cross-lingual synthesis is still worse than that of mono-lingual synthesis. We leave this issue to be addressed in the future work.

## 98. Text-to-Audio Generation using Instruction-Tuned LLM and Latent Diffusion Model

ID: `2304.13731` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2304.13731

Snapshot SHA-256: `9f87f6488446e8071f1b8489d15884f914a428e5b5edb7cff6e19b55ea1533f0`

Abstract extract: The immense scale of the recent large language models (LLM) allows many interesting properties, such as, instruction- and chain-of-thought-based fine-tuning, that has significantly improved zero- and few-shot performance in many natural language processing (NLP) tasks. Inspired by such successes, we adopt such an instruction-tuned LLM Flan-T5 as the text encoder for text-to-audio (TTA) generation -- a task where the goal is to generate an audio from its textual description. The prior works on TTA either pre-trained a joint text-audio encoder or used a non-instruction-tuned model, such as, T5. Consequently, our latent diffusion model (LDM)-based approach TANGO outperforms the state-of-the-art

**Method-oriented passage (PDF p. 3)**

We use the pre-trained LLM FLAN-T5-LARGE (780M) [3] as the text encoder (Etext) to obtain text encoding τ ∈RL×dtext, where L and dtext are the token count and token-embedding size, respectively. Due to the pre-training of FLAN-T5 models on a large-scale chain-of-thought- (CoT) and instruction-based dataset, Dai et al. [4] posit that they are able to learn a new task very well from the in-context information by mimicking gradient descent through attention weights. This property is missing in the older large models, such as RoBERTa [19] (used by Liu et al. [18]) and T5 [30] (used by Kreuk et al. [17]). Considering each input sample a distinct t

**Results-oriented passage (PDF p. 7)**

Table 1: The comparison between TANGO and baseline TTA models. FT indicates the model is fine-tuned on the Audiocaps (AC) dataset. The AS and AC stand for AudioSet and AudiocCaps datasets respectively. We borrowed all the results from [18] except for AudioLDM-L-Full which was evaluated using the model released by the authors on Huggingface. Despite the LDM being trained on a much smaller dataset, TANGO outperforms AudioLDM and other baseline TTA models as per both objective and subjective metrics. ‡ indicates the results are obtained using the checkpoints released by Liu et al. [18].

**Caveat-oriented passage (PDF p. 11)**

Text-to-Audio Generation. The field of text-to-audio generation has received limited attention until recently [17, 43]. In Yang et al. [43], a text encoder is used to obtain text features, which are then processed by a non-autoregressive decoder to generate spectrogram tokens. These tokens are fed to a vector quantized VAE (VQ-VAE) to generate mel 

## 99. HiFi-Codec: Group-residual Vector quantization for High Fidelity Audio Codec

ID: `2305.02765` | Theme: Representations/codecs | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2305.02765

Snapshot SHA-256: `59c441e3d674ac85778d0830c59b2e22b8bd290598f8b9d2d8ece302bee44605`

Abstract extract: Audio codec models are widely used in audio communication as a crucial technique for compressing audio into discrete representations. Nowadays, audio codec models are increasingly utilized in generation fields as intermediate representations. For instance, AudioLM is an audio generation model that uses the discrete representation of SoundStream as a training target, while VALL-E employs the Encodec model as an intermediate feature to aid TTS tasks. Despite their usefulness, two challenges persist: (1) training these audio codec models can be difficult due to the lack of publicly available training processes and the need for large-scale data and GPUs; (2) achieving good reconstruction perform

**Method-oriented passage (PDF p. 3)**

Our approach is based on a GAN objective, in which we opti- mize both the generator and the discriminators. Speciﬁcally, we jointly optimize a reconstruction loss term, a perceptual loss term (via discriminators), and the GRVQ commitment loss for the generator. The training objective of the generator comprises several loss terms, including a time domain term, a frequency domain term, three discriminator losses, and the corresponding feature loss terms acting as a perceptual loss and the GRVQ commitment loss. The discriminator loss is based on the adversarial hinge-loss function.

**Results-oriented passage (PDF p. 4)**

Table 1 shows the experimental results. We can see that our pro- posed HiFi-Codec realizes good reconstruction performance while only using 4 codebooks. The best performance can be ab- tained when we set downsample times as 240, and the number of codebooks as 8 (we set the each layer includes 4 codebooks, and two residual layers are used). Furthermore, our reproduced models (Encodec and SoundStream) also get comparable per- formance with Encodec [11]. We strongly recommend readers to use the HiFi-Codec model with 4 codebooks when readers try to train a generation model.

**Caveat-oriented passage (PDF p. 5)**

Although HiFi-Codec models realize good construction per- formance than Encodec model, the limitations still exist. (1) We do not use large-scale dataset to train a universal audio codec, the generalization cannot be validated very well. (2) We ﬁnd that the objective evaluation metrics may not very accurate to assess the reconstruction performance.

## 100. Improving Cascaded Unsupervised Speech Translation with Denoising Back-translation

ID: `2305.07455` | Theme: Loop/data selection | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2305.07455

Snapshot SHA-256: `3caf4347da3f76a02357bc0b03e5fef428f00297f32ebc263805d33365f6051e`

Abstract extract: Most of the speech translation models heavily rely on parallel data, which is hard to collect especially for low-resource languages. To tackle this issue, we propose to build a cascaded speech translation system without leveraging any kind of paired data. We use fully unpaired data to train our unsupervised systems and evaluate our results on CoVoST 2 and CVSS. The results show that our work is comparable with some other early supervised methods in some language pairs. While cascaded systems always suffer from severe error propagation problems, we proposed denoising back-translation (DBT), a novel approach to building robust unsupervised neural machine translation (UNMT). DBT successfully in

**Method-oriented passage (PDF p. 2)**

et al., 2017; Sun et al., 2020); however, improv- ing the robustness of UNMT is rarely studied. In this paper, we proposed denoising back-translation (DBT), a novel method to build a robust UNMT system. DBT combines the idea of denoising auto- encoding and back-translation (BT), dealing with error propagation issues in a fully unsupervised fashion. Brieﬂy speaking, the pseudo text of DBT is generated from text with some noise, and the model should learn to reconstruct the clean text from the pseudo text. According to our results, this method substantially increases the quality of the cascaded unsupervised speech translation system. Another is

**Results-oriented passage (PDF p. 7)**

original DBT ﬁne-tuning, but ﬁne-tunes on nor- malized source text and unnormalized target text. While directly ﬁne-tune the checkpoint pretrained on unnormalized text might induce mismatch be- tween pretraining and ﬁne-tuning. To address this problem, we further introduce normalized contin- ual training (NCT), which continual pretrains the checkpoint on normalized source text and unnor- malized target text, and follow NFT for down- stream task ﬁne-tuning. The results are shown in Table 5. we compare NFT (I) and NCT (II) with our two baselines: (I) UDN + UNMT (our original setting), (II) UNMT (only use the translation model of (I)). The perfo

**Caveat-oriented passage (PDF p. 2)**

Traditional S2TT system is composed of ASR and MT (Ney, 1999), and S2ST system further append a TTS model after the MT model (Lavie et al., 1997; Wahlster, 2000; Nakamura et al., 2006). However, cascaded systems might suffer from error propaga- tion and inference latency. Recent develpments in end-to-end S2TT (Bérard et al., 2016; Weiss et al., 201

## 101. Back Translation for Speech-to-text Translation Without Transcripts

ID: `2305.08709` | Theme: Loop/data selection | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2305.08709

Snapshot SHA-256: `334ac168e3763efec6411af15cac738dc0f3a059c63b95e14437648bb80a0ec6`

Abstract extract: The success of end-to-end speech-to-text translation (ST) is often achieved by utilizing source transcripts, e.g., by pre-training with automatic speech recognition (ASR) and machine translation (MT) tasks, or by introducing additional ASR and MT data. Unfortunately, transcripts are only sometimes available since numerous unwritten languages exist worldwide. In this paper, we aim to utilize large amounts of target-side monolingual data to enhance ST without transcripts. Motivated by the remarkable success of back translation in MT, we develop a back translation algorithm for ST (BT4ST) to synthesize pseudo ST data from monolingual target data. To ease the challenges posed by short-to-long ge

**Method-oriented passage (PDF p. 8)**

ent single models (e.g., models trained on different data) to achieve stronger performance. To synthe- size multiple diverse pseudo datasets from a single monolingual corpus, we introduce a simple Diverse BT4ST method. For the target-to-unit model, we activate the dropout modules during beam search decoding. For the unit-to-speech model, we ran- domly select the speaker embedding as above. By setting different random seeds, we can generate source speeches with different content and different speakers from the target text. In this way, we obtain multiple different pseudo datasets and train sev- eral models individually. We then combine these m

**Results-oriented passage (PDF p. 6)**

Table 2 shows the results on MuST-C En→De, En→Fr, and En→Es tst-COMMON set. First, we observe that our HU-TRANSFORMER is a strong baseline compared with previous baselines. Sec- ond, by synthesizing pseudo ST data with our pro- posed BT4ST and using it to pre-train the model, we achieve an average boost of 2.3 BLEU in three translation directions. It demonstrates that our ap- proach can effectively utilize external monolingual target data to improve the performance of ST.

**Caveat-oriented passage (PDF p. 2)**

compared to text-to-text back translation, gener- ating source speech from the target text without source transcripts is much more challenging4. First, the length of text is usually only tens or hundreds, but the length of speech is about tens of thousands5. Therefore, the model is required to generate an extremely long sequence from a short sequen

## 102. SpeechGPT: Empowering Large Language Models with Intrinsic Cross-Modal Conversational Abilities

ID: `2305.11000` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2305.11000

Snapshot SHA-256: `8869e490998b4703a3b0a3f48e128371dc1d4f78018e4c4943249cf93e528f21`

Abstract extract: Multi-modal large language models are regarded as a crucial step towards Artificial General Intelligence (AGI) and have garnered significant interest with the emergence of ChatGPT. However, current speech-language models typically adopt the cascade paradigm, preventing inter-modal knowledge transfer. In this paper, we propose SpeechGPT, a large language model with intrinsic cross-modal conversational abilities, capable of perceiving and generating multi-model content. With discrete speech representations, we first construct SpeechInstruct, a large-scale cross-modal speech instruction dataset. Additionally, we employ a three-stage training strategy that includes modality-adaptation pre-traini

**Method-oriented passage (PDF p. 2)**

In this paper, we propose SpeechGPT, a large language model with intrinsic cross-modal conver- sational abilities, capable of perceiving and generating multi-model content. We perform speech discretization with a self-supervised trained speech model to unify the modality between speech and text. The discrete speech tokens are then expanded into the vocabulary of the LLM, thus endowing the model with an inherent competence to perceive and generate the speech.

**Results-oriented passage (PDF p. 2)**

To evaluate the effectiveness of SpeechGPT, we conduct a wide range of human evaluations and case analyses to estimate the performance of SpeechGPT on textual tasks, speech-text cross-modal tasks, and spoken dialogue tasks. The results demonstrate that SpeechGPT exhibits a strong ability for unimodal and cross-modal instruction following tasks as well as spoken dialogue tasks.

**Caveat-oriented passage (PDF p. 2)**

While capable of perceiving and generating speech, the existing cascading methods or spoken language models still have several limitations. First, the LLM in the cascaded model only functions as a content generator. Since the representations of speech and text are not aligned, the LLM’s knowledge cannot be transferred to the speech modality. Second

## 103. DUB: Discrete Unit Back-translation for Speech Translation

ID: `2305.11411` | Theme: Loop/data selection | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2305.11411

Snapshot SHA-256: `e5b709b15d9c23ecacfbc8be8463bb3f6f88fdcf5f2b93972a8f59b38bf9006d`

Abstract extract: How can speech-to-text translation (ST) perform as well as machine translation (MT)? The key point is to bridge the modality gap between speech and text so that useful MT techniques can be applied to ST. Recently, the approach of representing speech with unsupervised discrete units yields a new way to ease the modality problem. This motivates us to propose Discrete Unit Back-translation (DUB) to answer two questions: (1) Is it better to represent speech with discrete units than with continuous features in direct ST? (2) How much benefit can useful MT techniques bring to ST? With DUB, the back-translation technique can successfully be applied on direct ST and obtains an average boost of 5.5 B

**Method-oriented passage (PDF p. 2)**

text. By leveraging the additional easily accessible text in the target language, we utilize the synthetic parallel data generated by the text-to-unit transla- tion model in conjunction with the original parallel data to update the ﬁnal unit-to-text model. Our contributions include the following. • We design a novel unit-text translation (U2TT) framework for direct ST by discretizing the speech feature in an unsupervised manner. Our analysis shows that in such a framework, the unit retains the semantic information for translation and can be used as model input. • Based on the U2TT framework, we propose DUB, which successfully applies the back

**Results-oriented passage (PDF p. 5)**

MuST-C As shown in Table 1, compared to the methods that do not involve the transcribed text, our method, U2TT (LARGE) with DUB, gets the best ST results by introducing extra target-language text, and DUB obtains an average boost of 5.5 BLEU compared with U2TT in the three En-X directions. Encouragingly, we ﬁnd that our method achieves comparable performance to previous models that utilize transcriptions through multi-task learning or pre-training. As for the baseline, U2TT outper- forms the Transformer-ST, where we believe that the discrete units still retain the semantic informa- tion of the audio feature (e.g. log Mel-ﬁlter bank, abbr. Fba

**Caveat-oriented passage (PDF p. 2)**

Speech translation Without using textual tran- scriptions during inference or training, translat- ing audio directly into the target language is very meaningful for languages that do not have a writ- ten form. Bérard et al. (2016) ﬁrst proposed an end-to-end encoder-decoder architecture for such direct speech-to-text translation. Later, novel mod- 

## 104. Laughter Synthesis using Pseudo Phonetic Tokens with a Large-scale In-the-wild Laughter Corpus

ID: `2305.12442` | Theme: Data/Indic speech | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2305.12442

Snapshot SHA-256: `d251bd46b91db05a823296bba8e455d4c8f28cea1ce841a551316299537ca83e`

Abstract extract: We present a large-scale in-the-wild Japanese laughter corpus and a laughter synthesis method. Previous work on laughter synthesis lacks not only data but also proper ways to represent laughter. To solve these problems, we first propose an in-the-wild corpus comprising $3.5$ hours of laughter, which is to our best knowledge the largest laughter corpus designed for laughter synthesis. We then propose pseudo phonetic tokens (PPTs) to represent laughter by a sequence of discrete tokens, which are obtained by training a clustering model on features extracted from laughter by a pretrained self-supervised model. Laughter can then be synthesized by feeding PPTs into a text-to-speech system. We furt

**Method-oriented passage (PDF p. 3)**

To solve the above problems, we propose pseudo phonetic tokens (PPTs) to represent laughter. The proposed PPT is in- spired by generative spoken language modeling [27, 28], which originally uses SSL models to discretize speech to do TTS in a textless manner. In this work, we further adapt this idea into nonverbal laughter. As shown in the top half of Figure 2 (a), the waveform is first fed into HuBERT [20] to convert it into continuous sequential features. Then, a k-means model [19] is trained upon the features, which can be used to convert the con- tinuous features into discrete tokens (cluster indices). Although the continuous features enco

**Results-oriented passage (PDF p. 4)**

utterances of which the first 6 are dummy samples used to enable the workers to get familiar with the task. The answers of the dummy samples are not counted in the final result. As a result, each utterance has 3 answers. The SMOS test is conducted in a similar setting with 45 listeners, but the GT utterances are excluded. All results are shown in Table 1. First, the baseline method has poor performance in both the objective and subjective evalua- tions. To verify if this is because the model fails to learn from the inputted phonemes, we further use GT acoustic features (pitch and energy) to synthesize the test utterances. The corresponding mo

**Caveat-oriented passage (PDF p. 2)**

process is illustrated in Figure 1. We first use several lists of casters and YouTubers obtained from Wikipedia 3 to crawl candi- date videos during June 2022 by searching the names in the list on YouTube, which results in about 10k videos. Using the lists ensures we only collect human speech instead of others like ani- mal sounds. Second, we use a

## 105. Scaling Speech Technology to 1,000+ Languages

ID: `2305.13516` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2305.13516

Snapshot SHA-256: `f83bf79e989b901b8fbf344d5940b1820534d67fd4bb3af5695d844825fbe490`

Abstract extract: Expanding the language coverage of speech technology has the potential to improve access to information for many more people. However, current speech technology is restricted to about one hundred languages which is a small fraction of the over 7,000 languages spoken around the world. The Massively Multilingual Speech (MMS) project increases the number of supported languages by 10-40x, depending on the task. The main ingredients are a new dataset based on readings of publicly available religious texts and effectively leveraging self-supervised learning. We built pre-trained wav2vec 2.0 models covering 1,406 languages, a single multilingual automatic speech recognition model for 1,107 language

**Method-oriented passage (PDF p. 2)**

To address this, we build a new dataset comprising a moderate amount of labeled data for 1,107 languages and another dataset of unlabeled speech in 3,809 languages (§3). We leverage this data to pre-train wav2vec 2.0 models supporting several times more languages than any known prior work (§4) and then fine-tune these models to build a multilingual speech recognition model supporting 1,107 languages (§5), language identification models for 4,017 languages (§6) and text-to-speech models for 1,107 languages (§7).

**Results-oriented passage (PDF p. 18)**

Table 5: Evaluation of MMS on Multilingual Benchmarks. MMS is fine-tuned on MMS-lab, FLEURS, CommonVoice, Voxpopuli and MLS. We report CER on FLEURS and WER on the other benchmarks. Results are averaged over all languages of a benchmark and (∗) indicates results with a different data normalization which does not enable a strict comparison to other results [Radford et al., 2022]. Our models use n-gram language models trained on Common Crawl during inference. For each approach, we show the number of languages an individual models supports and some prior results are based on multiple models, e.g., Wang et al. [2021].

**Caveat-oriented passage (PDF p. 2)**

Multilingual Speech Datasets. Current multilingual speech datasets with transcriptions are drawn from a variety of domains, including Wikipedia [Ardila et al., 2020, Conneau et al., 2022], political speech [Wang et al., 2021], audiobooks [Pratap et al., 2020c] to name a few. They are limited to about 100 languages with some datasets only containing

## 106. QLoRA: Efficient Finetuning of Quantized LLMs

ID: `2305.14314` | Theme: Efficiency/adaptation | Status: `selected_fulltext_review_plus_scoped_core_crosscheck`

Source: https://arxiv.org/pdf/2305.14314

Snapshot SHA-256: `33a4e757c19d6ea8d3cca8958fce8fe405e290272e135c99ee66065c775d5bd1`

Abstract extract: We present QLoRA, an efficient finetuning approach that reduces memory usage enough to finetune a 65B parameter model on a single 48GB GPU while preserving full 16-bit finetuning task performance. QLoRA backpropagates gradients through a frozen, 4-bit quantized pretrained language model into Low Rank Adapters~(LoRA). Our best model family, which we name Guanaco, outperforms all previous openly released models on the Vicuna benchmark, reaching 99.3% of the performance level of ChatGPT while only requiring 24 hours of finetuning on a single GPU. QLoRA introduces a number of innovations to save memory without sacrificing performance: (a) 4-bit NormalFloat (NF4), a new data type that is informat

**Method-oriented passage (PDF p. 15)**

While we provide a detailed evaluation for general chatbot performance, another limitation is that we only do a limited responsible AI evaluation of Guanaco. We evaluate the likelihood of Guanaco-65B to generate a socially biased sequence of tokens compared to other models in Table 8. We see that the average score in Guanaco-65B is much lower than other raw pretrained models. As such, it seems that finetuning on the OASST1 dataset reduces the bias of the LLaMA base model. While these results are encouraging, it is unclear if Guanaco does also well when assessed on other types of biases. We leave further evaluation of analyzing biases in Guana

**Results-oriented passage (PDF p. 2)**

QLORA reduces the average memory requirements of finetuning a 65B parameter model from >780GB of GPU memory to <48GB without degrading the runtime or predictive performance compared to a 16- bit fully finetuned baseline. This marks a significant shift in accessibility of LLM finetuning: now the largest publicly available models to date finetunable on a single GPU. Using QLORA, we train the Gua- naco family of models, with the second best model reaching 97.8% of the performance level of ChatGPT on the Vicuna [10] benchmark, while being trainable in less than 12 hours on a single consumer GPU; using a single professional GPU over 24 hours we ac

**Caveat-oriented passage (PDF p. 14)**

6.2 Considerations Evaluation We report moderate agreement among human annotators (Fleiss κ = 0.42) with additional deterioration when comparing two strong systems. This points to limitations in the current benchmarks and human evaluation protocols for chatbot task performance. When manually comparing generations from ChatGPT and Guanaco 65B on the

Additional interpretation and limitations: [core findings](CORE_FINDINGS.md).

## 107. The Curse of Recursion: Training on Generated Data Makes Models Forget

ID: `2305.17493` | Theme: Loop/data selection | Status: `selected_fulltext_review_plus_scoped_core_crosscheck`

Source: https://arxiv.org/pdf/2305.17493

Snapshot SHA-256: `db081e1b85409f99ebc6a017b0fe2851b2c2f689e051529d88a62d0853ee9507`

Abstract extract: Stable Diffusion revolutionised image creation from descriptive text. GPT-2, GPT-3(.5) and GPT-4 demonstrated astonishing performance across a variety of language tasks. ChatGPT introduced such language models to the general public. It is now clear that large language models (LLMs) are here to stay, and will bring about drastic change in the whole ecosystem of online text and images. In this paper we consider what the future might hold. What will happen to GPT-{n} once LLMs contribute much of the language found online? We find that use of model-generated content in training causes irreversible defects in the resulting models, where tails of the original content distribution disappear. We ref

**Method-oriented passage (PDF p. 2)**

We discover that learning from data produced by other models causes model collapse – a degenerative process whereby, over time, models forget the true underlying data distribution, even in the absence of a shift in the distribution over time. We give examples of model collapse for Gaussian Mixture Models (GMMs), Variational Autoencoders (VAE) and Large Language models (LLMs). We show that over time we start losing information about the true distribution, which first starts with tails disappearing, and over the generations learned behaviours start converging to a point estimate with very small variance. Furthermore, we show that this process i

**Results-oriented passage (PDF p. 11)**

We fine-tune the model on the wikitext2 dataset. For data generation from the trained models we use a 5-way beam-search. We block training sequences to be 64 tokens long; then for each token sequence in the training set, we ask the model to predict the next 64 tokens. We go through all of the original training dataset and produce an artificial dataset of the same size. Since we go though all of the original dataset and predict all of the blocks, if the model had 0.0 error it would produce the original wikitext2 dataset. Training for each of the generations starts with generation from the original training data. Each experiment is ran 5 times 

**Caveat-oriented passage (PDF p. 8)**

With this, instead of quantifying the distance exactly, we can instead lower bound it. The only limitation is that we are going to have to specify a functional approximation model. In order to achieve a W2 bound, we will be required to specify how the mean changes between generations. In the scenario where we only have access to the sample mean, we

Additional interpretation and limitations: [core findings](CORE_FINDINGS.md).

## 108. PromptStyle: Controllable Style Transfer for Text-to-Speech with Natural Language Descriptions

ID: `2305.19522` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2305.19522

Snapshot SHA-256: `c39f5bace8f9223d317044ae6fa18a79222f1c25874cf71b3d523e619283a841`

Abstract extract: Style transfer TTS has shown impressive performance in recent years. However, style control is often restricted to systems built on expressive speech recordings with discrete style categories. In practical situations, users may be interested in transferring style by typing text descriptions of desired styles, without the reference speech in the target style. The text-guided content generation techniques have drawn wide attention recently. In this work, we explore the possibility of controllable style transfer with natural language descriptions. To this end, we propose PromptStyle, a text prompt-guided cross-speaker style transfer system. Specifically, PromptStyle consists of an improved VITS

**Method-oriented passage (PDF p. 2)**

2.2. Cross-modal Style Encoder We introduce a cross-modal style encoder consisting of a style encoder and a prompt encoder for constructing a shared space of stylistic and semantic representation. The style encoder is used to extract the style information from Mel-spectrograms but not linear spectrograms, because linear spectrograms contain too much information which may prevent capturing the style information accurately. The style encoder consists of a reference encoder and an auxiliary adver- sarial component. The reference encoder almost has a simi- lar structure to the Global Style Tokens (GSTs) [24] discarding style token. The auxiliary 

**Results-oriented passage (PDF p. 4)**

quality, speaker similarity, and style similarity with a MOS test. The model setups and experimental results are shown in Table 2 and Table 3, respectively. As shown in Table 3, M1 maintains well the timbre of the target speaker but fails to achieve decent style transfer. Compar- ing M2 and M1, the results indicate that it is hard for a normaliz- ing flow to extract a proper style representation with both style embedding and speaker embedding as conditions. Comparing PromptStyle with M2, it is verified that PromptStyle can cap- ture more speaker timbre when the speaker embedding is added to the decoder of VITS. Finally, comparing M3 with Prom

**Caveat-oriented passage (PDF p. 5)**

[26] Y. Liu, Z. Xu, G. Wang, K. Chen, B. Li, X. Tan, J. Li, L. He, and S. Zhao, “Delightfultts: The microsoft speech synthesis system for blizzard challenge 2021,” arXiv preprint arXiv:2110.12612, 2021.

## 109. Simple and Controllable Music Generation

ID: `2306.05284` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2306.05284

Snapshot SHA-256: `b513ce6c6c5dae8914591ce932b8588798f6fb7c314c52ee8281c36e766e1b83`

Abstract extract: We tackle the task of conditional music generation. We introduce MusicGen, a single Language Model (LM) that operates over several streams of compressed discrete music representation, i.e., tokens. Unlike prior work, MusicGen is comprised of a single-stage transformer LM together with efficient token interleaving patterns, which eliminates the need for cascading several models, e.g., hierarchically or upsampling. Following this approach, we demonstrate how MusicGen can generate high-quality samples, both mono and stereo, while being conditioned on textual description or melodic features, allowing better controls over the generated output. We conduct extensive empirical evaluation, considerin

**Method-oriented passage (PDF p. 2)**

Our contribution: (i) We introduce a simple and efficient model to generate high quality music at 32 kHz. We show that MUSICGEN can generate consistent music with a single-stage language model through an efficient codebook interleaving strategy. (ii) We present a single model to perform both text and melody-conditioned generation and demonstrate that the generated audio is coherent with the provided melody and faithful to the text conditioning information. (iii) We provide extensive objective and human evaluations on the key design choices behind our method.

**Results-oriented passage (PDF p. 7)**

We evaluate MUSICGEN, conditioned jointly on textual and melodic representations, using objective and subjective metric on the held out evaluation set. For the objective evaluation, we introduce a new metric: chroma cosine-similarity, which measures the average cosine-similarity between frames corresponding to the same time steps, taken from the quantized chroma of the reference and the generated samples. We evaluate using 1000 randomly sampled files from a held-out set. To better evaluate the relation between the conditioned melody to the generated music, we introduce another human study. To that end, we present human raters with a reference

**Caveat-oriented passage (PDF p. 3)**

As stated before, the main issue with the representation Q we obtained from the EnCodec model is that there are K codebooks for each time step. One solution would be to flatten out Q, thus taking S = d · fr · K, e.g. first predicting the first codebook of the first time step, then the second codebook of the first time step, etc. Then, using eq. (1)

## 110. High-Fidelity Audio Compression with Improved RVQGAN

ID: `2306.06546` | Theme: Representations/codecs | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2306.06546

Snapshot SHA-256: `dbec2d2cd55f62dce77f3401f7c10309b9ab0025af5b25bf2db2f8b73686708e`

Abstract extract: Language models have been successfully used to model natural signals, such as images, speech, and music. A key component of these models is a high quality neural compression model that can compress high-dimensional natural signals into lower dimensional discrete tokens. To that end, we introduce a high-fidelity universal neural audio compression algorithm that achieves ~90x compression of 44.1 KHz audio into tokens at just 8kbps bandwidth. We achieve this by combining advances in high-fidelity audio generation with better vector quantization techniques from the image domain, along with improved adversarial and reconstruction losses. We compress all domains (speech, environment, music, etc.) 

**Method-oriented passage (PDF p. 1)**

Language models have been successfully used to model natural signals, such as images, speech, and music. A key component of these models is a high quality neural compression model that can compress high-dimensional natural signals into lower dimensional discrete tokens. To that end, we introduce a high-fidelity universal neural audio compression algorithm that achieves 90x compression of 44.1 KHz audio into tokens at just 8kbps bandwidth. We achieve this by combining advances in high-fidelity audio generation with better vector quantization tech- niques from the image domain, along with improved adversarial and reconstruction losses. We compr

**Results-oriented passage (PDF p. 3)**

An audio signal with sampling rate fs (Hz), encoder striding factor M, and Nq layers of RVQ produce a discrete code matrix of shape S ×Nq, where S is the frame rate defined as fs/M. Table 1 compares our proposed model against baselines to contrast the compression factors and the frame rate of latent codes. Note that the target bitrate mentioned is an upper bound, since all models support variable bitrates. Our model achieves a higher compression factor compared to all baseline methods while outperforming them in audio quality, as we show later. Finally, a lower frame rate is desirable when training a language model on the discrete codes, as i

**Caveat-oriented passage (PDF p. 3)**

Our proposed method also uses a convolutional encoder-decoder architecture, residual vector quan- tization and adversarial, perceptual losses. However, our recipe has the following key differences: 1) We introduce a periodic inductive bias using Snake activations [47, 21] 2) We improve codebook learning by projecting the encodings into a low-dimens

## 111. StyleTTS 2: Towards Human-Level Text-to-Speech through Style Diffusion and Adversarial Training with Large Speech Language Models

ID: `2306.07691` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2306.07691

Snapshot SHA-256: `f528cab389ea8af17cfcc95ab5847975bb79b00dd46424d6b2d44a1e44017c55`

Abstract extract: In this paper, we present StyleTTS 2, a text-to-speech (TTS) model that leverages style diffusion and adversarial training with large speech language models (SLMs) to achieve human-level TTS synthesis. StyleTTS 2 differs from its predecessor by modeling styles as a latent random variable through diffusion models to generate the most suitable style for the text without requiring reference speech, achieving efficient latent diffusion while benefiting from the diverse speech synthesis offered by diffusion models. Furthermore, we employ large pre-trained SLMs, such as WavLM, as discriminators with our novel differentiable duration modeling for end-to-end training, resulting in improved speech na

**Method-oriented passage (PDF p. 2)**

Diffusion Models for Speech Synthesis. Diffusion models have gained traction in speech synthesis due to their potential for diverse speech sampling and fine-grained speech control [15]. They have been applied to mel-based text-to-speech [16, 17, 18, 19, 20], mel-to-waveform vocoder [21, 22, 23, 24, 25, 26], and end-to-end speech generation [27, 28, 29]. However, their efficiency is limited compared to non-iterative methods, like GAN-based models [30, 31, 32], due to the need to iteratively sample mel-spectrograms, waveforms, or other latent representations proportional to the target speech duration [15]. Furthermore, recent works suggest that

**Results-oriented passage (PDF p. 8)**

In zero-shot tests, StyleTTS 2 surpasses Vall-E in naturalness with a CMOS of +0.67 (p ≪0.01), although it falls slightly short in similarity (Table 1). Im- portantly, StyleTTS 2 achieved these re- sults with only 245 hours of training data, compared to Vall-E’s 60k hours, a 250x difference. This makes StyleTTS 2 a data-efficient alternative to large pre- training methods like Vall-E. The MOS results in Table 3 support these findings, as our model exceeds all baseline models in both MOS-N and MOS-S. However, the difference in

**Caveat-oriented passage (PDF p. 6)**

where ℓi is the end position and ci is the center position of the ith phoneme ti. However, Gaussian upsampling has limitations due to its fixed width of Gaussian kernels determined by σ. This constraint prevents it from accurately modeling alignments with varying lengths depending on dpred. Non- attentive Tacotron [57] extends this by making σi tra

## 112. AudioPaLM: A Large Language Model That Can Speak and Listen

ID: `2306.12925` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2306.12925

Snapshot SHA-256: `76ff49cb6d0445f7a1922c1793e06b9e1f59648baa74dc1e24cd5da267f5ab9c`

Abstract extract: We introduce AudioPaLM, a large language model for speech understanding and generation. AudioPaLM fuses text-based and speech-based language models, PaLM-2 [Anil et al., 2023] and AudioLM [Borsos et al., 2022], into a unified multimodal architecture that can process and generate text and speech with applications including speech recognition and speech-to-speech translation. AudioPaLM inherits the capability to preserve paralinguistic information such as speaker identity and intonation from AudioLM and the linguistic knowledge present only in text large language models such as PaLM-2. We demonstrate that initializing AudioPaLM with the weights of a text-only large language model improves spee

**Method-oriented passage (PDF p. 2)**

In this work, we introduce AudioPaLM, a multimodal generative model of speech and text. At the heart of AudioPaLM is a joint vocabulary that can represent speech and text with a limited number of discrete tokens which, combined with an elementary markup description of tasks, allows training a single decoder-only model on a mixture of tasks that involve arbitrarily interleaved speech and text. This includes speech recognition, text-to-speech synthesis, and speech-to-speech translation, unifying tasks that are traditionally solved by heterogeneous models into a single architecture and training run. Moreover, as the underlying architecture of Au

**Results-oriented passage (PDF p. 9)**

Table 2 displays results on ASR, AST and S2ST benchmarks for our method and existing baselines. Our models come in two variants; the first variant (referred to as AST) is trained on AST tasks without S2ST and TTS data; the second variant (referred to as S2ST) is trained with S2ST and TTS data and is therefore able to produce speech as well. To generate the audio for the S2ST results we used SoundStorm [Borsos et al., 2023]. For details on the training mixtures see Section 3.5.

**Caveat-oriented passage (PDF p. 3)**

Recent work [Lakhotia et al., 2021, Wang et al., 2023] has explored generating speech by modeling discretized representations as target tokens of an autoregressive Transformer [Vaswani et al., 2017] network. Such discrete tokens can be extracted from self-supervised speech representations [Oord et al., 2018, Baevski et al., 2020, Hsu et al., 2021, 

## 113. Voicebox: Text-Guided Multilingual Universal Speech Generation at Scale

ID: `2306.15687` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2306.15687

Snapshot SHA-256: `53fb0eb4b581b51325da2ec62f72629be15ebe22eb55563a7c5da555c2176779`

Abstract extract: Large-scale generative models such as GPT and DALL-E have revolutionized the research community. These models not only generate high fidelity outputs, but are also generalists which can solve tasks not explicitly taught. In contrast, speech generative models are still primitive in terms of scale and task generalization. In this paper, we present Voicebox, the most versatile text-guided generative model for speech at scale. Voicebox is a non-autoregressive flow-matching model trained to infill speech, given audio context and text, trained on over 50K hours of speech that are not filtered or enhanced. Similar to GPT, Voicebox can perform many different tasks through in-context learning, but is

**Method-oriented passage (PDF p. 2)**

Popov et al., 2021, Huang et al., 2022, Tan et al., 2022, Casanova et al., 2021]. Previous works consider highly curated datasets such as VCTK [Yamagishi et al., 2019], which contains only clean audio recorded in studio from about 100 speakers with little speaking style and text variation. Such models struggle to synthesize speech with rich variation in emotion, voice, background noise, acoustic condition, and have not been tested on the abilities to generalize to tasks not explicitly trained on.

**Results-oriented passage (PDF p. 13)**

Table 5 presents the results comparing Voicebox with A3T and Demucs. It should be noted that A3T and Voicebox utilize transcript and location of the noise while Demucs does not. Nevertheless the goal of the study is to present a new paradigm and show Voicebox can perform denoising without being explicitly trained. Compared to the baselines, Voicebox generates samples that are much more intelligible (2.0% WER), more similar to the clean parts of the audio (0.612 SIM-o), and of higher quality (3.87 MOS) in this challenging noise condition. A3T is better than Demucs on intelligibilty and quality, but the infilled speech is not coherent because i

**Caveat-oriented passage (PDF p. 3)**

Controllable text-to-speech synthesis (TTS) is another common task, which aims to synthesize speech in a target audio style (e.g., voice, speaking style, recording environment) given text. While some styles like voice can be specified through labels [Kim et al., 2021] or pre-trained embeddings like YourTTS [Casanova et al., 2021] and Jia et al. [20

## 114. Self-supervised learning with diffusion-based multichannel speech enhancement for speaker verification under noisy conditions

ID: `2307.02244` | Theme: Evaluation/reliability | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2307.02244

Snapshot SHA-256: `a6fbe48b1cca602ebdec94a38bd2ba935b1a13b0a7cb21251c74e78dcb2c5943`

Abstract extract: The paper introduces Diff-Filter, a multichannel speech enhancement approach based on the diffusion probabilistic model, for improving speaker verification performance under noisy and reverberant conditions. It also presents a new two-step training procedure that takes the benefit of self-supervised learning. In the first stage, the Diff-Filter is trained by conducting timedomain speech filtering using a scoring-based diffusion model. In the second stage, the Diff-Filter is jointly optimized with a pre-trained ECAPA-TDNN speaker verification model under a self-supervised learning framework. We present a novel loss based on equal error rate. This loss is used to conduct selfsupervised learnin

**Method-oriented passage (PDF p. 2)**

We jointly optimized the Diff-Filter and ECAPA-TDNN as a multichannel SV. In joint optimization, the multichannel noisy signal is first given to Diff-Filter, which provides a single- channel Rank-1-MWF filtered clean speech signal. The error gradient passes through ECAPA-TDNN and Diff-Filter as a sin- gle unit because we back-propagate through both models that we are jointly training. To conduct the self-supervised learning with the unlabelled dataset, we created an RIR simulated dataset and applied it to clean speech from the LibriSpeech dataset [25] detailed in section 3. As shown in Figure 2, utterances 1 and 2 are given to the jointly opt

**Results-oriented passage (PDF p. 4)**

We compared the performance of the proposed approach with Conv-TasNet as baseline multichannel speech enhancement used as a front end to the ECAPA-TDNN system. For estab- lishing baseline Conv-TasNet, we trained under the same train- ing data used by the Diff-Filter system. Also, we used the same network configuration for Conv-TasNet as for the conditioning network of Diff-Filter. In addition to this, we also computed performance with oracle Rank-1 MWF in order to analyze the filtering approach based on the diffusion probabilistic model. We used EER as an evaluation metric to evaluate the multichan- nel SV systems on MRE and MRE hard trials f

**Caveat-oriented passage (PDF p. 1)**

Speaker verification (SV) aims to confirm the identity of a per- son based on his/her voice characteristics. SV has achieved sig- nificant performance gain in controlled or close-talk scenarios. However, it suffers from unsatisfactory performance in multi- channel far-field scenarios. This is due to complex environmen- tal settings as speech signal

## 115. WavJourney: Compositional Audio Creation with Large Language Models

ID: `2307.14335` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2307.14335

Snapshot SHA-256: `34bbeadb0de1a24779c42b523aa9c372423ead838dff74835222e17b0edcf479`

Abstract extract: Despite breakthroughs in audio generation models, their capabilities are often confined to domain-specific conditions such as speech transcriptions and audio captions. However, real-world audio creation aims to generate harmonious audio containing various elements such as speech, music, and sound effects with controllable conditions, which is challenging to address using existing audio generation systems. We present WavJourney, a novel framework that leverages Large Language Models (LLMs) to connect various audio models for audio creation. WavJourney allows users to create storytelling audio content with diverse audio elements simply from textual descriptions. Specifically, given a text inst

**Method-oriented passage (PDF p. 3)**

WavJourney offers multiple benefits for audio creation: as it is 1) Contextually adaptive, by leverag- ing the understanding capability and generalizable knowledge of LLMs, WavJourney can design au- dio storytelling scripts with diverse sound elements, and intricate acoustic relationships; 2) Compo- sitional, benefiting from its composable design, WavJourney can automatically decompose complex auditory scenes into independent sound elements, enabling the integration of various task-specific audio generation models to controllably create audio content. Our approach differs from previous methods (Liu et al., 2023a; Huang et al., 2023a), where e

**Results-oriented passage (PDF p. 7)**

Results on AudioCaps. WavJourney outperforms AudioGen and AudioLDM systems in all subjec- tive tests on the AudioCaps benchmark. As shown in the left part of Table 3, WavJourney achieves an OVL score of 3.75 and a REL score of 3.74. Compared with AudioLDM and AudioGen, WavJour- ney has 0.36 and 0.19 higher in OVL, and 0.4 and 0.22 higher in REL, respectively. WavJourney even marginally surpasses the ground truth audio in the OVL (3.73) metric and is on par in the REL (3.76) metric. The subjective preference-based testing results are consistent with the OVL and REL results, as shown on the left side of Figure 2. Specifically, against AudioGen,

**Caveat-oriented passage (PDF p. 2)**

speech, music, and sound effects from textual descriptions. Prior works have leveraged generative models to synthesize audio context that aligns with task-specific conditions, such as speech tran- scriptions (Panayotov et al., 2015), music descriptions (Agostinelli et al., 2023), and audio captions (Kim et al., 2019). However, the capabilities of t

## 116. A Novel Self-training Approach for Low-resource Speech Recognition

ID: `2308.05269` | Theme: Loop/data selection | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2308.05269

Snapshot SHA-256: `9c1e54567230d5697b3e8e86af832f05a4e8d57f433e8737ad6acbccff5bbe7a`

Abstract extract: In this paper, we propose a self-training approach for automatic speech recognition (ASR) for low-resource settings. While self-training approaches have been extensively developed and evaluated for high-resource languages such as English, their applications to low-resource languages like Punjabi have been limited, despite the language being spoken by millions globally. The scarcity of annotated data has hindered the development of accurate ASR systems, especially for low-resource languages (e.g., Punjabi and Māori languages). To address this issue, we propose an effective self-training approach that generates highly accurate pseudo-labels for unlabeled low-resource speech. Our experimental a

**Method-oriented passage (PDF p. 2)**

We propose a very simple, yet effective self-training method for the Punjabi language. However, the proposed method could work for any language having a small amount of annotated data and large unlabeled audio data.

**Results-oriented passage (PDF p. 4)**

We report the results in Table 2. To show the effectiveness of our 5-gram language model (LM), we demonstrate the results on the seed model with and without the language model. We find that our LM decoding further improves the seed model, consequently, we choose seed with LM as our baseline model. All of our experimental results (except seed without LM) are carried out with LM decoding. Raw PL uses all available pseudo-labels, whereas Best PL selects the best-performing pseudo-labels over multiple iterations of pseudo-labeling with different confidence thresholds. The results show that using pseudo-labels with a filter (Best PL) outperforms R

**Caveat-oriented passage (PDF p. 2)**

Semi-supervised approaches such as self-supervision and self- training have been active areas of research for the past few years. The goal of these approaches is to leverage the large unlabeled speech data to improve the overall accuracy of the ASR systems. These approaches showed significant results for low-resource languages. Self-training is a f

## 117. SeamlessM4T: Massively Multilingual & Multimodal Machine Translation

ID: `2308.11596` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2308.11596

Snapshot SHA-256: `d75272376c4d837a4fe734768d4d9773bb6482d998d336c79cff8c8ac2a557ff`

Abstract extract: What does it take to create the Babel Fish, a tool that can help individuals translate speech between any two languages? While recent breakthroughs in text-based models have pushed machine translation coverage beyond 200 languages, unified speech-to-speech translation models have yet to achieve similar strides. More specifically, conventional speech-to-speech translation systems rely on cascaded systems that perform translation progressively, putting high-performing unified systems out of reach. To address these gaps, we introduce SeamlessM4T, a single model that supports speech-to-speech translation, speech-to-text translation, text-to-speech translation, text-to-text translation, and autom

**Method-oriented passage (PDF p. 79)**

Based on our concurrent work [Muller et al., 2023], we discuss the representation bias of several datasets by focusing on how different genders are represented using lexical matching. The closest work that studies gender representation in data is Choubey et al. [2021], where the authors took on this research question using a synthetic dataset. The authors, however, did not share the details of the lexical nouns used to extract this representation. HolisticBias [Smith et al., 2022] provides a list of gendered nouns and pronouns. We rely on this list to track how many sentences in our data sets contain gendered markers. Since our analysis is on

**Results-oriented passage (PDF p. 2)**

human evaluations of speech-to-text translation outputs evinced similarly impressive results; for translations from English, XSTS scores for 24 evaluated languages are consistently above 4 (out of 5). For into English directions, we see significant improvement over Whisper- Large-v2’s baseline for 7 out of 24 languages. To further evaluate our system, we developed Blaser 2.0, which enables evaluation across speech and text with similar accuracy compared to its predecessor when it comes to quality estimation. Tested for robustness, our system performs better against background noises and speaker variations in speech-to-text tasks (average impr

**Caveat-oriented passage (PDF p. 9)**

Cascaded systems Before the emergence of unified speech translation models in recent years, much attention in speech-based research has been directed at cascaded approaches by chaining subsystems that perform disparate tasks such as ASR, T2TT, and TTS [Lavie et al., 1997; Wahlster, 2000; Nakamura et al., 2006]. For example, in a 3-stage S2ST cascad

## 118. Unsupervised Active Learning: Optimizing Labeling Cost-Effectiveness for Automatic Speech Recognition

ID: `2308.14814` | Theme: Loop/data selection | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2308.14814

Snapshot SHA-256: `d9e61820c585f671126015be7839a8b160af13a23f1cacd9622f3676ef60b559`

Abstract extract: In recent years, speech-based self-supervised learning (SSL) has made significant progress in various tasks, including automatic speech recognition (ASR). An ASR model with decent performance can be realized by fine-tuning an SSL model with a small fraction of labeled data. Reducing the demand for labeled data is always of great practical value. In this paper, we further extend the use of SSL to cut down labeling costs with active learning. Three types of units on different granularities are derived from speech signals in an unsupervised way, and their effects are compared by applying a contrastive data selection method. The experimental results show that our proposed data selection framewor

**Method-oriented passage (PDF p. 2)**

• We propose a novel, completely unsupervised active learn- ing framework for speech data selection, which effectively reduces the cost of data labeling. • We analyze the impact of different granularities levels on data selection and measure the trade-off between process com- plexity and recognition accuracy. • Our proposed framework can either reduce the WER by over 11% with the same amount of labeled data, or cut the labeling cost to half while maintaining the same WER, compared to random selection.

**Results-oriented passage (PDF p. 3)**

training set. In addition to the training set, we have constructed dedicated validation and test sets for each of the 4 topics. Each of these sets contains 5 hours of audio data, providing ample material for model development, evaluation, and comparison. For the integrity and representativeness of the training, val- idation, and test sets, we have taken care to avoid any overlap in audio segments between these sets during the sampling pro- cess. Specifically, for the validation and test sets, we have sam- pled from the M-size GigaSpeech training subset, as the word error rate of this subset is 0%. For the training set, however, we require 100

**Caveat-oriented passage (PDF p. 2)**

Unsupervised data selection is a crucial technique aimed at achieving the goal of reducing the need for labeled data while maintaining high performance in downstream tasks for a spec- ified target domain. In the field of natural language processing (NLP), various approaches [10, 11, 12] have been proposed for unsupervised data selection, including 

## 119. SpeechTokenizer: Unified Speech Tokenizer for Speech Large Language Models

ID: `2308.16692` | Theme: Representations/codecs | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2308.16692

Snapshot SHA-256: `c6b661ac5ac00948ff2d116a77e52e12e369717fd40fb67332b7e48c16534d8e`

Abstract extract: Current speech large language models build upon discrete speech representations, which can be categorized into semantic tokens and acoustic tokens. However, existing speech tokens are not specifically designed for speech language modeling. To assess the suitability of speech tokens for building speech language models, we established the first benchmark, SLMTokBench. Our results indicate that neither semantic nor acoustic tokens are ideal for this purpose. Therefore, we propose SpeechTokenizer, a unified speech tokenizer for speech large language models. SpeechTokenizer adopts the Encoder-Decoder architecture with residual vector quantization (RVQ). Unifying semantic and acoustic tokens, Spee

**Method-oriented passage (PDF p. 2)**

With the above motivation, we propose SpeechTokenizer, a unified speech tokenizer for speech large language models. SpeechTokenizer adopts the Encoder-Decoder architecture with residual vector quantization. Unifying semantic and acoustic tokens, SpeechTokenizer disentangles different aspects of speech information hierarchically across different RVQ layers. By employing a semantic teacher to guide the first RVQ quantizer, the first layer tokens can effectively capture content information. With residual structure, the subsequent quantizers complement the remaining paralinguistic information.

**Results-oriented passage (PDF p. 3)**

Building upon SpeechTokenizer, we build a Unified Speech Language Model consisting of autore- gressive and non-autoregressive models. Experimental results show that SpeechTokenizer performs comparably to EnCodec (Défossez et al., 2022) in speech reconstruction and demonstrates strong performance on the SLMTokBench benchmark. The USLM notably outperforms VALL-E (Wang et al., 2023) in zero-shot Text-to-Speech (TTS) tasks.

**Caveat-oriented passage (PDF p. 2)**

However, existing speech tokens are not explicitly designed for speech language modeling, and there has been no exploration into their suitability for building speech language models. To address this gap, we build Speech Language Model Token Benchmark, to assess the suitability of speech tokens for constructing speech language models. Our evaluatio

## 120. A Comparative Analysis of Pretrained Language Models for Text-to-Speech

ID: `2309.01576` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2309.01576

Snapshot SHA-256: `66fbc205036dde117593e4614549a432b128651f4a03e4d3a2348f1b335946e6`

Abstract extract: State-of-the-art text-to-speech (TTS) systems have utilized pretrained language models (PLMs) to enhance prosody and create more natural-sounding speech. However, while PLMs have been extensively researched for natural language understanding (NLU), their impact on TTS has been overlooked. In this study, we aim to address this gap by conducting a comparative analysis of different PLMs for two TTS tasks: prosody prediction and pause prediction. Firstly, we trained a prosody prediction model using 15 different PLMs. Our findings revealed a logarithmic relationship between model size and quality, as well as significant performance differences between neutral and expressive prosody. Secondly, we 

**Method-oriented passage (PDF p. 2)**

We investigate the impact of PLMs on prosody prediction us- ing eCat [21] because it is a state-of-the-art TTS system that operates in a prosodic latent space. eCat latent space is de- signed in a way to factor out phoneme and speaker information and capture prosody. It works in a two-step approach where it first learns word-level acoustic and duration-based prosodic representations through an auto-encoder step. In the first step, reference encoders generate the prosodic space based on the mel-spectrogram, and decoders synthesize the speech wave- form based on the prosodic representations. The acoustic repre- sentations are expected to captur

**Results-oriented passage (PDF p. 2)**

We select 15 pretrained language models, including the default PLM (RoBERTa-base), for both the prosody predictor and the pause prediction model. All language models are BERT-like models, i.e., transformer encoders trained with large corpora of data in a self-supervised fashion. Our selection aims to cover a broad spectrum of model sizes with diverse pretraining or distil- lation techniques. In Table 1, we provide a list of the pretrained language models, along with their corresponding HuggingFace name and model size. Note that the size refers to the embedding matrix and model architecture weights combined. We first select medium- and large-s

**Caveat-oriented passage (PDF p. 3)**

In this work, we did not tune hyperparameters for every model that was trained. We used the same learning rate and train- ing steps across all language models to maintain simplicity and consistency in our experiments. However, we fine-tuned lan- guage models of diverse sizes and pretraining techniques. This may have resulted in an advantage for the

## 121. Zero-Shot Audio Captioning via Audibility Guidance

ID: `2309.03884` | Theme: Captioning/grounding | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2309.03884

Snapshot SHA-256: `cf2b6b47f87ee2103ee9c3a347f4dbb5a026d3af0221e34ac1073162777e23c2`

Abstract extract: The task of audio captioning is similar in essence to tasks such as image and video captioning. However, it has received much less attention. We propose three desiderata for captioning audio -- (i) fluency of the generated text, (ii) faithfulness of the generated text to the input audio, and the somewhat related (iii) audibility, which is the quality of being able to be perceived based only on audio. Our method is a zero-shot method, i.e., we do not learn to perform captioning. Instead, captioning occurs as an inference process that involves three networks that correspond to the three desired qualities: (i) A Large Language Model, in our case, for reasons of convenience, GPT-2, (ii) A model 

**Method-oriented passage (PDF p. 2)**

The task of captioning can be mathematically framed as a sequence generation problem, wherein we seek to infer the conditional probability of the i-th word, denoted as xi, in the sentence. In essence, our goal is to optimize the probability distribution p(xi—[xt]t<i, A), where xt represents preceding words in the sentence, and A signifies the input - in our case, an audio clip. We introduce a zero-shot approach specifically designed for the audio domain, employing a large-scale text-audio alignment model in conjunction with audibility promoting classifier-based guidance that together steer a large-scale language model. Main Pipeline The propo

**Results-oriented passage (PDF p. 4)**

Table 2. Evaluation results on the AudioCaps dataset for varying values of the weight parameter λ2. The table displays several performance metrics, including BLEU (B), METEOR (M), ROUGE-L (R), and CIDEr (C), alongside a novel metric focused on audibility (A).

**Caveat-oriented passage (PDF p. 2)**

Captioning, in various forms, has been extensively studied for images and videos. However, the same cannot be said for audio content, especially in the realm of zero-shot learning, and as far as we can ascertain, our work is the first to tackle zero-shot audio captioning. Audio Captioning Historically, audio captioning research has predominantly ad

## 122. Training Audio Captioning Models without Audio

ID: `2309.07372` | Theme: Captioning/grounding | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2309.07372

Snapshot SHA-256: `371cc2cfb6483ed8850fecef5a68c5a7fc4e0e79e2ecfae2426233e81019d65e`

Abstract extract: Automated Audio Captioning (AAC) is the task of generating natural language descriptions given an audio stream. A typical AAC system requires manually curated training data of audio segments and corresponding text caption annotations. The creation of these audio-caption pairs is costly, resulting in general data scarcity for the task. In this work, we address this major limitation and propose an approach to train AAC systems using only text. Our approach leverages the multimodal space of contrastively trained audio-text models, such as CLAP. During training, a decoder generates captions conditioned on the pretrained CLAP text encoder. During inference, the text encoder is replaced with the p

**Method-oriented passage (PDF p. 2)**

The model is trained as a standard captioning system, where it learns to predict a caption (text tokens) ci conditioned on the prefix in an autoregressive fashion. We used Cross-Entropy as the loss function:

**Results-oriented passage (PDF p. 3)**

4.1. Text-only training Table 1 shows results of various models trained on both Au- dioCaps and Clotho. Models in rows 1-4 use both audio and text in training. The proposed text-only model (row 5) uses only text data and random Gaussian noise with a std of 0.015. It achieves comparable performance with the best audio cap- tioning models in the literature and obtains a SPIDEr score of

**Caveat-oriented passage (PDF p. 2)**

where γ denotes the model’s trainable parameters, contained only within the mapping network m (Figure 1). We use a model based on prefix-tuning architecture [7, 8]. However, in principle, the text-only training can be applied to any encoder- decoder AAC model. The text encoder and GPT2 are frozen.

## 123. Mandarin Lombard Flavor Classification

ID: `2309.07419` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2309.07419

Snapshot SHA-256: `e84de4bfac0f292a8a08b7ee4d2b1c46ea9495271b2abc22e79e1719475e4d70`

Abstract extract: The Lombard effect refers to individuals' unconscious modulation of vocal effort in response to variations in the ambient noise levels, intending to enhance speech intelligibility. The impact of different decibel levels and types of background noise on Lombard effects remains unclear. Building upon the characteristic of Lombard speech that individuals adjust their speech to improve intelligibility dynamically based on the self-feedback speech, we propose a flavor classification approach for the Lombard effect. We first collected Mandarin Lombard speech under different noise conditions, then simulated self-feedback speech, and ultimately conducted the statistical test on the word correct rate

**Method-oriented passage (PDF p. 2)**

distinct Lombard effect styles. Further, Hansen et al. first proposed that the Lombard effect has a different style [5]. They used a Gaussian Mix- ture Model (GMM) trained with 19 female speakers’ speech to classify 3-s duration Lombard utterances’ noise level (from 65 to 90dB SPL, 5 dB increments) and noise type (car noise, large crowd noise, and pink noise). The classification perfor- mance is significantly different from random. Thus, they sug- gested that Lombard speech exists distinct flavors responding to varying noise levels and types. Although Hansen proposed that the Lombard effect under different background noise types belong to dif

**Results-oriented passage (PDF p. 3)**

Table 1. Results of the classification of Lombard flavor over SSN levels. The ”t” columns represent the statistical test results between two noise conditions. Symbols: increase ↑, decrease ↓. ∗indicates a significant difference (p-value<0.001).

**Caveat-oriented passage (PDF p. 4)**

A total of 10 speakers (balanced by gender) were recruited to participate in creating the dataset, each recording Lombard speech across 11 distinct noise levels and 2 noise types. In each noise condition, the speakers recorded 20 sentences, re- sulting in a total of 4400 recorded sentences. The results for Lombard flavor classification over deci- b

## 124. Multilingual Audio Captioning using machine translated data

ID: `2309.07615` | Theme: Captioning/grounding | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2309.07615

Snapshot SHA-256: `097a08778a543737547a9805a55e2332e00d3b5e2608a091965c07ba298eea01`

Abstract extract: Automated Audio Captioning (AAC) systems attempt to generate a natural language sentence, a caption, that describes the content of an audio recording, in terms of sound events. Existing datasets provide audio-caption pairs, with captions written in English only. In this work, we explore multilingual AAC, using machine translated captions. We translated automatically two prominent AAC datasets, AudioCaps and Clotho, from English to French, German and Spanish. We trained and evaluated monolingual systems in the four languages, on AudioCaps and Clotho. In all cases, the models achieved similar performance, about 75% CIDEr on AudioCaps and 43% on Clotho. In French, we acquired manual captions of

**Method-oriented passage (PDF p. 3)**

To train our systems, we used the same hyperparameters as in our previous work [4]. The models were trained for 100 epochs on AC and 400 on CL, with the AdamW opti- mizer [16], a 5·10−4 learning rate, a large weight decay value of 2 and a cosine learning rate decay. We used Mixup [17] ap- plied to the audio and word embeddings, label smoothing [18] and SpecAugment [19]. For the multilingual systems, a train- ing epoch consists in using each audio file four times, in order to train the models in the four languages. At inference time, we used a beam search algorithm modified to prevent the models from repeating a same word twice in a caption, e

**Results-oriented passage (PDF p. 1)**

Automated Audio Captioning (AAC) systems attempt to gen- erate a natural language sentence, a caption, that describes the content of an audio recording, in terms of sound events. Exist- ing datasets provide audio-caption pairs, with captions written in English only. In this work, we explore multilingual AAC, using machine translated captions. We translated automati- cally two prominent AAC datasets, AudioCaps and Clotho, from English to French, German and Spanish. We trained and evaluated monolingual systems in the four languages, on AudioCaps and Clotho. In all cases, the models achieved sim- ilar performance, about 75% CIDEr on AudioCaps an

**Caveat-oriented passage (PDF p. 2)**

vided into three splits used respectively for training, valida- tion and testing, containing five captions per audio file. In our experiments, we resampled the audio files from 44.1 kHz to 32 kHz. During training, we randomly select one of five captions for each audio file. Machine translated versions. AC and CL contain English-only captions. In or

## 125. PromptTTS++: Controlling Speaker Identity in Prompt-Based Text-to-Speech Using Natural Language Descriptions

ID: `2309.08140` | Theme: Speech/audio generation and control | Status: `selected_fulltext_review_plus_scoped_core_crosscheck`

Source: https://arxiv.org/pdf/2309.08140

Snapshot SHA-256: `ab12800825634bcaf87ad7a75998f064f48367708ccaad2280db249210fc5c5c`

Abstract extract: We propose PromptTTS++, a prompt-based text-to-speech (TTS) synthesis system that allows control over speaker identity using natural language descriptions. To control speaker identity within the prompt-based TTS framework, we introduce the concept of speaker prompt, which describes voice characteristics (e.g., gender-neutral, young, old, and muffled) designed to be approximately independent of speaking style. Since there is no large-scale dataset containing speaker prompts, we first construct a dataset based on the LibriTTS-R corpus with manually annotated speaker prompts. We then employ a diffusion-based acoustic model with mixture density networks to model diverse speaker factors in the tr

**Method-oriented passage (PDF p. 1)**

We propose PromptTTS++, a prompt-based text-to-speech (TTS) synthesis system that allows control over speaker identity us- ing natural language descriptions. To control speaker identity within the prompt-based TTS framework, we introduce the con- cept of speaker prompt, which describes voice characteristics (e.g., gender-neutral, young, old, and muffled) designed to be approxi- mately independent of speaking style. Since there is no large-scale dataset containing speaker prompts, we first construct a dataset based on the LibriTTS-R corpus with manually annotated speaker prompts. We then employ a diffusion-based acoustic model with mixture den

**Results-oriented passage (PDF p. 4)**

Table 2 shows the subjective evaluation results. In terms of natu- ralness, all the proposed methods significantly outperformed the baseline system (B1). Among the proposed prompt-based TTS systems, the models without MDN worked better than the others (P1 vs. P3 and P2 vs. P4). This result can be attributed to the fact that human raters preferred the averaged voice characteristics gen- erated by the non-MDN models, likely due to the inability to cap- ture various speaker characteristics without using MDN. Note that the non-MDN models do not have the sampling capability. As for prompt-to-speech consistency, the proposed method (P1) achieved th

**Caveat-oriented passage (PDF p. 2)**

1Following GST [11], we use the term style embedding for the rest of this paper. However, note that the learned embeddings will reveal not only the style factors but also speaker factors.

Additional interpretation and limitations: [core findings](CORE_FINDINGS.md).

## 126. Audio Difference Learning for Audio Captioning

ID: `2309.08141` | Theme: Captioning/grounding | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2309.08141

Snapshot SHA-256: `12c75bd959e6fac3a32e160f22e19577f6cbb7f013850eef766964a922ab9555`

Abstract extract: This study introduces a novel training paradigm, audio difference learning, for improving audio captioning. The fundamental concept of the proposed learning method is to create a feature representation space that preserves the relationship between audio, enabling the generation of captions that detail intricate audio information. This method employs a reference audio along with the input audio, both of which are transformed into feature representations via a shared encoder. Captions are then generated from these differential features to describe their differences. Furthermore, a unique technique is proposed that involves mixing the input audio with additional audio, and using the additional 

**Method-oriented passage (PDF p. 2)**

In this paper, we propose audio difference learning which uti- lizes an additional reference audio input Xref ∈RT ×F . The proposed method is trained to describe the difference between the input Xinput and the reference Xref, allowing for the con- struction of a captioning system that takes into account subtle differences by learning the differences between audios. The key aspect of our method is to construct a network that can perform semantic transformations of audio content in the feature space by training a model based on differences in the representations. The structure is shown in Figure 1-(b). We start by encoding Xref into a reference

**Results-oriented passage (PDF p. 4)**

Table 1. Experimental results of the general audio captioning task setting: The proposed method employed the reference audio only during the training phase, and it was not used during the evaluation. These results highlight the impact of our proposed audio difference learning on the general audio captioning.

**Caveat-oriented passage (PDF p. 3)**

and we obtain ˆydiff which is a caption of the difference be- tween the input and the reference audio. The challenge here lies in the difficulty of obtaining ground truth labels of ydiff to calculate the cross-entropy loss,

## 127. Synth-AC: Enhancing Audio Captioning with Synthetic Supervision

ID: `2309.09705` | Theme: Loop/data selection | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2309.09705

Snapshot SHA-256: `1b8bae89dd018741d64d8fb34321b302a42d8af51671d3e21daa8aea58199bd9`

Abstract extract: Data-driven approaches hold promise for audio captioning. However, the development of audio captioning methods can be biased due to the limited availability and quality of text-audio data. This paper proposes a SynthAC framework, which leverages recent advances in audio generative models and commonly available text corpus to create synthetic text-audio pairs, thereby enhancing text-audio representation. Specifically, the text-to-audio generation model, i.e., AudioLDM, is used to generate synthetic audio signals with captions from an image captioning dataset. Our SynthAC expands the availability of well-annotated captions from the text-vision domain to audio captioning, thus enhancing text-au

**Method-oriented passage (PDF p. 1)**

To address the data scarcity issue of audio captioning, efforts have been made to directly increase the number of text-audio pairs by using external datasets [6–8]. For ex- ample, NetEase adopted a large-scale additional training dataset and significantly improved audio captioning perfor- mance [6]. However, such large-scale curated datasets are generally non-public, barring their use in research and real- world applications. Recently, the large language model, e.g., ChatGPT1, has been utilised to generate pseudo captions for audio datasets [7, 8]. In [7], a novel audio captioning dataset, i.e., WavCaps, was created by utilising ChatGPT to co

**Results-oriented passage (PDF p. 4)**

We evaluate the proposed SynthAC (i.e., Synth-P-Transformer) by using different amounts of ground truth data for model training, i.e. 12.5%, 25%, 37.5% and 50% of AudioCaps dataset, respectively. We also compare the performance of the model, trained with and without synthetic data. The results are shown in Table 4. Table 4 shows that the proposed SythnAC can signifi- cantly improve the captioning performance across the differ- ent amounts of ground truth data used for model training, es- pecially with a very limited amount of data, i.e., 12.5% of ground truth. With the enhanced text-audio relation by adopt-

**Caveat-oriented passage (PDF p. 4)**

ing our proposed SynthAC framework, Synth-P-Transformer outperforms the GPT-Similar with the complete training data in Table 2. In addition, the Synth-P-Transformer using only 37.5% ground truth data has better captioning performance than the P-Transformer with the complete training data in Ta- ble 2. The results further demonstrate the effectivene

## 128. RECAP: Retrieval-Augmented Audio Captioning

ID: `2309.09836` | Theme: Captioning/grounding | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2309.09836

Snapshot SHA-256: `26208edbbb5c05dd1cab87e387cc71aa7162a642f236843442d8779245cc12dc`

Abstract extract: We present RECAP (REtrieval-Augmented Audio CAPtioning), a novel and effective audio captioning system that generates captions conditioned on an input audio and other captions similar to the audio retrieved from a datastore. Additionally, our proposed method can transfer to any domain without the need for any additional fine-tuning. To generate a caption for an audio sample, we leverage an audio-text model CLAP to retrieve captions similar to it from a replaceable datastore, which are then used to construct a prompt. Next, we feed this prompt to a GPT-2 decoder and introduce cross-attention layers between the CLAP encoder and GPT-2 to condition the audio for caption generation. Experiments o

**Method-oriented passage (PDF p. 2)**

shared latent space. Thus, CLAP hidden state representations are better suited for captioning due to their enhanced linguis- tic comprehension. (2) We condition the audio for caption generation by introducing new cross-attention layers between CLAP and the GPT-2. (3) Finally, beyond just conditioning audio, we also condition a custom-constructed prompt for training and inference. We construct the prompt using the top-k captions most similar to the audio from a datastore re- trieved using CLAP. We provide more details in Section 3.1. RECAP builds on retrieval-augmented generation (RAG) [8], which offers multiple advantages discussed further in

**Results-oriented passage (PDF p. 4)**

Results. Table 1 and Table 2 compare the performance of RE- CAP against all our baselines evaluated on Clotho and Audio- Caps, respectively. We train our models in different settings and evaluate them with different datastores. While RECAP shows decent margins of improvement in in-domain settings, RECAP outperforms all baselines by a significant margin in out-of-domain settings when an in-domain datastore is avail- able. Without one, RECAP shows competitive performance with SOTA [6]. The presence of a larger data store (DSlarge) almost always improves performance. This opens possibil- ities to improve captioning performance by augmenting the 

**Caveat-oriented passage (PDF p. 2)**

Automated Audio Captioning. Current work in audio cap- tioning primarily employs encoder-decoder models where a caption is generated by an autoregressive language decoder conditioned on representations obtained from an audio en- coder [5, 6, 7]. The language decoder employed is either pre- trained on web-scale data [5, 6, 7] or learned from scratch

## 129. VoiceLDM: Text-to-Speech with Environmental Context

ID: `2309.13664` | Theme: Speech/audio generation and control | Status: `selected_fulltext_review_plus_scoped_core_crosscheck`

Source: https://arxiv.org/pdf/2309.13664

Snapshot SHA-256: `d4838b72877d9453589bcb6e1a2c774e8a566e0b2a1a074200ba49e63ed2b670`

Abstract extract: This paper presents VoiceLDM, a model designed to produce audio that accurately follows two distinct natural language text prompts: the description prompt and the content prompt. The former provides information about the overall environmental context of the audio, while the latter conveys the linguistic content. To achieve this, we adopt a text-to-audio (TTA) model based on latent diffusion models and extend its functionality to incorporate an additional content prompt as a conditional input. By utilizing pretrained contrastive language-audio pretraining (CLAP) and Whisper, VoiceLDM is trained on large amounts of real-world audio without manual annotations or transcriptions. Additionally, we

**Method-oriented passage (PDF p. 2)**

conditions cdesc and ccont and the timestep embedding to predict the diffusion score ϵθ. Starting from a random noise sampled from an isotropic Gaus- sian distribution zT ∼N(0, I), the reverse diffusion process itera- tively denoises zt for each time step t with the predicted diffusion score ϵθ and predicts the initial audio prior z0. z0 can then be de- coded back to the corresponding mel-spectrogram by the pre-trained variational autoencoder (VAE). Finally, the pre-trained HiFi-GAN vocoder [17] converts the mel-spectrogram into desired audio X.

**Results-oriented passage (PDF p. 3)**

We evaluate the performance of VoiceLDM on the AudioCaps [28] test set. Segments containing English speech are collected and the corresponding transcriptions are generated as described in Section 3.1. We denote the original test set as ac-full and the pro- cessed test set as ac-filtered. We use the captions from AudioSet as textdesc and the generated transcriptions as textcont. We use wdesc = 7, wcont = 7 for dual classifier-free guidance. We also substitute textdesc with the ground truth audio for the descriptive condition, and denote the experiment setting as VoiceLDM-Maudio. For objective evaluation, we additionally compare VoiceLDM with a

**Caveat-oriented passage (PDF p. 2)**

The training procedure of VoiceLDM mostly follows the latent dif- fusion model training procedure as done in [1, 18, 19]. However, the main difference is that the diffusion model utilizes two conditions. Starting from an audio X, the pre-trained VAE compresses the au- dio into the latent representation z0. A noisy representation of z0 at a certain 

Additional interpretation and limitations: [core findings](CORE_FINDINGS.md).

## 130. Active Learning Based Fine-Tuning Framework for Speech Emotion Recognition

ID: `2310.00283` | Theme: Loop/data selection | Status: `excluded_after_screening`

Source: https://arxiv.org/pdf/2310.00283

Snapshot SHA-256: `3a1c5455ecc113ed79da154dd38ce8d2fdcab6af718a6fcef35cdc49a8474449`

Excluded: Earlier conference AFTER framework; count extended 2405.00307 once

Abstract extract: Speech emotion recognition (SER) has drawn increasing attention for its applications in human-machine interaction. However, existing SER methods ignore the information gap between the pre-training speech recognition task and the downstream SER task, leading to sub-optimal performance. Moreover, they require much time to fine-tune on each specific speech dataset, restricting their effectiveness in real-world scenes with large-scale noisy data. To address these issues, we propose an active learning (AL) based Fine-Tuning framework for SER that leverages task adaptation pre-training (TAPT) and AL methods to enhance performance and efficiency. Specifically, we first use TAPT to minimize the info

**Method-oriented passage (PDF p. 2)**

world scenes. Specifically, we first propose an unsupervised task adaptation pre-training (TAPT) method [28] to reduce the information gap between the pre-trained and downstream SER task, where the pre-trained model can understand the semantic information of the SER task. Then, we created a large-scale heterogeneous and noisy dataset to simulate real- world scenes. Furthermore, we propose AL strategies with clustering-based initialization to iteratively select a smaller, more informative, and diverse subset of samples for fine- tuning, which can efficiently eliminate noise and outliers, improve generalization, and reduce the time-consuming. E

**Results-oriented passage (PDF p. 4)**

We first evaluated the performance of all baselines using the widely used benchmark dataset, IEMOCAP [23]. IEMOCAP is a multimodal database commonly employed for evaluat- ing SER performance. There are five conversation sessions in IEMOCAP, each with a female and a male actor attempt- ing to act in improvised and scripted scenarios. It consists of 10,039 speech utterances, with all audio signals sampled at 16kHz with a 16 bits resolution. To ensure a fair com- parison with previous works, we merge the “excited” class into the “happy” class, resulting in four considered emotions: neutral, happy, angry, and sad. Following Chen et al. [29], we a

**Caveat-oriented passage (PDF p. 2)**

Although Pseudo-TAPT [29] also adopts TAPT, they spent much time using K-means to extract frame-level emo- tional pseudo labels and continually pre-train their model in a supervised manner. However, K-means is sensitive to the initial value and outliers [32], making Pseudo-TAPT unstable and computationally expensive.

## 131. UniAudio: An Audio Foundation Model Toward Universal Audio Generation

ID: `2310.00704` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2310.00704

Snapshot SHA-256: `33b049a107912460d1755a4fe79b8d496f7e7530aa9a85066084ba5c8d1b4b63`

Abstract extract: Large Language models (LLM) have demonstrated the capability to handle a variety of generative tasks. This paper presents the UniAudio system, which, unlike prior task-specific approaches, leverages LLM techniques to generate multiple types of audio (including speech, sounds, music, and singing) with given input conditions. UniAudio 1) first tokenizes all types of target audio along with other condition modalities, 2) concatenates source-target pair as a single sequence, and 3) performs next-token prediction using LLM. Also, a multi-scale Transformer model is proposed to handle the overly long sequences caused by the residual vector quantization based neural codec in tokenization. Training o

**Method-oriented passage (PDF p. 2)**

Toward universal audio generation, this work presents UniAudio, which adopts LLM techniques and is able to generate multiple types of audio (speech, sounds, music, and singing) conditioned on various input modalities, such as phoneme sequences, textual descriptions, and audio itself. The proposed UniAudio is mainly featured as follows: First, all types of audio, along with all other input modalities, are tokenized as discrete sequences. Specifically, a universal neural codec model is built to effectively tokenize audio regardless of the audio type, and other tokenizers are used to tokenize other different modalites. Then, UniAudio concatenate

**Results-oriented passage (PDF p. 6)**

This section presents the overall evaluation results of the proposed UniAudio model over all 7 audio generation tasks during the training stage. A comprehensive comparison is conducted between UniAuduio and multiple prior works on each task, including not only the LM-based methods but also the diffusion model-based methods as well as other conventional audio generation methods. The detailed comparison is presented in Appendix B. We selected one of the most advanced prior work in each task and present the results in Table 2.

**Caveat-oriented passage (PDF p. 2)**

2 UNIAUDIO This section introduces the technical details of the proposed UniAudio. Section 2.1 explains how audio and other modalities are tokenized. Then, all considered audio generation tasks are uniformly formulated in Section 2.2. Subsequently, the multi-scale Transformer architecture is proposed in Section 2.3 to handle the overly long sequenc

## 132. Prosody Analysis of Audiobooks

ID: `2310.06930` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2310.06930

Snapshot SHA-256: `af864e4cbccaf4c5ec2b244bd864e427eaff77b585c6c6450d41d8eeab88a93a`

Abstract extract: Recent advances in text-to-speech have made it possible to generate natural-sounding audio from text. However, audiobook narrations involve dramatic vocalizations and intonations by the reader, with greater reliance on emotions, dialogues, and descriptions in the narrative. Using our dataset of 93 aligned book-audiobook pairs, we present improved models for prosody prediction properties (pitch, volume, and rate of speech) from narrative text using language modeling. Our predicted prosody attributes correlate much better with human audiobook readings than results from a state-of-the-art commercial TTS system: our predicted pitch shows a higher correlation with human reading for 22 out of the 

**Method-oriented passage (PDF p. 3)**

A. Text Input Representations We experiment with three input embeddings: TF-IDF rep- resentations, Mean-pooled GloVe embeddings computed from the CommonCrawl pre-trained GloVe model (840B tokens), and MPNet embeddings [19] (all-mpnet-base-v2). We compute a single value for each prosody attribute per text segment, and compute the z-scores across all segments in the chapter. We use a train-test split of 75-25% across books, i.e. we use 69 books (1,392 chapters) in the training set and 24 books (414 chapters) in the test set. All the models are trained on a 2GHz CPU.

**Results-oriented passage (PDF p. 4)**

To include more subtle information about the nature of individual characters (e.g. hero vs. villain, old vs. young) that may inform actors’ readings, we appended 908-dimensional character embeddings [12] to the input text representation and applied PCA for dimension reduction. Table IV shows the MSE on plain audio generated without SSML attributes (baseline) and enhanced audio generated with SSML attributes predicted from text and character embeddings. Appending character embeddings to the input results in improvements over the baseline, but not over our best models.

**Caveat-oriented passage (PDF p. 1)**

Audio books are actor-narrated recordings of written texts, typically full length novels. Audio books have grown rapidly in popularity in recent years, with annual sales in the United States reaching $1.3 billion dollars in 2020.1. The National Library Service for the Blind has recorded tens of thousands of talking books for the sight impaired sinc

## 133. SALMONN: Towards Generic Hearing Abilities for Large Language Models

ID: `2310.13289` | Theme: Captioning/grounding | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2310.13289

Snapshot SHA-256: `3b8e3381c203f4c0dd282b7bc03774328ace13c10d0a09ca22842878f6089cd6`

Abstract extract: Hearing is arguably an essential ability of artificial intelligence (AI) agents in the physical world, which refers to the perception and understanding of general auditory information consisting of at least three types of sounds: speech, audio events, and music. In this paper, we propose SALMONN, a speech audio language music open neural network, built by integrating a pre-trained text-based large language model (LLM) with speech and audio encoders into a single multimodal model. SALMONN enables the LLM to directly process and understand general audio inputs and achieve competitive performances on a number of speech and audio tasks used in training, such as automatic speech recognition and t

**Method-oriented passage (PDF p. 2)**

window-level query Transformer (Q-Former) (Li et al., 2023a) is used as the connection module to convert a variable-length encoder output sequence to a variable number of augmented audio tokens input to the Vicuna LLM (Chiang et al., 2023) and can achieve audio-text alignment with high tem- poral resolution. The low-rank adaptation (LoRA) approach (Hu et al., 2022) is applied to Vicuna as a cross-modal adaptor to align Vicuna’s augmented input space with its output space and further improve its performance. A number of speech, audio, and music tasks are used in the cross-modal pre-training and instruction tuning stages of the window-level Q-F

**Results-oriented passage (PDF p. 8)**

Table 3: Results of all 15 tasks produced by SALMONN without & with activation tuning (w/o & w/ Activation). The ASR results are presented in a tuple with three the %WERs evaluated on 3 test sets, namely (LibriSpeech test-clean, LibriSpeech test-other, GigaSpeech).

**Caveat-oriented passage (PDF p. 4)**

Task Over-fitting: Although SALMONN built with only the first two stages of training can produce competitive results on the tasks trained in instruction tuning, it exhibits limited or almost no ability to perform untrained cross-modal tasks, especially the tasks that require cross-modal co-reasoning abilities. In particular, the model sometimes vio

## 134. Style Description based Text-to-Speech with Conditional Prosodic Layer Normalization based Diffusion GAN

ID: `2310.18169` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2310.18169

Snapshot SHA-256: `aefeef0602d02f03a2aa6d6e87a57ee8b8b846aa6d4e55e511dd020a0037e393`

Abstract extract: In this paper, we present a Diffusion GAN based approach (Prosodic Diff-TTS) to generate the corresponding high-fidelity speech based on the style description and content text as an input to generate speech samples within only 4 denoising steps. It leverages the novel conditional prosodic layer normalization to incorporate the style embeddings into the multi head attention based phoneme encoder and mel spectrogram decoder based generator architecture to generate the speech. The style embedding is generated by fine tuning the pretrained BERT model on auxiliary tasks such as pitch, speaking speed, emotion,gender classifications. We demonstrate the efficacy of our proposed architecture on multi

**Method-oriented passage (PDF p. 2)**

vocoder [17] to produce time-domain waveforms. The generator architecture uses the phoneme encoder, conditional style layer normalization framework, variance adaptor, mel-spectrogram de- coder along with denoiser conditioned on style token, timesteps and noisy melspectrogram to generate mel-spectrogram features x0. The phoneme encoder and mel-spectrogram decoder is based on a multi-head self-attention network, and position feed- forward network which consists of two Conv1D and normaliza- tion stages. The proposed method stacks multiple multi-head self-attention[13] blocks with phoneme embedding and position encoding as an input at the encoder

**Results-oriented passage (PDF p. 4)**

Twenty samples of speakers are taken for PromptSpeech and LibriTTS test set are used to perform MOS [25] to evaluate the generated samples in terms of naturalness(how the synthesized voices sound natural like human), similarity(how the synthesized voices sound with respect to the input style description).We compare the MOS of audio samples including: (1) GT, the ground-truth recordings; (2) GT mel + HiFiGAN, where we first convert ground-truth speech into mel-spectrogram, and then convert the mel-spectrogram back to speech using HiFiGAN [17]; (3) PromptTTS; (4) Prosodic Diff-TTS. Both systems in (3) and (4) use HiFiGAN as vocoder. According t

**Caveat-oriented passage (PDF p. 1)**

In this paper, we present a Diffusion GAN based approach (Prosodic Diff-TTS) to generate the corresponding high-fidelity speech based on the style description and content text as an input to generate speech samples within only 4 denoising steps. It leverages the novel conditional prosodic layer normalization to incorporate the style embeddings into

## 135. Qwen-Audio: Advancing Universal Audio Understanding via Unified Large-Scale Audio-Language Models

ID: `2311.07919` | Theme: Captioning/grounding | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2311.07919

Snapshot SHA-256: `ec2582e1767927a67bc68db1fa9324c3a7839b8d2efa348ac6c76c57f5b44fae`

Abstract extract: Recently, instruction-following audio-language models have received broad attention for audio interaction with humans. However, the absence of pre-trained audio models capable of handling diverse audio types and tasks has hindered progress in this field. Consequently, most existing works have only been able to support a limited range of interaction capabilities. In this paper, we develop the Qwen-Audio model and address this limitation by scaling up audio-language pre-training to cover over 30 tasks and various audio types, such as human speech, natural sounds, music, and songs, to facilitate universal audio understanding abilities. However, directly co-training all tasks and datasets can le

**Method-oriented passage (PDF p. 2)**

To promote the growth and development of the audio-text multimodal community, we introduce Qwen-Audio, a large-scale audio-language model. Qwen-Audio is a multi-task language model conditioning on audio and text inputs, that extends the Qwen-7B (Bai et al., 2023a) language model to effectively perceive audio signals by the connection of a single audio encoder. Different from previous works that primarily cater to a single type of audio such as human speech, or focus on specific tasks like speech recognition and captioning, or limit models to a single language (Wang et al., 2023a; Lyu et al., 2023; Wu et al., 2023b; Gong et al., 2023b; Shu et 

**Results-oriented passage (PDF p. 11)**

Speech Recognition (ASR) results, as depicted in Table 3, where Qwen-Audio exhibits superior perfor- mance compared to previous multi-task learning models. Specifically, it achieves a 2.0% and 4.2% WER on the librispeech test-clean and test-other datasets, respectively. Similarly, the Chinese Mandarin ASR results demonstrate Qwen-Audio’s competitive performance against previous approaches. To the best of our knowledge, Qwen-Audio achieves state-of-the-art results on the Aishell1 dev and test sets. Furthermore, we evaluate Qwen-Audio’s speech translation performance on the CoVoST2 dataset. The results reveal that Qwen-Audio outperforms the bas

**Caveat-oriented passage (PDF p. 1)**

Recently, instruction-following audio-language models have received broad attention for audio interaction with humans. However, the absence of pre-trained audio models capable of handling diverse audio types and tasks has hindered progress in this field. Consequently, most existing works have only been able to support a limited range of inter- acti

## 136. Zero-shot audio captioning with audio-language model guidance and audio context keywords

ID: `2311.08396` | Theme: Captioning/grounding | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2311.08396

Snapshot SHA-256: `1a0f7da4a537998cfcd40464dffcec1422f5f07c4c6af4dcdb41027245a7a086`

Abstract extract: Zero-shot audio captioning aims at automatically generating descriptive textual captions for audio content without prior training for this task. Different from speech recognition which translates audio content that contains spoken language into text, audio captioning is commonly concerned with ambient sounds, or sounds produced by a human performing an action. Inspired by zero-shot image captioning methods, we propose ZerAuCap, a novel framework for summarising such general audio signals in a text caption without requiring task-specific training. In particular, our framework exploits a pre-trained large language model (LLM) for generating the text which is guided by a pre-trained audio-langu

**Method-oriented passage (PDF p. 2)**

Zero-shot captioning. Recently, several zero-shot image captioning methods were proposed [34, 36, 35, 44, 38] which use CLIP [30] to guide text generation with an LLM. A first line of work optimizes hidden activations in the language model to adapt the predicted tokens towards the captioning target [36, 35]. In contrast, our approach avoids this costly step and directly chooses the next token based on a fitness function. A second line of work chooses the next token by introducing guidance in the decoding process [44, 34]. [44] conditions the LLM on CLIP-detected class names and then ranks multiple sampled captions based on CLIP similarity, wh

**Results-oriented passage (PDF p. 4)**

Quantitative results. We present quantitative results for zero-shot audio captioning in Table 1. ZerAuCap outperforms [32] by a wide margin on most metrics, setting a new state of the art on AudioCaps [15]. Additionally, it outperforms our baseline that does not have access to any audio input on both datasets. As randomly generated texts already might have some overlap with the ground-truth captions, our baseline yields non-zero scores. Interestingly, on AudioCaps the baseline significantly outperforms the recently proposed zero-shot audio captioning model [32] in terms of the ROUGE-L score. Our model always outperforms the baseline and [32] 

**Caveat-oriented passage (PDF p. 1)**

Concurrently to our work, [32] introduced the zero-shot audio captioning task which tackles the aforementioned challenges and limitations. Their proposed approach seeks to generate textual descriptions for audio content by using guidance through an audio-text matching score that determines if the generated caption describes audible content. They us

## 137. SPIRE-SIES: A Spontaneous Indian English Speech Corpus

ID: `2312.00698` | Theme: Data/Indic speech | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2312.00698

Snapshot SHA-256: `684a41d2bc8522090ccd549d385f5d39764d4fb600cf5b28aca410bb9417cbf3`

Abstract extract: In this paper, we present a 170.83 hour Indian English spontaneous speech dataset. Lack of Indian English speech data is one of the major hindrances in developing robust speech systems which are adapted to the Indian speech style. Moreover this scarcity is even more for spontaneous speech. This corpus is crowd sourced over varied Indian nativities, genders and age groups. Traditional spontaneous speech collection strategies involve capturing of speech during interviewing or conversations. In this study, we use images as stimuli to induce spontaneity in speech. Transcripts for 23 hours is generated and validated which can serve as a spontaneous speech ASR benchmark. Quality of the corpus is v

**Method-oriented passage (PDF p. 2)**

how English is spoken by different nativities [15], [16]. With our image-stimulated spontaneous speech collection strategy, where multiple speakers from varied nativities speak about a common set of images, variation of linguistic content within semantically correlated utterances from different Indian na- tivities is captured. This could be potentially used to improve the performance of Indian English ASR and Spontaneous TTS systems. Taking a step to meet the demand for Spontaneous Indian English Speech corpus, we are open-sourcing 170.83 hours of spontaneous speech data in the English language corpus, called SPIRE-SIES spoken by Indian nativ

**Results-oriented passage (PDF p. 3)**

As the data collection is crowd-sourced and recorded in an uncontrolled environment, multiple pre-processing steps were implemented to enhance the quality of the dataset. This section details the pre-processing steps used in the SPIRE-SIES corpus having a total of 37,895 samples collected over the span of three years from 2021 and 2023. Although the data collection process had 1000 images, recordings from 761 images were obtained. This could be because contributors skipped several images that were difficult to be described by them. The dataset was accompanied by a JSON metadata file con- taining essential speaker information such as ID, gende

**Caveat-oriented passage (PDF p. 5)**

The development and implementation of a specialized Spon- taneous English Indian ASR system, as discussed in the papers by Ramabhadran et al. [30] and Sharma et al. [31], yields significant benefits across diverse sectors. This system, trained on a comprehensive dataset of spontaneous Indian English speech, effectively addresses the challenges pose

## 138. OpenVoice: Versatile Instant Voice Cloning

ID: `2312.01479` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2312.01479

Snapshot SHA-256: `94b03cdacc4c83ef9ce00b30e3dda6ec128d21cd38818f4713e514cb9a937291`

Abstract extract: We introduce OpenVoice, a versatile voice cloning approach that requires only a short audio clip from the reference speaker to replicate their voice and generate speech in multiple languages. OpenVoice represents a significant advancement in addressing the following open challenges in the field: 1) Flexible Voice Style Control. OpenVoice enables granular control over voice styles, including emotion, accent, rhythm, pauses, and intonation, in addition to replicating the tone color of the reference speaker. The voice styles are not directly copied from and constrained by the style of the reference speaker. Previous approaches lacked the ability to flexibly manipulate voice styles after cloning

**Method-oriented passage (PDF p. 2)**

To address the first two problems, OpenVoice is designed to decouple the components in a voice as much as possible. The generation of language, tone color, and other important voice features are made independent of each other, enabling flexible manipulation over individual voice styles and language types. This is achieved without labeling any voice style in the MSML training set. We would like to clarify that the zero-shot cross-lingual task in this study is different from that in VALLE-X [18]. In VALLE-X, data for all languages need to be included in the MSML training set, and the model cannot generalize to an unseen language outside the MSM

**Results-oriented passage (PDF p. 5)**

The evaluation of voice cloning is hard to be objective for several reasons. First, different research studies (e.g., [8], [2]) usually have different training and test sets. The numerical comparison could be intrinsically unfair. Even their metrics such as Mean Opinion Score can be evaluated by crowd- sourcing, the diversity and difficulty of the test set would significantly influence the results. For example, if many samples in the test set are neural voices that concentrate on the mean of human voice distributions, then it is relatively easy for most methods to achieve good voice cloning results. Second, different studies usually have diff

**Caveat-oriented passage (PDF p. 6)**

optimized version of OpenVoice (including the base speaker model and the tone converter) is able achieve 12× real-time performance on a single A10G GPU, which means it only takes 85ms to generate a one second speech. Through detailed GPU usage analysis, we estimate that the upper bound is around 40× real-time, but we will leave this improvement as 

## 139. Audiobox: Unified Audio Generation with Natural Language Prompts

ID: `2312.15821` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2312.15821

Snapshot SHA-256: `201b3e4b8809f055f769b9ecad0dbdefb80be292fa25b99d907c1beb10f67a11`

Abstract extract: Audio is an essential part of our life, but creating it often requires expertise and is time-consuming. Research communities have made great progress over the past year advancing the performance of large scale audio generative models for a single modality (speech, sound, or music) through adopting more powerful generative models and scaling data. However, these models lack controllability in several aspects: speech generation models cannot synthesize novel styles based on text description and are limited on domain coverage such as outdoor environments; sound generation models only provide coarse-grained control based on descriptions like "a person speaking" and would only generate mumbling h

**Method-oriented passage (PDF p. 8)**

Following Le et al. (2023), we train a flow-matching duration model only with labeled data. It was shown in Le et al. (2023) that FM duration model has better diversity compared to regression duration models. However, it is less stable and sometimes produces unnatural prosody. To alleviate the issue, we propose to average over a small number of duration sequences for stabilization, which empirically shows better trade-off between diversity and quality. The averaging operation is reasonable as duration distributions are relatively unimodal. When averaging more samples, it approaches the mean, which is the estimation produced by regression mode

**Results-oriented passage (PDF p. 10)**

Audiobox Speech achieves a new best on style similarity (0.745 vs. 0.710 from UniAudio) on the audiobook domain test set (LS). More importantly, Audiobox Speech drastically improves Voicebox on all other domains, with similarity improvement ranging from 0.096 to 0.156. The results suggest that Audiobox Speech generalizes much better thanks to scaling data to cover more domains. The subjective evaluations presented in Table 2 again confirms that Audiobox Speech transfers styles significantly better than the baselines, and generate audio with better quality.

**Caveat-oriented passage (PDF p. 2)**

Limitation of existing models: Existing audio generative models are still limited in controllability and generalizability. First, the real world audio content often contain a mix of speech, music, and sound effects. However, existing audio generative models are mostly modality-specific, which only generate either speech, music, or sound effects. In

## 140. End to end Hindi to English speech conversion using Bark, mBART and a finetuned XLSR Wav2Vec2

ID: `2401.06183` | Theme: Speech/audio generation and control | Status: `excluded_after_screening`

Source: https://arxiv.org/pdf/2401.06183

Snapshot SHA-256: `11944138347cd86e2314eb180e1ed98ec52ad019eadf89cf0dffc9d0a2b181aa`

Excluded: Hindi-to-English translation application; weak fit to the requested caption/control task

Abstract extract: Speech has long been a barrier to effective communication and connection, persisting as a challenge in our increasingly interconnected world. This research paper introduces a transformative solution to this persistent obstacle an end-to-end speech conversion framework tailored for Hindi-to-English translation, culminating in the synthesis of English audio. By integrating cutting-edge technologies such as XLSR Wav2Vec2 for automatic speech recognition (ASR), mBART for neural machine translation (NMT), and a Text-to-Speech (TTS) synthesis component, this framework offers a unified and seamless approach to cross-lingual communication. We delve into the intricate details of each component, eluci

**Method-oriented passage (PDF p. 2)**

The Common Voice corpus[13] stands as an extensive and remarkably diverse repository of transcribed speech, featuring an impressive collection of 19,160 validated hours across 114 languages. Each dataset entry comprises a distinctive MP3 audio file along with its corresponding text transcript. Additionally, the resource includes valuable demographic metadata, encompassing details such as age, gender, and accent, in a substantial portion of the 28,751 recorded hours. This supplementary metadata proves invaluable for augmenting the accuracy of speech recognition systems. Despite its vast size and inclusivity, the Common Voice corpus poses chall

**Results-oriented passage (PDF p. 1)**

Speech has long been a barrier to effective communication and connection, persisting as a challenge in our increasingly interconnected world. This research paper introduces a transformative solution to this persistent obstacle – an end-to-end speech conversion framework tailored for Hindi-to-English translation, culminating in the synthesis of English audio. By integrating cutting-edge technologies such as XLSR Wav2Vec2 for automatic speech recognition (ASR), mBART for neural machine translation (NMT), and a Text-to-Speech (TTS) synthesis component, this framework offers a unified and seamless approach to cross-lingual communication. We delve

**Caveat-oriented passage (PDF p. 3)**

Bark, developed by Suno, is an innovative text-to-audio model that utilizes transformer-based technology to produce natural-sounding speech in multiple languages. This advanced system is not limited to speech generation but can also create various types of audio content, including music, ambient sounds, and basic sound effects. Additionally, Bark h

## 141. On the Audio Hallucinations in Large Audio-Video Language Models

ID: `2401.09774` | Theme: Captioning/grounding | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2401.09774

Snapshot SHA-256: `79d30614ba372028786f113b344303c77cb38453dc671b6c0f3435d6ca528dda`

Abstract extract: Large audio-video language models can generate descriptions for both video and audio. However, they sometimes ignore audio content, producing audio descriptions solely reliant on visual information. This paper refers to this as audio hallucinations and analyzes them in large audio-video language models. We gather 1,000 sentences by inquiring about audio information and annotate them whether they contain hallucinations. If a sentence is hallucinated, we also categorize the type of hallucination. The results reveal that 332 sentences are hallucinated with distinct trends observed in nouns and verbs for each hallucination type. Based on this, we tackle a task of audio hallucination classificati

**Method-oriented passage (PDF p. 4)**

Table 1 shows the classification performance in the zero-shot and fine-tuning settings. When comparing our zero-shot ap- proach with the random baseline, our approach performs bet- ter than the random baseline by 10% in F1. LAION-CLAP achieves slightly better than MS-CLAP by 0.7%. In terms of the fine-tuning setting, both models outperform the zero-shot methods, indicating the possibility of training the classifier to detect audio hallucinations. When comparing back- bones, we observe that MS-CLAP outperforms LAION-CLAP by +11% in F1. The cause of this discrepancy is unclear, but a potential factor is attributed to the nature of the text data

**Results-oriented passage (PDF p. 1)**

are hallucinated. This paper focuses on analyzing the audio hallucinations of large-scale audio-video language models. The analysis com- prises four key processes. Firstly, we formulate prompts to in- quire about audio information and gather 1,000 responses from the Video LLAMA. Secondly, we manually annotate whether the sentences are hallucinated or not. Thirdly, we also anno- tate the hallucination type associated with the hallucinated sen- tences. Finally, we aggregate the annotation results, reveal- ing that 323 sentences were indeed hallucinated, with distinct trends observed in nouns and verbs for each hallucination type. It is notewort

**Caveat-oriented passage (PDF p. 2)**

The key limitation of audio captioning is that there exists indistinguishable sound only from the audio information, such as the sound of a working tractor and lawnmower. Video-audio captioning is one of the important topics in audio-visual learn- ing [18, 19, 20, 21, 22], aiming to generate the correct descrip- tions by fusing audio and visual inf

## 142. Empowering Communication: Speech Technology for Indian and Western Accents through AI-powered Speech Synthesis

ID: `2401.11771` | Theme: Speech/audio generation and control | Status: `excluded_after_screening`

Source: https://arxiv.org/pdf/2401.11771

Snapshot SHA-256: `30e14ed35db914ba4e8196b992e2d6e7d5fc1e3c40ea4d3daf1603bc5e10e424`

Excluded: Insufficient usable extracted body passages; do not count as a full-text excerpt review

Abstract extract: Neural Text-to-speech (TTS) synthesis is a powerful technology that can generate speech using neural networks. One of the most remarkable features of TTS synthesis is its capability to produce speech in the voice of different speakers. This paper introduces voice cloning and speech synthesis https://pypi.org/project/voice-cloning/ an open-source python package for helping speech disorders to communicate more effectively as well as for professionals seeking to integrate voice cloning or speech synthesis capabilities into their projects. This package aims to generate synthetic speech that sounds like the natural voice of an individual, but it does not replace the natural human voice. The archi

**Method-oriented passage (PDF p. 1)**



**Results-oriented passage (PDF p. 1)**



**Caveat-oriented passage (PDF p. 1)**



## 143. SpeechBERTScore: Reference-Aware Automatic Evaluation of Speech Generation Leveraging NLP Evaluation Metrics

ID: `2401.16812` | Theme: Evaluation/reliability | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2401.16812

Snapshot SHA-256: `e39b7627bc90169b643af7a9d4b97b9adb5146d6443862582711e2cf9e715717`

Abstract extract: While subjective assessments have been the gold standard for evaluating speech generation, there is a growing need for objective metrics that are highly correlated with human subjective judgments due to their cost efficiency. This paper proposes reference-aware automatic evaluation methods for speech generation inspired by evaluation metrics in natural language processing. The proposed SpeechBERTScore computes the BERTScore for self-supervised dense speech features of the generated and reference speech, which can have different sequential lengths. We also propose SpeechBLEU and SpeechTokenDistance, which are computed on speech discrete tokens. The evaluations on synthesized speech show that 

**Method-oriented passage (PDF p. 4)**

4. Conclusions In this paper, we proposed speech evaluation metrics based on objective text generation metrics, including SpeechBERTScore, SpeechBLEU and SpeechTokenDistance. Experimental eval- uations showed that SpeechBERTScore correlates better with human subjective ratings than traditional reference-aware met- rics and previous MOS prediction models. Our evaluations also suggested the cross-lingual applicability, indicating high practi- cal potential. Future work includes exploring a wider range of text generation metrics, such as MoverScore [11]. Acknowledgements: Part of this work was supported by JSPS KAKENHI Grant Number 23H03418, 23K

**Results-oriented passage (PDF p. 3)**

We first conducted evaluations on English synthetic speech as in § 3.1.2. For SpeechBERTScore, we used the wavlm-large model. We also used SpeechBLEU with no token repetition, 𝐾= 200 and the 𝐺= 2 setting, while we used SpeechTok- enDistance with token repetition and 𝐾= 200. Table 2 lists the results. Our metrics, SpeechBERTScore, SpeechBLEU, and SpeechTokenDistance (Jaro-Winkler), outperformed traditional reference-aware metrics in all criteria. They also showed higher correlations than the unsupervised SpeechLMScore and the su- pervised UTMOS. There was no overlap in the 95% confidence intervals between the proposed SpeechBERTScore and previ

**Caveat-oriented passage (PDF p. 2)**

We used three types of evaluation datasets, where the sampling rate was set to 16 kHz. We used the SOMOS dataset [27] for the evaluation of English synthesized speech. It contains LJSpeech [28] voices synthesized by 200 different text-to-speech (TTS) acoustic models and the LPCNet [29] vocoder, along with the corresponding ratings. Since our evalua

## 144. Natural language guidance of high-fidelity text-to-speech with synthetic annotations

ID: `2402.01912` | Theme: Speech/audio generation and control | Status: `selected_fulltext_review_plus_scoped_core_crosscheck`

Source: https://arxiv.org/pdf/2402.01912

Snapshot SHA-256: `4e396572b438e53fde290a44b58707e7e4fd762fcbed9e3de9c032f3e1a35753`

Abstract extract: Text-to-speech models trained on large-scale datasets have demonstrated impressive in-context learning capabilities and naturalness. However, control of speaker identity and style in these models typically requires conditioning on reference speech recordings, limiting creative applications. Alternatively, natural language prompting of speaker identity and style has demonstrated promising results and provides an intuitive method of control. However, reliance on human-labeled descriptions prevents scaling to large datasets. Our work bridges the gap between these two approaches. We propose a scalable method for labeling various aspects of speaker identity, style, and recording conditions. We th

**Method-oriented passage (PDF p. 1)**

Text-to-speech models trained on large-scale datasets have demonstrated impressive in-context learning capabilities and naturalness. However, control of speaker identity and style in these models typically requires conditioning on reference speech recordings, limiting creative applications. Alterna- tively, natural language prompting of speaker identity and style has demonstrated promising results and provides an intuitive method of control. However, reliance on human-labeled de- scriptions prevents scaling to large datasets. Our work bridges the gap between these two approaches. We propose a scalable method for labeling various aspects of sp

**Results-oriented passage (PDF p. 4)**

racy of 94%. In a similar fashion, we re-use our accent classifier (see Section 3.1.1) and classify the accents of our generated ac- cent test set. Here, we see a somewhat poorer accuracy of 68%. We hypothesize that this is likely to be due to noisy labeling and a very imbalanced distribution of accents in the training set. The remaining attributes that we labeled are continuous variables. For these variables, we run our generated test sets through the same models that were used to label the training set (see Section 3.1). The results can be seen in Figure 3. We see that for every attribute other than C50, the model performs fairly well at ge

**Caveat-oriented passage (PDF p. 2)**

The authors of [12] move away from computational label- ing methods and explore human annotation. They label 44 hours of data with natural language sentences describing style and emotion but rely on a fixed set of speaker IDs to control speaker likeness. Human annotation is used again in [13] (with an even smaller 6-hour dataset) in service of styl

Additional interpretation and limitations: [core findings](CORE_FINDINGS.md).

## 145. Careless Whisper: Speech-to-Text Hallucination Harms

ID: `2402.08021` | Theme: Captioning/grounding | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2402.08021

Snapshot SHA-256: `15533b4b52c54dcff85dd43ed2117516056006a500c8fcac854d3bb34326b304`

Abstract extract: Speech-to-text services aim to transcribe input audio as accurately as possible. They increasingly play a role in everyday life, for example in personal voice assistants or in customer-company interactions. We evaluate Open AI's Whisper, a state-of-the-art automated speech recognition service outperforming industry competitors, as of 2023. While many of Whisper's transcriptions were highly accurate, we find that roughly 1\% of audio transcriptions contained entire hallucinated phrases or sentences which did not exist in any form in the underlying audio. We thematically analyze the Whisper-hallucinated content, finding that 38\% of hallucinations include explicit harms such as perpetuating vi

**Method-oriented passage (PDF p. 3)**

1To protect patient privacy due to the small number of samples across non-white and non-African American race groups, we aggregate these patients into one category, yielding three racial categories in our sample (white, African American, other). 2Aphasia speakers not only speak slower, they also utter (on average) fewer ground truth words per segment: 12 words (aphasia) versus 16 words (control). In terms of segment duration, aphasia speakers average 15.5 seconds while control speakers average 7.8 seconds. Even if we restrict to segments with durations that fall within the overlap of minimum/maximum aphasia/control segments (i.e., removing in

**Results-oriented passage (PDF p. 6)**

Table 1. Examples of Whisper transcriptions with hallucinations that are not present in the underlying audio. Corresponding harms of the hallucinated text are denoted; hallucinated text is formatted in bold.

**Caveat-oriented passage (PDF p. 1)**

ALLISON KOENECKE, Cornell University, USA ANNA SEO GYEONG CHOI∗, Cornell University, USA KATELYN X. MEI∗, University of Washington, USA HILKE SCHELLMANN†, New York University, USA MONA SLOANE†, University of Virginia, USA

## 146. APCodec: A Neural Audio Codec with Parallel Amplitude and Phase Spectrum Encoding and Decoding

ID: `2402.10533` | Theme: Representations/codecs | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2402.10533

Snapshot SHA-256: `5160f74beb0bc11e38d824df030848fb861b32e847c95b1d5af14c1309f2226b`

Abstract extract: This paper introduces a novel neural audio codec targeting high waveform sampling rates and low bitrates named APCodec, which seamlessly integrates the strengths of parametric codecs and waveform codecs. The APCodec revolutionizes the process of audio encoding and decoding by concurrently handling the amplitude and phase spectra as audio parametric characteristics like parametric codecs. It is composed of an encoder and a decoder with the modified ConvNeXt v2 network as the backbone, connected by a quantizer based on the residual vector quantization (RVQ) mechanism. The encoder compresses the audio amplitude and phase spectra in parallel, amalgamating them into a continuous latent code at a 

**Method-oriented passage (PDF p. 6)**

To attain low-latency streamable inference, we implement modifications to specific components of the APCodec, cov- ering the following three aspects. 1) Unlike some well- known codecs like SoundStream [25] and Encodec [26] that employ causal convolutions, the streamable APCodec replaces all non-causal convolutional layers (excluding up- sampling/downsampling layers) with feed-forward layers. This approach is conducive to reducing model size and improving generation efficiency; 2) Replacing the original non-causal upsampling deconvolutional layers with causal ones; 3) Setting the kernel size of the downsampling convolutional layer to be smalle

**Results-oriented passage (PDF p. 8)**

First, we comprehensively evaluated the performance of these compared audio codecs using multiple objective metrics. These objective metrics were specifically designed to evaluate the amplitude spectrum quality, overall audio objective quality, intelligibility, phase spectrum quality, generation speed and model complexity, respectively.

**Caveat-oriented passage (PDF p. 2)**

The waveform codecs aim at encoding the input audio wave- form directly and reproducing a faithful reconstruction of the input audio waveform, such as pulse code modulation (PCM) [20]. Although waveform codecs can decode high-quality audio, they also require a higher bitrate, which increases storage and transmission costs. In recent times, end-to-e

## 147. IndicVoices: Towards building an Inclusive Multilingual Speech Dataset for Indian Languages

ID: `2403.01926` | Theme: Data/Indic speech | Status: `selected_fulltext_review_plus_scoped_core_crosscheck`

Source: https://arxiv.org/pdf/2403.01926

Snapshot SHA-256: `7b956d7148d4960018bc63f1172163af91300c683b7544e5088ece62088e953c`

Abstract extract: We present INDICVOICES, a dataset of natural and spontaneous speech containing a total of 7348 hours of read (9%), extempore (74%) and conversational (17%) audio from 16237 speakers covering 145 Indian districts and 22 languages. Of these 7348 hours, 1639 hours have already been transcribed, with a median of 73 hours per language. Through this paper, we share our journey of capturing the cultural, linguistic and demographic diversity of India to create a one-of-its-kind inclusive and representative dataset. More specifically, we share an open-source blueprint for data collection at scale comprising of standardised protocols, centralised tools, a repository of engaging questions, prompts and 

**Method-oriented passage (PDF p. 18)**

the desired distribution of age, gender, education levels, professions, etc. as outlined in section 2 (iii) the test set should have fair representation of speakers from every district and (iv) the test set should keep growing as more data gets collected in later phases of the project to allow for representation from newer districts, while adhering to conditions listed above. Creating such a balanced test set is challenging as it requires satisfying multiple demographic constraints simultaneously.

**Results-oriented passage (PDF p. 19)**

Evaluation: We train a multilingual 130M conformer based model (IndicASR) following the same architecture as proposed by [38], using only the INDICVOICES train set. We evaluate this model on the INDICVOICES test set and compare it with existing state of the art models. As seen in Table 7, IndicASR is the first model to support all the 22 languages and it outperforms all existing models on supported languages.

**Caveat-oriented passage (PDF p. 3)**

standard procedure. Second, to elicit meaningful responses from participants capturing local customs, traditions, beliefs, lifestyles, preferences, culture, etc., we created a repository of 2.5K questions, 46.6K prompts, and 1.1K (Dogri) to 4.1K (Hindi) role-play scenarios covering 21 domains and 28 topics of interest, and anchored in practical, da

Additional interpretation and limitations: [core findings](CORE_FINDINGS.md).

## 148. NaturalSpeech 3: Zero-Shot Speech Synthesis with Factorized Codec and Diffusion Models

ID: `2403.03100` | Theme: Representations/codecs | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2403.03100

Snapshot SHA-256: `9c7798d5c3f4f21144e1835c2c343f46f3c34679af17f3514042f973564af802`

Abstract extract: While recent large-scale text-to-speech (TTS) models have achieved significant progress, they still fall short in speech quality, similarity, and prosody. Considering speech intricately encompasses various attributes (e.g., content, prosody, timbre, and acoustic details) that pose significant challenges for generation, a natural idea is to factorize speech into individual subspaces representing different attributes and generate them individually. Motivated by it, we propose NaturalSpeech 3, a TTS system with novel factorized diffusion models to generate natural speech in a zero-shot way. Specifically, 1) we design a neural codec with factorized vector quantization (FVQ) to disentangle speech

**Method-oriented passage (PDF p. 2)**

To effectively generate speech with better quality, similarity and prosody, we propose a TTS system with novel factorized diffusion models to generate natural speech in a zero-shot way. Specifically, 1) we introduce a novel neural speech codec with factorized vector quantization (FVQ), named FACodec, to decompose speech waveform into distinct subspaces of content, prosody, timbre, and acoustic details and reconstruct speech waveform with these disentangled representations, leveraging information bottleneck [16, 17], various supervised losses, and adversarial training [18] to enhance disentanglement; 2) we propose a factorized diffusion model,

**Results-oriented passage (PDF p. 8)**

Table 1: The evaluation results for NaturalSpeech 3 and the baseline methods on LibriSpeech test- clean. ♠means the results are obtained from the authors. ♥means the results directly obtained from the paper. ♣means the results are infered from offical checkpoints. ♦means the reproduced results. Abbreviation: LT (LibriTTS), V (VCTK), LJ (LJSpeech), LL⋆(Librilight Small, Medium), EX (Expresso), MS (MSSS Kor), NI (NIKL Kor). Please refer to Appendix A.4 for more results on 1) WER inferred by an advanced ASR system, and 2) UTMOS, an automatic metric for MOS.

**Caveat-oriented passage (PDF p. 12)**

that NaturalSpeech 3 can enable speech attribute manipulation, by customizing speech attribute prompts. Furthermore, we demonstrate that NaturalSpeech 3 achieves human-level performance on the multi-speaker LibriSpeech dataset for the first time and better performance by scaling to 1B parameters and 200K hours of training data. We list the limitati

## 149. VoiceCraft: Zero-Shot Speech Editing and Text-to-Speech in the Wild

ID: `2403.16973` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2403.16973

Snapshot SHA-256: `31126f50990f86b6ad9ed77925ed176f09b8f5593b8ab2ba73139e27ad97b2e2`

Abstract extract: We introduce VoiceCraft, a token infilling neural codec language model, that achieves state-of-the-art performance on both speech editing and zero-shot text-to-speech (TTS) on audiobooks, internet videos, and podcasts. VoiceCraft employs a Transformer decoder architecture and introduces a token rearrangement procedure that combines causal masking and delayed stacking to enable generation within an existing sequence. On speech editing tasks, VoiceCraft produces edited speech that is nearly indistinguishable from unedited recordings in terms of naturalness, as evaluated by humans; for zero-shot TTS, our model outperforms prior SotA models including VALLE and the popular commercial model XTTS-v

**Method-oriented passage (PDF p. 1)**

We introduce VOICECRAFT, a token infilling neural codec language model, that achieves state-of-the-art performance on both speech editing and zero-shot text-to-speech (TTS) on audiobooks, internet videos, and podcasts1. VOICECRAFT employs a Transformer decoder architecture and introduces a token rearrange- ment procedure that combines causal mask- ing and delayed stacking to enable generation within an existing sequence. On speech editing tasks, VOICECRAFT produces edited speech that is nearly indistinguishable from unedited recordings in terms of naturalness, as evaluated by humans; for zero-shot TTS, our model out- performs prior SotA model

**Results-oriented passage (PDF p. 8)**

on intelligibility and naturalness. Our VOICE- CRAFToutperforms FluentSpeech on both intel- ligibility and naturalness MOS across different sources. Interestingly, FluentSpeech achieves a WER lower than the original recording (4.5 v.s. 5.4), although its intelligibility MOS (3.97) is worse than both VOICECRAFT (4.11) and original recording (4.22). This suggests that ASR model and human judgement diverge on FluentSpeech’s intelligibility. Anecdotally, we observe that Flu- entSpeech tends to produce dull and sometimes robotic speech 6, and we hypothesize that this type of speech tends be more easily recognized by ASR, but is less intelligible t

**Caveat-oriented passage (PDF p. 9)**

Given the advancement of made by VOICECRAFT, there are still limitations. First and foremost is the long silence and scratching sound that occa- sionally occur during generation. Although in this work, we overcome it with sampling multiple utter- ances and selecting the shorter ones, more elegant and efficient methods are needed. Another impor- tan

## 150. Hallucination of Multimodal Large Language Models: A Survey

ID: `2404.18930` | Theme: Captioning/grounding | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2404.18930

Snapshot SHA-256: `e99d86d4722b091c73bc0094b95a8edc856c8bcff1d611a0c0f9463e419aa0d6`

Abstract extract: This survey presents a comprehensive analysis of the phenomenon of hallucination in multimodal large language models (MLLMs), also known as Large Vision-Language Models (LVLMs), which have demonstrated significant advancements and remarkable abilities in multimodal tasks. Despite these promising developments, MLLMs often generate outputs that are inconsistent with the visual content, a challenge known as hallucination, which poses substantial obstacles to their practical deployment and raises concerns regarding their reliability in real-world applications. This problem has attracted increasing attention, prompting efforts to detect and mitigate such inaccuracies. We review recent advances in

**Method-oriented passage (PDF p. 3)**

contrast, there are very few surveys on hallucination in the field of MLLMs. To the best of our knowledge, there is only one concurrent work [112], a short survey on the hallucination problem of LVLMs. However, our survey distinguishes itself in terms of both taxonomy and scope. We present a layered and granular classification of hallucinations, as shown in Fig. 1, drawing a clearer landscape of this field. Additionally, our approach does not limit itself to specific model architectures as prescribed in the work of [112], but rather dissects the causes of hallucinations by tracing back to various affecting factors. We cover a larger range of 

**Results-oriented passage (PDF p. 11)**

In the paper of CHAIR [137], the range of objects is restricted to the 80 MSCOCO objects. Sentence tokenization and synonyms mapping are applied to determine whether a generated sentence contains hallucinated objects. Ground-truth caption and object segmentations both serve as ground- truth objects in the computation. In the MLLM era, this metric is still widely used for assessing the response of MLLMs. POPE [103]. When used in MLLMs, the work of [103] argues that the CHAIR metric can be affected by the instruction designs and the length of generated captions. Therefore, it proposes a new evaluation metric as well as a benchmark, called Pooli

**Caveat-oriented passage (PDF p. 12)**

includes a non-existent object, despite the ground truth answer being a negative indefinite pronoun (e.g., "none", "no one", etc). This is denoted as NegP. b) Incorrectness occurs when a VL model fails to accurately respond to a question with a ground truth answer that is anything other than NegP, denoted as Others. This paper argues that the exist

## 151. Active Learning with Task Adaptation Pre-training for Speech Emotion Recognition

ID: `2405.00307` | Theme: Loop/data selection | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2405.00307

Snapshot SHA-256: `1024fbaa5574da6e115d3032633366c9599a1c3c5c655e319af8765e647bd43e`

Abstract extract: Speech emotion recognition (SER) has garnered increasing attention due to its wide range of applications in various fields, including human-machine interaction, virtual assistants, and mental health assistance. However, existing SER methods often overlook the information gap between the pre-training speech recognition task and the downstream SER task, resulting in sub-optimal performance. Moreover, current methods require much time for fine-tuning on each specific speech dataset, such as IEMOCAP, which limits their effectiveness in real-world scenarios with large-scale noisy data. To address these issues, we propose an active learning (AL)-based fine-tuning framework for SER, called \textsc{

**Method-oriented passage (PDF p. 20)**

In this section, we primarily delineate three key distinctions between this version and the conference version of our research. (1) We introduced novel methodologies by extending AFTER to accommodate more complex real-world scenarios. Specifically, we first explored various initialization methods for AFTER in Section 5.1. Subsequently, we investigated the impact of integrating AFTER with different pre-trained ASR models in Section 5.6. Finally, we extended AFTER to encompass more complex scenarios involving multiple annotators in Section 5.7 and soft-labels in Section 5.8. (2) We redefined the motivation behind this study in Section 1, as wel

**Results-oriented passage (PDF p. 8)**

IEMOCAP: We first evaluated the performance of all baseline models using the widely used benchmark dataset, IEMOCAP [35]. IEMOCAP is a multimodal database commonly employed to evaluate SER performance. It comprises five conversation sessions, each featuring a female and a male actor engaging in improvised and scripted scenarios. The dataset includes 10,039 speech utterances, all sampled at 16kHz with a 16 bits resolution. To ensure a fair comparison, we merged the “excited” class into the “happy” class, resulting in four considered emotions: neutral, happy, angry, and sad. Following the approach of [41], we adopted a 5-fold cross-validation m

**Caveat-oriented passage (PDF p. 3)**

The remainder of this paper is organized as follows. In Section 2, we provide a literature review of the most related work, including speech emotion recognition, active learning, and task-adaptation pre-training. In Section 3, we carefully introduce our methodology: AFTER, in detail. In Section 4, we describe the experimental corpora and setup in d

## 152. Does Fine-Tuning LLMs on New Knowledge Encourage Hallucinations?

ID: `2405.05904` | Theme: Captioning/grounding | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2405.05904

Snapshot SHA-256: `0a96d2a4b42a73f207b3e4311739989984cc41c0ef214eaa4fdaa4d9d77ac3fb`

Abstract extract: When large language models are aligned via supervised fine-tuning, they may encounter new factual information that was not acquired through pre-training. It is often conjectured that this can teach the model the behavior of hallucinating factually incorrect responses, as the model is trained to generate facts that are not grounded in its pre-existing knowledge. In this work, we study the impact of such exposure to new knowledge on the capability of the fine-tuned model to utilize its pre-existing knowledge. To this end, we design a controlled setup, focused on closed-book QA, where we vary the proportion of the fine-tuning examples that introduce new knowledge. We demonstrate that large lang

**Method-oriented passage (PDF p. 2)**

To study the impact of new knowledge, we must be able to assess whether a single fine-tuning ex- ample is consistent with the model’s knowledge. We propose SliCK, a hierarchy of four knowl- edge categories, derived from a continuous mea- sure that quantifies the agreement between model- generated answers and the ground-truth labels. In SliCK, examples are first categorized into Known and Unknown types, where the latter corresponds to examples with facts that are most likely unknown to the model. The Known examples are subse- quently split into three categories: HighlyKnown, MaybeKnown, and WeaklyKnown (Figure 2). Equipped with the above metho

**Results-oriented passage (PDF p. 5)**

filtering-out all the Unknown examples from D. For each D variant, we create a corresponding ablated variant DKnown, consisting only from the Known ex- amples in D. E.g., if D has 25% Unknown, we filter them out and are left with the remaining 75% Known examples and get |DKnown | = 0.75 × |D|. Figure 3b presents the results. Perhaps surpris- ingly, for EARLY_STOP the results for D are almost identical to DKnown, indicating that the Unknown examples had a neutral effect on performance (as their removal had minimal impact). Conversely, the CONVERGENCE results show that with longer train- ing, Unknown examples are actually very harmful. In this 

**Caveat-oriented passage (PDF p. 2)**

1While we focus on supervised fine-tuning, our findings may be relevant to offline preference optimization methods like DPO (Rafailov et al., 2024) that may add new knowledge, which we leave for future work. 2We use the term “struggle” to describe how LLMs con- verge slowly for examples containing new factual knowledge. Since this term carries emot

## 153. A Comprehensive Survey of Hallucination in Large Language, Image, Video and Audio Foundation Models

ID: `2405.09589` | Theme: Captioning/grounding | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2405.09589

Snapshot SHA-256: `8f697aac78807f41e6c640bb140c26990c034b4ea09c83196debc372ee4a86bf`

Abstract extract: The rapid advancement of foundation models (FMs) across language, image, audio, and video domains has shown remarkable capabilities in diverse tasks. However, the proliferation of FMs brings forth a critical challenge: the potential to generate hallucinated outputs, particularly in high-stakes applications. The tendency of foundation models to produce hallucinated content arguably represents the biggest hindrance to their widespread adoption in real-world scenarios, especially in domains where reliability and accuracy are paramount. This survey paper presents a comprehensive overview of recent developments that aim to identify and mitigate the problem of hallucination in FMs, spanning text, 

**Method-oriented passage (PDF p. 5)**

Dai et al. (2022) investigated the issue of object hal- lucinations in Vision-Language Pre-training (VLP) models, where textual descriptions generated by these models contain non-existent or inaccurate objects based on input images. Li et al. (2023g) revealed widespread and severe object hallucina- tion issues and suggested that visual instructions may influence hallucination, noting that objects frequently appearing in visual instructions or co- occurring with image objects are more likely to be hallucinated. To enhance the evaluation of ob- ject hallucination, they introduced a polling-based query method called POPE, which demonstrates impr

**Results-oriented passage (PDF p. 4)**

framework, integrating advanced long text embed- dings like e5-mistral-7b-instruct, along with mod- els such as GPT-3, SpanBERT, and RoFormer. This MTL approach demonstrated a 40% average im- provement in accuracy on the FACTOID bench- mark compared to leading textual entailment meth- ods. Hallucination mitigation efforts have predomi- nantly relied on empirical methods, leaving uncer- tainty regarding the possibility of complete elimi- nation. To tackle this challenge, Xu et al. (2024b) introduced a formal framework defining hallucina- tion as inconsistencies between computable LLMs and a ground truth function. The study exam- ines existing 

**Caveat-oriented passage (PDF p. 2)**

Most of the existing survey papers have explored hallucination in the context of large language mod- els (LLMs) (Huang et al., 2023), (Chen et al., 2024b), (Tonmoy et al., 2024). Recent studies have shown that hallucination can also occur in vision, audio, and video foundation models, highlighting the need for a comprehensive understanding of this 

## 154. Seed-TTS: A Family of High-Quality Versatile Speech Generation Models

ID: `2406.02430` | Theme: Evaluation/reliability | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2406.02430

Snapshot SHA-256: `3c56b7d33ee852cad3546f453985729bdf0018d2e80ebf1ab88ce02f9114fe0f`

Abstract extract: We introduce Seed-TTS, a family of large-scale autoregressive text-to-speech (TTS) models capable of generating speech that is virtually indistinguishable from human speech. Seed-TTS serves as a foundation model for speech generation and excels in speech in-context learning, achieving performance in speaker similarity and naturalness that matches ground truth human speech in both objective and subjective evaluations. With fine-tuning, we achieve even higher subjective scores across these metrics. Seed-TTS offers superior controllability over various speech attributes such as emotion and is capable of generating highly expressive and diverse speech for speakers in the wild. Furthermore, we pr

**Method-oriented passage (PDF p. 2)**

• We introduce Seed-TTS, a family of speech generation models capable of generating highly expressive, human-like speech. We demonstrate that Seed-TTS achieves state-of-the-art (SOTA) performance in multiple evaluations. Under a zero-shot ICL setup, we show that Seed-TTS is able to generate robust, similar, and highly dynamic speech that is indistinguishable from human speech. • We present a novel self-distillation extension of Seed-TTS for timbre disentanglement and demonstrate SOTA performance in the voice conversion task. • We introduce a novel RL-based post-training extension for Seed-TTS, which holistically im- proves the model’s perform

**Results-oriented passage (PDF p. 4)**

Evaluation metrics. We adopt the word error rate (WER) and speaker similarity (SIM) metrics for objective evaluation. For WER, we employ Whisper-large-v3 [Radford et al., 2023] and Paraformer- zh [Gao et al., 2023b] as the automatic speech recognition (ASR) engines for English and Mandarin, respectively. For SIM, we use WavLM-large fine-tuned on the speaker verification task [Chen et al., 2022b,c] to obtain speaker embeddings used to calculate the cosine similarity of speech samples of each test utterance against reference clips. We use Comparative Mean Opinion Scores (CMOS) studies for subjective evaluation, as follows. For each test sample,

**Caveat-oriented passage (PDF p. 2)**

Lastly, we discuss potential applications and limitations of Seed-TTS, as well as several challenges we encountered during development, including those related to building socially responsible artificial intelligence (AI). The capabilities and limitations of Seed-TTS give rise to significant and novel challenges in multimedia and safety application

## 155. Combining X-Vectors and Bayesian Batch Active Learning: Two-Stage Active Learning Pipeline for Speech Recognition

ID: `2406.02566` | Theme: Loop/data selection | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2406.02566

Snapshot SHA-256: `75ee22625cbd718bcfe682b095c9c68679ed64c45d4decaf16d2ea568eabda4b`

Abstract extract: This paper introduces a novel two-stage active learning (AL) pipeline for automatic speech recognition (ASR), combining unsupervised and supervised AL methods. The first stage utilizes unsupervised AL by using x-vectors clustering for diverse sample selection from unlabeled speech data, thus establishing a robust initial dataset for the subsequent supervised AL. The second stage incorporates a supervised AL strategy, with a batch AL method specifically developed for ASR, aimed at selecting diverse and informative batches of samples. Here, sample diversity is also achieved using x-vectors clustering, while the most informative samples are identified using a Bayesian AL method tailored for ASR

**Method-oriented passage (PDF p. 2)**

in transcriptions between these models quantifies uncertainty. Notably, [22] focuses on samples at the intersection of those chosen by the committee approach and those identified through the lowest confidence measures, to refine sample selection further. All the methods discussed so far have been within the scope of supervised AL. Unsupervised AL, in contrast, does not require an initial set of labeled data.1 These methods may in- volve strategies like clustering or density estimation to identify valuable or representative samples from the unlabeled dataset. The study [23] presents an unsupervised AL method for ASR that employs acoustic featu

**Results-oriented passage (PDF p. 12)**

SMCA is outperformed by the iterative random sampling approach due to two key factors. One of the reasons is that its uncertainty measure correlates less with the actual WER compared to our proposed method, as shown in Table IV, which results in a slight reduction in its effectiveness when selecting informative samples. In addition, and more importantly, while the test set is designed to evaluate models on diverse data, SMCA in our case tends to select the most uncertain samples, which likely come from a small number of clusters. This leads to a less diverse training set for SMCA- based ASR models, further limiting their performance. In contr

**Caveat-oriented passage (PDF p. 2)**

context, ’informativeness,’ ’uncertainty,’ and ’confidence’ are often used interchangeably. Studies like [11]–[13] apply these AL approaches in ASR, calculating the confidence levels of predictions based on path probabilities, or the posterior probabilities of tokens, derived from the softmax layer during sequence decoding. The methods discussed ab

## 156. XTTS: a Massively Multilingual Zero-Shot Text-to-Speech Model

ID: `2406.04904` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2406.04904

Snapshot SHA-256: `7aeb909fe08fbebbe1e2f10a77b4c5cdbb9a687199084b85bd7362b1331c2b46`

Abstract extract: Most Zero-shot Multi-speaker TTS (ZS-TTS) systems support only a single language. Although models like YourTTS, VALL-E X, Mega-TTS 2, and Voicebox explored Multilingual ZS-TTS they are limited to just a few high/medium resource languages, limiting the applications of these models in most of the low/medium resource languages. In this paper, we aim to alleviate this issue by proposing and making publicly available the XTTS system. Our method builds upon the Tortoise model and adds several novel modifications to enable multilingual training, improve voice cloning, and enable faster training and inference. XTTS was trained in 16 languages and achieved state-of-the-art (SOTA) results in most of t

**Method-oriented passage (PDF p. 2)**

solve this issue by proposing a massive multilingual ZS-TTS model that supports 16 languages, including English (en), Span- ish (es), French (fr), German (de), Italian (it), Portuguese (pt), Polish (pl), Turkish (tr), Russian (ru), Dutch (nl), Czech (cs), Arabic (ar), Chinese (zh), Hungarian (hu), Korean (ko), and Japanese (ja). The contributions of this work are as follows: • We introduced XTTS, a new multilingual ZS-TTS model that achieves SOTA results in 16 languages; • XTTS is the first massively multilingual ZS-TTS model sup- porting low/medium resource languages; • Our model can perform cross-language ZS-TTS without needing a parallel t

**Results-oriented passage (PDF p. 4)**

confirming the over-fitting issue, and showing that previous models miss-compared their model with YourTTS. Compar- ing Monolingual YourTTS (Exp. 1) with the YourTTS trained on the XTTS dataset (Exp. 2) we can see a huge gap, in all the metrics indicating that comparing multilingual models with monolingual models is not fair. It also shows that YourTTS had difficulties to learn all 16 languages well. XTTS model (Exp. 3) achieved the better CER and it achieved competitive results in all the other metrics. It is impressive especially be- cause our model was trained in 16 languages and we are com- paring it with related works that were trained o

**Caveat-oriented passage (PDF p. 2)**

XTTS builds upon Tortoise [12], but includes several novel modifications to enable multilingual training, improve ZS-TTS, and enable faster training and inference. Figure 1 shows an overview of the XTTS architecture. XTTS is composed of three components: VQ-VAE: A Vector Quantised-Variational AutoEncoder (VQ-VAE) with 13M parameters receives a mel-

## 157. Spectral Codecs: Improving Non-Autoregressive Speech Synthesis with Spectrogram-Based Audio Codecs

ID: `2406.05298` | Theme: Representations/codecs | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2406.05298

Snapshot SHA-256: `e85ddaafed59362e15e35b7a2645ea3540db32a750087b6bc8e4d5a7cc2e0d1b`

Abstract extract: Historically, most speech models in machine-learning have used the mel-spectrogram as a speech representation. Recently, discrete audio tokens produced by neural audio codecs have become a popular alternate speech representation for speech synthesis tasks such as text-to-speech (TTS). However, the data distribution produced by such codecs is too complex for some TTS models to predict, typically requiring large autoregressive models to get good quality. Most existing audio codecs use Residual Vector Quantization (RVQ) to compress and reconstruct the time-domain audio signal. We propose a spectral codec which uses Finite Scalar Quantization (FSQ) to compress the mel-spectrogram and reconstruct

**Method-oriented passage (PDF p. 3)**

which takes text, pitch, and duration as input to predict a mel- spectrogram. To improve quality we also condition the model on energy as in [3] and extract duration information during training using the alignment strategy in [18]. FastPitch predicts continuous mel-spectrogram features with an L2 loss. To predict audio tokens, we replace the L2 loss with a softmax loss predicting codebooks. All codecs have eight codebooks, resulting in eight softmax layers which predict the entries of the different codebooks in parallel. For the softmax loss we include logit normalization [19] with a temperature τ = 0.02. For some experiments we introduce an 

**Results-oriented passage (PDF p. 4)**

We conduct an ablation study on the TTS quality of Fast- Pitch when trained to predict the tokens of the five codec models, and the continuous mel-spectrogram with the HiFi- GAN baseline. The results are in Table II. To evaluate perceptual quality we use MOS and ViSQOL [23]. To measure intelligibility of TTS outputs we look at ESTOI [26], as well as the word error rate (WER) and character error rate (CER) of transcriptions using NVIDIA’s Fast Conformer-Transducer XL [27]. We include the Real- Time Factor (RTF) for each TTS system, normalized by the RTF of our HiFi-GAN baseline. All metrics are reported with a 95% confidence interval. For WER 

**Caveat-oriented passage (PDF p. 3)**

III. EXPERIMENTS A. Datasets While most speech domains use 16 kHz audio, many TTS applications require 44.1 kHz data. For TTS training we use HiFi-TTS [20], containing 300 hours of high quality 44.1 kHz audio from 10 speakers. To train a robust audio codec we need a larger dataset. However most public datasets that are uploaded at 44.1 kHz

## 158. Controlling Emotion in Text-to-Speech with Natural Language Prompts

ID: `2406.06406` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2406.06406

Snapshot SHA-256: `cd867cc4d13442fae17fdd876a3c3ba5e9afffc2112044244b67fe58f6ec6854`

Abstract extract: In recent years, prompting has quickly become one of the standard ways of steering the outputs of generative machine learning models, due to its intuitive use of natural language. In this work, we propose a system conditioned on embeddings derived from an emotionally rich text that serves as prompt. Thereby, a joint representation of speaker and prompt embeddings is integrated at several points within a transformer-based architecture. Our approach is trained on merged emotional speech and text datasets and varies prompts in each training iteration to increase the generalization capabilities of the model. Objective and subjective evaluation results demonstrate the ability of the conditioned s

**Method-oriented passage (PDF p. 1)**

In recent years, prompting has quickly become one of the stan- dard ways of steering the outputs of generative machine learn- ing models, due to its intuitive use of natural language. In this work, we propose a system conditioned on embeddings derived from an emotionally rich text that serves as prompt. Thereby, a joint representation of speaker and prompt embeddings is in- tegrated at several points within a transformer-based architec- ture. Our approach is trained on merged emotional speech and text datasets and varies prompts in each training iteration to increase the generalization capabilities of the model. Objec- tive and subjective eva

**Results-oriented passage (PDF p. 3)**

We calculate the speaker similarity as the cosine similarity be- tween speaker embeddings of ground truth speech samples and synthesized ones. Thereby speaker embeddings are extracted using a pre-trained speaker verification model [47]. The re- sults in Table 2 show a high overall speaker similarity across all speakers of ESD, demonstrating that speaker identities are almost perfectly preserved during synthesis and not affected by the integration of prompt embeddings. Comparing our results to EmoSpeech, both our proposed system and our baseline per- form significantly better. This is likely caused by the multi- speaker training phase in our c

**Caveat-oriented passage (PDF p. 4)**

and compare those to the ground truth labels of the applied prompts. The confusion matrices in Figure 3 illustrate the rela- tive frequencies of predicted emotion labels opposed to underly- ing ones. Furthermore, as a measure of association strength be- tween emotion labels, Cram´er’s V [49] is calculated with results shown in Table 3. The emotion 

## 159. Understanding Sounds, Missing the Questions: The Challenge of Object Hallucination in Large Audio-Language Models

ID: `2406.08402` | Theme: Captioning/grounding | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2406.08402

Snapshot SHA-256: `9cecc4849cbcf921f70131893223be60e3d345799c2eee010721d0d703305974`

Abstract extract: Large audio-language models (LALMs) enhance traditional large language models by integrating audio perception capabilities, allowing them to tackle audio-related tasks. Previous research has primarily focused on assessing the performance of LALMs across various tasks, yet overlooking their reliability, particularly concerning issues like object hallucination. In our study, we introduce methods to assess the extent of object hallucination of publicly available LALMs. Our findings reveal that LALMs are comparable to specialized audio captioning models in their understanding of audio content, but struggle to answer discriminative questions, specifically those requiring the identification of the

**Method-oriented passage (PDF p. 3)**

In order to mitigate potential errors introduced by auto- mated measurement methods, we introduce GPT-4 as a refer- ence baseline. We feed captions generated by LALMs, along with ground truth captions and labels, into GPT-4, requesting it to analyze which objects are considered hallucinations and which are not. Consequently, we can also use the decomposed results of GPT-4 and calculate the ECHO and Cover scores. We name it as ECHOI, g, ECHOS, g and Coverg. For noisy auto- matic speech recognition task, we also report the word error rate (WER) as a reference and select Whisper [36] large v3 as a baseline model for comparison.

**Results-oriented passage (PDF p. 3)**

Table 2: Results of generative tasks. E stands for ECHO, with subscripts I and S indicating instance and sentence level, respectively. The subscript g refers to the use of GPT-4 as the evaluator. Std denotes the standard deviation of ECHO across five prompts. SPICE is referenced from [34]. Due to its reliance on fixed template inputs, Qwen-Audio cannot accommodate varying prompts. Specialized in audio captioning refers to specialized audio caption model [35], while in ASR, it refers to Whisper [36] large v3. (Unit: %)

**Caveat-oriented passage (PDF p. 4)**

Despite recent advancements, LALMs present reliability con- cerns, particularly with object hallucination. We deploy task- oriented methodologies to gauge this issue, revealing that de- spite LALMs’ capability to perform audio captioning compa- rably to specialized models, they struggle significantly with discriminative tasks and exhibit severe obj

## 160. E2 TTS: Embarrassingly Easy Fully Non-Autoregressive Zero-Shot TTS

ID: `2406.18009` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2406.18009

Snapshot SHA-256: `5d6da9f9bdef42d090c05ae43628c1e87364b02f0f29a76a5ef11e92740c6fdc`

Abstract extract: This paper introduces Embarrassingly Easy Text-to-Speech (E2 TTS), a fully non-autoregressive zero-shot text-to-speech system that offers human-level naturalness and state-of-the-art speaker similarity and intelligibility. In the E2 TTS framework, the text input is converted into a character sequence with filler tokens. The flow-matching-based mel spectrogram generator is then trained based on the audio infilling task. Unlike many previous works, it does not require additional components (e.g., duration model, grapheme-to-phoneme) or complex techniques (e.g., monotonic alignment search). Despite its simplicity, E2 TTS achieves state-of-the-art zero-shot TTS capabilities that are comparable t

**Method-oriented passage (PDF p. 6)**

We introduced E2 TTS, a novel fully NAR zero-shot TTS. In the E2 TTS framework, the text input is converted into a character sequence with filler tokens to match the length of the input character sequence and the output mel-filterbank sequence. The flow-matching-based mel spectrogram generator is then trained based on the audio infill- ing task. Despite its simplicity, E2 TTS achieved state-of-the-art zero-shot TTS capabilities that were comparable to or surpass previ- ous works, including Voicebox and NaturalSpeech 3. The simplicity of E2 TTS also allowed for flexibility in the input representation. We proposed several variants of E2 TTS to 

**Results-oriented passage (PDF p. 4)**

Table 1. Objective results for LibriSpeech-PC test-clean evaluation set. WER is expressed in percentage. † Our reproduction. LL, LH, and PP stand for Librilight, Libriheavy, and Proprietary, respectively.

**Caveat-oriented passage (PDF p. 3)**

2.5.2. Extension 2: Enabling explicit indication of pronunciation for parts of words in a sentence In certain scenarios, users want to specify the pronunciation of a spe- cific word such as unique foreign names. Retraining the model to ac- commodate such new words is both expensive and time-consuming. To tackle this challenge, we introduce another 

## 161. Automatic Speech Recognition for Hindi

ID: `2406.18135` | Theme: Speech/audio generation and control | Status: `excluded_after_screening`

Source: https://arxiv.org/pdf/2406.18135

Snapshot SHA-256: `c93662daa772e6cbde2a1d889fa72518747c0e665a3361d3f855b0f8adefed2c`

Excluded: Hindi ASR annotation application; insufficient task-specific evidence in inspected passages

Abstract extract: Automatic speech recognition (ASR) is a key area in computational linguistics, focusing on developing technologies that enable computers to convert spoken language into text. This field combines linguistics and machine learning. ASR models, which map speech audio to transcripts through supervised learning, require handling real and unrestricted text. Text-to-speech systems directly work with real text, while ASR systems rely on language models trained on large text corpora. High-quality transcribed data is essential for training predictive models. The research involved two main components: developing a web application and designing a web interface for speech recognition. The web application,

**Method-oriented passage (PDF p. 3)**

handles large amounts of audio files and their transcriptions, and performs collaborative human correction of the ASR transcripts. The web app is designed to operate in real-time, using a client-server architecture, whereby information about each manual edit is posted to the server and a change record is maintained. 2. Designing a web interface for speech recognition. This involved specific

**Results-oriented passage (PDF p. 1)**

handles large amounts of audio files and their transcriptions, and performs collaborative human correction of the ASR transcripts. The web app is designed to operate in real-time, using a client-server architecture, whereby information about each manual edit is posted to the server and a change record is maintained. 2. Designing a web interface for speech recognition. This involved specific

**Caveat-oriented passage (PDF p. 1)**

handles large amounts of audio files and their transcriptions, and performs collaborative human correction of the ASR transcripts. The web app is designed to operate in real-time, using a client-server architecture, whereby information about each manual edit is posted to the server and a change record is maintained. 2. Designing a web interface for

## 162. PicoAudio: Enabling Precise Timestamp and Frequency Controllability of Audio Events in Text-to-audio Generation

ID: `2407.02869` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2407.02869

Snapshot SHA-256: `c7eea7051cf0f36de81e4ccfaff6c98282d93a8c57db39f428b92e225aca5f63`

Abstract extract: Recently, audio generation tasks have attracted considerable research interests. Precise temporal controllability is essential to integrate audio generation with real applications. In this work, we propose a temporal controlled audio generation framework, PicoAudio. PicoAudio integrates temporal information to guide audio generation through tailored model design. It leverages data crawling, segmentation, filtering, and simulation of fine-grained temporally-aligned audio-text data. Both subjective and objective evaluations demonstrate that PicoAudio dramantically surpasses current state-of-the-art generation models in terms of timestamp and occurrence frequency controllability. The generated 

**Method-oriented passage (PDF p. 1)**

particular, in the largest audio captioning dataset AudioCaps, the phrase “xx times”, indicating frequency, appears only in 1086/56796(≈1.9%) annotations. Moreover, there are scarce annotations regarding timestamps. High-quality temporally- aligned audio-text data is crucial for training temporal con- trollable models. The more meticulously annotated the data, the better the models can learn the precise correspondence be- tween audio outputs and temporal textual conditions, thereby achieving finer-grained control. Second, the diffusion model has limited knowledge of timestamp information. Existing diffusion-based models aim to learn the relat

**Results-oriented passage (PDF p. 4)**

Table 1: Evaluation results. F1segment / Lfreq 1 respectively measures the timestamp alignment / occurrence frequencies error between generated audio and input conditions. FAD measures the audio quality. MOS denotes subjective metrics. Ablation study: “w/o T” indicates that the model does not utilize timestamp matrix O, which shares a similar framework with the baseline models.

**Caveat-oriented passage (PDF p. 4)**

straightforward for GPT-4 after being prompted. Therefore, it can be said that the PicoAudio can achieve arbitrary precise temporal control. However, due to constraints imposed by the audio sources, PicoAudio’s limitation lies in its temporary capacity to exercise temporal control over a limited number of events. Expanding the quantity of events an

## 163. Emilia: An Extensive, Multilingual, and Diverse Speech Dataset for Large-Scale Speech Generation

ID: `2407.05361` | Theme: Data/Indic speech | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2407.05361

Snapshot SHA-256: `5265cc368d39b7279b9a2c22b80c37e843f5a65d784f40dc573c18d5bacc772e`

Abstract extract: Recent advancements in speech generation models have been significantly driven by the use of large-scale training data. However, producing highly spontaneous, human-like speech remains a challenge due to the scarcity of large, diverse, and spontaneous speech datasets. In response, we introduce Emilia, the first large-scale, multilingual, and diverse speech generation dataset. Emilia starts with over 101k hours of speech across six languages, covering a wide range of speaking styles to enable more natural and spontaneous speech generation. To facilitate the scale-up of Emilia, we also present Emilia-Pipe, the first open-source preprocessing pipeline designed to efficiently transform raw, in-t

**Method-oriented passage (PDF p. 4)**

The Emilia dataset comprises a collection of speech data from a wide range of video platforms and podcasts, capturing diverse speaking styles of real human speech. To quantify this diversity, we conducted analyses on both the acoustic and semantic feature space, comparing it with the MLS dataset, which is derived from audiobooks and widely used for training speech generation models.

**Results-oriented passage (PDF p. 3)**

The evaluation is conducted on an independent server with eight NVIDIA RTX 4090 GPUs. The whole processing time takes about 3.99 hours. Table 2 shows the processing results of Emilia-Pipe on this subset. The raw data has a wide range of audio durations from 9.22 to 18,056.98 seconds, with an average of 1,572.53 seconds and high variability. The DNSMOS P.835 OVRL scores range from 1.08 to 3.51, with an average of 2.50, indicating varied overall quality. After filtering, the total duration for the resulting data is further reduced to 176.22 hours, retaining 29.43% of the raw speech data, and the average DNSMOS P.835 OVRL score significantly imp

**Caveat-oriented passage (PDF p. 1)**

In the past few years, the research of speech generation has made significant advancements with the emergence of various generative models [1–4] and the use of large-scale training data [5, 6]. The models such as SoundStorm [1], VoiceBox [7] and NaturalSpeech 3 [3] have considerably progressed in (zero-shot) speech generation by considerably scalin

## 164. CosyVoice: A Scalable Multilingual Zero-shot Text-to-speech Synthesizer based on Supervised Semantic Tokens

ID: `2407.05407` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2407.05407

Snapshot SHA-256: `943cfccccb8abaf2e3be1949e48de6990e9ebb5c4815b618270f157eb9c41f1a`

Abstract extract: Recent years have witnessed a trend that large language model (LLM) based text-to-speech (TTS) emerges into the mainstream due to their high naturalness and zero-shot capacity. In this paradigm, speech signals are discretized into token sequences, which are modeled by an LLM with text as prompts and reconstructed by a token-based vocoder to waveforms. Obviously, speech tokens play a critical role in LLM-based TTS models. Current speech tokens are learned in an unsupervised manner, which lacks explicit semantic information and alignment to the text. In this paper, we propose to represent speech with supervised semantic tokens, which are derived from a multilingual speech recognition model by 

**Method-oriented passage (PDF p. 4)**

Under the scheduled flow, there are more genera- tion steps at the beginning. Classifier-free guidance (CFG) has been proven to improve the generation quality of diffusion prob- abilistic models (Ho and Salimans, 2022b; Nichol and Dhariwal, 2021; Le et al., 2024). Therefore, we propose to adapt the CFG into conditional flow matching models. At the training stage, we ran- domly drop the conditions Ψ = {v, {µl}1:L, ˜ X1} with a fixed probability of 0.2. In this manner, we

**Results-oriented passage (PDF p. 7)**

Similar to other autoregressive language models, we employ a random sampling decoding strategy for our token LM and assessed the synthesis pro- cess using five different random seed values: 0, 7, 42, 123, and 1,337. The resultant evaluation metrics were averaged to determine the mean and standard deviation. Additionally, we conducted an ASR re-ranking to demonstrate potential perfor- mance improvements in offline mode. Tables 8 and 9 present the results for English and Chinese, respectively. On the English dataset, CosyVoice attained human-level performance with similar content recognition and higher speaker sim- ilarity. ASR re-ranking notab

**Caveat-oriented passage (PDF p. 4)**

CosyVoice models exhibit zero-shot in-context learning capabilities, allowing for the replication of an arbitrary voice with only a brief reference speech sample. This process entails the careful con- struction of input sequences for the token language model (LM), depicted in Figure 2. For prompt speech and input text in the same language, we merge

## 165. Qwen2-Audio Technical Report

ID: `2407.10759` | Theme: Captioning/grounding | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2407.10759

Snapshot SHA-256: `4ddac6d6b779f567efffb06144a4a9030e8524168ca54e504e26c81767758826`

Abstract extract: We introduce the latest progress of Qwen-Audio, a large-scale audio-language model called Qwen2-Audio, which is capable of accepting various audio signal inputs and performing audio analysis or direct textual responses with regard to speech instructions. In contrast to complex hierarchical tags, we have simplified the pre-training process by utilizing natural language prompts for different data and tasks, and have further expanded the data volume. We have boosted the instruction-following capability of Qwen2-Audio and implemented two distinct audio interaction modes for voice chat and audio analysis. In the voice chat mode, users can freely engage in voice interactions with Qwen2-Audio witho

**Method-oriented passage (PDF p. 3)**

Model Architecture The training process of Qwen2-Audio is depicted in Figure 2, which contains an audio encoder and a large language model. Given the paired data (a, x), where the a and x denote the audio sequences and text sequences, the training objective is to maximize the next text token probability as

**Results-oriented passage (PDF p. 5)**

In this section, we present a comprehensive evaluation of the Qwen2-Audio model, assessing its performance across various tasks without any task-specific fine-tuning. We begin by examining its English Automatic Speech Recognition (ASR) results, as depicted in Table 2, where Qwen2-Audio exhibits superior performance compared to previous multi-task learning models. Specifically, it achieves a 1.6% and 3.6% WER on the librispeech test-clean and test-other datasets, respectively. Compared with Whisper-large-v3 on Fleurs zh subset, we achieve better results than Whisper-large-v3. One point to note is that Qwen2-Audio is not evaluated in a zero-sho

**Caveat-oriented passage (PDF p. 5)**

In practice, we have found that many previous test datasets are highly limited and cannot adequately reflect performance in real-world scenarios, such as some SLU (Spoken Language Understanding) and SER (Speech Emotion Recognition) datasets. Therefore, we mainly evaluated performance directly on AIR-Bench. We discovered that the scores from AIR-Ben

## 166. Efficient Audio Captioning with Encoder-Level Knowledge Distillation

ID: `2407.14329` | Theme: Captioning/grounding | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2407.14329

Snapshot SHA-256: `d80dfb737307d9c55a0d3124da76dbe6c994c25592b5fddb28374d1a0588b6ed`

Abstract extract: Significant improvement has been achieved in automated audio captioning (AAC) with recent models. However, these models have become increasingly large as their performance is enhanced. In this work, we propose a knowledge distillation (KD) framework for AAC. Our analysis shows that in the encoder-decoder based AAC models, it is more effective to distill knowledge into the encoder as compared with the decoder. To this end, we incorporate encoder-level KD loss into training, in addition to the standard supervised loss and sequence-level KD loss. We investigate two encoder-level KD methods, based on mean squared error (MSE) loss and contrastive loss, respectively. Experimental results demonstra

**Method-oriented passage (PDF p. 2)**

where T1 and T2 are sequence lengths or embeddings from the teacher and student encoders since they may use different tem- poral resolutions. Then the teacher model predicts the caption Ttea conditioned on the encoded embeddings:

**Results-oriented passage (PDF p. 2)**

brought closer while embeddings from different audio clips are pushed further apart. With this design, we encourage the student encoder to learn the same ability as the teacher to distinguish between different audio clips. Based on the EfficientNet [13] architecture, we combine the standard sequence level KD and our proposed encoder-level KD for training. Experimental re- sults show that KDcontra performs more robustly than KDmse in the data scarcity scenario. Compared with training from scratch, KD achieves significant performance improvement. Incorporat- ing unannotated audio-only data into training further improves the performance, resulti

**Caveat-oriented passage (PDF p. 2)**

Student Motivated by the finding that Transformer serves as an effective teacher for CNN students [19], we adopt EfficientNet-B2 [13] as the student encoder. Depthwise con- volution [20] is used instead of the standard convolution to en- hance parameter efficiency. For the decoder, we adopt a shal- low 2-layer Transformer due to its competitive per

## 167. On the Problem of Text-To-Speech Model Selection for Synthetic Data Generation in Automatic Speech Recognition

ID: `2407.21476` | Theme: Loop/data selection | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2407.21476

Snapshot SHA-256: `fcc1d9c4155297179db71da5d0352cfe1110504c2d65ae82fa140428b468f8cf`

Abstract extract: The rapid development of neural text-to-speech (TTS) systems enabled its usage in other areas of natural language processing such as automatic speech recognition (ASR) or spoken language translation (SLT). Due to the large number of different TTS architectures and their extensions, selecting which TTS systems to use for synthetic data creation is not an easy task. We use the comparison of five different TTS decoder architectures in the scope of synthetic data generation to show the impact on CTC-based speech recognition training. We compare the recognition results to computable metrics like NISQA MOS and intelligibility, finding that there are no clear relations to the ASR performance. We al

**Method-oriented passage (PDF p. 2)**

For flow-based TTS systems, the decoder is an invertible neural network that can be applied in both directions from the spectro- grams xT 1 into latent space variables zT 1 and vice-versa. Dur- ing training, the target features are transformed into the latent space and matched against a normal distribution with a mean µT 1 = µθ(hT 1 ) and unit variance. The target objective is to maximize the likelihood of the latent space samples given the distributions. For inference, the latent space values are sampled from the distribution with a mean function µθ, temperature τ, and passed backwards through the flow fθ:

**Results-oriented passage (PDF p. 3)**

In a first comparison we evaluated the systems via the synthetic data only ASR training, the NISQA MOS and the sWER. Table 2 shows the results of each of the five decoders compared to the reference values of the real data. For all metrics we used text data unseen during training. With respect to the final ASR train- ing evaluation, all TTS systems have a reasonable performance and there is no strong outlier. In general, using the synthetic data for training results in a system with double the error rate when training TTS only on the available ASR data, which is a consistent result to previous literature [5, 11]. [34] showed that even when usi

**Caveat-oriented passage (PDF p. 4)**

When training with synthetic data only, we achieved a WER performance which is less than factor 2 worse compared to training on the real data. In relation, [5] reported reaching ra- tios of around 2 on the LibriSpeech-960 task, and [11] reported ratios of more than 3. In this work we specifically investigated decoder architectures. In future work t

## 168. SpeechCraft: A Fine-grained Expressive Speech Dataset with Natural Language Description

ID: `2408.13608` | Theme: Data/Indic speech | Status: `selected_fulltext_review_plus_scoped_core_crosscheck`

Source: https://arxiv.org/pdf/2408.13608

Snapshot SHA-256: `4ac8cb86f742e6273387fcbdbbf9f4b7135a94589cfa00ce73e3870e59670b0a`

Abstract extract: Speech-language multi-modal learning presents a significant challenge due to the fine nuanced information inherent in speech styles. Therefore, a large-scale dataset providing elaborate comprehension of speech style is urgently needed to facilitate insightful interplay between speech audio and natural language. However, constructing such datasets presents a major trade-off between large-scale data collection and high-quality annotation. To tackle this challenge, we propose an automatic speech annotation system for expressiveness interpretation that annotates in-the-wild speech clips with expressive and vivid human language descriptions. Initially, speech audios are processed by a series of e

**Method-oriented passage (PDF p. 4)**

Signal Processing Tools. We utilize traditional signal processing tools to analyze audio signals and further predict acoustic proper- ties such as pitch, energy, and speed. Speed and energy labels are categorized three-fold. As to the pitch label, following the precedent standard of Audiobox [42], we obey the common sense that female tends to have a higher pitch than male, setting categories of pitch by gender. Speaker Information Identification. With the rapid develop- ment of large-scale audio representative learning methods, the high-level speaking features are well-detected by the hidden lay- ers of powerful audio encoders. The pre-traine

**Results-oriented passage (PDF p. 6)**

based age and gender classification model achieved precisions of 97.72% and 87.7% respectively on the AISHELL 3 dataset, which provides authentic speaker information. The officially released fine- tuned version of Emotion2vec [26] model for speech emotion recog- nition task outperformed other SERs with an accuracy of 84% on the internal English emotion dataset. To evaluate the performance of SECap [48], which describes speech emotion with short sen- tences, we employed ChatGPT to summarize the main emotional tendency of the captioned sentence within the range of single-word emotions. The results indicated that the accuracy of the summary of S

**Caveat-oriented passage (PDF p. 2)**

natural language, both for expressive speech language understanding (SLU) and controllable speech synthesis. It is widely acknowledged that human annotation datasets are typically costly, time-consuming, and limited in scope. To tackle the trade-off between large-scale data collection and high-quality annotation, we develop an automatic speech anno

Additional interpretation and limitations: [core findings](CORE_FINDINGS.md).

## 169. MaskGCT: Zero-Shot Text-to-Speech with Masked Generative Codec Transformer

ID: `2409.00750` | Theme: Representations/codecs | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2409.00750

Snapshot SHA-256: `6dd855c9ae03d6e4c98c03b0ac227ef9b19b3f6640e61103e3794a240807b3c3`

Abstract extract: The recent large-scale text-to-speech (TTS) systems are usually grouped as autoregressive and non-autoregressive systems. The autoregressive systems implicitly model duration but exhibit certain deficiencies in robustness and lack of duration controllability. Non-autoregressive systems require explicit alignment information between text and speech during training and predict durations for linguistic units (e.g. phone), which may compromise their naturalness. In this paper, we introduce Masked Generative Codec Transformer (MaskGCT), a fully non-autoregressive TTS model that eliminates the need for explicit alignment information between text and speech supervision, as well as phone-level durat

**Method-oriented passage (PDF p. 2)**

In this work, we propose MaskGCT, a fully non-autoregressive model for text-to-speech synthesis that uses masked generative transformers without requiring text-speech alignment supervision and phone-level duration prediction. MaskGCT is a two-stage system, both stages are trained using the mask-and-predict learning paradigm. The first stage, the text-to-semantic (T2S) model, predicts masked semantic tokens with in-context learning, using text token sequences and prompt speech semantic token sequences as the prefix, without explicit duration prediction. The second stage, the semantic-to-acoustic (S2A) model, utilizes semantic tokens to predict

**Results-oriented passage (PDF p. 7)**

Table 2: Evaluation results for MaskGCT and the baseline methods on LibriSpeech test-clean, SeedTTS test-en, SeedTTS test-zh. The boldface denotes the best result, the underline denotes the second best. gt length denotes the result obtained by using ground truth total speech length. The results in ‘()’ means the result is the best one selected from five random samples (rerank 5).

**Caveat-oriented passage (PDF p. 2)**

inference. Some previous works have attempted to introduce masked generative models into the field of TTS. SoundStorm [19] was the first attempt to use a masked generative transformer to predict multi-layer acoustic tokens extracted from SoundStream, conditioned on speech semantic tokens; however, it needs to receive the semantic tokens of an AR mo

## 170. IndicVoices-R: Unlocking a Massive Multilingual Multi-speaker Speech Corpus for Scaling Indian TTS

ID: `2409.05356` | Theme: Data/Indic speech | Status: `selected_fulltext_review_plus_scoped_core_crosscheck`

Source: https://arxiv.org/pdf/2409.05356

Snapshot SHA-256: `0a760298e57926bea32c98a2d32ebe21f26d142639b3ee41da235c209bcfd4f8`

Abstract extract: Recent advancements in text-to-speech (TTS) synthesis show that large-scale models trained with extensive web data produce highly natural-sounding output. However, such data is scarce for Indian languages due to the lack of high-quality, manually subtitled data on platforms like LibriVox or YouTube. To address this gap, we enhance existing large-scale ASR datasets containing natural conversations collected in low-quality environments to generate high-quality TTS training data. Our pipeline leverages the cross-lingual generalization of denoising and speech enhancement models trained on English and applied to Indian languages. This results in IndicVoices-R (IV-R), the largest multilingual Indi

**Method-oriented passage (PDF p. 2)**

We propose a pipeline to denoise and enhance ASR data, effectively addressing the poor quality of au- dio samples, which often include background noise, intermittent chatter, echoes, and high reverb. Such data is frequently collected at a lower sampling rate of 16 KHz, compared to the 48 KHz typically found in professional studio recordings. We leverage the significant progress in Speech Enhancement and Restoration models to effectively address these is- sues. We find that these models, although pre-trained on English, show good cross-lingual generalization and can enhance Indian speech data without affect- ing intelligibility. Using the prop

**Results-oriented passage (PDF p. 9)**

observed in Table 5, VoiceCraft fine-tuned on INDICVOICES-R achieves better speaker similarity scores on the zero-shot benchmark with nearly on-par N-MOS compared to the model fine-tuned on IndicTTS.

**Caveat-oriented passage (PDF p. 2)**

Achieving Human-level Speech Quality NaturalSpeech [14] is a pioneering work that achieved human-level speech quality in neural TTS with large-scale phoneme encoder pre-training and im- proved architectures leveraging fully end-to-end training. Similarly, StyleTTS2 [15] surpasses the quality of human recordings by using multiple techniques such as 

Additional interpretation and limitations: [core findings](CORE_FINDINGS.md).

## 171. Enhancing Emotional Text-to-Speech Controllability with Natural Language Guidance through Contrastive Learning and Diffusion Models

ID: `2409.06451` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2409.06451

Snapshot SHA-256: `25809604d28ea9be8e0c919ea0ab336ce660ed6ea7a7e559242f04e5ab9dc4d7`

Abstract extract: While current emotional text-to-speech (TTS) systems can generate highly intelligible emotional speech, achieving fine control over emotion rendering of the output speech still remains a significant challenge. In this paper, we introduce ParaEVITS, a novel emotional TTS framework that leverages the compositionality of natural language to enhance control over emotional rendering. By incorporating a text-audio encoder inspired by ParaCLAP, a contrastive language-audio pretraining (CLAP) model for computational paralinguistics, the diffusion model is trained to generate emotional embeddings based on textual emotional style descriptions. Our framework first trains on reference audio using the au

**Method-oriented passage (PDF p. 1)**

Abstract—While current emotional text-to-speech (TTS) systems can generate highly intelligible emotional speech, achieving fine control over emotion rendering of the output speech still remains a significant challenge. In this paper, we introduce ParaEVITS, a novel emotional TTS framework that leverages the composi- tionality of natural language to enhance control over emotional rendering. By incorporating a text-audio encoder inspired by ParaCLAP, a contrastive language-audio pretraining (CLAP) model for computational paralinguistics, the diffusion model is trained to generate emotional embeddings based on textual emotional style description

**Results-oriented passage (PDF p. 4)**

that produces multiple ‘candidate’ outputs for a given prompt and lets the user select the most suitable one. Participants rated the emotional similarity of each pair on a 5-point scale, where 1 indicates completely different emotional styles (worst), and 5 indicates that the samples have identical emotional styles with distinct expressions (best). Additionally, we categorized the score range into three distinctive classes: score < 3 indicates that the two samples contain different emotions, score = 3 shows that the two samples have identical emotions but with minor difference in style, and score > 3 means that the two samples have the same e

**Caveat-oriented passage (PDF p. 2)**

note that in the Text-to-Image field, the text embedding of CLIP [30] can still be transformed into an image by the image decoder with only minimal loss of detail [31]. However, preliminary experiments with ParaCLAP-NP revealed that using its text embeddings directly as emotion embeddings in eVITS led to unintelligible speech generation. This highl

## 172. NDVQ: Robust Neural Audio Codec with Normal Distribution-Based Vector Quantization

ID: `2409.12717` | Theme: Representations/codecs | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2409.12717

Snapshot SHA-256: `dac5a0e68e478e6ad5b600ecc3cbfbaf647ec826dace7ce379ca62cceaa8b8f8`

Abstract extract: Built upon vector quantization (VQ), discrete audio codec models have achieved great success in audio compression and auto-regressive audio generation. However, existing models face substantial challenges in perceptual quality and signal distortion, especially when operating in extremely low bandwidth, rooted in the sensitivity of the VQ codebook to noise. This degradation poses significant challenges for several downstream tasks, such as codec-based speech synthesis. To address this issue, we propose a novel VQ method, Normal Distribution-based Vector Quantization (NDVQ), by introducing an explicit margin between the VQ codes via learning a variance. Specifically, our approach involves mapp

**Method-oriented passage (PDF p. 2)**

Due to the susceptibility to noise, codebook collapse, and low code- book usage, audio compression with high fidelity and low bitrate is still a challenging task for neural codec modeling. To deal with these problems, in this section, we introduce our new codec model NDVQ. For a given audio x ∈[−1, 1]T , where T is the total number of samples, calculated as T = d×sr with duration d and sample rate sr, our objective is to compress and transmit this audio information using the fewest possible bits without compromising quality.

**Results-oriented passage (PDF p. 4)**

We compared our model with the previous SOTA audio compres- sion model EnCodec across various bandwidths, specifically 1.5, 3, 6, 12, 24. We use the LibriTTS test-other [14] subset as our test dataset. To evaluate the model’s performance from a comprehensive perspective, we use various criteria related to perceptual quality and signal distortion. Detailed descriptions follow Table 2. Perceptual Quality Assessment Metrics: To simulate the human hearing perception of reconstructed audio quality, we employed the Perceptual Evaluation of Speech Quality (PESQ) [15] and VISQOL [16]. Following VISQOL general guidelines, we col- lect 8∼10s audios and

**Caveat-oriented passage (PDF p. 3)**

where Meli denotes a 64-bin mel-spectrogram with a window size selected from the set {32, 64, 128, 256, 512, 1024, 2048}, and a hop length chosen from {4, 8, 16, 32, 64, 128, 256}. |s| represents the number of windows. Codebook Loss VQ models can be optimized by gradient or exponential moving average (EMA) updates [13]. For the former, we minimize 

## 173. Audio Codec Augmentation for Robust Collaborative Watermarking of Speech Synthesis

ID: `2409.13382` | Theme: Representations/codecs | Status: `excluded_after_screening`

Source: https://arxiv.org/pdf/2409.13382

Snapshot SHA-256: `6e131ef42cc759f9f3708945a6a5d8bd276723966af1e5bc5c576cf0c89a3e73`

Excluded: Watermark robustness is outside the selected Track 2 research question

Abstract extract: Automatic detection of synthetic speech is becoming increasingly important as current synthesis methods are both near indistinguishable from human speech and widely accessible to the public. Audio watermarking and other active disclosure methods of are attracting research activity, as they can complement traditional deepfake defenses based on passive detection. In both active and passive detection, robustness is of major interest. Traditional audio watermarks are particularly susceptible to removal attacks by audio codec application. Most generated speech and audio content released into the wild passes through an audio codec purely as a distribution method. We recently proposed collaborative

**Method-oriented passage (PDF p. 4)**

Equal error rates (EERs) are listed in Table I. Table columns represent various codec augmentation configurations, while rows correspond to evaluation conditions. Columns alternate between Ob- server and Collaborator training (labeled ‘o’ and ‘c’, respectively) for otherwise matching configurations. System augmented with DAC has only seen DAC during training, while the systems with MP3/Opus augmentation choose one of the codecs randomly. The leftmost column used no codec augmentation and corresponds to fine-tuning the detector and HiFi-GAN models. The rightmost column for ‘MP3/Opus all’ has seen both MP3 and Opus at all four bitrates. Detecti

**Results-oriented passage (PDF p. 2)**

Watermarking methods have various applications, and the specific application guides what trade-offs should be made with robustness, perceptibility, and capacity [20]. For disclosing generated content, ro- bustness is highly important, and watermark should be imperceptible enough not to hinder the primary use of generated content. However, useful capacity can potentially be as low as zero bits for a binary real/fake detection [18], i.e., the watermark is present if a sample is detected as fake. Classic signal processing-based audio watermarking techniques include spread spectrum [21], phase coding [22], echo hiding [23], spectral patchwork sta

**Caveat-oriented passage (PDF p. 2)**

2) Observer attempts to passively classify between real and generated waveforms. However, no gradients are passed to the generator and the Generator is agnostic to the observer. This corresponds to classic anti-spoofing countermeasure training. 3) Collaborator attempts to classify between real and generated samples, and the generator is actively tr

## 174. ESPnet-Codec: Comprehensive Training and Evaluation of Neural Codecs for Audio, Music, and Speech

ID: `2409.15897` | Theme: Representations/codecs | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2409.15897

Snapshot SHA-256: `ff3d32263679a1188193110177dd5e244a01a1c9d79f7f90fbf06d591f8bf7f2`

Abstract extract: Neural codecs have become crucial to recent speech and audio generation research. In addition to signal compression capabilities, discrete codecs have also been found to enhance downstream training efficiency and compatibility with autoregressive language models. However, as extensive downstream applications are investigated, challenges have arisen in ensuring fair comparisons across diverse applications. To address these issues, we present a new open-source platform ESPnet-Codec, which is built on ESPnet and focuses on neural codec training and evaluation. ESPnet-Codec offers various recipes in audio, music, and speech for training and evaluation using several widely adopted codec models. T

**Method-oriented passage (PDF p. 2)**

of models from different toolkits [17, 18, 23, 24, 34, 36]. Notably, some of the best publicly available pre-trained models are not asso- ciated with public datasets [23, 35]. Moreover, there has been a need for a uniﬁed yet comprehen- sive evaluation toolkit for signal quality measures. Existing toolkits either do not support in-toolkit evaluation or provide limited eval- uation metrics. In Table 1, AcademiCodec, DAC, AudioCraft, and FunCodec provide evaluation protocols, but all of them support only a few metrics for evaluation.2 When using only one or two metrics, potential biases can be easily introduced (see Sec. 4 for analysis). In cont

**Results-oriented passage (PDF p. 5)**

The results of LibriTTS-base experiments are shown in Table 3. In general, our reproduced codec models achieve performance compa- rable to existing codec implementations, with notably better perfor- mance on WER by Whisper. We also observe diverse differences across various evaluation metrics, as no single model achieves the best scores in all metrics. For instance, while the original DAC per- forms better in several metrics, it has much worse WER by Whisper compared to FunCodec. This ﬁnding supports our motivation for proposing VERSA, as discussed in Sec. 2. Within ESPnet-Codec models, Encodec shows the best performance in most metrics, whil

**Caveat-oriented passage (PDF p. 3)**

As discussed in Sec. 2, previous codec-related toolkits typically sup- port a limited set of evaluation metrics, leading to discrepancies in metric selection. Moreover, reported numbers can vary due to dif- ferences in hyper-parameter setups or the downstream models used for evaluation. Additionally, some metrics, while demonstrating su- perior qua

## 175. Description-based Controllable Text-to-Speech with Cross-Lingual Voice Control

ID: `2409.17452` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2409.17452

Snapshot SHA-256: `da4aa88918760456abbb58b82e44784b5b6309a063dfe208704adf32fe012bae`

Abstract extract: We propose a novel description-based controllable text-to-speech (TTS) method with cross-lingual control capability. To address the lack of audio-description paired data in the target language, we combine a TTS model trained on the target language with a description control model trained on another language, which maps input text descriptions to the conditional features of the TTS model. These two models share disentangled timbre and style representations based on self-supervised learning (SSL), allowing for disentangled voice control, such as controlling speaking styles while retaining the original timbre. Furthermore, because the SSL-based timbre and style representations are language-agno

**Method-oriented passage (PDF p. 2)**

Due to the modularized structure of our framework, we adopt the following three-stage training. NANSY++: First, we train a NANSY++ model using an unlabeled audio-only dataset, which may contain diverse data from multiple languages. In this stage, contrastive loss, multi-resolution short-time Fourier transform (STFT) loss, and adversarial loss are employed to obtain disentangled representations and enable high-fidelity recon- struction of waveforms. TTS acoustic model: Second, we train the TTS acoustic model using the target language’s TTS dataset. To extract the target features of the TTS acoustic model, we use a pre-trained NANSY++ analyzer.

**Results-oriented passage (PDF p. 4)**

tems, making the baseline system (C2) perform worse in naturalness. (3) Our proposed method performed best regarding audio-description consistency for both languages, significantly outperforming the base- line systems (C4 vs. C2). Furthermore, there was no statistically significant difference (in a student’s t-test with a 5 % significance level) in the consistency compared to zero-shot TTS and reference speech (C4 vs. Z1 and C4 vs. R1), suggesting sufficient controllability of our method. Meanwhile, in terms of naturalness, we observed that zero-shot TTS performed much worse than the best description TTS system (C4 vs. Z1). In addition, for J

**Caveat-oriented passage (PDF p. 4)**

We proposed a description-based controllable TTS method with cross-lingual control capability. We demonstrated the feasibility of description-based control across different languages by employing language-agnostic disentangled representations derived from SSL- based models. Experiments on English and Japanese TTS confirmed that our method effective

## 176. Moshi: a speech-text foundation model for real-time dialogue

ID: `2410.00037` | Theme: Evaluation/reliability | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2410.00037

Snapshot SHA-256: `ea702589e103f8d02b4fbec733c556b08d136c2ccaa013eb48a91a7366c7e390`

Abstract extract: We introduce Moshi, a speech-text foundation model and full-duplex spoken dialogue framework. Current systems for spoken dialogue rely on pipelines of independent components, namely voice activity detection, speech recognition, textual dialogue and text-to-speech. Such frameworks cannot emulate the experience of real conversations. First, their complexity induces a latency of several seconds between interactions. Second, text being the intermediate modality for dialogue, non-linguistic information that modifies meaning -- such as emotion or non-speech sounds -- is lost in the interaction. Finally, they rely on a segmentation into speaker turns, which does not take into account overlapping sp

**Method-oriented passage (PDF p. 2)**

Yet, the experience offered by these interfaces remains far from natural conversations. First, latency compounds along the many components of these pipelines, resulting in a typical global latency of several seconds. This is unlike natural conversations which demon- strate response times of a few hundred milliseconds. Second, as language understanding and generation happens in the textual domain, any non-written information is ignored by the model. This goes from paralinguistic information, such as emotion and accent, to non-speech audio, such as surrounding acoustic events. Finally, these models remain fun- damentally turn-based, assuming th

**Results-oriented passage (PDF p. 11)**

Transformers prove to be useful with regard to perceived audio quality, while Transformer in the encoder also improves the distillation of semantic information described below (see Table 3 for ablation studies).

**Caveat-oriented passage (PDF p. 5)**

Speech-text Models. Such models typically start from a pretrained text language model and either finetune it to predict audio (Hassid et al., 2023), or propose a speech-text finetun- ing task (Rubenstein et al., 2023; Maiti et al., 2023; Nachmani et al., 2024; Nguyen et al., 2024; Mitsui et al., 2024; Zhang et al., 2024a): For instance, AudioPALM (

## 177. F5-TTS: A Fairytaler that Fakes Fluent and Faithful Speech with Flow Matching

ID: `2410.06885` | Theme: Speech/audio generation and control | Status: `selected_fulltext_review_plus_scoped_core_crosscheck`

Source: https://arxiv.org/pdf/2410.06885

Snapshot SHA-256: `ee2aa766bd6ad9395967dfdaed70f948713cba9859d6fcbb6283908714b899f3`

Abstract extract: This paper introduces F5-TTS, a fully non-autoregressive text-to-speech system based on flow matching with Diffusion Transformer (DiT). Without requiring complex designs such as duration model, text encoder, and phoneme alignment, the text input is simply padded with filler tokens to the same length as input speech, and then the denoising is performed for speech generation, which was originally proved feasible by E2 TTS. However, the original design of E2 TTS makes it hard to follow due to its slow convergence and low robustness. To address these issues, we first model the input with ConvNeXt to refine the text representation, making it easy to align with the speech. We further propose an in

**Method-oriented passage (PDF p. 2)**

ral and realistic synthesized results. However, we found that robustness issues exist in E2 TTS for the text and speech alignment. Seed-TTS (Anas- tassiou et al., 2024) employs a similar strategy and achieves excellent results, though not elaborated in model details. In these ways of not explicitly modeling phoneme-level duration, models learn to assign the length of each word or phoneme accord- ing to the given total sequence length, resulting in improved prosody and rhythm. In this paper, we propose F5-TTS, a Fairytaler that Fakes Fluent and Faithful speech with Flow matching. Maintaining the simplicity of pipeline without phoneme alignment

**Results-oriented passage (PDF p. 7)**

Table 2: Results on two test sets, Seed-TTS test-en and test-zh. The boldface indicates the best result, the underline denotes the second best, and * denotes scores reported in baseline papers.

**Caveat-oriented passage (PDF p. 9)**

There are two limitations to this work. First, al- though F5-TTS accelerates the training and infer- ence while maintaining the simplicity of the system through better structure design, the mel spectro- gram sequence length is still much longer than the text modality. Therefore, research and employ- ment of a more efficient and hopefully universal 

Additional interpretation and limitations: [core findings](CORE_FINDINGS.md).

## 178. ERVQ: Enhanced Residual Vector Quantization with Intra-and-Inter-Codebook Optimization for Neural Audio Codecs

ID: `2410.12359` | Theme: Representations/codecs | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2410.12359

Snapshot SHA-256: `db1d50ab299cf2991937dc287efab0ada4c7619d11a5684ce41d178430f4f11c`

Abstract extract: Current neural audio codecs typically use residual vector quantization (RVQ) to discretize speech signals. However, they often experience codebook collapse, which reduces the effective codebook size and leads to suboptimal performance. To address this problem, we introduce ERVQ, Enhanced Residual Vector Quantization, a novel enhancement strategy for the RVQ framework in neural audio codecs. ERVQ mitigates codebook collapse and boosts codec performance through both intra- and inter-codebook optimization. Intra-codebook optimization incorporates an online clustering strategy and a code balancing loss to ensure balanced and efficient codebook utilization. Inter-codebook optimization improves th

**Method-oriented passage (PDF p. 2)**

intra-codebook optimization, we adopt an online clustering strategy and introduce a code balancing loss to tackle the codebook collapse problem and improve the expressiveness of each VQ. Specifically, the online clustering strategy calculates the average codebook usage at each iteration and dynamically reinitializes the codebook based on this usage, ensuring each code vector is optimized. The code balancing loss assumes a uniform prior distribution of codes and improves codebook utilization by minimizing the difference between the prior and posterior code distributions. For inter-codebook optimization, we propose maximizing the difference in 

**Results-oriented passage (PDF p. 11)**

model [48] provided in FunASR8 [49] to transcribe the syn- thesized speech. For reference, it achieved a 2.580% CER and 7.107% WER on the clean test set. Speaker similarity (SS) was assessed by calculating the cosine similarity between the speaker embeddings extracted from Resemblyzer9 [50], a pre- trained speaker verification model for both the prompt speech and the synthesized speech using the Amphion toolkit10 [51]. Additionally, the naturalness of the synthesized speech was evaluated using UTMOS11 [52], a non-intrusive pre-trained scoring network. For subjective evaluation, we conducted a se- ries of listening tests to measure the natural

**Caveat-oriented passage (PDF p. 3)**

the model structure, potentially increasing parameter count and altering the target bitrate, which may complicate its integration into existing codecs. Most notably, these strategies focus primarily on optimizing each VQ module independently, overlooking the hierarchical and residual structure inherent to RVQ. Additionally, prior works have propose

## 179. A Unified Framework for Collecting Text-to-Speech Synthesis Datasets for 22 Indian Languages

ID: `2410.14197` | Theme: Data/Indic speech | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2410.14197

Snapshot SHA-256: `9d464d1fa0f53ebe22e34f13fa87b74bf6e3e2dd04f78822bb457ad8c6c4d4e8`

Abstract extract: The performance of a text-to-speech (TTS) synthesis model depends on various factors, of which the quality of the training data is of utmost importance. Millions of data are collected around the globe for various languages, but resources for Indian languages are few. Although there are many efforts involved in data collection, a common set of protocols for data collection becomes necessary for building TTS systems in Indian languages primarily because of the need for a uniform development of TTS systems across languages. In this paper, we present our learnings on data collection efforts' for Indic languages over 15 years. These databases have been used in unit selection synthesis, hidden Mar

**Method-oriented passage (PDF p. 4)**

A FastSpeech2+HiFi-GAN [18] system was trained for 4 datasets from the IndicTTS23 database. We evaluated the standalone performance10 of these systems using MCD scores. MCD score is an objective measure that determines the distortion in mel-cepstral features of a synthesised speech compared to a reference audio [19]. For the dataset, 20 audio files from the test (not seen during training) were considered for evaluation. MCD scores of the synthesised audio files are given in Table III.

**Results-oriented passage (PDF p. 4)**

The languages Sanskrit and Nepali are not available in the IndicTTS database, resulting in only System A for these datasets. Instead of conducting a MOS-like test for these languages, a degradation MOS (DMOS) test was conducted. In the DMOS test, the MOS scores are normalised with respect to the ground-truth audio, presented to the evaluators in random order. From Table V, we see high DMOS scores for System A, indicating human-like audio quality. The DMOS score of Sanskrit is greater than 5, as more than 50% of the evaluators had rated synthesised utterances more than the actual recordings. The feedback given by evaluators was that it was ver

**Caveat-oriented passage (PDF p. 2)**

• While good quality read speech TTS systems are avail- able today, spontaneous speech synthesis is a requirement today. Our early efforts on “conversational-style TTS systems” show that conversational speech has significant variation in prosody, and can be built by adapting read speech systems with a some amount of prosodically rich data [10], [11

## 180. Can Large Audio-Language Models Truly Hear? Tackling Hallucinations with Multi-Task Assessment and Stepwise Audio Reasoning

ID: `2410.16130` | Theme: Captioning/grounding | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2410.16130

Snapshot SHA-256: `8df7715b5a4ddd502aaaa6b88a31e0bb22c4952a3b4d119d91cedf9ab43dd6ec`

Abstract extract: Recent advancements in large audio-language models (LALMs) have shown impressive capabilities in understanding and reasoning about audio and speech information. However, these models still face challenges, including hallucinating non-existent sound events, misidentifying the order of sound events, and incorrectly attributing sound sources, which undermine their reliability and real-world application. To systematically evaluate these issues, we propose three distinct tasks: object existence, temporal order, and object attribute within audio. These tasks assess the models' comprehension of critical audio information aspects. Our experimental results reveal limitations in these fundamental task

**Method-oriented passage (PDF p. 2)**

The temporal order task assesses the models’ capability to deter- mine the sequence of sound events. We source data from the CompA- order [42] dataset. The original CompA-order dataset includes 400 test instances, where each instance contains at least two audio-caption pairs. These pairs feature the same sound events, but the order of the events is different. In this way, each audio sample contains two distinct sounds with a clear temporal relationship. We test the model’s understanding of temporal information in the audio by using prompt text such as “Does the sound of a dog barking occur before the sound of a car horn honking in the audio?”

**Results-oriented passage (PDF p. 4)**

ground truth is “yes”, while the “after” segment is “no” due to manipulations like removing or reordering sound events, or changing their sources. High C-I scores indicate that, even when models answer the “before” question correctly, they often fail to fully comprehend the audio. These findings underscore key areas where current models need improvement in audio understanding. For the emphasis setting, some baseline models improve their recall and F1 scores when sound events were highlighted with parentheses. This is observed in models like Qwen-Audio-Chat, Qwen2-Audio- Instruct, and Gemini. We also experiment with using bold text in markdown

**Caveat-oriented passage (PDF p. 1)**

Abstract—Recent advancements in large audio-language models (LALMs) have shown impressive capabilities in understanding and reasoning about audio and speech information. However, these models still face challenges, including hallucinating non-existent sound events, misidentifying the order of sound events, and incorrectly attributing sound sources,

## 181. MMAU: A Massive Multi-Task Audio Understanding and Reasoning Benchmark

ID: `2410.19168` | Theme: Evaluation/reliability | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2410.19168

Snapshot SHA-256: `455dbfa3f7cb020120e3e0d0c624f707324e9596dd3b26b8c82e9b855580d41a`

Abstract extract: The ability to comprehend audio--which includes speech, non-speech sounds, and music--is crucial for AI agents to interact effectively with the world. We present MMAU, a novel benchmark designed to evaluate multimodal audio understanding models on tasks requiring expert-level knowledge and complex reasoning. MMAU comprises 10k carefully curated audio clips paired with human-annotated natural language questions and answers spanning speech, environmental sounds, and music. It includes information extraction and reasoning questions, requiring models to demonstrate 27 distinct skills across unique and challenging tasks. Unlike existing benchmarks, MMAU emphasizes advanced perception and reasonin

**Method-oriented passage (PDF p. 2)**

Our Contributions. We present MMAU, the first comprehensive benchmark tailored for multi- modal audio understanding and reasoning. MMAU features over 10,000 expertly annotated audio- question-response pairs evenly distributed across speech, sound, and music domains. With informa- tion extraction and reasoning questions that require models to demonstrate proficiency in 27 distinct skills across unique tasks, MMAU achieves significant breadth. Additionally, it covers depth by in- cluding tasks that require advanced reasoning, such as multi-speaker role mapping, emotional shift detection, and temporal acoustic event analysis. Our audio data is s

**Results-oriented passage (PDF p. 7)**

Table 3: Performance comparison of various LALMs and LLMs on the test subset of MMAU across sound, speech, and music domains. Human evaluation results are shown for the MMAU test-mini split. We also mark if the training data used to train these models include either of speech, sound or music. The best-performing models in each category are highlighted in bold, and the second-best scores are underlined.

**Caveat-oriented passage (PDF p. 2)**

Figure 2: Examples from the MMAU benchmark illustrating the diverse range of reasoning and information extraction tasks across the domains of sound, speech, and music. Each task involves rich, context-specific audio paired with human-annotated QA pairs that require expert-level knowledge and reasoning abilities. The benchmark covers a wide range of

## 182. Augmenting Polish Automatic Speech Recognition System With Synthetic Data

ID: `2410.22903` | Theme: Loop/data selection | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2410.22903

Snapshot SHA-256: `72c746f6060f4a380fbebdee2545e8e3b3d859cb5b8f0ffbc90c41d6fe07ef57`

Abstract extract: This paper presents a system developed for submission to Poleval 2024, Task 3: Polish Automatic Speech Recognition Challenge. We describe Voicebox-based speech synthesis pipeline and utilize it to augment Conformer and Whisper speech recognition models with synthetic data. We show that addition of synthetic speech to training improves achieved results significantly. We also present final results achieved by our models in the competition.

**Method-oriented passage (PDF p. 2)**

As our approach focuses mainly on utilization of synthetic data for augmentation of ASR system, we decided to use two standard speech recognition models without any modifications. Both models utilize BPE text tokenization scheme.

**Results-oriented passage (PDF p. 4)**

Results of our internal evaluations are shown in Table 3. We provide results for both Conformer and Whisper models trained on all studied training datasets. For comparison, we also evaluated Whisper without any fine-tuning. Results confirm that the addition of synthetic data improves quality of both models. The results are also not clearly saturated even in the case of mix-01 where total duration of training data was almost tripled. Addition of synthetic data seems to have more impact on the results of Conformer model - between mix-01 and baseline, total WER was reduced by 4.77, whereas in the case of Whisper it was reduced only by 2.32. This

**Caveat-oriented passage (PDF p. 2)**

However, augmentation with synthetic speech presented challenges due to the differences between synthetic and real data. This problem was addressed with the development of zero-shot voice-cloning TTS systems such as VALL-E X [20] and Voicebox [21]. Authors of Voicebox compared performance of ASR systems trained on real and synthetic data and observ

## 183. MACE: Leveraging Audio for Evaluating Audio Captioning Systems

ID: `2411.00321` | Theme: Captioning/grounding | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2411.00321

Snapshot SHA-256: `30b777c9ac87fef341a073bf395a3830b89693991bd6d53e2d42c4dd325352a4`

Abstract extract: The Automated Audio Captioning (AAC) task aims to describe an audio signal using natural language. To evaluate machine-generated captions, the metrics should take into account audio events, acoustic scenes, paralinguistics, signal characteristics, and other audio information. Traditional AAC evaluation relies on natural language generation metrics like ROUGE and BLEU, image captioning metrics such as SPICE and CIDEr, or Sentence-BERT embedding similarity. However, these metrics only compare generated captions to human references, overlooking the audio signal itself. In this work, we propose MACE (Multimodal Audio-Caption Evaluation), a novel metric that integrates both audio and reference ca

**Method-oriented passage (PDF p. 2)**

gle in audio captioning, where diverse descriptions can ac- curately represent the same sound. Advanced metrics like METEOR [7] introduced synonym-matching and stemming for better semantic alignment, while CIDEr [19] used TF-IDF weighting to emphasize rare, meaningful N-grams. SPICE, developed for image captioning, compares “object-graphs” between captions to model conceptual relationships, and SPI- DEr [20], combining SPICE and CIDEr, aimed to improve robustness and alignment with human judgment. Embedding-based metrics. BERT-score [21], BLUERT [22] and Sentence-BERT encode candidate and reference sentences as vectors using pre-trained langu

**Results-oriented passage (PDF p. 3)**

To evaluate the effectiveness of MACE, we conducted comprehensive benchmarking experiments on two widely- used datasets: Clotho-Eval and AudioCaps-Eval. The task consists of evaluating a pair of captions and selecting the better caption of the two. One of the captions in each pair is the preferred caption based on the scores assigned by human evaluators. TThe primary metric for comparison is pair accuracy, which measures a metric’s ability to correctly identify the human-preferred caption in each pair. To better understand and analyze the results, the tests are categorized into four groups: HC (two correct human captions), HI (one correct and

**Caveat-oriented passage (PDF p. 1)**

sentence-BERT embeddings. However, a key limitation of existing metrics is their exclusion of audio information and needing reference captions to perform evaluation. We hypothesize that incorporating audio information into AAC metrics will enhance semantic accuracy and better align with human judgment. Audio information can be integrated ei- ther t

## 184. I2TTS: Image-indicated Immersive Text-to-speech Synthesis with Spatial Perception

ID: `2411.13314` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2411.13314

Snapshot SHA-256: `ce3551bfb2030e65c659435a7f4e4f7704b40dac1cce2cda905e5842c4a72b5e`

Abstract extract: Controlling the style and characteristics of speech synthesis is crucial for adapting the output to specific contexts and user requirements. Previous Text-to-speech (TTS) works have focused primarily on the technical aspects of producing natural-sounding speech, such as intonation, rhythm, and clarity. However, they overlook the fact that there is a growing emphasis on spatial perception of synthesized speech, which may provide immersive experience in gaming and virtual reality. To solve this issue, in this paper, we present a novel multi-modal TTS approach, namely Image-indicated Immersive Text-to-speech Synthesis (I2TTS). Specifically, we introduce a scene prompt encoder that integrates vi

**Method-oriented passage (PDF p. 4)**

To further evaluate our model’s robustness across diverse acoustic conditions, we analyze performance separately in wide and narrow environments. As shown in Table II, our pro- posed method significantly outperforms ViT-TTS and MS2KU- VTTS in both scenarios. In wide environments, which typically exhibit longer reverberation tails and more diffuse reflections, our model achieves the lowest Scene Reverb Error (SRE) at 25.3% and the highest IMOS score of 4.01. This suggests that the model is more capable of capturing complex spatial cues from wide scenes, leading to more immersive and perceptually accurate reverberation. In narrow environments, 

**Results-oriented passage (PDF p. 4)**

Table I presents the objective and subjective evaluation results across different models. Compared to the baseline and prior scene-aware TTS systems (ViT-TTS and MS2KU- VTTS), our proposed method consistently achieves superior performance across nearly all metrics.From the objective per- spective, our full model attains the lowest WER (7.6%) and MCD (4.22), indicating enhanced intelligibility and spectral fidelity. Furthermore, it shows a notable improvement in SRE, reducing the mismatch between predicted and target scene acoustics to 27.2%, a significant gain over ViT-TTS (64.2%) and MS2KU-VTTS (57.1%). The SECS also improves to 0.62, demons

**Caveat-oriented passage (PDF p. 2)**

Reverberation modeling has traditionally been addressed in the field of audio signal processing, where techniques such as convolution with room room impulse responses (RIR) are used to simulate the effects of different acoustic environments on speech. In the context of speech synthesis, reverberation is often applied as a post-processing step, wher

## 185. Speech Separation using Neural Audio Codecs with Embedding Loss

ID: `2411.17998` | Theme: Representations/codecs | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2411.17998

Snapshot SHA-256: `a61e1a3232ebc2c05d2bf09f889cdf19afb6437d051db150d95d033543fce919`

Abstract extract: Neural audio codecs have revolutionized audio processing by enabling speech tasks to be performed on highly compressed representations. Recent work has shown that speech separation can be achieved within these compressed domains, offering faster training and reduced inference costs. However, current approaches still rely on waveform-based loss functions, necessitating unnecessary decoding steps during training. We propose a novel embedding loss for neural audio codec-based speech separation that operates directly on compressed audio representations, eliminating the need for decoding during training. To validate our approach, we conduct comprehensive evaluations using both objective metrics a

**Method-oriented passage (PDF p. 2)**

• We investigate the impact of pre-training data quantity and diversity on separation performance, comparing sep- aration using the DAC model trained on open source datasets, LibriTTS, AMUSE, and the original DAC [13] dataset. II. METHODOLOGY In this work we propose Codecformer-EL, based on the recently proposed Codecformer [21], which modifies the train- ing method for Codecformer by employing embedding loss as shown in Figure 1. While Codecformer utilizes both the encoder and decoder of the neural audio codec and performs waveform comparison loss, Codecformer-EL only requires the encoder. The loss computed is mean squared error (MSE) loss w

**Results-oriented passage (PDF p. 4)**

B. Comparison between Codecformer-EL and Codecformer Table II presents the separation performance of three neural audio codecs pre-trained on the AMUSE dataset, comparing our Codecformer-EL (embedding loss) method with the orig- inal Codecformer (waveform loss) approach. A consistent pattern emerges: Codecformer models achieve higher scores on objective metrics (SI-SDR, SI-SDRi, SDR, SDRi), while Codecformer-EL models perform better on per- ceptual metrics, despite lower objective scores. This discrep- ancy highlights a known limitation of objective waveform- matching metrics for evaluating resynthesized speech [30]. The neural audio codec’s 

**Caveat-oriented passage (PDF p. 5)**

In this paper, we introduced Codecformer-EL, a novel ap- proach to speech separation that leverages neural audio codecs and employs an embedding-level loss function. Our method demonstrates significant improvements in computational effi- ciency and training speed compared to previous approaches, while maintaining comparable or superior perceptual q

## 186. AlignFormer: Modality Matching Can Achieve Better Zero-shot Instruction-Following Speech-LLM

ID: `2412.01145` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2412.01145

Snapshot SHA-256: `043bdcff66b57f69106da1716aa9f83a45f07aedc418c0e1135377dc2ffcc093`

Abstract extract: Integrating speech into LLM (speech-LLM) has gaining increased attention recently. The mainstream solution is to connect a well-trained speech encoder and LLM with a neural adapter. However, the length mismatch between the speech and text sequences are not well handled, leading to imperfect modality matching between the speech and text. In this work, we propose a novel neural adapter, AlignFormer, to reduce the length gap between the two modalities. AlignFormer consists of CTC and dynamic-window QFormer layers, where the CTC alignment provides the dynamic window information for QFormer. The LLM backbone is frozen in training to preserve its text capability, especially the instruction followi

**Method-oriented passage (PDF p. 2)**

the performance of these tasks are not as competitive as the instruction-tuned model. [26] and [27] further propose to add emotion and para-lingual information when generating LLM response so that the para-lingual information can be preserved in speech encoder. [28] reveals the similar zero-shot behaviour with ASR training data only. Overall, the prior methods unlock the instruction-following speech-LLM through data efforts and do not consider a well-aligned speech and text joint space except [28]. Consequently, the model performance would be limited. Moreover, we are lacking a systematic way to track the instruction following capability of t

**Results-oriented passage (PDF p. 6)**

reduce the token rate as an adapter. The window size for qformer is 4, leading to a 320ms token rate which is close to that of AlignFormer for LLM inputs. The zero-shot results of WavLLM data are reported in Table III including the task metrics and the IFR (except ASR on Librispeech clean and other data). The results of cascaded whisper + LLM and those in WavLLM paper are presented in the table for reference. Note that the WavLLM results in the second row is with instruction tuning stage using in-domain training data. For the ASR tasks, we use the repeat prompt during evaluation. The poor performance of E1 on Librispeech is due to the halluci

**Caveat-oriented passage (PDF p. 3)**

where I is the task prompt. I can be different for different speech and audio tasks. The speech-LLM can learn to follow these prompts through the instruction tuning stage. To achieve better speech understanding performance, LLM parameters are either full-fintuned or through LoRA finetuning [42]. However, the text capability, especially the instruct

## 187. Towards Controllable Speech Synthesis in the Era of Large Language Models: A Systematic Survey

ID: `2412.06602` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2412.06602

Snapshot SHA-256: `5f098e1936a6d27da629c9103140999d781018d72b68f0f74f34ea2975741823`

Abstract extract: Text-to-speech (TTS) has advanced from generating natural-sounding speech to enabling fine-grained control over attributes like emotion, timbre, and style. Driven by rising industrial demand and breakthroughs in deep learning, e.g., diffusion and large language models (LLMs), controllable TTS has become a rapidly growing research area. This survey provides the first comprehensive review of controllable TTS methods, from traditional control techniques to emerging approaches using natural language prompts. We categorize model architectures, control strategies, and feature representations, while also summarizing challenges, datasets, and evaluations in controllable TTS. This survey aims to guid

**Method-oriented passage (PDF p. 3)**

Method (Non-autoregressive) Zero-shot Controlability Model Architectures Feature Release Pit. Ene. Spe. Pro. Tim. Emo. Env. Des. Acoustic Model Vocoder FastSpeech (Ren et al., 2019) ✓ ✓ Transformer WaveGlow (Prenger et al., 2019) MelS 2019.05 FastSpeech 2 (Ren et al., 2021a) ✓ ✓ ✓ ✓ Transformer Parallel WaveGAN (Yamamoto et al., 2020) MelS 2020.06 FastPitch (Ła´ncucki, 2021) ✓ ✓ Transformer WaveGlow MelS 2020.06 Parallel Tacotron (Elias et al., 2021a) ✓ Transformer + VAE + CNN WaveRNN (Kalchbrenner et al., 2018) MelS 2020.10 StyleTagging-TTS (Kim et al., 2021) ✓ ✓ ✓ Transformer + CNN HiFi-GAN (Kong et al., 2020) MelS 2021.04 SC-GlowTTS (Casan

**Results-oriented passage (PDF p. 7)**

The evolution of TTS control has moved from basic attribute manipulation to sophisticated, instruction- guided synthesis, reflecting AI’s trend toward in- tuitive, fine-grained control. Early methods like style tagging controlled predefined attributes (e.g., pitch, emotion) but offered limited expressive di- versity. Reference speech prompts enabled zero- shot TTS and voice cloning, separating timbre from style for greater personalization. To improve user-friendliness, natural language descriptions (e.g., PromptTTS) allowed users to specify vocal characteristics through text. The latest advance, instruction-guided control, leverages LLMs to i

**Caveat-oriented passage (PDF p. 10)**

We acknowledge several limitations that may af- fect the completeness of our survey. First, this survey does not explore the interactions between controllable attributes. Most existing studies focus on modeling each factor, such as emotion, speaker identity, or prosody, as an independent variable. However, understanding how these attributes in- flu

## 188. LatentSpeech: Latent Diffusion for Text-To-Speech Generation

ID: `2412.08117` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2412.08117

Snapshot SHA-256: `4850ae772950a8ae8fdb555a00c12e3a382c14ce26e824451700366413028735`

Abstract extract: Diffusion-based Generative AI gains significant attention for its superior performance over other generative techniques like Generative Adversarial Networks and Variational Autoencoders. While it has achieved notable advancements in fields such as computer vision and natural language processing, their application in speech generation remains under-explored. Mainstream Text-to-Speech systems primarily map outputs to Mel-Spectrograms in the spectral space, leading to high computational loads due to the sparsity of MelSpecs. To address these limitations, we propose LatentSpeech, a novel TTS generation approach utilizing latent diffusion models. By using latent embeddings as the intermediate rep

**Method-oriented passage (PDF p. 2)**

In this section, we introduce the architecture of La- tentSpeech. We first encode speech A into latent space using an Autoencoder (AE). Then, we set latent embeddings as the intermediate representation Z and train a diffusion-based TTS model to map embeddings. In the end, we generate speech directly from the latent space to the audio space using the trained decoder. An overview of the entire system is provided in Figure 1.

**Results-oriented passage (PDF p. 4)**

WER, we further evaluate the Phoneme-level WER (WER- P) and Style-level WER (WER-S). We assess the accuracy of synthesized speech using WER by first generating speech with a TTS system and then transcribing it through OpenAI’s Whisper API [21]. Result: Table I presents results of our experiment. La- tentSpeech shows significant improvements over FastSpeech and StyleSpeech. Specifically, it achieves a 25% improvement in WER and a 24% improvement in MCD compared to existing baseline models when trained on the 4k sentence dataset. These improvements further increase to 49.5% and 26%, respectively, when the model is trained with the larger 9k sen

**Caveat-oriented passage (PDF p. 1)**

Abstract—Diffusion-based Generative AI gains significant at- tention for its superior performance over other generative tech- niques like Generative Adversarial Networks and Variational Autoencoders. While it has achieved notable advancements in fields such as computer vision and natural language processing, their application in speech generation r

## 189. CosyVoice 2: Scalable Streaming Speech Synthesis with Large Language Models

ID: `2412.10117` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2412.10117

Snapshot SHA-256: `b407f3e132f6ca73adb44f94b8d14963e005d6d61e80b47bc79615b7dddc3e74`

Abstract extract: In our previous work, we introduced CosyVoice, a multilingual speech synthesis model based on supervised discrete speech tokens. By employing progressive semantic decoding with two popular generative models, language models (LMs) and Flow Matching, CosyVoice demonstrated high prosody naturalness, content consistency, and speaker similarity in speech in-context learning. Recently, significant progress has been made in multi-modal large language models (LLMs), where the response latency and real-time factor of speech synthesis play a crucial role in the interactive experience. Therefore, in this report, we present an improved streaming speech synthesis model, CosyVoice 2, which incorporates co

**Method-oriented passage (PDF p. 1)**

In our previous work, we introduced CosyVoice, a multilingual speech synthesis model based on supervised discrete speech tokens. By employing progressive se- mantic decoding with two popular generative models, language models (LMs) and Flow Matching, CosyVoice demonstrated high prosody naturalness, content con- sistency, and speaker similarity in speech in-context learning. Recently, significant progress has been made in multi-modal large language models (LLMs), where the response latency and real-time factor of speech synthesis play a crucial role in the interactive experience. Therefore, in this report, we present an improved stream- ing sp

**Results-oriented passage (PDF p. 10)**

We first evaluated our CosyVoice 2 models on a limited English text domain and compared it with several open-source models, such as ChatTTS [56], GPT-SoVITs [57], OpenVoice [58], ParlerTTS [59], EmotiVoice [60], and its predecessor CosyVoice [34]. The objective results are presented in Table 5, including content consistency (WER), speech quality (NMOS) and speaker similarity (SS). From the table, we can see that CosyVoice 2 achieves state-of-the-art performance on the Librispeech test-clean set, surpassing all baseline models acros all evaluation metrics. Notably, CosyVoice 2 even demonstrates higher content consistency, speech quality, and s

**Caveat-oriented passage (PDF p. 15)**

CosyVoice 2 has several limitations that need to be addressed. First, it supports only a limited number of languages. For languages with overlapping character sets, synthesis performance may degrade, presenting an open challenge for future research. Second, CosyVoice 2 cannot control acoustic characteristics, such as timbre, through textual instruc

## 190. Analysis of Speech Temporal Dynamics in the Context of Speaker Verification and Voice Anonymization

ID: `2412.17164` | Theme: Evaluation/reliability | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2412.17164

Snapshot SHA-256: `343886b84fb6d824dcc417f97c2e1ca91369a7d0b8afbdf49b2b0249edebfe29`

Abstract extract: In this paper, we investigate the impact of speech temporal dynamics in application to automatic speaker verification and speaker voice anonymization tasks. We propose several metrics to perform automatic speaker verification based only on phoneme durations. Experimental results demonstrate that phoneme durations leak some speaker information and can reveal speaker identity from both original and anonymized speech. Thus, this work emphasizes the importance of taking into account the speaker's speech rate and, more importantly, the speaker's phonetic duration characteristics, as well as the need to modify them in order to develop anonymization systems with strong privacy protection capacity.

**Method-oriented passage (PDF p. 1)**

methods use large-scale pre-trained models for extracting speciﬁc attributes and provide better content and privacy preservation than signal processing based methods. The diversity of approaches is illustrated by the VoicePrivacy 2024 Challenge [10], which provided six baseline anonymization systems, namely anonymization using x- vectors and a neural source-ﬁlter model [6], [11], signal processing based anonymization using the McAdams coefﬁcient [2], anonymiza- tion using phonetic transcription and generation of artiﬁcial pseudo- speaker embeddings by a generative adversarial network (GAN) [12] anonymization using neural audio codec (NAC) lan

**Results-oriented passage (PDF p. 3)**

2) SAS-2: SAS-2, proposed in [25], is one of the best systems developed by the VoicePrivacy 2024 Challenge participants in terms of linguistic content and privacy preservation. It is a cascaded ASR- TTS system, where ﬁrst the text transcripts are obtained from the source audio and then a TTS system is used to generate correspond- ing anonymized speech from the obtained transcripts with a new anonymized speaker voice. The ASR model is the medium English Whisper model [26]. The TTS model is VITS (variational inference with adversarial learning for end-to-end text-to-speech, [27]), trained on the LibriTTS dataset [28]. 3) Automatic speaker veriﬁ

**Caveat-oriented passage (PDF p. 2)**

Experiments were conducted on the LibriSpeech2 [23] corpus of read English audiobooks, which was used in all VoicePrivacy Challenge editions. It contains approximately 1,000 hours of speech from 2,484 speakers sampled at 16 kHz. We conducted the ﬁrst series of experiments and analyses on the full LibriSpeech-train-960 dataset that contains data fro

## 191. DrawSpeech: Expressive Speech Synthesis Using Prosodic Sketches as Control Conditions

ID: `2501.04256` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2501.04256

Snapshot SHA-256: `382723b28eec7ae5a8801df9319d1305d91a538e84279a098f7c6c6dcce5e354`

Abstract extract: Controlling text-to-speech (TTS) systems to synthesize speech with the prosodic characteristics expected by users has attracted much attention. To achieve controllability, current studies focus on two main directions: (1) using reference speech as prosody prompt to guide speech synthesis, and (2) using natural language descriptions to control the generation process. However, finding reference speech that exactly contains the prosody that users want to synthesize takes a lot of effort. Description-based guidance in TTS systems can only determine the overall prosody, which has difficulty in achieving fine-grained prosody control over the synthesized speech. In this paper, we propose DrawSpeech

**Method-oriented passage (PDF p. 3)**

where Enc and Dec are the encoder and decoder part of VAE, xrec denotes the reconstructed mel-spectrogram. Secondly, a contour encoder and a sketch encoder are employed to generate conditions for the latent diffusion model (LDM). Specifically, the contour encoder quantizes pitch and energy (P and E during training, and Ppred and Epred during inference) into 256 discrete values, subsequently converting them into pitch embedding Hp ∈RM×F and energy embed- ding He ∈RM×F . The same process takes place in the sketch encoder, except that it utilizes Pske and Eske as inputs and produces pitch sketch embedding Hp ske ∈RM×F and energy sketch embedding

**Results-oriented passage (PDF p. 3)**

1) Dataset: LJSpeech dataset [35] is a widely used speech corpus containing 13,100 short audio clips from a single speaker, each paired with a transcription. The total recording duration is roughly 24 hours. We randomly divided the dataset into three subsets: 12,500 samples for training, 300 for vali- dation, and 300 for testing, with a sample rate of 22,050 Hz. 2) Implementation Details: The text encoder and sketch- to-contour predictor are composed of multiple stacked Trans- former [36] blocks (6 blocks for the former and 2 blocks for the latter). In both, the linear layer in the feed-forward network is replaced by a 1D convolutional layer.

**Caveat-oriented passage (PDF p. 1)**

Abstract—Controlling text-to-speech (TTS) systems to synthe- size speech with the prosodic characteristics expected by users has attracted much attention. To achieve controllability, current studies focus on two main directions: (1) using reference speech as prosody prompt to guide speech synthesis, and (2) using natural language descriptions to co

## 192. A Domain Adaptation Framework for Speech Recognition Systems with Only Synthetic data

ID: `2501.12501` | Theme: Loop/data selection | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2501.12501

Snapshot SHA-256: `f08bf5697f48dde974a95023eb436d67d1d12efaea96988927df200b8f689183`

Abstract extract: We introduce DAS (Domain Adaptation with Synthetic data), a novel domain adaptation framework for pre-trained ASR model, designed to efficiently adapt to various language-defined domains without requiring any real data. In particular, DAS first prompts large language models (LLMs) to generate domain-specific texts before converting these texts to speech via text-to-speech technology. The synthetic data is used to fine-tune Whisper with Low-Rank Adapters (LoRAs) for targeted domains such as music, weather, and sports. We introduce a novel one-pass decoding strategy that merges predictions from multiple LoRA adapters efficiently during the auto-regressive text generation process. Experimental 

**Method-oriented passage (PDF p. 1)**

Current state-of-the-art speech recognition systems are trained on extensive and varied datasets. For example, the Whisper model [1] underwent training with 680,000 hours of multilingual data, encompassing a wide array of audio conditions and environments. This extensive training strategy has enabled these models to express a high level of robustness in speech recognition across diverse conditions and multiple evaluation datasets [1]. Such robustness motivates us to question whether domain-specific data distribution, especially transcript distribution over language characterizing a given topic such as music or sports, are still relevant. Are 

**Results-oriented passage (PDF p. 3)**

Datasets For evaluation, we utilize three real speech internal datasets collected using the Meta Ray Ban Glasses, with each sample being manually annotated. These datasets are divided into three language-defined domains: Music, Weather, and Sports. Given the nature of the data, the content predominantly features chatbot-style interactions, where a user requests Meta AI to perform tasks that involve verifying information via the internet. Statistics of the generated synthetic (for training) and evaluation datasets are available in Table III. Implementation details We use Whisper-base as the pre- trained ASR model in this study. Whisper-base ar

**Caveat-oriented passage (PDF p. 4)**

that DAS still maintains superior performance. We further evaluate DAS in a completely out-of-domain setting using the LibriSpeech test-clean and test-other test sets, which feature vocabulary unrelated to that chatbot language that DAS was adapted to. As demonstrated in Table V, DAS maintains performance comparable to the original Whisper model, w

## 193. Meta Audiobox Aesthetics: Unified Automatic Quality Assessment for Speech, Music, and Sound

ID: `2502.05139` | Theme: Evaluation/reliability | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2502.05139

Snapshot SHA-256: `c11aa42b80e5421e1c2f525ff036abf95edf841359af288c48ba77b47de6fcd7`

Abstract extract: The quantification of audio aesthetics remains a complex challenge in audio processing, primarily due to its subjective nature, which is influenced by human perception and cultural context. Traditional methods often depend on human listeners for evaluation, leading to inconsistencies and high resource demands. This paper addresses the growing need for automated systems capable of predicting audio aesthetics without human intervention. Such systems are crucial for applications like data filtering, pseudo-labeling large datasets, and evaluating generative audio models, especially as these models become more sophisticated. In this work, we introduce a novel approach to audio aesthetic evaluatio

**Method-oriented passage (PDF p. 2)**

To better understand the quality of arbitrary audio, we propose a new annotation guideline with four axes named the aesthetic (AES) scores, which cover several human perceptual dimensions. Based on the annotated AES data, we also respectively train four predictors for non-intrusive and utterance-level automatic audio aesthetic assessment (Audiobox-Aesthetics) models. Since the training data includes speech, music, and sounds, the proposed AES predictors are robust to arbitrary audio clips. Comprehensive data analysis and objective evaluations are conducted to show the effectiveness of the proposed AES scores and predictors compared to the sta

**Results-oriented passage (PDF p. 6)**

As shown in Table 1, although the proposed AES models are general to arbitrary audio, the Audiobox- Aesthetics-PQ, Audiobox-Aesthetics-CE, and Audiobox-Aesthetics-CU predictors achieve comparable per- formances to other top speech-focus predictors in both utterance-level Pearson correlation coefficient (utt-PCC) and system-level Spearman’s rank correlation coefficient (sys-SRCC) measurements while the general PAM predictor struggles in evaluating speech qualities. The OOD results also demonstrate the robustness of the proposed models, whose training data is mostly English but tested in Chinese. On the other hand, since the pro- duction comple

**Caveat-oriented passage (PDF p. 2)**

quality evaluation from generative tasks. To ease the out-of-domain robustness degradation caused by the limited available annotated data, most current systems focus on leveraging self-supervised learning (SSL) and system ensemble (Cooper et al., 2022; Saeki et al., 2022; Qi et al., 2023; Kaito et al., 2024). In the audio and music domains, Fréchet

## 194. Lost in Transcription, Found in Distribution Shift: Demystifying Hallucination in Speech Foundation Models

ID: `2502.12414` | Theme: Captioning/grounding | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2502.12414

Snapshot SHA-256: `c583ab1d60cb264f7500eea6753fd840f20cd6f29b40f9830ea203cab54b291e`

Abstract extract: Speech foundation models trained at a massive scale, both in terms of model and data size, result in robust systems capable of performing multiple speech tasks, including automatic speech recognition (ASR). These models transcend language and domain barriers, yet effectively measuring their performance remains a challenge. Traditional metrics like word error rate (WER) and character error rate (CER) are commonly used to evaluate ASR performance but often fail to reflect transcription quality in critical contexts, particularly when detecting fabricated outputs. This phenomenon, known as hallucination, is especially concerning in high-stakes domains such as healthcare, legal, and aviation, whe

**Method-oriented passage (PDF p. 2)**

The use of ASR systems in high-stakes domains, including healthcare (Afonja et al., 2024; Huh et al., 2023; Adedeji et al., 2024; Sunder et al., 2022), le- gal proceedings (Saadany et al., 2022; Garneau and Bolduc, 2024), and finance (Del Rio et al., 2021; Liao et al., 2023), has heightened the necessity for ensuring their robustness. Conventionally, the per- formance of these models is assessed using metrics such as WER and CER (Serai et al., 2022). Szy- ma´nski et al. (2023); Sasindran et al. (2024) They show that when these metrics are used in isolation, they exhibit notable limitations. Recent studies have extensively investigated hal- lu

**Results-oriented passage (PDF p. 6)**

you about the classification on a scale of 1–10? Confidence:”. We report the resulting confidence scores in Tables 2 and 3 for fine-grained and coarse- grained evaluations, respectively. The results show that GPT-4o-mini’s self- assessed confidence remains consistently high across most categories. In the fine-grained eval- uation, the “Hallucination Error” (HE) and “Oscil- lation Error” (OE) classes achieve nearly perfect confidence scores, with median and 25%ile values of 10.0. The “No Error” (NE) predictions also ex- hibit strong confidence, with an overall average of 8.81 across fine-grained classes, highlighting robust certainty in identi

**Caveat-oriented passage (PDF p. 7)**

Agreement with Human Evaluation and Heuris- tic Baseline. To validate our approach, we com- pare model-to-human and human-to-human agree- ment scores using a coarse-grained prompt. Our results demonstrate strong human-to-human raw agreement (0.71), indicating consistency. Addition- ally, we observe good agreement (0.6) between hu- man annotations a

## 195. Speech Enhancement Using Continuous Embeddings of Neural Audio Codec

ID: `2502.16240` | Theme: Representations/codecs | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2502.16240

Snapshot SHA-256: `1b677cebd50125902113491791a5273f1ec6fe200069d0ecfd5be10a09cdc3e8`

Abstract extract: Recent advancements in Neural Audio Codec (NAC) models have inspired their use in various speech processing tasks, including speech enhancement (SE). In this work, we propose a novel, efficient SE approach by leveraging the pre-quantization output of a pretrained NAC encoder. Unlike prior NAC-based SE methods, which process discrete speech tokens using Language Models (LMs), we perform SE within the continuous embedding space of the pretrained NAC, which is highly compressed along the time dimension for efficient representation. Our lightweight SE model, optimized through an embedding-level loss, delivers results comparable to SE baselines trained on larger datasets, with a significantly low

**Method-oriented passage (PDF p. 1)**

Abstract—Recent advancements in Neural Audio Codec (NAC) models have inspired their use in various speech processing tasks, including speech enhancement (SE). In this work, we propose a novel, efficient SE approach by leveraging the pre-quantization output of a pretrained NAC encoder. Unlike prior NAC-based SE methods, which process discrete speech tokens using Language Models (LMs), we perform SE within the continuous embedding space of the pretrained NAC, which is highly compressed along the time dimension for efficient representation. Our lightweight SE model, optimized through an embedding-level loss, delivers results comparable to SE bas

**Results-oriented passage (PDF p. 3)**

set. Sepformer is a transformer-based model used for speech separation [32] and enhancement [34]. It is similar to our transformer model and serves as a suitable candidate for comparison. The main difference between our model and Sepformer is the use of DAC as the encoder and decoder, as well as the use of only a single stack of transformers, compared to Sepformer’s dual-path architecture. In Table I we compare both systems under a practical online audio transmission scenario, where the audio signal is processed on the cloud and sent to a local device (see figure 1(a) and (c) for illustration). To investigate whether the codec transmission de

**Caveat-oriented passage (PDF p. 3)**

Trainset Following previous NAC [20] and LM-based [24] SE works, we gathered clean speech and noise clips to generate noisy speech on the fly during training with signal-to-noise ratio (SNR) in [-5, 20] dB. Specifically, our train set consists of 40 hours of clean speech and 15 hours of noise clips from the 2022 DNS Challenge [25], where the clean 

## 196. MMS-LLaMA: Efficient LLM-based Audio-Visual Speech Recognition with Minimal Multimodal Speech Tokens

ID: `2503.11315` | Theme: Speech/audio generation and control | Status: `excluded_after_screening`

Source: https://arxiv.org/pdf/2503.11315

Snapshot SHA-256: `279a9164b8e5c97d82c25ead23a3e36d4fcde8992c1953725cb9b826a8271ff8`

Excluded: Audio-visual speech compression; outside the audio-only design scope

Abstract extract: Audio-Visual Speech Recognition (AVSR) achieves robust speech recognition in noisy environments by combining auditory and visual information. However, recent Large Language Model (LLM) based AVSR systems incur high computational costs due to the high temporal resolution of audio-visual speech processed by LLMs. In this work, we introduce an efficient multimodal speech LLM framework that minimizes token length while preserving essential linguistic content. Our approach employs an early AV-fusion module for streamlined feature integration, an audio-visual speech Q-Former that dynamically allocates tokens based on input duration, and a refined query allocation strategy with a speech rate predic

**Method-oriented passage (PDF p. 3)**

timodal speech learners by leveraging their context modeling capabilities. Motivated by this finding, we adopt their framework as our baseline AVSR model. As illustrated in Figure 1, the architecture con- sists of three main components: a visual encoder, an audio encoder, and an LLM decoder that pre- dicts sentences from multimodal tokens. Building on these components, and with the goal of reducing the number of multimodal tokens while retaining essential linguistic information, we introduce three additional modules: the early AV-fusion module, the AV Q-Former, and the speech rate predictor.

**Results-oriented passage (PDF p. 7)**

and achieves a WER of 0.97% with 2.24T FLOPs and 18.2GB gpu memory usage. With the addition of the early av fusion component, token throughput is reduced to 12.5 multimodal speech tokens per second, FLOPs decreases to 1.81T, while the WER improves slightly to 0.92%. Next, we add the AV Q-Former component. Its impact is evaluated under three different query fre- quency configurations of 1, 2, and 3. Please note that the results using query frequencies of 1, 2, and 3 are shown from top to bottom in the table, respec- tively. The query frequency of 1 yields the lowest FLOPs of 1.35T and gpu memory usage of 12.1 GB, but the WER increases signific

**Caveat-oriented passage (PDF p. 2)**

the number of multimodal tokens, we propose a speech rate predictor. It accounts for differences in speaking speed across each audio sample, enabling the assignment of more tokens to faster speech. Reflecting the growing trend toward efficient multimodal models and leveraging insights from efficient multimodal LLMs that utilize minimal vi- sion tok

## 197. Qwen2.5-Omni Technical Report

ID: `2503.20215` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2503.20215

Snapshot SHA-256: `95906505512440a3a32c37b10a6aeeef092c44d60fcfaebfb309950685b7cbf1`

Abstract extract: In this report, we present Qwen2.5-Omni, an end-to-end multimodal model designed to perceive diverse modalities, including text, images, audio, and video, while simultaneously generating text and natural speech responses in a streaming manner. To enable the streaming of multimodal information inputs, both audio and visual encoders utilize a block-wise processing approach. To synchronize the timestamps of video inputs with audio, we organize the audio and video sequentially in an interleaved manner and propose a novel position embedding approach, named TMRoPE(Time-aligned Multimodal RoPE). To concurrently generate text and speech while avoiding interference between the two modalities, we prop

**Method-oriented passage (PDF p. 2)**

In this report, we introduce Qwen2.5-Omni, a unified single model capable of processing multiple modalities and generating text and natural speech responses simultaneously in a streaming format. To tackle the first challenge, we propose a novel position embedding approach, named TMRoPE (Time- aligned Multimodal RoPE). We organize these audio and video frames in an interleaved structure to represent video sequences in time order. For the second challenge, we present Thinker-Talker architecture, wherein Thinker is tasked with text generation while the Talker focuses on generating streaming speech tokens. Talker receives high-level representatio

**Results-oriented passage (PDF p. 2)**

Qwen2.5-Omni is comparable with the similarly sized Qwen2.5-VL (Wang et al., 2024c) and outperforms Qwen2-Audio (Chu et al., 2024b) in image and audio capabilities respectively. Furthermore, Qwen2.5- Omni achieves state-of-the-art performance on multimodal benchmarks such as OmniBench (Li et al., 2024b) and AV-Odyssey Bench (Gong et al., 2024). Notably, Qwen2.5-Omni’s performance in end-to- end speech instruction following is comparable to its capabilities with text inputs, as evidenced by benchmarks such as MMLU (Hendrycks et al., 2021a) and GSM8K (Cobbe et al., 2021). As for speech generation, Qwen2.5-Omni achieves 1.42%, 2.33% and 6.54% WE

**Caveat-oriented passage (PDF p. 2)**

In daily life, humans are capable of simultaneously perceiving the visual and auditory information around them. After processing this information through the brain, they express feedback through writing, vocalization, or using tools (and physical actions), thereby engaging in information exchange with various organisms in the world and exhibiting i

## 198. EmoVoice: LLM-based Emotional Text-To-Speech Model with Freestyle Text Prompting

ID: `2504.12867` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2504.12867

Snapshot SHA-256: `65840d4e3f8e0aec3ee9a96bf77cb6db2423348b57938f61f1fa7578f79db090`

Abstract extract: Human speech goes beyond the mere transfer of information; it is a profound exchange of emotions and a connection between individuals. While Text-to-Speech (TTS) models have made huge progress, they still face challenges in controlling the emotional expression in the generated speech. In this work, we propose EmoVoice, a novel emotion-controllable TTS model that exploits large language models (LLMs) to enable fine-grained freestyle natural language emotion control, and a phoneme boost variant design that makes the model output phoneme tokens and audio tokens in parallel to enhance content consistency, inspired by chain-of-thought (CoT) and chain-of-modality (CoM) techniques. Besides, we intr

**Method-oriented passage (PDF p. 2)**

preferences, and pioneer the effort to evaluate emotional speech with SOTA multimodal LLMs GPT-4o-audio1 and Gemini2 with comprehensive capabilities. Our main contributions can be summarized as follows: • We propose EmoVoice, a novel fine-grained freestyle text prompt- based emotion-controllable TTS model based on LLMs. Inspired by CoT and CoM methods, we propose EmoVoice-PP, a variant of EmoVoice that outputs audio and phoneme tokens in parallel to improve content consistency. • We construct EmoVoice-DB, a high-quality 40-hour English emo- tion dataset with expressive speech and natural language emotion description labels. • EmoVoice achieve

**Results-oriented passage (PDF p. 6)**

human perception. Specifically, we randomly sample 10 utterances form each of six emotion categories from the test set, totaling 60 au- dio samples. These samples are evaluated by 30 distinct participants, each of whom rates 10 random groups of speech produced by six representative models. The evaluation focuses on two key aspects: the overall emotional expressiveness of the synthesized speech and its adherence to the given emotional instructions. Ratings are scored on a scale of 1 to 5, with increments of 0.5. The results presented in Table 3 reveal that the MOS trends align closely with the objective emotion metrics, validating the consis- 

**Caveat-oriented passage (PDF p. 2)**

datasets, and evaluation metrics are still in their infancy, leaving ample room for further exploration and development. Prior research efforts on emotional TTS primarily rely on coarse emotion category labels [7, 13, 21, 37], which are insufficient to comprehensively capture the nuanced emotion states conveyed in speech. Ideally, we envision a mod

## 199. Calm-Whisper: Reduce Whisper Hallucination On Non-Speech By Calming Crazy Heads Down

ID: `2505.12969` | Theme: Captioning/grounding | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2505.12969

Snapshot SHA-256: `f30f8618933e0f6664bd4af4b5b18b1fe71ff6d6ab1de8d3ceffd7a7050b1d20`

Abstract extract: OpenAI's Whisper has achieved significant success in Automatic Speech Recognition. However, it has consistently been found to exhibit hallucination issues, particularly in non-speech segments, which limits its broader application in complex industrial settings. In this paper, we introduce a novel method to reduce Whisper's hallucination on non-speech segments without using any pre- or post-possessing techniques. Specifically, we benchmark the contribution of each self-attentional head in the Whisper-large-v3 decoder to the hallucination problem by performing a head-wise mask. Our findings reveal that only 3 of the 20 heads account for over 75% of the hallucinations on the UrbanSound dataset.

**Method-oriented passage (PDF p. 2)**

hallucinations within the model itself. We hypothesize that only certain self-attention heads in the decoder are noise-sensitive and hallucinatory. To validate this, we mask these heads one by one and benchmark their impact on hallucination occur- rence. After identifying the most hallucinatory heads, we con- duct calm-down fine-tuning only on these heads using non- speech audio paired with blank labels. Results show that our approach reduces non-speech hallucinations by over 80% while maintaining undegraded speech recognition accuracy.

**Results-oriented passage (PDF p. 4)**

In the same manner as in Section 3.2, we benchmark the fine- tuned models on UrbanSound8K and the LibriSpeech test-clean and test-other datasets, comparing their performance with the non-fine-tuned models. It should be noted that we do not apply any head masks during the inference for the fine-tuned models. The results are shown in Table 3.

**Caveat-oriented passage (PDF p. 1)**

Previous studies have explored Whisper’s hallucination problem and offered potential solutions. In Careless-Whisper [7], the authors highlight that approximately 1% of Whis- per’s transcriptions contain hallucinated phrases or sentences not present in the original audio. Notably, 38% of these hal- lucinations include explicit harms such as perpetua

## 200. DualCodec: A Low-Frame-Rate, Semantically-Enhanced Neural Audio Codec for Speech Generation

ID: `2505.13000` | Theme: Representations/codecs | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2505.13000

Snapshot SHA-256: `9db674705eb35740f2acf1688ce814610d66162e34b3d8211e6b909e55ddb86c`

Abstract extract: Neural audio codecs form the foundational building blocks for language model (LM)-based speech generation. Typically, there is a trade-off between frame rate and audio quality. This study introduces a low-frame-rate, semantically enhanced codec model. Existing approaches distill semantically rich self-supervised (SSL) representations into the first-layer codec tokens. This work proposes DualCodec, a dual-stream encoding approach that integrates SSL and waveform representations within an end-to-end codec framework. In this setting, DualCodec enhances the semantic information in the first-layer codec and enables the codec system to maintain high audio quality while operating at a low frame rat

**Method-oriented passage (PDF p. 4)**

Metrics. We adopt VALL-E [4] and AR+SoundStorm [7, 8] as TTS systems and train each TTS with different codec sys- tems. VALL-E has 270M parameters in AR, 400M in NAR. AR+SoundStorm has 800M in AR, 300M in NAR. For Dual- Codec, models G2 and G5 in Table 3 are used for 25Hz and 12.5Hz, respectively. For all codecs we use 8 RVQ codebooks. We report the WER and speaker similarity SIM-O (SIM) on Seed-TTS-Eval benchmark [34]. We report the real-time-factor (RTF) tested on an A100 GPU which correlates to the inference speed. Results are shown in Table 4. Performance Comparisons. Table 4 demonstrates that Du- alCodec outperforms SpeechTokenizer and M

**Results-oriented passage (PDF p. 3)**

Metrics. We evaluate the semantic preservation of the RVQ- 1 tokens by reporting the ASR Word Error Rate (WER) on the codec-decoded audio, using only RVQ-1. The evaluations leverage Whisper-large-v3 for English (EN) and Paraformer-zh for Chinese (ZH), tested on the Seed-TTS-Eval [34] dataset. The results are summarized in Table 2. Group A baselines. Group A (A1 and A2) models are ground- truth and official SpeechTokenizer checkpoint, respectively. The A2 SpeechTokenizer model has semantic distillation and 1024 EMA codebooks. While it is trained on English-only data, we report its Chinese performance and find that its RVQ-1 has extremely high 

**Caveat-oriented passage (PDF p. 2)**

found that lower SSL layers encode speaker-related informa- tion whereas higher layers contain rich pronunciation and word meaning information, benefiting tasks such as speech recogni- tion (ASR) [19, 13, 15]. Discretizing SSL representations into semantic tokens have also been explored, using k-means [5] or vector quantization (VQ) [20]. However, 

## 201. Discrete Audio Representations for Automated Audio Captioning

ID: `2505.14989` | Theme: Captioning/grounding | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2505.14989

Snapshot SHA-256: `9541bf2c09a45cd0803142eeed4854e5fe106f3b2a4c2d5756d14e7a530dd9c3`

Abstract extract: Discrete audio representations, termed audio tokens, are broadly categorized into semantic and acoustic tokens, typically generated through unsupervised tokenization of continuous audio representations. However, their applicability to automated audio captioning (AAC) remains underexplored. This paper systematically investigates the viability of audio token-driven models for AAC through comparative analyses of various tokenization methods. Our findings reveal that audio tokenization leads to performance degradation in AAC models compared to those that directly utilize continuous audio representations. To address this issue, we introduce a supervised audio tokenizer trained with an audio taggi

**Method-oriented passage (PDF p. 1)**

Discrete audio representations, termed audio tokens, are broadly categorized into semantic and acoustic tokens, typically generated through unsupervised tokenization of continuous au- dio representations. However, their applicability to automated audio captioning (AAC) remains underexplored. This paper systematically investigates the viability of audio token-driven models for AAC through comparative analyses of various tok- enization methods. Our findings reveal that audio tokenization leads to performance degradation in AAC models compared to those that directly utilize continuous audio representations. To address this issue, we introduce a 

**Results-oriented passage (PDF p. 4)**

Table 1: The performance of AAC models on the Clotho evaluation set. RepCodec-VQ/RVQ and Supervised-VQ/RVQ denote the RepCodec and supervised audio tokenizer with VQ/RVQ, respectively. ID indicates training the tokenizer with in-domain data, while OD indicates training with out-of-domain data. ∗indicates that the results are sourced from [25].

**Caveat-oriented passage (PDF p. 3)**

The GPT-2 XL-based AAC model employs a decoder-only framework, as shown in Figure 1 (c), inspired by the work of [28]. The input representation sequence undergoes a 3× down- sampling via a Conv1D layer, analogous to the BART-based model. To handle varying audio representation lengths, we concatenate a fixed number of learnable embeddings with the d

## 202. From Tens of Hours to Tens of Thousands: Scaling Back-Translation for Speech Recognition

ID: `2505.16972` | Theme: Loop/data selection | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2505.16972

Snapshot SHA-256: `dbfe72723b47beaa1f4d253670da4e0299c89e8a15649bae05614b7b4106a318`

Abstract extract: Recent advances in Automatic Speech Recognition (ASR) have been largely fueled by massive speech corpora. However, extending coverage to diverse languages with limited resources remains a formidable challenge. This paper introduces Speech Back-Translation, a scalable pipeline that improves multilingual ASR models by converting large-scale text corpora into synthetic speech via off-the-shelf text-to-speech (TTS) models. We demonstrate that just tens of hours of real transcribed speech can effectively train TTS models to generate synthetic speech at hundreds of times the original volume while maintaining high quality. To evaluate synthetic speech quality, we develop an intelligibility-based as

**Method-oriented passage (PDF p. 7)**

The experiments in Section 5.3 are essentially con- ducted under out-of-domain conditions, as the TTS models are trained on the viVoice dataset but the final ASR performance are evaluated with the Com- mon Voice dataset. Notably, we identified only about three hours of transcribed audio in Com- mon Voice Vietnamese available for training. This prompts an important research question: how can we effectively leverage such a small but valuable amount of in-domain data? We propose three meth- ods for effectively utilizing the in-domain data to enhance model performance:

**Results-oriented passage (PDF p. 6)**

We now investigate extending TTS support to a new language, Vietnamese, using limited amounts of transcribed speech data. To explore how the quantity of training data impacts TTS model per- formance, we sampled datasets at increments of {20,40,60,80,100} hours and trained each for up to 10 epochs. The results, shown in Figure 5, clearly indicate that performance consistently improves as the amount of training data and the number of epochs increase. Specifically, the model trained on the 100-hour dataset reaching a WER of 10% in the end, which closely approaches the baseline WER for natural speech. Next, we analyze the relationship between TTS

**Caveat-oriented passage (PDF p. 9)**

While our approach demonstrates significant im- provements in multilingual ASR performance, sev- eral limitations should be noted. First, the synthetic speech data generated through TTS models may not fully capture the acoustic complexity present in real-world environ- ments, particularly in scenarios with background noise, multiple speakers, or va

## 203. P2VA: Converting Persona Descriptions into Voice Attributes for Fair and Controllable Text-to-Speech

ID: `2505.17093` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2505.17093

Snapshot SHA-256: `593420b0c7ab24f3ab9c8562144b560c82c2305e53f0f8c8c300cd7811ae9292`

Abstract extract: While persona-driven large language models (LLMs) and prompt-based text-to-speech (TTS) systems have advanced significantly, a usability gap arises when users attempt to generate voices matching their desired personas from implicit descriptions. Most users lack specialized knowledge to specify detailed voice attributes, which often leads TTS systems to misinterpret their expectations. To address these gaps, we introduce Persona-to-Voice-Attribute (P2VA), the first framework enabling voice generation automatically from persona descriptions. Our approach employs two strategies: P2VA-C for structured voice attributes, and P2VA-O for richer style descriptions. Evaluation shows our P2VA-C reduces

**Method-oriented passage (PDF p. 3)**

For P2VA-C, we define a fixed list of style attributes by exam- ining the most frequent labels in Parler-TTS’s training data. Our preset includes options for gender, accent (e.g., Amer- ican, British, Asian, Indian), tone (e.g., Analytical, Warm, Engaging), speed (e.g., Slow, Normal, Fast), and pitch (e.g., Low, Medium, High).

**Results-oriented passage (PDF p. 3)**

We measure synthesized speech quality and accuracy using Word Error Rate (WER), UTMOS, and Mean Opinion Score (MOS) estimated by LLM and human listeners. These metrics evaluate synthesized speech from multiple perspectives, such as clarity, naturalness, and alignment with user intent. We randomly sample a total of 1000 persona–transcript pairs from the Persona-1M dataset. Then, we generate speech using three approaches: Baseline (as-is), P2VA-C, and P2VA- O. As shown in Table 2, the P2VA-C achieves the best perfor- mance across all metrics. While the improvement in UTMOS may not be statistically significant, the reduction in WER is about 5%, 

**Caveat-oriented passage (PDF p. 2)**

Prompt-based TTS offers fine-grained control of speech gen- eration through natural language instructions. PromptTTS [7] showed that text descriptions alone can drive prosodic vari- ation without reference audio. PromptTTS++ [8] added con- trol of speaker identity expressed in natural language, turning style and identity into a joint control proble

## 204. RASMALAI: Resources for Adaptive Speech Modeling in Indian Languages with Accents and Intonations

ID: `2505.18609` | Theme: Data/Indic speech | Status: `selected_fulltext_review_plus_scoped_core_crosscheck`

Source: https://arxiv.org/pdf/2505.18609

Snapshot SHA-256: `977f44bcda0e0c4861426519ec18600145d004a0d173842bbaf047a2dea5d1d4`

Abstract extract: We introduce RASMALAI, a large-scale speech dataset with rich text descriptions, designed to advance controllable and expressive text-to-speech (TTS) synthesis for 23 Indian languages and English. It comprises 13,000 hours of speech and 24 million text-description annotations with fine-grained attributes like speaker identity, accent, emotion, style, and background conditions. Using RASMALAI, we develop IndicParlerTTS, the first open-source, text-description-guided TTS for Indian languages. Systematic evaluation demonstrates its ability to generate high-quality speech for named speakers, reliably follow text descriptions and accurately synthesize specified attributes. Additionally, it effect

**Method-oriented passage (PDF p. 1)**

text-prompted TTS for Indian languages. To address this gap, we propose generating text-based speech descriptions using Large Language Models (LLMs) by leveraging attribute information in the form of structured tags. Specifically, we aggregate multiple existing TTS datasets con- taining {audio, transcript} pairs and extract three categories of attributes: (i) metadata attributes such as age, gender, and speaker identity, where available; (ii) stylistic attributes, includ- ing Ekman emotions when annotated; and (iii) acoustic features such as pitch [14], speaking rate, and clarity index [15, 16], derived using speech processing libraries. Thes

**Results-oriented passage (PDF p. 3)**

enizer, following the approach in [20], enabling better subword segmentation in Indian languages. Training Setup: We train INDICPARLERTTS using 32 H100 GPUs for 1.5 days, leveraging the open-sourced configuration from the original Parler-TTS implementation. We followed the hyperparameters outlined in the configuration, and replace the original scheduler with CosineLR with 3,000 warm-up steps, with an effective batch size of 256. Data: We pretrain the model on RASMALAI’s pretraining set, which spans 24 languages and 13,000 hours of data, and further finetune it on the finetuning set, comprising high-fidelity data from 18 languages with 1,804 h

**Caveat-oriented passage (PDF p. 4)**

showing the model’s strong ability to follow given instructions accurately. Additionally, the attribute accuracy scores presented in Table 6 show strong performance in adhering to the spec- ified attributes across most categories. Together, these metrics highlight our model as a highly faithful executor of instructions. However, we note that PESQ a

Additional interpretation and limitations: [core findings](CORE_FINDINGS.md).

## 205. KIT's Low-resource Speech Translation Systems for IWSLT2025: System Enhancement with Synthetic Data and Model Regularization

ID: `2505.19679` | Theme: Loop/data selection | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2505.19679

Snapshot SHA-256: `ec3bedf9dab11ba409fb81287339c7daf9550b29ab672a116d480067c2ae1b01`

Abstract extract: This paper presents KIT's submissions to the IWSLT 2025 low-resource track. We develop both cascaded systems, consisting of Automatic Speech Recognition (ASR) and Machine Translation (MT) models, and end-to-end (E2E) Speech Translation (ST) systems for three language pairs: Bemba, North Levantine Arabic, and Tunisian Arabic into English. Building upon pre-trained models, we fine-tune our systems with different strategies to utilize resources efficiently. This study further explores system enhancement with synthetic data and model regularization. Specifically, we investigate MT-augmented ST by generating translations from ASR data using MT models. For North Levantine, which lacks parallel ST 

**Method-oriented passage (PDF p. 2)**

The IWSLT 2025 low-resource track defines two system categories: constrained, where models are trained exclusively on datasets provided by the or- ganizers, and unconstrained, where participants are free to use any external resources. In this work, we focus on the unconstrained condition, aiming to reflect better practical and real-world scenarios, where leveraging diverse data sources is often es- sential for building effective translation systems.

**Results-oriented passage (PDF p. 6)**

For Bemba, we explore the use of ViTTS and E2TTS to generate synthetic training data. The TTS models are trained using the training split of the development dataset. The source text used for synthesis is derived from NLLB, selected based on criteria such as appropriate text length, as outlined in Table 2. Evaluation results for the TTS systems are provided in Appendix A. We generate 120K synthetic training samples for each TTS model. This synthetic data is com- bined with the original development set for training, while the validation split remains unchanged. Fol- lowing the procedure used for other end-to-end

**Caveat-oriented passage (PDF p. 2)**

Data scarcity remains a key challenge in low- resource natural language processing tasks, par- ticularly for end-to-end speech translation (ST). To address this limitation, this work investigates data augmentation approaches using synthetic data. We focus on two augmentation approaches that address different modalities: the MT-augmented method, whi

## 206. Mitigating Audiovisual Mismatch in Visual-Guide Audio Captioning

ID: `2505.22045` | Theme: Captioning/grounding | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2505.22045

Snapshot SHA-256: `09dfbe3ba52226e616fe535d3a2a7b0ed673f790552fe894356fdf5520e9682b`

Abstract extract: Current vision-guided audio captioning systems frequently fail to address audiovisual misalignment in real-world scenarios, such as dubbed content or off-screen sounds. To bridge this critical gap, we present an entropy-aware gated fusion framework that dynamically modulates visual information flow through cross-modal uncertainty quantification. Our novel approach employs attention entropy analysis in cross-attention layers to automatically identify and suppress misleading visual cues during modal fusion. Complementing this architecture, we develop a batch-wise audiovisual shuffling technique that generates synthetic mismatched training pairs, greatly enhancing model resilience against align

**Method-oriented passage (PDF p. 1)**

textual modality. However, these approaches face two signif- icant limitations: First, they assume semantic consistency be- tween the modalities, which can introduce noise when this as- sumption is violated, such as when ambient sounds come from off-screen objects or when visible objects have no correspond- ing sounds. This prevalent but overlooked audiovisual mis- match problem can significantly degrade model performance by misleading cross-modal reasoning. Second, when process- ing long-form video inputs, concatenation-based systems incur prohibitive computational costs, as they require redundant en- coding of dense frame-level visual featu

**Results-oriented passage (PDF p. 3)**

Table 3 demonstrates the effectiveness of our proposed SMS through systematic evaluation under varying degrees of audio- visual mismatch. First, our method exhibits superior robustness to modality mismatch compared to the baseline AVCap. Across seven out of eight evaluation metrics (excluding CIDEr), the proposed ap- proach shows strictly smaller performance degradation than the baseline when test-time shuffle probability escalates from 0% to 100%. This resilience is particularly evident in semantic metrics like SPICE, where our method preserves 98.8% of the original performance compared to AVCap’s 92.4% retention. Notably, our method trained

**Caveat-oriented passage (PDF p. 3)**

The proposed method demonstrates competitive performance across all metrics on the AudioCaps test set. As shown in Ta- ble 1. Our data augmentation variant achieves state-of-the-art results in all BLEU metrics, showing the effectiveness of data augmentation for n-gram-based evaluation. However, the base Proposed model without augmentation obtains t

## 207. Can Quantized Audio Language Models Perform Zero-Shot Spoofing Detection?

ID: `2506.06756` | Theme: Captioning/grounding | Status: `excluded_after_screening`

Source: https://arxiv.org/pdf/2506.06756

Snapshot SHA-256: `d2a0e4bd6050d4e597b2ffbb250c3f61fad2462df75a009780cc747513ab4c86`

Excluded: Quantized spoof detection; no direct evidence of caption/control quality

Abstract extract: Quantization is essential for deploying large audio language models (LALMs) efficiently in resource-constrained environments. However, its impact on complex tasks, such as zero-shot audio spoofing detection, remains underexplored. This study evaluates the zero-shot capabilities of five LALMs, GAMA, LTU-AS, MERaLiON, Qwen-Audio, and SALMONN, across three distinct datasets: ASVspoof2019, In-the-Wild, and WaveFake, and investigates their robustness to quantization (FP32, FP16, INT8). Despite high initial spoof detection accuracy, our analysis demonstrates severe predictive biases toward spoof classification across all models, rendering their practical performance equivalent to random classifica

**Method-oriented passage (PDF p. 2)**

Consider an audio sample represented as a sequence of acoustic frames X = {x1, x2, . . . , xT }, where each frame xi ∈Rd, T is the total number of frames, and d is the dimensionality of each frame. Let fθ denote a pretrained LALM parameterized by weights θ. Given an audio sample X and a prompt p, the LALM outputs a probability distribution over the vocabulary V: P = fθ(X, p) ∈∆|V|−1. The binary classification decision is based on comparing the probabilities of the target classification tokens, assigning the class y = spoof if P(tspoof | X, p) > P(tbonafide | X, p), else bonafide, where tspoof, tbonafide ∈V are the vocabulary tokens correspond

**Results-oriented passage (PDF p. 2)**

dio processing capabilities with a transformer decoder, enabling versatile audio-text alignment applicable across various audio forms including speech, music, and environmental sounds. Fi- nally, SALMONN [18] integrates Whisper and BEATs audio encoders through a window-level Q-Former combined with a Vicuna-based [19] LLM, providing unified and sophisticated multimodal processing across speech, audio events, and music. Our experiments utilize multiple diverse datasets contain- ing bonafide and synthetically spoofed audio samples that were created using various synthesis methods. We specifically se- lected datasets that reflect distinct class d

**Caveat-oriented passage (PDF p. 3)**

ples. As a result, the overall accuracy metrics were misleading and resembled random predictions. Further dataset-wise analysis provides deeper insights into the distinct behaviors of each model. The spoof-heavy ASVspoof2019 dataset exacerbated model biases, causing ro- bust models such as MERaLiON and LTU-AS to frequently misclassify genuine audio

## 208. Reducing Object Hallucination in Large Audio-Language Models via Audio-Aware Decoding

ID: `2506.07233` | Theme: Captioning/grounding | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2506.07233

Snapshot SHA-256: `c078e7fb7bc465188d7495ce0395eb26bed2a431e1aaf5f20b3a3fbc924986f2`

Abstract extract: Large Audio-Language Models (LALMs) can take audio and text as the inputs and answer questions about the audio. While prior LALMs have shown strong performance on standard benchmarks, there has been alarming evidence that LALMs can hallucinate what is presented in the audio. To mitigate the hallucination of LALMs, we introduce Audio-Aware Decoding (AAD), a lightweight inference-time strategy that uses contrastive decoding to compare the token prediction logits with and without the audio context. By contrastive decoding, AAD promotes the tokens whose probability increases when the audio is present. We conduct our experiment on object hallucination datasets with three LALMs and show that AAD i

**Method-oriented passage (PDF p. 2)**

However, because the model can over-rely on its model priors, e.g., what it has learned during training, it sometimes neglects the content in the input audio and hallucinates objects that do not actually appear in the audio. To address this issue, we introduce AAD, a contrastive decoding method that reduces the tendency to rely on the model’s prior knowledge. To resolve the model’s over-reliance on its prior knowledge and neglect of the input audio, we use AAD to modify the token distribution during decoding. Precisely, at each generation step t, we feed two different inputs to the model separately: (1) input with audio: the LALM’s input cont

**Results-oriented passage (PDF p. 4)**

When absent objects are selected randomly, both Prompt- Engineering Only and AAD substantially improve over the De- fault baseline, with AAD consistently achieving the strongest results. For instance, on SALMONN-7B, the Default setting yields an F1 score of just 0.233. Prompt-Only significantly boosts this to 0.564 (+142%), and AAD further elevates it to 0.737 (+216%). Similar patterns occur with Qwen2- Audio-7B, where F1 improves from 0.302 (Default) to 0.397 (Prompt-Only), ultimately reaching 0.737 with AAD. Like- wise, SALMONN-13B sees a notable increase from 0.384 (Default) to 0.533 (Prompt-Only) and finally to 0.676 with AAD. These large

**Caveat-oriented passage (PDF p. 6)**

In this paper, we introduce audio-aware decoding (AAD), a contrastive decoding method designed for reducing the halluci- nation of LALMs. By comparing the output token logits when the input contains audio and does not contain audio, AAD promotes the token whose likelihood increases when the audio contexts are presented. By extensive experiments wit

## 209. Fine-Tuning Large Audio-Language Models with LoRA for Precise Temporal Localization of Prolonged Exposure Therapy Elements

ID: `2506.09707` | Theme: Captioning/grounding | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2506.09707

Snapshot SHA-256: `809e8dc91f42993090d0263bfdf784327a68bd9d720e73833d2147c7554071bf`

Abstract extract: Prolonged Exposure (PE) therapy is an effective treatment for post-traumatic stress disorder (PTSD), but evaluating therapist fidelity remains labor-intensive due to the need for manual review of session recordings. We present a method for the automatic temporal localization of key PE fidelity elements, identifying their start and stop times, directly from session audio and transcripts. Our approach fine-tunes a large pre-trained audio-language model, Qwen2-Audio, using Low-Rank Adaptation (LoRA) to process focused 30-second windows of audio-transcript input. Fidelity labels for three core protocol phases, therapist orientation (P1), imaginal exposure (P2), and post-imaginal processing (P3),

**Method-oriented passage (PDF p. 1)**

Prolonged Exposure (PE) therapy is an effective treatment for post- traumatic stress disorder (PTSD), but evaluating therapist fidelity re- mains labor-intensive due to the need for manual review of session recordings. We present a method for the automatic temporal local- ization of key PE fidelity elements, identifying their start and stop times, directly from session audio and transcripts. Our approach fine-tunes a large pre-trained audio-language model, Qwen2-Audio, using Low-Rank Adaptation (LoRA) to process focused 30-second windows of audio-transcript input. Fidelity labels for three core protocol phases, therapist orientation (P1), ima

**Results-oriented passage (PDF p. 3)**

Table 3 presents the mean ± standard deviation of MAE across three random seeds. Our best-performing configuration, 30-second windows with LoRA rank r = 8, achieved an average MAE of 5.3 seconds compared to ground truth across P1 (5.9 ± 1.4s), P2 (5.0 ± 1.8s), and P3 (5.0 ± 0.5s). Notably, an MAE of 5.3s falls within the natural variance of human cognitive pauses. This sug- gests the model’s localization error is effectively indistinguishable from human rater variability for the purpose of clinical quality con- trol. This level of precision is promising for downstream clinical

**Caveat-oriented passage (PDF p. 4)**

support scalable, automated fidelity assessment in PTSD therapy, aiding clinician supervision, training, and quality assurance. By lo- calizing key therapeutic phases automatically, the approach reduces the burden of manual review. Future work will expand to addi- tional fidelity markers and test generalization across diverse therapy settings. Ulti

## 210. UmbraTTS: Adapting Text-to-Speech to Environmental Contexts with Flow Matching

ID: `2506.09874` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2506.09874

Snapshot SHA-256: `29ebc06b71556d5690abd7c106952dd0295e66ed8acb6d77aa87b2186e8a52c2`

Abstract extract: Recent advances in Text-to-Speech (TTS) have enabled highly natural speech synthesis, yet integrating speech with complex background environments remains challenging. We introduce UmbraTTS, a flow-matching based TTS model that jointly generates both speech and environmental audio, conditioned on text and acoustic context. Our model allows fine-grained control over background volume and produces diverse, coherent, and context-aware audio scenes. A key challenge is the lack of data with speech and background audio aligned in natural context. To overcome the lack of paired training data, we propose a self-supervised framework that extracts speech, background audio, and transcripts from unannota

**Method-oriented passage (PDF p. 2)**

We introduce UmbraTTS, a flow-matching (Lipman et al., 2022) based method for environmental-aware text-to-speech. Following the F5-TTS framework (Chen et al., 2024), which demonstrated the effectiveness of flow matching for text- to-speech, we propose an advanced architecture for envi- ronmental conditioning. The architecture of our method is illustrated in Fig. 1 and described below.

**Results-oriented passage (PDF p. 3)**

First, we evaluated our model’s capability to generate speech with integrated environmental sounds. To assess this, we use the AudioCaps test subset as described in VoiceLDM (Lee et al., 2024), which contains audio recordings with both speech and background noise. During evaluation, our model is conditioned on the target text and the background sound from the test subset. The results are presented in Table 1. For quantitative evaluation, we report the Frechet Audio Dis- tance (FAD) (Kilgour et al., 2018), Kullback-Leiber (KL), word error rate (WER), computed using Whisper large-v3 (Radford et al., 2023), and the CLAP score (Wu et al., 2023), 

**Caveat-oriented passage (PDF p. 1)**

A naive approach to integrating speech with background noise is to first generate clean speech and then overlay en- vironmental sounds. However, this method has three major limitations. First, it overlooks how speakers naturally adjust vocal effort, tone, and rhythm according to their surround- ings - a behavior known as the Lombard effect (Zolling

## 211. Investigation of Zero-shot Text-to-Speech Models for Enhancing Short-Utterance Speaker Verification

ID: `2506.14226` | Theme: Evaluation/reliability | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2506.14226

Snapshot SHA-256: `ab51bc0caf9696c2b609a57df8194b995d9f17b955d69dc58029990000d1dfdf`

Abstract extract: Short-utterance speaker verification presents significant challenges due to the limited information in brief speech segments, which can undermine accuracy and reliability. Recently, zero-shot text-to-speech (ZS-TTS) systems have made considerable progress in preserving speaker identity. In this study, we explore, for the first time, the use of ZS-TTS systems for test-time data augmentation for speaker verification. We evaluate three state-of-the-art pre-trained ZS-TTS systems, NatureSpeech 3, CosyVoice, and MaskGCT, on the VoxCeleb 1 dataset. Our experimental results show that combining real and synthetic speech samples leads to 10%-16% relative equal error rate (EER) reductions across all d

**Method-oriented passage (PDF p. 3)**

CosyVoice [24] is a scalable multilingual zero-shot TTS system that employs supervised semantic tokens from a multilingual ASR model to enhance content consistency and speaker similar- ity. Its architecture includes a text encoder, a speech tokenizer, a large language model (LLM), and a conditional flow matching module. By integrating x-vectors, it separates content, speaker identity, and prosody—enabling more natural, diverse synthe- sized speech.

**Results-oriented passage (PDF p. 3)**

Table 1 and Figure 2 illustrate the impact of TTS-synthesized speech on speaker recognition. We evaluated CosyVoice, MaskGCT, and NaturalSpeech 3 with varying prompt durations. The results show distinct performance patterns: CosyVoice and NaturalSpeech 3 perform better with shorter prompts, while MaskGCT excels with longer ones. To assess whether these gains stem solely from the in- creased utterance length introduced by TTS-generated speech, we conducted an experiment where short utterances were re- peated to 15 seconds and fused with the original speaker embed- ding. Results confirm that the primary benefits arise from ad- ditional speaker-

**Caveat-oriented passage (PDF p. 4)**

Table 1 also presents the equal error rate (EER) for different TTS models across various speech durations. The results con- firm that as speech duration decreases, the EER increases signif- icantly for all models, highlighting the considerable challenge of short-utterance speaker recognition. Notably, our proposed method exhibits a more pronounced 

## 212. InstructTTSEval: Benchmarking Complex Natural-Language Instruction Following in Text-to-Speech Systems

ID: `2506.16381` | Theme: Evaluation/reliability | Status: `selected_fulltext_review_plus_scoped_core_crosscheck`

Source: https://arxiv.org/pdf/2506.16381

Snapshot SHA-256: `b42a1fcd2d8374c75cfbc83cb7ee0ae01f6022e72846c5e3b1fbc46f74754c20`

Abstract extract: In modern speech synthesis, paralinguistic information--such as a speaker's vocal timbre, emotional state, and dynamic prosody--plays a critical role in conveying nuance beyond mere semantics. Traditional Text-to-Speech (TTS) systems rely on fixed style labels or inserting a speech prompt to control these cues, which severely limits flexibility. Recent attempts seek to employ natural-language instructions to modulate paralinguistic features, substantially improving the generalization of instruction-driven TTS models. Although many TTS systems now support customized synthesis via textual description, their actual ability to interpret and execute complex instructions remains largely unexplored

**Method-oriented passage (PDF p. 2)**

Guo et al., 2024; Kim et al., 2021), and some re- cent works explore free-form natural-language con- trol and show encouraging progress (Yang et al., 2023; Guo et al., 2022; Leng et al., 2023; Liu et al., 2023; Du et al., 2024b; Ji et al., 2023, 2024; Lyth and King, 2024; Zhou et al., 2024; Yang et al., 2025). However, current metrics are in- sufficient for evaluation: most common objective metrics measure speech quality like word error rate (WER) and speaker similarity (SIM), while subjective MOS evaluations depend on costly hu- man annotation and often suffer from inconsistent standards. We still lack standardized benchmarks specifically de

**Results-oriented passage (PDF p. 2)**

tone, etc.) and manifest these choices in the syn- thesized output. To ensure realism, we build our dataset bottom- up: we mine highly expressive clips from movies and TV, apply rigorous cleaning and filtering, and then reverse-generate style instructions from the audio. In total, we offer three tasks with 1,000 English and 1,000 Chinese examples (6,000 in- structions overall), each paired with a reference audio. Finally, we leverage Gemini’s powerful speech-understanding capabilities—using an LLM- as-a-judge setup—to evaluate state-of-the-art in- struct TTS systems. Results show that fine-grained acoustic control remains a major open challen

**Caveat-oriented passage (PDF p. 9)**

We acknowledge that our work may have the fol- lowing limitations: 1) Subjectivity and evalua- tion cost. Some of our tasks, particularly for the Role-Play (RP), are inherently subjective. Inter- annotator agreement among human raters is rela- tively low compared to APS and DSD tasks, which introduces noise when using automated evalua- tors like Ge

Additional interpretation and limitations: [core findings](CORE_FINDINGS.md).

## 213. A Self-Training Approach for Whisper to Enhance Long Dysarthric Speech Recognition

ID: `2506.22810` | Theme: Loop/data selection | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2506.22810

Snapshot SHA-256: `74cb010448c0d249b368f640d293a91a8146281fe4f5a060128372ad4388e98a`

Abstract extract: Dysarthric speech recognition (DSR) enhances the accessibility of smart devices for dysarthric speakers with limited mobility. Previously, DSR research was constrained by the fact that existing datasets typically consisted of isolated words, command phrases, and a limited number of sentences spoken by a few individuals. This constrained research to command-interaction systems and speaker adaptation. The Speech Accessibility Project (SAP) changed this by releasing a large and diverse English dysarthric dataset, leading to the SAP Challenge to build speaker- and text-independent DSR systems. We enhanced the Whisper model's performance on long dysarthric speech via a novel self-training method.

**Method-oriented passage (PDF p. 2)**

Figure 2: Segmentation algorithm (a) and (b). ‘wn’ represents the number of words. ‘Ref’: ‘Reference’. ‘Algo’: ‘Algorithm’. complete sentences even from partial inputs. Liu et al. [24] observed similar mismatches in speech recognition. Both stud- ies addressed this by incorporating “partial sequence” data into training. Following their approach, we attempted to incorporate segmented data to mitigate the training-inference inconsistency. We segmented the unused long dysarthric speech and annotated it using a self-training method. Self-training, a common semi-supervised learning method [25, 26, 27, 28, 29, 30], is employed when labeled data is 

**Results-oriented passage (PDF p. 1)**

effectiveness of fine-tuning models like wav2vec 2.0 [16] and Whisper [2] on previous SAP data (with Whisper showing su- perior performance), we prioritized base model selection. We compared Whisper against other advanced ASR technologies not yet evaluated on the SAP data, including HuBERT [17], and pre-trained models from ESPnet [18] and Wenet [19]. Due to Challenge time constraints and GPU utilization efficiency, we trained on short speech segments (see Section 3.2 for specific training speech duration limits). Furthermore, because Whis- per’s audio encoder truncates long spectrograms to fit its posi- tional encoding (leading to incomplete 

**Caveat-oriented passage (PDF p. 1)**

Dysarthria, a speech disorder stemming from neurological con- ditions like Parkinson’s disease and cerebral palsy, affects vo- cal control and leads to speech impediments such as stutter- ing, abnormal pauses, altered prosody, and mispronunciation. These characteristics pose significant challenges for automatic speech recognition (ASR) systems, whi

## 214. Audio Flamingo 3: Advancing Audio Intelligence with Fully Open Large Audio Language Models

ID: `2507.08128` | Theme: Captioning/grounding | Status: `selected_fulltext_review_plus_scoped_core_crosscheck`

Source: https://arxiv.org/pdf/2507.08128

Snapshot SHA-256: `f966955628f247ed76c7207b7b86048a1790794cc3b5cea47287ec14417f3508`

Abstract extract: We present Audio Flamingo 3 (AF3), a fully open state-of-the-art (SOTA) large audio-language model that advances reasoning and understanding across speech, sound, and music. AF3 introduces: (i) AF-Whisper, a unified audio encoder trained using a novel strategy for joint representation learning across all 3 modalities of speech, sound, and music; (ii) flexible, on-demand thinking, allowing the model to do chain-of-thought-type reasoning before answering; (iii) multi-turn, multi-audio chat; (iv) long audio understanding and reasoning (including speech) up to 10 minutes; and (v) voice-to-voice interaction. To enable these capabilities, we propose several large-scale training datasets curated us

**Method-oriented passage (PDF p. 5)**

(1) We expand coverage of existing reasoning skills and introduce new ones using additional audio sources, increasing the dataset by 3.5M QA pairs: (a) For sounds, we incorporate data from YouTube8M and synthetic sources. (b) For music, we include Music4All [102] and the Million Song Dataset [8]. For YouTube8M, we adapt captions from AudioSetCaps [6] and generate QA using GPT-4.1 with general reasoning prompts from AF2. Additionally, we introduce new reasoning skills and design corresponding prompts to support them. For music, we generate data for novel skills (as AudioSkills was focused more on sounds; details in Table 6) and go beyond capti

**Results-oriented passage (PDF p. 2)**

Table 1: Comparison of various LALMs in terms of capabilities and openness. AF3 stands out as the most capable and open model to date, achieving SOTA results across benchmarks (A in Chat stands for Audio). *Voice-out is powered by our novel streaming TTS implementation, which is also applicable to other LALMs.

**Caveat-oriented passage (PDF p. 2)**

However, existing models still fall short in key areas critical to AGI, such as expert-level reasoning [88, 101], multi-turn and multi-audio dialogue [44], and long audio understanding [40]. We identify two core limitations: (i) most LALMs are trained primarily on short audio for recognition tasks rather than ones that require deliberate reasoning;

Additional interpretation and limitations: [core findings](CORE_FINDINGS.md).

## 215. Active Learning for Text-to-Speech Synthesis with Informative Sample Collection

ID: `2507.08319` | Theme: Loop/data selection | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2507.08319

Snapshot SHA-256: `f71c5e2aa4a61613312e0ed970b48d41b9d9544f77d27264d9890908ffda2d4f`

Abstract extract: The construction of high-quality datasets is a cornerstone of modern text-to-speech (TTS) systems. However, the increasing scale of available data poses significant challenges, including storage constraints. To address these issues, we propose a TTS corpus construction method based on active learning. Unlike traditional feed-forward and model-agnostic corpus construction approaches, our method iteratively alternates between data collection and model training, thereby focusing on acquiring data that is more informative for model improvement. This approach enables the construction of a data-efficient corpus. Experimental results demonstrate that the corpus constructed using our method enables 

**Method-oriented passage (PDF p. 5)**

4) Investigation for data quality estimator: Since our pro- posed method samples a subset of the candidate data for training the data quality estimator, it is important to investigate whether this modification affects the behavior of the estimator. Fig. 7 7 shows a comparison between the estimators trained under two different conditions: the “Baseline” method, which uses all candidate data for training, and our proposed method (“Ours”), which uses only 10% of that data. The results indicate a strong correlation between the two estimators, suggesting that the proposed method maintains similar behavior despite the reduced training data. This fi

**Results-oriented passage (PDF p. 3)**

a result, 2, 719 YouTube videos were processed, yielding approximately 66 hours of candidate speech data, comprising around 60, 000 Japanese utterances. Note that downloading all of them simultaneously was not required. To calculate pseudo MOS, we used 100 phonetically balanced sentences from the JVS corpus [5]. For the final evaluation of the trained TTS models, we used 324 test sentences from the ITA corpus [24]. 2) Text-to-speech model: We employed FastSpeech 2 [25] as our multi-speaker TTS model and used the UNI- VERSAL V1 configuration of the pre-trained HiFi-GAN vocoder [26], [27]. The model architecture and hyperparame- ters were adopt

**Caveat-oriented passage (PDF p. 3)**

1) Real speaker: A straightforward strategy is to sample from the set {xi} i = 1N. Since the corpus construction pro- cess aims to enable high-quality synthesis (above θhq) for as many speakers in Dall as possible, we expect that using these x-vectors will result in synthetic speech that meets or exceeds the threshold. In cases where the synthesize

## 216. Expressive Speech Retrieval using Natural Language Descriptions of Speaking Style

ID: `2508.11187` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2508.11187

Snapshot SHA-256: `175a41296fe8b09aa02a365e8429e6f59d4ce86a4519ac9be93cd37758c897c7`

Abstract extract: We introduce the task of expressive speech retrieval, where the goal is to retrieve speech utterances spoken in a given style based on a natural language description of that style. While prior work has primarily focused on performing speech retrieval based on what was said in an utterance, we aim to do so based on how something was said. We train speech and text encoders to embed speech and text descriptions of speaking styles into a joint latent space, which enables using free-form text prompts describing emotions or styles as queries to retrieve matching expressive speech segments. We perform detailed analyses of various aspects of our proposed framework, including encoder architectures, t

**Method-oriented passage (PDF p. 5)**

Table II shows the main expressive speech retrieval results from our experiments. Our best-performing model configura- tions (RoBERTa + emotion2vec and Flan-T5 + emotion2vec) overall achieve performance on par with, or even slightly exceeding, that of the classification-based baselines. However, note that the baselines are limited to classifying (and therefore retrieving) only speech based on classes that they were trained on. Meanwhile, our proposed framework enables retrieval based on arbitrary natural language queries, which need not perfectly match the style classes seen during training. This offers significantly more flexibility for real

**Results-oriented passage (PDF p. 4)**

C. Evaluation We adopt a controlled protocol to evaluate the retrieval performance of the various models. For each style class, we randomly construct a set of 1000 “retrieval trials”, where each trial is generated by randomly sampling one speech segment that matches the given target class (a positive sample) and 400 distractor utterances sampled from all other classes (negative samples). In other words, each trial is set up to have exactly one relevant target within a set of 401 candidates. To perform evaluation for a given trial, we consider all possible combinations of prompt templates and synonyms for the target style as potential queries 

**Caveat-oriented passage (PDF p. 2)**

II. BACKGROUND AND RELATED WORK A. Speech retrieval Traditionally, speech retrieval has been treated as an exten- sion of text retrieval by transcribing audio using automatic speech recognition (ASR), followed by performing text-based keyword or semantic search over the transcribed content [20]– [22]. However, these cascaded approaches are suscepti

## 217. EmoSSLSphere: Multilingual Emotional Speech Synthesis with Spherical Vectors and Discrete Speech Tokens

ID: `2508.11273` | Theme: Evaluation/reliability | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2508.11273

Snapshot SHA-256: `59cb4e4bfd5e2d197343b4cdc9fdafac9bd5894c730acaf6a032de295424a183`

Abstract extract: This paper introduces EmoSSLSphere, a novel framework for multilingual emotional text-to-speech (TTS) synthesis that combines spherical emotion vectors with discrete token features derived from self-supervised learning (SSL). By encoding emotions in a continuous spherical coordinate space and leveraging SSL-based representations for semantic and acoustic modeling, EmoSSLSphere enables fine-grained emotional control, effective cross-lingual emotion transfer, and robust preservation of speaker identity. We evaluate EmoSSLSphere on English and Japanese corpora, demonstrating significant improvements in speech intelligibility, spectral fidelity, prosodic consistency, and overall synthesis qualit

**Method-oriented passage (PDF p. 2)**

Although existing methods demonstrate notable progress in emotional speech synthesis, challenges remain in achieving ef- fective integration of linguistic, emotional, and acoustic fea- tures, especially in multilingual settings. Current models often struggle with accurately preserving semantic fidelity, speaker individuality, and fine-grained emotional controllability simul- taneously. To address these issues, we propose EmoSSL- Sphere, a multilingual emotional TTS framework that lever- ages spherical emotional vectors and self-supervised learning (SSL)-derived discrete token representations. EmoSSLSphere extends the EmoSphere-TTS [6] archite

**Results-oriented passage (PDF p. 4)**

Table 2: Evaluation results on speech quality and naturalness. The last group of rows represents an ablation study of the proposed model. The nMOS scores are presented with 95% confidence intervals.

**Caveat-oriented passage (PDF p. 6)**

This study introduced EmoSSLSphere, a multilingual emo- tional TTS framework that integrates spherical emotion vectors with discrete token features derived from SSL. By combining interpretable emotion control with prosody-aware token repre- sentations, EmoSSLSphere addresses key limitations in emo- tional TTS synthesis—particularly in emotional con

## 218. MMAU-Pro: A Challenging and Comprehensive Benchmark for Holistic Evaluation of Audio General Intelligence

ID: `2508.13992` | Theme: Evaluation/reliability | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2508.13992

Snapshot SHA-256: `1a60bfa56f0ba68b42e1be53a86a14d0ebc4616081478111f9588dc3187999b4`

Abstract extract: Audio comprehension-including speech, non-speech sounds, and music-is essential for achieving human-level intelligence. Consequently, AI agents must demonstrate holistic audio understanding to qualify as generally intelligent. However, evaluating auditory intelligence comprehensively remains challenging. To address this gap, we introduce MMAU-Pro, the most comprehensive and rigorously curated benchmark for assessing audio intelligence in AI systems. MMAU-Pro contains 5,305 instances, where each instance has one or more audios paired with human expert-generated question-answer pairs, spanning speech, sound, music, and their combinations. Unlike existing benchmarks, MMAU-Pro evaluates auditory

**Method-oriented passage (PDF p. 5)**

Instruction Following Enabling foundation models to follow human instructions is essential for building con- trollable and reliable AI assistants (Ouyang et al. 2022; Chen et al. 2024a; Zhou et al. 2023a). However, evaluating instruction-following remains challenging due to the open- ended nature of many prompts (e.g., “Write a short poem based on the sound you hear”) (Chen et al. 2024a; Wang et al. 2024). To enable objective evaluation, we adopt the constraint-based approach of Zhou et al. (2023b), framing instruction-following as a verifiable subtask within MMAU- Pro. Our design is further inspired by IFEval-Audio (Gao et al. 2025), which i

**Results-oriented passage (PDF p. 6)**

swer. The evaluation is then conducted by comparing this prediction to the ground truth label. This embedding-based selection strategy allows for semantically meaningful pre- dictions even when explicit answer tokens are not gener- ated, and avoids reliance on string-based pattern matching. For evaluating open-ended responses, we employ Qwen2.5- 7B-Instruct as a judge and provide it with the ground truth answer and the prediction. We evaluate each model’s re- sponse on 5 fronts - (i) Correctness: How factually accurate is the response compared to the reference? (ii) Relevance: How well does the response address the specific question asked? (i

**Caveat-oriented passage (PDF p. 1)**

Audio comprehension-including speech, non-speech sounds, and music-is essential for achieving human-level intelligence. Consequently, AI agents must demonstrate holistic audio un- derstanding to qualify as generally intelligent. However, eval- uating auditory intelligence comprehensively remains chal- lenging. To address this gap, we introduce MMAU

## 219. A Framework for Robust Speaker Verification in Highly Noisy Environments Leveraging Both Noisy and Enhanced Audio

ID: `2508.18913` | Theme: Evaluation/reliability | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2508.18913

Snapshot SHA-256: `a1f95e432bd049a29cea8436f37cf06f030ece4594dc599a4cde10008e4a3025`

Abstract extract: Recent advancements in speaker verification techniques show promise, but their performance often deteriorates significantly in challenging acoustic environments. Although speech enhancement methods can improve perceived audio quality, they may unintentionally distort speaker-specific information, which can affect verification accuracy. This problem has become more noticeable with the increasing use of generative deep neural networks (DNNs) for speech enhancement. While these networks can produce intelligible speech even in conditions of very low signal-to-noise ratio (SNR), they may also severely alter distinctive speaker characteristics. To tackle this issue, we propose a novel neural netwo

**Method-oriented passage (PDF p. 2)**

Several previous studies have investigated speaker ver- ification in noisy conditions. Some of these works pro- pose training a speech enhancement module specifically for speaker verification, using a tailored loss function [11] or learning a mapping from noisy to clean speech embeddings [12, 13]. Other approaches focus on learning to extract ro- bust speaker embeddings by separately capturing noise and speaker characteristics [14, 15]. A common strategy is to use a cascaded architecture, where instead of separately pro- cessing speech enhancement and speaker verification, the two modules are integrated into a single framework through joint o

**Results-oriented passage (PDF p. 4)**

Table 1: Speaker verification results using our proposed method, compared to verification on noisy signals and noisy signals enhanced with DeepFilterNet3 [3]. The evaluation was performed using SpeakerNet [1] and ECAPA-TDNN [8] speaker em- beddings, with noise from the MUSAN corpus [21], covering three noise types at varying SNR levels. Performance is measured using the Equal Error Rate (EER), with the best results highlighted in bold.

**Caveat-oriented passage (PDF p. 2)**

for speech enhancement. These models can produce superior speech quality and effectively enhance speech contaminated by higher noise levels. However, their generative nature can lead to significant distortions of the speaker’s intrinsic char- acteristics in the speech signal, especially under challenging noise conditions.

## 220. Towards Improved Speech Recognition through Optimized Synthetic Data Generation

ID: `2508.21631` | Theme: Loop/data selection | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2508.21631

Snapshot SHA-256: `d17242c192ac936d7ec7fa3300b7cdcf9a39fa081a6526e991d72cf1115fe060`

Abstract extract: Supervised training of speech recognition models requires access to transcribed audio data, which often is not possible due to confidentiality issues. Our approach to this problem is to generate synthetic audio from a text-only corpus using a state-of-the-art text-to-speech model with voice cloning capabilities. Our goal is to achieve automatic speech recognition (ASR) performance comparable to models trained on real data. We explore ways to optimize synthetic data generation through finetuning, filtering and evaluation, and its use for training an end-to-end encoder-decoder ASR model. Experiments were conducted using two datasets of spontaneous, conversational speech in Québec French. We sh

**Method-oriented passage (PDF p. 3)**

Generator-Verifier Duration filtering approach does not explicitly evaluate linguistic content fidelity. To address this limitation, we propose leveraging a robust ASR model for content validation. The assumption is that a strong ASR system failing to correctly transcribe a given audio sample means that it likely contains noise, distortions, or linguistic content that does not match the TTS input text. We designed a generation pipeline composed of a Generator and a Verifier. The generator, which may be any TTS model, is responsible for produc- ing synthetic utterances. The verifier, implemented as a pretrained ASR model, transcribes each syn-

**Results-oriented passage (PDF p. 2)**

Table 1: Baseline results on real male and female development and test sets: %WERR refers to WER evaluated with a model trained on real data. BastR and CharbR stand for the original corpora of Bast and Charb.

**Caveat-oriented passage (PDF p. 6)**

In this study, we used XTTS as our only synthesis model, which may have limited the diversity of the resulting generated data. We considered conduct- ing experiments using the model proposed in (Le et al., 2023) due to its promising performance on LibriSpeech, but its unavailability to the research community precluded its use in our study. Investi-

## 221. Do You Hear What I Mean? Quantifying the Instruction-Perception Gap in Instruction-Guided Expressive Text-To-Speech Systems

ID: `2509.13989` | Theme: Speech/audio generation and control | Status: `selected_fulltext_review_plus_scoped_core_crosscheck`

Source: https://arxiv.org/pdf/2509.13989

Snapshot SHA-256: `b87981ff0f92443d8bcc7b996654575f360b1d78f3fb35f608c8861d35b02f28`

Abstract extract: Instruction-guided text-to-speech (ITTS) enables users to control speech generation through natural language prompts, offering a more intuitive interface than traditional TTS. However, the alignment between user style instructions and listener perception remains largely unexplored. This work first presents a perceptual analysis of ITTS controllability across two expressive dimensions (adverbs of degree and graded emotion intensity) and collects human ratings on speaker age and word-level emphasis attributes. To comprehensively reveal the instruction-perception gap, we provide a data collection with large-scale human evaluations, named Expressive VOice Control (E-VOC) corpus. Furthermore, we 

**Method-oriented passage (PDF p. 3)**

We recruited native English speakers from the United States via the Prolific platform. All participants completed a brief training session before starting the main annotation task. To ensure the reliability of our data, we implemented a rigorous quality control protocol. We embedded check utterances with gold-standard labels sourced from public corpora, including CREMA-D [28] (for emotion inten- sity), EMNS (for emphasis), and Nexdata.ai [29]/CREMA-D [28]

**Results-oriented passage (PDF p. 2)**

We introduce two dimensions to evaluate fine-grained controlla- bility, because complex expressions like sarcasm require subtle prosodic shifts. Precise scalar control is thus a prerequisite for high-fidelity synthesis. Task I. Adverbs of Degree (Adv. Deg.) tests whether models fol- low degree modifiers such as slightly, very, and extremely to adjust prosody (loudness, pitch, speaking rate) and emotion. This dimen- sion is important because adverbial scaling provides users with a simple way to control the fine-grained prosodic variation, essential for storytelling and emotional expression. Task II. Emotion–Intensity Adjective (Emo-I.A.) evalu

**Caveat-oriented passage (PDF p. 2)**

to correlate audio-text embeddings with human judgments of style relevance, while Emosphere [16] utilized emotion2vec [17] embed- dings to evaluate emotion similarity. (3) Instruction-following perceptual measures. A third line of work directly involves human listeners or automated judges to rate how well synthesized speech matches a textual instru

Additional interpretation and limitations: [core findings](CORE_FINDINGS.md).

## 222. Aligning Audio Captions with Human Preferences

ID: `2509.14659` | Theme: Captioning/grounding | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2509.14659

Snapshot SHA-256: `df6fd91bfe989c38eb51bbf496c40893f0e2923700210bd5f4e943cbfbb6b630`

Abstract extract: Current audio captioning relies on supervised learning with paired audio-caption data, which is costly to curate and may not reflect human preferences in real-world scenarios. To address this, we propose a preference-aligned audio captioning framework based on Reinforcement Learning from Human Feedback (RLHF). To capture nuanced preferences, we train a Contrastive Language-Audio Pretraining (CLAP) based reward model using human-labeled pairwise preference data. This reward model is integrated into an RL framework to fine-tune any baseline captioning system without ground-truth annotations. Extensive human evaluations across multiple datasets show that our method produces captions preferred o

**Method-oriented passage (PDF p. 1)**

Current audio captioning relies on supervised learning with paired audio-caption data, which is costly to curate and may not reflect human preferences in real-world scenarios. To address this, we propose a preference-aligned audio captioning frame- work based on Reinforcement Learning from Human Feedback (RLHF). To capture nuanced preferences, we train a Contrastive Language-Audio Pretraining (CLAP) based reward model using human-labeled pairwise preference data. This reward model is integrated into an RL framework to fine-tune any baseline cap- tioning system without ground-truth annotations. Extensive hu- man evaluations across multiple dat

**Results-oriented passage (PDF p. 4)**

We evaluate our RLHF framework on both public and propri- etary datasets, including challenging cases where baseline mod- els fail to produce accurate or natural captions. We observe that higher scores on automated metrics do not necessarily translate to improved human satisfaction. Table 1 shows that although the baseline performs well on metrics such as BLEU and CIDEr, it does not align with human preferences, while semantic met- rics such as S-BERT and FENSE exhibit inconsistent trends, highlighting the limitations of rule-based and semantic evalu- ation metrics. In contrast, our RLHF model improves caption quality, as reflected by higher 

**Caveat-oriented passage (PDF p. 1)**

Audio captioning, the task of generating natural language de- scriptions for acoustic scenes, has become an important bench- mark for evaluating audio-language models. Unlike image cap- tioning, which benefits from explicit spatial and semantic cues, audio captioning faces inherent ambiguity and temporal com- plexity, making accurate and human-alig

## 223. Qwen3-Omni Technical Report

ID: `2509.17765` | Theme: Speech/audio generation and control | Status: `selected_fulltext_review_plus_scoped_core_crosscheck`

Source: https://arxiv.org/pdf/2509.17765

Snapshot SHA-256: `4608d7f5d0694dd09a66144dac921797e161331d92b5eef133615bec392ec928`

Abstract extract: We present Qwen3-Omni, a single multimodal model that, for the first time, maintains state-of-the-art performance across text, image, audio, and video without any degradation relative to single-modal counterparts. Qwen3-Omni matches the performance of same-sized single-modal models within the Qwen series and excels particularly on audio tasks. Across 36 audio and audio-visual benchmarks, Qwen3-Omni achieves open-source SOTA on 32 benchmarks and overall SOTA on 22, outperforming strong closed-source models such as Gemini-2.5-Pro, Seed-ASR, and GPT-4o-Transcribe. Qwen3-Omni adopts a Thinker-Talker MoE architecture that unifies perception and generation across text, images, audio, and video, yi

**Method-oriented passage (PDF p. 5)**

Architecturally, our approach departs from Xu et al. (2025) by operating directly on RVQ tokens. The Talker employs a hierarchical prediction scheme: the backbone ingests the aggregated codebook features of the current frame and uses a linear head to predict the zeroth codebook, after which a multi-token prediction (MTP) module generates all residual codebooks. This strategy enables the model to learn a complete representation of acoustic details, enhancing vocal expressivity. Consequently, waveform reconstruction is simplified to a lightweight causal ConvNet (Code2Wav), which significantly reduces inference latency and computational cost (FL

**Results-oriented passage (PDF p. 11)**

Additionally, on VoiceBench shown in Table 7, Qwen3-Omni-Thinking achieves an impressive average score of 89.5, surpassing all other audio language models except Gemini-2.5-Pro (89.6). This showcases our model’s strong capabilities in speech interaction. Qwen3-Omni also demonstrates impressive performance in audio reasoning, outperforming the powerful closed-source models Gemini-2.5-Pro and Gemini-2.5-Flash on the MMAU benchmark, as well as Gemini-2.5-Flash and GPT-4o-Audio on MMSU. These results demonstrate the powerful capabilities of Qwen3-Omni in general audio understanding and reasoning.

**Caveat-oriented passage (PDF p. 12)**

To assess its capabilities, we evaluated the performance of Qwen3-Omni-Thinking against several state- of-the-art reasoning models. The comparative results, summarized in Table 10, indicate that our proposed model achieves significant advancements. For instance, on Math and STEM benchmarks, it outperforms the Qwen3-Omni-Instruct baseline by 4.4 poi

Additional interpretation and limitations: [core findings](CORE_FINDINGS.md).

## 224. Towards Evaluating Generative Audio: Insights from Neural Audio Codec Embedding Distances

ID: `2509.18823` | Theme: Representations/codecs | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2509.18823

Snapshot SHA-256: `e9986bd58eb1085ead389da04284b4cb29d756c05f0041e087a4edf7951823dd`

Abstract extract: Neural audio codecs (NACs) achieve low-bitrate compression by learning compact audio representations, which can also serve as features for perceptual quality evaluation. We introduce DACe, an enhanced, higher-fidelity version of the Descript Audio Codec (DAC), trained on diverse real and synthetic tonal data with balanced sampling. We systematically compare Fréchet Audio Distance (FAD) and Maximum Mean Discrepancy (MMD) on MUSHRA tests across speech, music, and mixed content. FAD consistently outperforms MMD, and embeddings from higher-fidelity NACs (such as DACe) show stronger correlations with human judgments. While CLAP LAION Music (CLAP-M) and OpenL3 Mel128 (OpenL3-128M) embeddings achie

**Method-oriented passage (PDF p. 1)**

Neural audio codecs (NACs) achieve low-bitrate com- pression by learning compact audio representations, which can also serve as features for perceptual quality evaluation. We introduce DACe, an enhanced, higher-fidelity version of the Descript Audio Codec (DAC), trained on diverse real and synthetic tonal data with balanced sampling. We systemati- cally compare Fr´echet Audio Distance (FAD) and Maximum Mean Discrepancy (MMD) on MUSHRA tests across speech, music, and mixed content. FAD consistently outperforms MMD, and embeddings from higher-fidelity NACs (such as DACe) show stronger correlations with human judgments. While CLAP LAION Music (C

**Results-oriented passage (PDF p. 3)**

domized onset timing and Poisson-distributed event density. Balanced sampling ensured that 33% of each mini-batch con- sisted exclusively of challenging synthetic tonal excerpts. A MUSHRA test (Fig. 2) compared DAC and DACe at 32 kb/s stereo using dual-mono coding. Test excerpts were drawn from an internal dataset (since ODAQ excerpts were not suf- ficiently challenging), with none overlapping the training set, and were selected based on maximal Mel-loss [7] deviation between the two NACs. As shown in Fig. 2, DACe consis- tently outperforms DAC, with strong gains on tonal items (e.g., triangles and the MPEG glockenspiel test file sm02) and on

**Caveat-oriented passage (PDF p. 2)**

The goal of an audio codec is to compress audio to a low bi- trate while reconstructing a signal that is perceptually close to the original. Time-domain, end-to-end neural audio codecs (NACs) [6, 7, 18] typically employ a fully convolutional en- coder that processes the waveform and outputs embeddings at a reduced sampling rate. These embeddings ar

## 225. AUV: Teaching Audio Universal Vector Quantization with Single Nested Codebook

ID: `2509.21968` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2509.21968

Snapshot SHA-256: `aa25471037414955c28991b8d6b687eef5c22a44c2438dcbc762aeb69f7cce24`

Abstract extract: We propose AUV, a unified neural audio codec with a single codebook, which enables a favourable reconstruction of speech and further extends to general audio, including vocal, music, and sound. AUV is capable of tackling any 16 kHz mixed-domain audio segment at bit rates around 700 bps. To accomplish this, we guide the matryoshka codebook with nested domain-specific partitions, assigned with corresponding teacher models to perform distillation, all in a single-stage training. A conformer-style encoder-decoder architecture with STFT features as audio representation is employed, yielding better audio quality. Comprehensive evaluations demonstrate that AUV exhibits comparable audio reconstructi

**Method-oriented passage (PDF p. 2)**

As illustrated in Fig. 1, AUV builds upon the framework established by existing acoustic codecs, namely EnCodec [8], DAC [9], and so on. A single-codebook acoustic audio codec typically maintains an encoder-quantizer-decoder structure, the encoder transforms the in- put audio features into latent representations, the single-layer quan- tizer discretizes the latents into tokens, and the decoder finally re- constructs the waveform from the compressed discrete tokens. Consistent with the findings of previous research [35], our early experiments reveal that scaling the encoder yields minimal gains for reconstruction while scaling the decoder boos

**Results-oriented passage (PDF p. 2)**

output [36]. We weight more parameters to the codec decoder for the reason mentioned above, in practice, using more layers for the decoder compared to the encoder. The Fourier transform is config- ured with a chosen hop length to obtain spectrum features, with the same token rate desired for discrete tokens after vector quantization. Thus, there are no learnable upsampling or downsampling modules in the structure. By comparing with the highly competitive baseline, which is VQ with Mimi [5] encoder-decoder, we demonstrate the effectiveness of our model design. The details are provided in the experiments section. The basic loss functions of AUV

**Caveat-oriented passage (PDF p. 2)**

Fig. 1. Overview of AUV framework. During training, the input au- dio domain is made aware to the model, whereas it remains agnostic during inference, meeting the actual usage scenario.

## 226. HiStyle: Hierarchical Style Embedding Predictor for Text-Prompt-Guided Controllable Speech Synthesis

ID: `2509.25842` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2509.25842

Snapshot SHA-256: `338eacfe0004bc98e37c54d4b7c888e6ad213f6cebc54241be6b8ab5e9621cc3`

Abstract extract: Controllable speech synthesis refers to the precise control of speaking style by manipulating specific prosodic and paralinguistic attributes, such as gender, volume, speech rate, pitch, and pitch fluctuation. With the integration of advanced generative models, particularly large language models (LLMs) and diffusion models, controllable text-to-speech (TTS) systems have increasingly transitioned from label-based control to natural language description-based control, which is typically implemented by predicting global style embeddings from textual prompts. However, this straightforward prediction overlooks the underlying distribution of the style embeddings, which may hinder the full potentia

**Method-oriented passage (PDF p. 3)**

– We conduct a comprehensive visualization and analysis of the style embed- ding spaces in mainstream TTS systems, revealing their hierarchical orga- nization: globally clustered by timbre and further subdivided by style at- tributes. – We propose HiStyle, a novel two-stage style embedding predictor with con- trastive learning, which hierarchically predicts style embeddings conditioned on textual prompts and achieves significantly improved controllability and naturalness in speech synthesis. – We develop an improved data annotation pipeline that integrates statistical analysis with human perceptual evaluation, achieving more accurate and perc

**Results-oriented passage (PDF p. 11)**

handling both linguistic and paralinguistic cues. Moreover, our method main- tains a low WER of 3.32% and a low UTMOS of 3.41, demonstrating that en- hanced controllability does not come at the cost of speech intelligibility or natu- ralness. Additionally, for subjective indicators, our method achieves a Style-MOS score of 3.71 ± 0.05, the highest among all competing systems, demonstrating superior style controllability and a stronger alignment between the intended and perceived speaking style. In terms of naturalness, our method obtains a N-MOS of 3.80 ± 0.08, which is competitive with the best performing baseline (Query Encoder: 3.83 ± 0.09

**Caveat-oriented passage (PDF p. 2)**

In recent years, there has been a growing research focus on developing style- controllable TTS systems that allow flexible control of speaking style attributes, such as speech rate, pitch, and volume. A common approach in prior work [8–10] is to use categorical labels, e.g. speaking rate level or emotion category, to rep- resent and control these s

## 227. Post-Training Quantization for Audio Diffusion Transformers

ID: `2510.00313` | Theme: Efficiency/adaptation | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2510.00313

Snapshot SHA-256: `b2d23b639e5597a16770259fb7bcc443a39d77885372fd288b074bb36cc540c2`

Abstract extract: Diffusion Transformers (DiTs) enable high-quality audio synthesis but are often computationally intensive and require substantial storage, which limits their practical deployment. In this paper, we present a comprehensive evaluation of post-training quantization (PTQ) techniques for audio DiTs, analyzing the trade-offs between static and dynamic quantization schemes. We explore two practical extensions (1) a denoising-timestep-aware smoothing method that adapts quantization scales per-input-channel and timestep to mitigate activation outliers, and (2) a lightweight low-rank adapter (LoRA)-based branch derived from singular value decomposition (SVD) to compensate for residual weight errors. U

**Method-oriented passage (PDF p. 2)**

For our analysis, we chose Stable Audio Open [29] because it is fully open-source and provides open access to the model’s weights. Moreover, its architecture combines an autoencoder, T5- based text conditioning, and transformer-based diffusion, which is representative of modern DiTs for audio generation. Finally, the model is optimized for consumer GPUs, has strong community support, and has reproducible computational benchmarks, thus ideal for our study. Same as Stable Audio Open, we use AudioCaps [30] as benchmark. Most DiTs, including Stable Audio’s, are constructed from stacks of transformer blocks, each comprising self-attention layers a

**Results-oriented passage (PDF p. 4)**

We evaluate three quantization strategies under two precision set- tings: W8A8 and W4A8. The quantization strategies are SmoothQuant Dynamic (SQD) with and without low-rank adaptation (+LoRA), and SmoothQuant Static (SQS). Please see Section 2 for details about these methods. Results are shown in Table 1. We found that SQD models closely match or even surpass our full-precision baseline across objective metrics (CLAP, KLpasst, and FDopenl3) for the two precision configurations. This shows that dynamic calibration effectively handles activation outliers at each timestep, with minimal performance loss after quantization.

**Caveat-oriented passage (PDF p. 4)**

In this paper, we conducted a comprehensive study of PTQ strategies for audio DiTs, with a focus on the trade-offs between static and dynamic calibration. We introduced two practical extensions: denoising-timestep-aware smoothing and LoRA to compensate for residual weight errors. Our results show that SQD, with or without LoRA, preserves generation

## 228. Semantic Differentiation in Speech Emotion Recognition: Insights from Descriptive and Expressive Speech Roles

ID: `2510.03060` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2510.03060

Snapshot SHA-256: `337f0ed7d62f4df1c8d984673c63b0b2dd8796425409a92d4533f8259e017519`

Abstract extract: Speech Emotion Recognition (SER) is essential for improving human-computer interaction, yet its accuracy remains constrained by the complexity of emotional nuances in speech. In this study, we distinguish between descriptive semantics, which represents the contextual content of speech, and expressive semantics, which reflects the speaker's emotional state. After watching emotionally charged movie segments, we recorded audio clips of participants describing their experiences, along with the intended emotion tags for each clip, participants' self-rated emotional responses, and their valence/arousal scores. Through experiments, we show that descriptive semantics align with intended emotions, wh

**Method-oriented passage (PDF p. 3)**

Our contribution lies in bridging the gap between stimulus-based emotion elicitation and the actual emotions conveyed by participants in speech. By segmenting utterances according to their semantic roles and analyzing how different roles align with either intended or evoked emotions, we propose a novel way to interpret emotional speech beyond tra- ditional modality-based or label-based approaches. While prior SER studies have emphasized either acoustic or multimodal representations, our work suggests that semantic structure in language - ac- cessible only through text - offers a distinct and in- terpretable signal for differentiating between 

**Results-oriented passage (PDF p. 2)**

Emotions are complex psychological and physio- logical responses to salient events, involving bod- ily sensations, expressive behaviors, and cogni- tive evaluations (Moors, 2024, 2009). Various lin- guistic features, including prosody, lexical choice, and sentence structure, play a role in the percep- tion and expression of emotions (Mohammad and Turney, 2010; Barrett et al., 2007; Keltner et al., 2019). Speech emotion recognition (SER) mod- els aim to detect emotional states from speech us- ing acoustic, textual, or multimodal signals. With the advancement of LLMs and automatic speech recognitions (ASR), text-based emotion classifi- cation h

**Caveat-oriented passage (PDF p. 3)**

et al., 2020), SAMAINE (McKeown et al., 2011), and RECOLA (Ringeval et al., 2013), and elicited speech datasets, such as LSSED (Fan et al., 2021), BAUM-1 (Zhalehpour et al., 2016), and eNTER- FACE (Batliner et al., 2006), audios are recorded in a freely speaking environment or with emotion elicitation methods. Speech is then annotated by a third pa

## 229. Detecting and Mitigating Insertion Hallucination in Video-to-Audio Generation

ID: `2510.08078` | Theme: Captioning/grounding | Status: `excluded_after_screening`

Source: https://arxiv.org/pdf/2510.08078

Snapshot SHA-256: `3438f76d8f5470f77ddd01a46de7dea2fb072f905487489379e4c37de2da0f40`

Excluded: Video-to-audio insertion hallucination; outside chosen audio-only generation design

Abstract extract: Video-to-Audio generation has made remarkable strides in automatically synthesizing sound for video. However, existing evaluation metrics, which focus on semantic and temporal alignment, overlook a critical failure mode: models often generate acoustic events, particularly speech and music, that have no corresponding visual source. We term this phenomenon Insertion Hallucination and identify it as a systemic risk driven by dataset biases, such as the prevalence of off-screen sounds, that remains completely undetected by current metrics. To address this challenge, we first develop a systematic evaluation framework that employs a majority-voting ensemble of multiple audio event detectors. We al

**Method-oriented passage (PDF p. 2)**

menter [8], YAMNet [9], and PANNs [14], and fusing their outputs through majority voting. The pipeline is then vali- dated on a human-annotated set to assess its accuracy. Fi- nally, we introduce two metrics, IH@vid (the fraction of videos containing hallucination) and IH@dur (the fraction of hallucinated duration), to quantify the frequency and severity of IH in V2A models. Building on this, we propose a novel inference-time con- ditioning method called HALCON. HALCON does not re- quire retraining the model and instead operates in three stages. In Stage 1, the model generates an initial audio pre- diction from the input video. In Stage 2, we

**Results-oriented passage (PDF p. 6)**

We next apply our validated IH metrics to state-of-the-art V2A models and to evaluate the effectiveness of our pro- posed HALCON method. Baseline models exhibit systematic hallucination. Ta- ble 1 reports results across Kling-Audio-Eval, VGGSound, and AVE. Both MMAudio and ThinkSound generate hal- lucinations in a substantial portion of videos (IH@vid 12– 24%), with spurious speech or music often occupying 4– 15% of the total duration. These findings establish that IH is not a rare anomaly but a widespread failure pattern in cur- rent V2A systems. The Ground-truth (GT) row, obtained by running our proposed IH detection pipeline on the dataset

**Caveat-oriented passage (PDF p. 4)**

Detecting hallucinations reliably requires addressing the limitations of individual audio classifiers. To this end, we design a multi-detector ensemble that combines three com- plementary detectors: inaSpeechSegmenter [8], YAMNet [9], and PANNs [14]. Our pipeline consists of three stages: 1. Candidate Filtering. Samples with ground-truth labels in 

## 230. UALM: Unified Audio Language Model for Understanding, Generation and Reasoning

ID: `2510.12000` | Theme: Captioning/grounding | Status: `selected_fulltext_review_plus_scoped_core_crosscheck`

Source: https://arxiv.org/pdf/2510.12000

Snapshot SHA-256: `4d6a32f30d9afc43b475251f7ac0aa74f3e2f3b731b2f4ad31cc69372c52006f`

Abstract extract: Recent advances in the audio language modeling (ALM) domain tackle audio understanding and text-to-audio generation as separate tasks. Very few studies attempt to unify these tasks -- an essential step toward advanced multimodal reasoning. This paper introduces U}nified Audio Language Model (UALM), which aims to unify audio understanding, text-to-audio generation, and multimodal reasoning in a single model. To achieve this goal, we first present UALM-Gen, a text-to-audio language model that directly predicts audio tokens and is comparable to state-of-the-art diffusion-based models. We then demonstrate, using proper data blending, training recipes, and inference techniques, that our single UA

**Method-oriented passage (PDF p. 2)**

The first challenge is to achieve high-quality text-to-audio via a language model. Prior diffusion- based text-to-audio models (Evans et al., 2024; Lee et al., 2024; Fei et al., 2024) outperform autore- gressive models (Yang et al., 2023; Copet et al., 2024) in quality, potentially due to better inductive bias (Vastola, 2025) and data efficiency (Prabhudesai et al., 2025). We discover several important findings for successful text-to-audio generation via a decoder-only language model: (i) in terms of data scaling, we need an order of magnitude more audio data than diffusion-based models; (ii) we show that training and sampling with classifier

**Results-oriented passage (PDF p. 7)**

Table 1: Audio Generation results of UALM-Gen (§2.2) and UALM (§2.3) compared to LM-based and diffusion-based baselines. 5-scale subjective scores (OVL, REL) 95% CI ≈0.10. Bold indicates best, underline second-best.

**Caveat-oriented passage (PDF p. 2)**

modeling paradigms: understanding tasks are mainly addressed with auto-regressive large language models (Goel et al., 2025; Xu et al., 2025), while state-of-the-art generation models are mostly based on diffusion models (Lee et al., 2024; Fei et al., 2024; Valle et al., 2025). Second, reasoning within the audio domain remains highly under-explored.

Additional interpretation and limitations: [core findings](CORE_FINDINGS.md).

## 231. LongCat-Audio-Codec: An Audio Tokenizer and Detokenizer Solution Designed for Speech Large Language Models

ID: `2510.15227` | Theme: Representations/codecs | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2510.15227

Snapshot SHA-256: `54f8b2abe324e544b5e7b6a4c6393d4d6b0d94277edf593aa4958111bcf8b044`

Abstract extract: This paper presents LongCat-Audio-Codec, an audio tokenizer and detokenizer solution designed for industrial grade end-to-end speech large language models. By leveraging a decoupled model architecture and a multistage training strategy, LongCat-Audio-Codec exhibits robust semantic modeling capabilities, flexible acoustic feature extraction capabilities, and low-latency streaming synthesis capabilities. It encodes speech at an ultra-low frame rate of 16.67 Hz, with a minimum bitrate of 0.43 kbps and a maximum bitrate of 0.87 kbps. Evaluation results demonstrate that LongCat-Audio-Codec achieves strong speech intelligibility and is capable of synthesizing highquality speech at low bitrate, thu

**Method-oriented passage (PDF p. 4)**

Building upon these findings, we introduce a semantic-acoustic tokenization framework. Our architecture implements specialized encoders for independent feature extraction: a semantic encoder for linguistic information capture and an acoustic encoder for detailed speech characteristic preservation. This dual-path approach facilitates more robust and comprehensive speech representation learning.

**Results-oriented passage (PDF p. 5)**

Our semantic training pipeline begins with unsupervised pre-training using the BEST-RQ [25] method on in-house speech data, followed by supervised fine-tuning for ASR tasks of Chinese and English with CTC loss [26]. The complete semantic encoder contains approximately 500M parameters. We subsequently conducted a comprehensive comparison of K-means clustering results using embeddings extracted from various hidden layers of both models. Downstream task evaluations, as listed in Table 3, demonstrate that the last layer of the CTC fine-tuned model contains the most semantically rich representations. The proposed semantic-acoustic splited architec

**Caveat-oriented passage (PDF p. 2)**

Understanding in text-speech multimodal systems refers to the ability to establish robust cross-modal associations between text and speech, leveraging the rich knowledge embedded in textual corpora while minimizing reliance on large-scale aligned training data. While acoustic-only tokenization frameworks have been validated in prior work [20], thei

## 232. Hallucination Benchmark for Speech Foundation Models

ID: `2510.16567` | Theme: Evaluation/reliability | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2510.16567

Snapshot SHA-256: `e062e6aa31f7132cf510b9f90d4ea00fb7e5dfcf31ecfd39fbfba759790e233f`

Abstract extract: Hallucinations in automatic speech recognition (ASR) systems refer to fluent and coherent transcriptions produced by neural ASR models that are completely unrelated to the underlying acoustic input (i.e., the speech signal). While similar to conventional decoding errors in potentially compromising the usability of transcriptions for downstream applications, hallucinations can be more detrimental due to their preservation of syntactically and semantically plausible structure. This apparent coherence can mislead subsequent processing stages and introduce serious risks, particularly in critical domains such as healthcare and law. Conventional evaluation metrics are primarily centered on error-b

**Method-oriented passage (PDF p. 1)**

Hallucinations in automatic speech recognition (ASR) systems refer to fluent and coherent transcriptions produced by neural ASR models that are completely un- related to the underlying acoustic input (i.e., the speech signal). While similar to conventional decoding errors in potentially compromising the usability of tran- scriptions for downstream applications, hallucinations can be more detrimental due to their preservation of syntactically and semantically plausible structure. This apparent coherence can mislead subsequent processing stages and introduce serious risks, particularly in critical domains such as healthcare and law. Conventiona

**Results-oriented passage (PDF p. 8)**

Metrics correlation. Figure 3 reports the Spearman correlation between SHALLOW’s four hallucina- tion metrics across five WER regimes. At low WER (10–30%), the metrics exhibit strong monotonic relationships (ρs > 0.80), indicating that when errors are sparse, they tend to co-occur and scale similarly across categories. However, as WER increases, these correlations degrade substantially. By WER 50%, several metric pairs show weak or even negative associations (e.g., Lexical–Morphological at ρs = –0.14), and by WER 90%, correlations such as Lexical–Semantic drop below –0.45. This trend suggests that hallucination types decouple under degraded c

**Caveat-oriented passage (PDF p. 4)**

stems from the inherent balance between maintaining acoustic fidelity and producing fluent, coherent text. ASR outputs are typically evaluated using error-based metrics like WER, which computes the minimum edit distance between reference and hypothesized transcriptions Levenshtein et al. (1966). While easy to calculate, WER has pitfalls, mainly bec

## 233. Modeling strategies for speech enhancement in the latent space of a neural audio codec

ID: `2510.26299` | Theme: Representations/codecs | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2510.26299

Snapshot SHA-256: `5892aefaf740c2d9053cca811b5a5cd9d1834e2c3149e6d0f1c93fe827ffd03a`

Abstract extract: Neural audio codecs (NACs) provide compact latent speech representations in the form of sequences of continuous vectors or discrete tokens. In this work, we investigate how these two types of speech representations compare when used as training targets for supervised speech enhancement. We consider both autoregressive and non-autoregressive speech enhancement models based on the Conformer architecture, as well as a simple baseline where the NAC encoder is simply fine-tuned for speech enhancement. Our experiments reveal three key findings: predicting continuous latent representations consistently outperforms discrete token prediction; autoregressive models achieve higher quality but at the ex

**Method-oriented passage (PDF p. 2)**

noisy tokens y, the clean speech tokens xt,1:n−1 at time t and quan- tization stages 1 to n −1, and the past clean speech tokens x1:t−1 at all quantization stages. Therefore, we have PK k=1 ft,n,k(·) = 1. Inspired by the RQ-Transformer model [20] for text-to-image gen- eration and by the Conformer model [24] for speech recognition, in this work, we propose the RQ-Conformer to implement the function f (D-AR). The proposed model is composed of 3 modules: (i) a bidi- rectional Conformer for processing the noisy speech tokens y, (ii) a causal Conformer to autoregressively process the clean speech to- kens over time x1:t−1, and (iii) a causal tran

**Results-oriented passage (PDF p. 4)**

Table 1 reports objective evaluations across all models. The most noticeable observation is that models trained to predict continuous codec representations consistently outperform their discrete coun- terparts, irrespective of AR/NAR design (on average, +0.80 UTMOS and +0.40 SIG, comparing C-AR, C-NAR, and C-FT with their dis- crete counterparts). This gap is also evident when comparing C-FT against D-FT. To further investigate the weakness of discrete models, we in- troduce a variant of D-NAR that uses continuous inputs ¯y instead of discrete noisy tokens y. This allows us to measure to what extent the input representation affects the D-NAR 

**Caveat-oriented passage (PDF p. 2)**

where N denotes a multivariate Gaussian distribution over ¯xt with mean vector f (C-AR) t (·) and identity covariance matrix IL. Here, f denotes a causal Conformer model for processing the noisy speech embeddings ¯y concatenated to the clean speech latent vectors ¯x1:t−1. In this approach, we consider temporal dependencies using an AR model over ti

## 234. PASE: Leveraging the Phonological Prior of WavLM for Low-Hallucination Generative Speech Enhancement

ID: `2511.13300` | Theme: Captioning/grounding | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2511.13300

Snapshot SHA-256: `1e817a826fc316d449285df71b0482c80cb40479eab66173437ee973d7451b0e`

Abstract extract: Generative models have shown remarkable performance in speech enhancement (SE), achieving superior perceptual quality over traditional discriminative approaches. However, existing generative SE approaches often overlook the risk of hallucination under severe noise, leading to incorrect spoken content or inconsistent speaker characteristics, which we term linguistic and acoustic hallucinations, respectively. We argue that linguistic hallucination stems from models' failure to constrain valid phonological structures and it is a more fundamental challenge. While language models (LMs) are well-suited for capturing the underlying speech structure through modeling the distribution of discrete toke

**Method-oriented passage (PDF p. 2)**

limited number of discrete tokens inherently discards essen- tial acoustic information such as pitch and timbre, making them ill-equipped to handle acoustic hallucinations. To overcome these limitations, we propose the Phonologically Anchored Speech Enhancer (PASE), a novel generative framework that circumvents the pitfalls of LM-based approaches. First, instead of learning a phonological prior from corrupted inputs, PASE directly leverages the robust, pre-existing prior embedded in the self-supervised model WavLM (Chen et al. 2022). Second, PASE operates entirely in the continuous representation space, avoiding the information loss from disc

**Results-oriented passage (PDF p. 6)**

4.3 Comparison with Baselines Results on the LibriTTS Test Set We compare PASE against various SOTA baselines, with results on our simu- lated test set summarized in Table 6. The key findings are as follows: (1) The discriminative TF-GridNet achieves a low WER of 9.93% and a high SpkSim of 0.80, confirm- ing that discriminative models are less prone to hallucina- tions. However, this comes at the cost of perceptual qual- ity, as evidenced by its significantly lower UTMOS score of 2.62. (2) The LM-based LLaSE-G1 suffers from severe hallucinations, with a markedly high WER of 36.58% and a poor SpkSim of 0.42, supporting our hypothesis that mod-

**Caveat-oriented passage (PDF p. 3)**

guistically inconsistent outputs. Some DLM variants, such as SELM (Wang et al. 2024) and LLaSE-G1 (Kang et al. 2025), adopt a parallel prediction paradigm, framing denois- ing as a masked prediction task in order to encourage the model to capture contextual dependencies when inferring the “masked” (i.e., noisy) tokens. However, we contend this anal

## 235. Training Text-to-Speech Model with Purely Synthetic Data: Feasibility, Sensitivity, and Generalization Capability

ID: `2512.17356` | Theme: Loop/data selection | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2512.17356

Snapshot SHA-256: `466bae0c18fe205662fe8f66c8132987676ce4d8260a8a0d468eac3d56f602af`

Abstract extract: The potential of synthetic data in text-to-speech (TTS) model training has gained increasing attention, yet its rationality and effectiveness require systematic validation. In this study, we systematically investigate the feasibility of using purely synthetic data for TTS training and explore how various factors--including text richness, speaker diversity, noise levels, and speaking styles--affect model performance. Our experiments reveal that increasing speaker and text diversity significantly enhances synthesis quality and robustness. Cleaner training data with minimal noise further improves performance. Moreover, we find that standard speaking styles facilitate more effective model learni

**Method-oriented passage (PDF p. 2)**

In recent years, large-scale zero-shot TTS models have significantly advanced, achieving remarkable improvements in speech naturalness and expressiveness. Diffusion or Flow-matching based Zero-Shot TTS [5, 27] is one of the repre- sentative methods, which handle the problem in a non-auto regressive man- ner. Auto-regressive TTS [6, 28], especially neural-codec based model [4, 29–31], on the other hand, predicts each audio sample or feature frame sequentially. Both methods significantly improve the quality and versatility of synthesized speech, demonstrating the role of scaling laws in the TTS task. In this work, we choose several SOTA or infl

**Results-oriented passage (PDF p. 4)**

Table 2. Performance Comparison on LibriSpeech and SeedTTS test sets. “Ground Truth” means calculating evaluation metrics (skip SIM) directly on the two test dataset. “XTTS-v2”, “CosyVoice2”, and “ChatTTS” mean using the three large scale TTS models to infer test dataset respectively. Since ChatTTS does not support zero-shot TTS tasks, there is no SIM metrics in this case. “Matcha-TTS” means our experiment on four different training data. R refers to real data LibriSpeech train-100. FXT T S−v2, FCosyV oice2, and FChatT T S refer to synthetic data generated by the three large scale TTS models respectively.

**Caveat-oriented passage (PDF p. 7)**

increases across all evaluation metrics, suggesting that greater speaker variability enhances the system’s generalization and robustness by exposing the model to a wider range of speaker characteristics. However, when the number of speakers exceeds 50, improvements in Word Error Rate (WER) and Unweighted Task Mean Opinion Score (UTMOS) begin to pla

## 236. OV-InstructTTS: Towards Open-Vocabulary Instruct Text-to-Speech

ID: `2601.01459` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2601.01459

Snapshot SHA-256: `9cb54203577cdb27e5e609187653d57f3f8c6ad255d35d52f76ac880112b7855`

Abstract extract: Instruct Text-to-Speech (InstructTTS) leverages natural language descriptions as style prompts to guide speech synthesis. However, existing InstructTTS methods mainly rely on a direct combination of audio-related labels or their diverse rephrasings, making it difficult to handle flexible, high-level instructions. Such rigid control is insufficient for users such as content creators who wish to steer generation with descriptive instructions. To address these constraints, we introduce OV-InstructTTS, a new paradigm for open-vocabulary InstructTTS. We propose a comprehensive solution comprising a newly curated dataset, OV-Speech, and a novel reasoning-driven framework. The OV-Speech dataset pai

**Method-oriented passage (PDF p. 3)**

We propose OV-InstructTTS-TEP, a reasoning-driven framework that leverages the unified comprehension, reasoning, and genera- tion capabilities of LALMs for OV-InstructTTS. This framework reformulates OV-InstructTTS from a direct high-level instruction- to-speech mapping into a structured two-step process. Rather than implicitly learning the mapping, the model is explicitly guided to first “think” by generating a reasoning chain, then synthesiz- ing speech conditioned on it. This design leverages the strong in-context learning capabilities of LALMs to bridge the semantic gap between high-level user instructions and low-level acoustic realizati

**Results-oriented passage (PDF p. 4)**

As shown in Table 2, our proposed OV-InstructTTS-TEP achieves the best overall performance across both objective and subjective metrics. For the Gemini-based evaluation, our proposed model achieves the highest Gemini Score (70.42) and the best Gem- ini Rank (3.39/6), excluding GroundTruth. This demonstrates a substantial improvement over existing TTS approaches in open- vocabulary instruction following. In subjective evaluations, it out- performs all baselines in both naturalness (MOS 4.28) and instruc- tion consistency (ICMOS 3.91), with MOS even exceeding that of GroundTruth recordings. Furthermore, the model achieves the best speaker simil

**Caveat-oriented passage (PDF p. 2)**

The first challenge in developing an OV-InstructTTS system is the lack of suitable data that pairs speech with open-vocabulary instruc- tions. To address this, we constructed OV-Speech, a large-scale, multi-layered dataset built upon the ContextSpeech corpus, a 476.8- hour resource of multi-speaker audiobooks paired with their cor- responding novel

## 237. Qwen3-TTS Technical Report

ID: `2601.15621` | Theme: Speech/audio generation and control | Status: `selected_fulltext_review_plus_scoped_core_crosscheck`

Source: https://arxiv.org/pdf/2601.15621

Snapshot SHA-256: `4a857188ba3478a410faacc0045cf00b40a00ecb0499617b4e9d70e7cf4b87c8`

Abstract extract: In this report, we present the Qwen3-TTS series, a family of advanced multilingual, controllable, robust, and streaming text-to-speech models. Qwen3-TTS supports state-of-the-art 3-second voice cloning and description-based control, allowing both the creation of entirely novel voices and fine-grained manipulation over the output speech. Trained on over 5 million hours of speech data spanning 10 languages, Qwen3-TTS adopts a dual-track LM architecture for real-time synthesis, coupled with two speech tokenizers: 1) Qwen-TTS-Tokenizer-25Hz is a single-codebook codec emphasizing semantic content, which offers seamlessly integration with Qwen-Audio and enables streaming waveform reconstruction vi

**Method-oriented passage (PDF p. 3)**

Streaming Detokenizer To enable streaming audio generation, particularly for long sequences, we propose a sliding-window block attention mechanism that restricts each token to a limited context. Specifically, we use a Diffusion Transformer (DiT) trained with Flow Matching (Lipman et al.). The input code sequence is first mapped to a mel-spectrogram via Flow Matching, after which a modified BigVGAN (Lee et al.) reconstructs the waveform from the generated mel-spectrogram.

**Results-oriented passage (PDF p. 7)**

We conduct a comparative analysis of Qwen3-TTS against leading state-of-the-art zero-shot TTS systems. Table 5 reports the Word Error Rate (WER) as the primary metric for content consistency. The results highlight several key findings. 1): Qwen3-TTS delivers robust performance across languages, attributed to the diverse acoustic data seen during pretraining and continual pretraining. 2): We observe that the 12Hz variants consistently outperform the 25Hz counterparts in terms of content accuracy (WER). This suggests that the coarser temporal resolution of the Qwen-TTS-Tokenizer-12Hz allows the autoregressive model to better model long-term dep

**Caveat-oriented passage (PDF p. 10)**

We assess the instruction-following capabilities of Qwen3-TTS using the InstructTTSEval benchmark. By adopting the ChatML format, Qwen3-TTS treats voice control as a language modeling task, allowing for nuanced manipulation of speech attributes. The evaluation covers two distinct scenarios: Voice Design (Creation): In this scenario, the model gener

Additional interpretation and limitations: [core findings](CORE_FINDINGS.md).

## 238. TAC: Timestamped Audio Captioning

ID: `2602.15766` | Theme: Captioning/grounding | Status: `selected_fulltext_review_plus_scoped_core_crosscheck`

Source: https://arxiv.org/pdf/2602.15766

Snapshot SHA-256: `a25d82eb9e98c42f1680ee0483c0d075cc8adbdd59dd6091c9cef5e09293bd67`

Abstract extract: Large Audio Language Models struggle to disentangle overlapping events in complex acoustic scenes, yielding temporally inconsistent captions and frequent hallucinations. We introduce Timestamped Audio Captioner (TAC), a model that produces temporally grounded audio descriptions at varying degrees of detail and resolution. TAC is trained with a synthetic data pipeline that constructs challenging and dynamic mixtures from real-world audio sources, enabling robust learning under realistic polyphonic conditions. Across event detection and dense captioning, TAC outperforms all competing methods, with a low hallucination rate and accurate temporal grounding. We also introduce TAC-V, an audio-visua

**Method-oriented passage (PDF p. 5)**

Standard cross-entropy loss is often insufficient for dense captioning, as it treats short-duration timestamp tokens equally with semantic tokens. To strictly enforce temporal precision, we tokenize timestamps as atomic special tokens (e.g., <|1.23|>), as done in prior work Radford et al. [2023], Chu et al. [2023]. Unlike prior work, we introduce a weighted loss objective Ltotal:

**Results-oriented passage (PDF p. 7)**

We evaluate TAC on the held-out test set of the TACOS benchmark, and zero-shot performance on AudioCaps Kim et al. [2019] and Clotho-v2 Drossos et al. [2020], unlike baselines trained on these datasets (Table 3a), using METEOR, CIDEr, SPICE, and FENSE Zhou et al. [2022]. For TACOS, every baseline was evaluated both zero-shot and few-shot with in-context examples of the required output format, and we report whichever condition scored higher. This permissive selection was made on the test set for baselines, whereas TAC’s configuration was fixed on a separate development set; the comparison is therefore optimistic toward the baselines. Timestamp

**Caveat-oriented passage (PDF p. 2)**

LALMs. Recent work in audio perception and understanding has shifted from task-specific models [Gong et al., 2021, Chen et al., 2023] to general-purpose generative systems. Works like LTU [Gong et al., 2024] and SALMONN [Tang et al., 2024] demonstrated that aligning audio encoders (e.g., Whisper, AudioMAE) with LLMs enables zero-shot speech and aud

Additional interpretation and limitations: [core findings](CORE_FINDINGS.md).

## 239. Koopman Regularized Deep Speech Disentanglement for Speaker Verification

ID: `2603.05577` | Theme: Evaluation/reliability | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2603.05577

Snapshot SHA-256: `483f5f55fee7db51ee0933f797b3d34fbb56477df10fc1bc3adb19c54b6244c1`

Abstract extract: Human speech contains both linguistic content and speaker dependent characteristics making speaker verification a key technology in identity critical applications. Modern deep learning speaker verification systems aim to learn speaker representations that are invariant to semantic content and nuisance factors such as ambient noise. However, many existing approaches depend on labelled data, textual supervision or large pretrained models as feature extractors, limiting scalability and practical deployment, raising sustainability concerns. We propose Deep Koopman Speech Disentanglement Autoencoder (DKSD-AE), a structured autoencoder that combines a novel multi-step Koopman operator learning mod

**Method-oriented passage (PDF p. 2)**

speech attributes as slow system dynamics, enforcing this through architectural and operator-theoretic inductive biases. Koopman operator theory [14] offers us a means to achieve this, as it enables the modelling of system dynamics through a linear, but infinite-dimensional, operator that governs the evolution of latent variables. This formulation allows temporal behavior to be explicitly represented and shaped through spectral or structural constraints on the operator [15]. For SV, linguistic content is a nuisance variable, thus effective speaker representations should be invariant to verbal- content variations. To explicitly suppress conten

**Results-oriented passage (PDF p. 6)**

We evaluated our proposed method on the VCTK [45] and TIMIT [46] datasets. VCTK contains 110 speakers with about 400 utterances each. TIMIT includes a total of 630 speakers with 10 utterances per speaker. To facilitate one-to- one comparison with existing benchmarks for VCTK, we use 80% /10%/10% split for training, validation and testing as well as downsample audio to 16 kHz. Our splits are stratified based on speaker gender. For TIMIT we follow the official split, that is, 462 speakers for training and 24 speakers for testing, but also present results on the full test set containing 167 speakers. Both datasets are pre-processed with a custom

**Caveat-oriented passage (PDF p. 3)**

yielding a linear but infinite-dimensional representation of nonlinear dynamics in a function space [28]. Reducing non- linear dynamics to a linear space allows system analysis by spectral decomposition of the Koopman operator. However, being infinite dimensional, the Koopman operator presents practical issues for computation and analysis. To addre

## 240. StuPASE: Towards Low-Hallucination Studio-Quality Generative Speech Enhancement

ID: `2603.09234` | Theme: Evaluation/reliability | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2603.09234

Snapshot SHA-256: `bc89cf8cb5e9cf3cbd012d41b4d8c8ae45ee9be57beec0eab5b70fd5459e09d1`

Abstract extract: Achieving high perceptual quality without hallucination remains a challenge in generative speech enhancement (SE). A representative approach, PASE, is robust to hallucination but has limited perceptual quality under adverse conditions. We propose StuPASE, built upon PASE to achieve studio-level quality while retaining its low-hallucination property. First, we show that finetuning PASE with dry targets rather than targets containing simulated early reflections substantially improves dereverberation. Second, to address performance limitations under strong additive noise, we replace the GAN-based generative module in PASE with a flow-matching module, enabling studio-quality generation even unde

**Method-oriented passage (PDF p. 1)**

• We reveal the benefit of dry training targets for dereverbera- tion in PASE, as finetuning pre-trained PASE with such tar- gets substantially improves dereverberation. • We introduce StuPASE, which replaces PASE’s GAN-based generative module with a flow-matching module, enabling studio-quality speech generation under adverse conditions. • We show that StuPASE outperforms existing state-of-the-art (SOTA) SE methods, simultaneously achieving low halluci- nation and studio-level perceptual quality.

**Results-oriented passage (PDF p. 3)**

We investigate the effects of dry-target finetuning on the DNS1 with-reverb subset, with results reported in Table 1. For brevity, we only report UTMOS, SpkSim, and dWER here. To clar- ify, DeWavLM and DeWavLM-R are evaluated by synthesiz- ing waveforms from phonetic representations using a phonetic vocoder trained on clean speech for reconstruction. Comparisons between DeWavLM and DeWavLM-R, as well as between PASE and PASE-R, show that dry-target su- pervision consistently improves perceptual quality, evidenced by substantial gains in UTMOS (2.42 to 3.98 and 1.61 to 3.23). In addition, the further reduction in dWER (10.30% to 8.69% and 9.78

**Caveat-oriented passage (PDF p. 1)**

Achieving high perceptual quality without hallucination re- mains a challenge in generative speech enhancement (SE). A representative approach, PASE, is robust to hallucination but has limited perceptual quality under adverse conditions. We propose StuPASE, built upon PASE to achieve studio-level quality while retaining its low-hallucination proper

## 241. VAANI: Capturing the language landscape for an inclusive digital India

ID: `2603.28714` | Theme: Data/Indic speech | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2603.28714

Snapshot SHA-256: `915fb14e917a69b770d7ea0477981207b264071b00c2dbef9fcb7c414be6b847`

Abstract extract: Voice based technologies have the potential to bridge digital accessibility gaps; however, existing datasets fail to capture the linguistic and regional diversity of Indic languages. We present Project VAANI, a large scale multimodal dataset designed to represent India's linguistic landscape across 165 districts. Speech data is collected using image based prompts to elicit spontaneous responses, while images are curated through a separate pipeline covering diverse themes across regions. The dataset undergoes a rigorous multi stage quality control process, combining automated and manual evaluation to ensure high audio quality and transcription accuracy. We release approximately 289K images, 3

**Method-oriented passage (PDF p. 4)**

Districts were selected to maximize coverage of the languages reported in the 2011 Census of India [2] along with broad geographic representation. For the majority of districts, approximately 200 hours of audio were collected, of which 5–10% was manually transcribed. To capture intra-district linguistic variation, recordings were gathered from multiple locations within each district. The 105 languages (Table 5) span four language families: Indo-Aryan (e.g., Hindi, Bengali, Marathi, Maithili, Bhojpuri, Chakma), Dravidian (Tamil, Telugu, Kannada, Malayalam, Tulu), Tibeto-Burman (Mizo, Garo, Wancho, Idu Mishmi, Lepcha), and Austroasiatic (Santal

**Results-oriented passage (PDF p. 5)**

vendors established an extensive network of coordinators in each district to facilitate data collection. For audio collection and transcription, we collaborated with three vendors, Shaip[33], Megdap[34], and Karya[35] each tasked with providing high-quality audio data, and transcriptions of 10% of those audios, that pass the quality evaluations. We also engaged GTS[36] as the vendor to collect images from each district.

**Caveat-oriented passage (PDF p. 9)**

VAANI’s scale, linguistic breadth, and multimodal structure support a range of downstream ap- plications: ASR for low-resource Indic languages, end-to-end and cascaded speech translation, region-specific and culturally grounded benchmarking, voice conversion and speaker-adaptive TTS, and multimodal audio-visual modeling enabled by the aligned image

## 242. Audio Hallucination Attacks: Probing the Reliability of Large Audio Language Models

ID: `2603.29263` | Theme: Captioning/grounding | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2603.29263

Snapshot SHA-256: `1059ef456e166f360aa39be1d88de8ce6777fea6ff211d391556db054549e144`

Abstract extract: Large Audio Language Models (LALMs) achieve strong performance on audio-language tasks; however, their reliability in real-world settings remains underexplored. We introduce Audio Hallucination Attacks (AHA), an attack suite called AHA-Eval, comprising 6.5K QA pairs designed to test whether LALMs genuinely ground their responses in the audio input. AHA targets two attack surfaces: (i) query-based attacks, which exploit question structure to induce hallucinations about absent sounds, and (ii) audio-based attacks, which inject synthetic speech describing non-existent events into the audio stream. Evaluating state-of-the-art LALMs, including Audio Flamingo 3 and Gemini 3 Pro, we observe high at

**Method-oriented passage (PDF p. 2)**

plausible speech utterances that suggest the presence of nonex- istent sounds, thereby probing reliability under acoustically grounded false cues. We evaluate attack effectiveness using the Attack Success Rate (ASR) [20]. Using AHA, we demon- strate that even state-of-the-art audio understanding models, such as Audio Flamingo 3 [7] and Gemini 3 Pro [1], remain highly vulnerable, achieving ASRs of 95.35% and 79.65%, re- spectively. To mitigate these vulnerabilities, we investigate inference-time strategies such as Chain-of-Thought prompting (CoT) [21] and training-time alignment via Direct Preference Optimization (DPO) [22]. We further constru

**Results-oriented passage (PDF p. 3)**

Table 2: Comparing hallucination mitigation methods. We evaluate several mitigation techniques on AHA-Eval, including test-time methods such as Chain-of-Thought (CoT) and train- time approaches such as DPO.

**Caveat-oriented passage (PDF p. 3)**

about it, as illustrated in Fig. 2. These attack take more open- ended forms such as counting (e.g., “How many times does a cow moo in the recording?”) or causal questions (e.g., “Why is the police siren wailing in the background?”). A LALM should first verify that the presupposed sound is absent and reject the false premise before responding. Howe

## 243. Why Your Tokenizer Fails in Information Fusion: A Timing-Aware Pre-Quantization Fusion for Video-Enhanced Audio Tokenization

ID: `2604.12145` | Theme: Representations/codecs | Status: `excluded_after_screening`

Source: https://arxiv.org/pdf/2604.12145

Snapshot SHA-256: `cd430d69fe7ce97e540e8a0eb5d51c6694c131437a90d63c8cef0d43af02baf4`

Excluded: Video-conditioned tokenizer fusion; outside chosen audio-only scope

Abstract extract: Audio tokenization has emerged as a critical component in end-to-end audio language models, enabling efficient discrete representation learning for both audio understanding and generation tasks. However, existing audio tokenizers face fundamental limitations in understanding tasks due to single-modality constraints, particularly when audio signals contain ambiguous or incomplete information. While incorporating additional modality information can significantly enhance audio understanding, current multimodal fusion approaches invariably degrade reconstruction quality. This degradation is unacceptable for end-to-end audio systems that require high-fidelity audio generation capabilities. In thi

**Method-oriented passage (PDF p. 2)**

on adapting fusion strategies from continuous representation learning without adequately considering the unique constraints and objectives of discrete tokenization [25, 26]. The quantiza- tion process inherent in tokenization introduces optimization challenges that may not be present in continuous representation spaces, potentially requiring fundamentally different fusion approaches [31, 32]. Furthermore, the temporal nature of both audio and visual modalities suggests that conventional feature- space fusion methods may not optimally exploit the natural correspondences between these modalities [33]. To address these fundamental challenges, th

**Results-oriented passage (PDF p. 6)**

weight reveals fundamental differences: quantization-level fu- sion catastrophically degrades (0.6838→0.5004, -26.8%), while pre-quantization fusion improves (0.6797→0.6952, +2.3%). This validates Hypothesis 1—pre-quantization fusion allows gradients from reconstruction and alignment to find compromise solutions in continuous space, whereas quantization-level fusion forces competing gradients through a discrete bottleneck where they interfere. Pre-quantization fusion provides a stable optimization landscape that enables strengthening multimodal supervision without triggering collapse. Distillation Proves Superior to Contrastive Learning in Di

**Caveat-oriented passage (PDF p. 3)**

and negative sampling, its applicability to discrete tokenizer architectures remains questionable [49]. The discrete nature of tokenized representations fundamentally alters the optimization landscape, potentially rendering contrastive objectives less effective or even counterproductive for tokenizer training. Given these limitations, alternative s

## 244. SpotSound: Enhancing Large Audio-Language Models with Fine-Grained Temporal Grounding

ID: `2604.13023` | Theme: Captioning/grounding | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2604.13023

Snapshot SHA-256: `2fafa61f31c11cfa30303aa47a0b6945d8f8db3f8f05e43260ea4cf68972d6bc`

Abstract extract: Large Audio-Language Models (ALMs) have recently demonstrated remarkable capabilities in holistic audio understanding, yet they remain unreliable for temporal grounding, i.e., the task of pinpointing exactly when an event occurs within long-form audio. This limitation stems from two factors: training data dominated by clip-level supervision lacking precise timestamps, and benchmarks that fail to simulate real-world scenarios where short events are obscured by dense background sounds. In this paper, we introduce SpotSound, an audio language model designed for grounding audio events. SpotSound incorporates a novel training objective, specifically designed to suppress hallucinated timestamps fo

**Method-oriented passage (PDF p. 2)**

real-world audio is characterized by complex acoustic scenes where short, fleeting events are embedded within continuous background noise, making detection significantly more challenging. This paper presents SpotSound, a framework designed to bridge this gap by equipping large ALMs with precise temporal reasoning capabilities. Central to our approach is a temporal encoding mech- anism that interleaves timestamp tokens with audio embeddings, enabling accurate event boundary localization for open-vocabulary natural language queries. To ensure response reliability, we in- troduce a specialized training objective that explicitly targets hal- luci

**Results-oriented passage (PDF p. 5)**

Results. As shown in Table 3, our comparisons highlight key limi- tations of prior approaches and the efficacy of our method. Built upon Qwen2-Audio [6] and Audio Flamingo 3 [13], we developed SpotSound-Q and SpotSound-A. First, task-specific models generalize poorly across distributions. WTATG, for instance, achieves a mIoU of 51.4 on its training bench- mark AudioGrounding, yet collapses to 9.1 on Clotho-Moment. However, it is worth noting that these specialized models retain a degree of temporal stability on complex audio; their performance on SpotSound-Bench exceeds that of existing ALMs. Second, existing large audio-language models, e.g.

**Caveat-oriented passage (PDF p. 1)**

Large Audio-Language Models (ALMs) [6, 9, 13] have recently demonstrated remarkable proficiency in holistic tasks, such as gen- erating captions or summarizing entire audio clips. However, they exhibit deficiencies in temporal grounding: the ability to precisely localize specific events within a continuous audio stream. This limitation restricts th

## 245. MINT-Bench: A Comprehensive Multilingual Benchmark for Instruction-Following Text-to-Speech

ID: `2604.17958` | Theme: Evaluation/reliability | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2604.17958

Snapshot SHA-256: `44a55af245f4d134c93f71f105fe907d499f3fae06b16a7d39c2794c97f2eea8`

Abstract extract: Instruction-following text-to-speech (TTS) has emerged as an important capability for controllable and expressive speech generation, yet its evaluation remains underdeveloped due to limited benchmark coverage, weak diagnostic granularity, and insufficient multilingual support. We present \textbf{MINT-Bench}, a comprehensive multilingual benchmark for instruction-following TTS. MINT-Bench is built upon a hierarchical multi-axis taxonomy, a scalable multi-stage data construction pipeline, and a hierarchical hybrid evaluation protocol that jointly assesses content consistency, instruction following, and perceptual quality. Experiments across ten languages show that current systems remain far fr

**Method-oriented passage (PDF p. 2)**

• We present MINT-Bench, a comprehensive multilingual benchmark for instruction-following TTS designed to sup- port systematic, fine-grained, and scalable evaluation of controllability and generation quality. We will open-source MINT-Bench, together with its data construction and eval- uation toolkit, to facilitate future research on instruction- following TTS. • We introduce a hierarchical multi-axis taxonomy together with a scalable multi-stage data construction pipeline, en- abling semantically clear, structurally controlled, and exten- sible benchmark construction across diverse control settings and languages. • We design a hierarchical h

**Results-oriented passage (PDF p. 7)**

Table 4: Multilingual evaluation results across ten languages. The columns of Overall, Timbre, and Style are reported as Instruction-Following (IF) / Perceptual Quality (PE) scores, while the per-language columns report PE score. Within each system category (Commercial and Open-source), the best results are bolded and the second-best are underlined.

**Caveat-oriented passage (PDF p. 8)**

Table 4 summarizes multilingual evaluation results across ten lan- guages. The summary columns, namely Overall, Timbre, and Style, are reported as IF/PE score pairs. By contrast, the language-specific columns report PE scores only due to space limitations. Multilingual results are led by a small frontier group, while multilingual robustness remains

## 246. HalluAudio: A Comprehensive Benchmark for Hallucination Detection in Large Audio-Language Models

ID: `2604.19300` | Theme: Evaluation/reliability | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2604.19300

Snapshot SHA-256: `a0257c4dbb4c9769ce8386e87b52529576875b95c4d327169ab55ac88d0ff466`

Abstract extract: Large Audio-Language Models (LALMs) have recently achieved strong performance across various audio-centric tasks. However, hallucination, where models generate responses that are semantically incorrect or acoustically unsupported, remains largely underexplored in the audio domain. Existing hallucination benchmarks mainly focus on text or vision, while the few audio-oriented studies are limited in scale, modality coverage, and diagnostic depth. We therefore introduce HalluAudio, the first large-scale benchmark for evaluating hallucinations across speech, environmental sound, and music. HalluAudio comprises over 5K human-verified QA pairs and spans diverse task types, including binary judgment

**Method-oriented passage (PDF p. 2)**

Large-Audio Language Models Inspired by the success of LLMs, recent work integrates audio rep- resentations with LLMs, giving rise to LALMs that process speech, environmental sounds, and music to generate textual responses and reason- ing outputs. Early efforts such as AudioLM (Bor- sos et al., 2023) demonstrated that discretized audio tokens can be effectively modeled with language modeling techniques, enabling coher- ent continuation of speech and music. Subse- quent models, including SALMONN (Tang et al., 2024), Qwen2-Audio (Chu et al., 2024), and Audio Flamingo (Kong et al., 2024), further align audio encoders with LLMs to support tasks s

**Results-oriented passage (PDF p. 5)**

Task Composition and Statistics Table 2 presents a detailed breakdown of the HalluAu- dio dataset. The benchmark spans three domains, speech, environmental sound, and music, and cov-

**Caveat-oriented passage (PDF p. 2)**

tion on the dataset. We curate HalluAudio through a five-step pipeline including data collection, task construction, adversarial augmentation, automated filtering, and multi-round human verification, re- sulting in a large-scale benchmark spanning three audio domains, dozens of task types, and over 5K carefully validated QA pairs. We evaluate a ran

## 247. Indic-CodecFake meets SATYAM: Towards Detecting Neural Audio Codec Synthesized Speech Deepfakes in Indic Languages

ID: `2604.19949` | Theme: Representations/codecs | Status: `excluded_after_screening`

Source: https://arxiv.org/pdf/2604.19949

Snapshot SHA-256: `9ebe7950933a96a2c3772b4722861231b1be80c84201b495beeb0210014833a2`

Excluded: Codec deepfake detection; peripheral, not used as architecture evidence

Abstract extract: The rapid advancement of Audio Large Language Models (ALMs), driven by Neural Audio Codecs (NACs), has led to the emergence of highly realistic speech deepfakes, commonly referred to as CodecFakes (CFs). Consequently, CF detection has attracted increasing attention from the research community. However, existing studies predominantly focus on English or Chinese, leaving the vulnerability of Indic languages largely unexplored. To bridge this gap, we introduce Indic-CodecFake (ICF) dataset, the first large-scale benchmark comprising real and NAC-synthesized speech across multiple Indic languages, diverse speaker profiles, and multiple NAC types. We use IndicSUPERB as the real speech corpus for 

**Method-oriented passage (PDF p. 2)**

been conducted in this direction for CF detection (Xie et al., 2025; Chen et al., 2025). Despite this progress, existing CF detection datasets are pre- dominantly English-focused or atmost including Chinese. However, CF datasets for other language groups remains largely unaddressed. In this work, we extend CF detection to Indic languages, one of the world’s most linguistically diverse settings. India, now the most populous country globally encompasses speakers from ma- jor Indo-European and Dravidian families as well as Austro-Asiatic and Tibeto–Burman languages. This diversity has fueled rapid growth in Indic speech technologies, including l

**Results-oriented passage (PDF p. 6)**

detection (Phukan et al., 2024a; Wu et al., 2024b; ?). All the experiments with ICF has been car- ried out on CFs generated using test-known set of Indic-SUPERB. Only the experiments for Unseen- codec evaluation (clean and noisy test-unknown) below, we perform on CFs generated using test- unknown (Second evaluation setting as mentioned in Section 3 Generation Pipeline of ICF). Training on previous benchmark CF dataset and testing on ICF: We train AASIST on CodecFake (Wu et al., 2024b) and then evaluate it zero-shot on ICF. While AASIST performs strongly in-domain on CodecFake (94.21% ACC / 10.13% EER, Ta- ble 2), its performance drops sharply

**Caveat-oriented passage (PDF p. 9)**

One limitation of our work is that we consider a single LLM decoder family. However, prior studies have shown that the choice of LLM decoder has a relatively limited impact on performance in audio LLM pipelines (Li et al., 2025), a trend that is also reflected in our experimental results. In addition, our framework employs two audio encoders; while

## 248. Enhancing Speaker Verification with Whispered Speech via Post-Processing

ID: `2604.20229` | Theme: Evaluation/reliability | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2604.20229

Snapshot SHA-256: `599da5cfde5297151f54fe7ae2200b8d874a4f7f606fc157c20c2c60adac11fd`

Abstract extract: Speaker verification is a task of confirming an individual's identity through the analysis of their voice. Whispered speech differs from phonated speech in acoustic characteristics, which degrades the performance of speaker verification systems in real-life scenarios, including avoiding fully phonated speech to protect privacy, disrupt others, or when the lack of full vocalization is dictated by a disease. In this paper we propose a model with a training recipe to obtain more robust representations against whispered speech hindrances. The proposed system employs an encoder--decoder structure built atop a fine-tuned speaker verification backbone, optimized jointly using cosine similarity--bas

**Method-oriented passage (PDF p. 4)**

The most recent studies explored the x-vector/PLDA/SPLICE system [8], which scored 17.8% EER in neutral-whispered conditions on CHAINS, resulting in a 0.5% relative improvement compared to the baseline. Semi-supervised learning models were also explored in the context of SV with whispered speech. A system based on wav2vec 2.0 with augmentation based on whisper synthesis using Praat software and domain score normalization with whisper detection achieved 2.29% EER on CHAINS in whisper vs whisper trials and 46.31% relative improvement on the MSP-AVW in normal vs whisper conditions [6]. In this article, we propose a new model with a training fram

**Results-oriented passage (PDF p. 2)**

Abstract. Speaker verification is a task of confirming an individual’s identity through the analysis of their voice. Whispered speech differs from phonated speech in acoustic characteristics, which degrades the performance of speaker verification systems in real-life scenarios, includ- ing avoiding fully phonated speech to protect privacy, disrupt others, or the lack of full vocalization may be dictated by a disease. In this paper we propose a model with a training recipe to obtain more robust repre- sentations against whispered speech hindrances. The proposed system employs an encoder–decoder structure built atop a fine-tuned speaker verific

**Caveat-oriented passage (PDF p. 13)**

verification systems under whispered speech conditions. We discovered that even contemporary solutions must adapt to maintain their advanced performance, particularly with whispered speech. For instance, ReDimNet-B6’s effectiveness in verifying normal vs normal speech compared to normal vs whispered speech decreased by relatively 55.42%. We also an

## 249. Exploring Audio Hallucination in Egocentric Video Understanding

ID: `2604.23860` | Theme: Captioning/grounding | Status: `excluded_after_screening`

Source: https://arxiv.org/pdf/2604.23860

Snapshot SHA-256: `d88126cd3287fc82f51275b31dcc8f89599a0c91235ff741c23ce32fdb72a0eb`

Excluded: Egocentric audio-visual hallucination; peripheral to the selected task

Abstract extract: Egocentric videos provide a distinctive setting in which sound serves as crucial cues to understand user activities and surroundings, particularly when visual information is unstable or occluded due to continuous camera movement. State-of-the-art large audio-visual language models (AV-LLMs) can generate multimodal descriptions. However, we show in this work that they are prone to audio hallucinations, often inferring sounds from visual cues that are visible but not heard. We present a systematic and automatic evaluation framework for analyzing audio hallucinations in egocentric video through a targeted question-answering (Q/A) protocol. We curate a dataset of 300 egocentric videos and design

**Method-oriented passage (PDF p. 2)**

To systematically probe the influence of visual context on audio perception in egocentric videos, we introduce a curated dataset derived from 300 clips of the Ego4D corpus [5], en- compassing 50 distinct visual scenarios. As shown in Fig 2, our data curation pipeline, starts with the segmentation of the source audio into non-overlapping 10-second clips. For each segment, we generate preliminary audio annotations using the Qwen2.5 Omni model [9] to produce descriptive captions of sound events. These machine-generated captions, along with time-aligned human narrations detailing object interactions, are then processed by the LLaMA3-70B [10]

**Results-oriented passage (PDF p. 3)**

Table 1 presents the performance of four AV-LLMs on factual (Fact.) and hallucinatory (Hal.) question answering (Q/A) across both foreground and background sounds in egocen- tric videos. While most AV-LLMs perform close to random guessing, SOTA models such as Qwen2.5 Omni reach 56.2% on foreground factual and 63.4% on background factual Q/A, but only 27.3% and 39.5% on the corresponding hallucina- tory tasks, highlighting substantial room for improvement. We observe that VideoLLaMA2 and MiniCPM perform com- parably, both surpassing ImageBind-LLM, with the largest gains on background sounds (e.g., 52.6% for VideoLLaMA2 compared to 44.5% for Im

**Caveat-oriented passage (PDF p. 2)**

Audio-Visual Language Models (AV-LLMs). Recent ad- vances in AV-LLMs and multimodal large language mod- els (MLLMs) have enabled rich multimodal understanding, including video captioning, sound description, and action recognition [1, 2]. These models integrate visual and audi- tory modalities to generate coherent descriptions; however, they often s

## 250. PSP: An Interpretable Per-Dimension Accent Benchmark for Indic Text-to-Speech

ID: `2604.25476` | Theme: Evaluation/reliability | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2604.25476

Snapshot SHA-256: `1def34c511d6d22eadca30feca2fcb565062834fbb5ce055ee5c1f355cb2e538`

Abstract extract: Standard text-to-speech (TTS) evaluation measures intelligibility (WER, CER) and overall naturalness (MOS, UTMOS) but does not quantify accent. A synthesiser may score well on all four yet sound non-native on features that are phonemic in the target language. For Indic languages, these features include retroflex articulation, aspiration, vowel length, and the Tamil retroflex approximant (letter zha). We present PSP, the Phoneme Substitution Profile, an interpretable, per-phonological-dimension accent benchmark for Indic TTS. PSP decomposes accent into six complementary dimensions: retroflex collapse rate (RR), aspiration fidelity (AF), vowel-length fidelity (LF), Tamil-zha fidelity (ZF), Fre

**Method-oriented passage (PDF p. 5)**

(“audio_prompt_path”) conditions the acoustic decoder on a target speaker’s timbre and prosody. We reuse the commercial systems’ own pilot-set outputs as voice prompts — a 9 s Sarvam Bulbul female Telugu clip, an 8 s Cartesia Sonic-3 male Telugu clip — and regenerate the Praxy R6 smoke set with two sampling overrides (exaggeration 0.7, temperature 0.6, min_p 0.1; defaults are 0.5, 0.8, 0.05). These choices were selected by a com- pact three-configuration sweep on the Cartesia reference: a “preserve endings” setting (repetition_penalty 1.2, min_p 0.03) diverged (LLM-WER 0.159, intent 0.60); a “stress + stability” setting (the reported one) won

**Results-oriented passage (PDF p. 1)**

Abstract—Standard text-to-speech (TTS) evaluation measures intelligibility (WER, CER) and overall natu- ralness (MOS, UTMOS) but does not quantify accent. A synthesiser may score well on all four yet sound non-native on features that are phonemic in the target language. For Indic languages, these features include retroflex articulation, aspiration, vowel length, and the Tamil retroflex approximant /r̲/ (Tamil letter ￿). We present PSP, the Phoneme Substitution Profile, an in- terpretable, per-phonological-dimension accent bench- mark for Indic TTS. PSP decomposes accent into six complementary dimensions (retroflex collapse rate RR, aspiration

**Caveat-oriented passage (PDF p. 7)**

Intended workflow. PSP is designed as a per- dimension diagnostic, not a leaderboard summary: a sys- tem developer reads which cells move under an interven- tion and routes the next intervention accordingly. The companion paper [3] reports a worked example in which an R5→R6 data scale-up closed FAD on Telugu by 34% but opened PSD by ∼4×, localising

## 251. AgentSteerTTS: A Multi-Agent Closed-Loop Framework for Composite-Instruction Text-to-Speech

ID: `2605.17583` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2605.17583

Snapshot SHA-256: `ab8625ff0e689fa7f456e10477470b8a81d86742c637508b0846e997a2cb1cf5`

Abstract extract: While existing text-to-speech (TTS) models exhibit high expressiveness, fine-grained control over composite instructions remains challenging due to the structural mismatch between discrete textual intents and continuous acoustic realizations. Inspired by human cognitive decoupling, we introduce AgentSteerTTS, a multi-agent closed-loop framework designed for intent-faithful expressive control of composite instructions. First, in our framework, an adversarial disentanglement agent mitigates speaker-emotion leakage by learning separable identity and emotion-prosody subspaces with leakage-suppressing regularization. Next, a Dual-Stream Anchoring Controller grounds abstract intents using a large-

**Method-oriented passage (PDF p. 2)**

Our Solution. Motivated by this insight, we propose AGENTSTEERTTS, a multi-agent closed-loop framework for composite-instruction expressive steering. First, we in- troduce an Adversarial Disentanglement Module (ADM) that uses adversarial learning (Kim et al., 2021) to reduce speaker–emotion leakage and encourage latent factoriza- tion of expressive attributes. Second, we integrate a Dual- Stream Anchoring Controller (DAC), where a retrieval mod- ule fetches high-expressivity acoustic prototypes from a large reference library with perceptual pruning, and a syn- thesis controller maps discrete textual intents into contin- uous control vectors v

**Results-oriented passage (PDF p. 6)**

Composite Instruction Comparison. Table 2 re- ports results on our composite-instruction benchmark. AGENTSTEERTTS improves composite alignment, reach- ing E-SIM=0.955 (Gemini3 backend) vs. IndexTTS2 (0.864) and CosyVoice2 (0.748), and achieves the highest speaker similarity (S-SIM=0.841). It also attains the lowest WER (1.34) with stable subjective quality under strict emo- tion constraints (SMOS=4.28, PMOS=4.40, QMOS=4.38).

**Caveat-oriented passage (PDF p. 3)**

However, many controllable TTS systems learn a single- point mapping from instruction to acoustics, fθ(t; s, ℓ) 7→ˆa. This creates a key limitation: composite instructions ad- mit many valid realizations (e.g., different combinations of speaking rate, pauses, and energy), so the conditional tar- get distribution p(a | t) is typically multi-modal (L

## 252. Ultra-Low-Bitrate Mel-Spectrogram-based Neural Speech Coding with Flow-Matching-based Refinement and Vocoding-driven Reconstruction

ID: `2605.25669` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2605.25669

Snapshot SHA-256: `b651a9a99cf262cac882454be5d7f6a1d16622109108c1e077fcc67e4da42b95`

Abstract extract: Ultra-low-bitrate speech coding is pivotal for bandwidth-constrained communication and deep compression, yet maintaining naturalness and speaker identity at such extreme bit budgets remains challenging due to pronounced information loss and quantization instability. To this end, we propose FMelCodec, an ultra-low-bitrate neural speech codec in the mel-spectrogram domain, cast as a three-stage coding-refinement-reconstruction (CRR) framework that can operate at as low as 250 bps. In the CRR framework, the front-end mel-spectrogram coding stage employs a highly aggressive 640x compression/decompression encoder-decoder structure with a single 1024-entry VQ codebook, coupled with an online clust

**Method-oriented passage (PDF p. 2)**

their corresponding inverse transforms, with RVQ adopted for quantization. In contrast, Spectral Codec [17] compresses mel- spectrograms into discrete tokens using multiple finite scalar quantization (FSQ) and reconstructs speech with a neural vocoder-style decoder. A key advantage of spectral-domain codecs is that the features are already temporally subsampled by the analysis hop, so the encoder-decoder needs only mild additional downsampling/upsampling, reducing computation and improving deployment efficiency, especially on CPU- only devices. Both the aforementioned waveform-domain and spectral-domain codecs typically rely on multiple VQ or

**Results-oriented passage (PDF p. 10)**

• Subjective Metrics. When comparing FMelCodec with other baselines at equal bitrates, due to the involvement of multiple codecs, we conducted naturalness MOS (NMOS) and speaker-similarity MOS (SMOS) tests on Amazon Mechanical Turk (AMT)9. For each MOS evaluation, we constructed a set of 20 utterances and collected ratings from at least 30 listeners. In the NMOS test, participants rated naturalness on a 5-point scale with 1-point increments. In the SMOS test, participants rated how similar the reconstructed speaker sounds compared to a natural reference, using the same 5-point scale. We also computed the 95% confidence intervals of the MOS sc

**Caveat-oriented passage (PDF p. 6)**

In the preceding stage, despite the incorporation of re- construction losses, the quantization mechanism remains rel- atively simplistic, inevitably resulting in a decoded coarse mel-spectrogram f M. To address this limitation, the CFM- based mel-spectrogram refinement stage, denoted as ϕref, is introduced to further refine f M, thereby enhancing t

## 253. CFMDCTCodec: A Low-Bitrate Neural Speech Codec with Noise-Prior-aware Conditional Flow Matching for MDCT-Spectral Enhancement

ID: `2605.26812` | Theme: Representations/codecs | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2605.26812

Snapshot SHA-256: `d361874f80a8df74bb9c927549c371319cf5b08950cbcc617381bffa53fec626`

Abstract extract: High-quality speech coding at low bitrates is crucial for bandwidth-constrained applications, yet remains challenging due to the severe loss of quality-critical information in highly compressed representations. To overcome this challenge, we propose CFMDCTCodec, a low-bitrate neural speech codec that operates entirely in the modified discrete cosine transform (MDCT) domain. CFMDCTCodec integrates a lightweight encoder-quantizer-decoder-style MDCT-spectral codec with a noise-prior-aware, conditional-flow-matching (CFM)-based MDCT-spectral enhancer. Within this framework, the codec serves as a base module that compactly discretizes the MDCT spectrum extracted from speech and produces an initia

**Method-oriented passage (PDF p. 2)**

ploit spectral structure, enabling lighter encoder–decoder back- bones and more stable training. For example, in our prior work, we proposed MDCTCodec [15], which operates directly on real-valued modified discrete cosine transform (MDCT) coef- ficients and adopts a compact, fully convolutional architecture. By working in the MDCT domain, MDCTCodec significantly reduces model size and computational complexity compared with waveform-based codecs. However, MDCTCodec likewise relies on a residual quantization strategy and therefore suffers from the same discrete-capacity bottleneck at low bitrates. A straightforward approach to achieving high-qua

**Results-oriented passage (PDF p. 2)**

back into the decoded speech waveform via inverse MDCT (IMDCT). CFMDCTCodec is trained end-to-end via joint optimization of the MDCT-spectral codec and enhancer under combined reconstruction and CFM objectives. Both objective and subjective evaluations confirm that the proposed CFMD- CTCodec achieves significantly better decoded speech quality than baseline codecs at low bitrates (e.g., 0.65 kbps), while requiring lower model complexity and computational cost. Speech samples are available on our demo page1. The contributions of CFMDCTCodec are threefold. First, it introduces a new solution for low-bitrate speech coding in the MDCT spectral do

**Caveat-oriented passage (PDF p. 12)**

efficiency/complexity remained acceptable. Compared to the waveform-based DAC, our CFMDCTCodec demanded only about 20% of DAC’s computational complexity, underscoring the advantages of MDCT-domain coding over direct waveform coding. Our CFMDCTCodec used only 13% of the model parameters and less than a quarter of the FLOPs of BigCodec while achievin

## 254. SVHalluc: Benchmarking Speech-Vision Hallucination in Audio-Visual Large Language Models

ID: `2606.02642` | Theme: Evaluation/reliability | Status: `excluded_after_screening`

Source: https://arxiv.org/pdf/2606.02642

Snapshot SHA-256: `40ed5c301c5e4623b5b750889bde6445f048ab9ec522cab5446ee5b67844a66d`

Excluded: Speech-vision hallucination; outside audio-only scope

Abstract extract: Despite the success of audio-visual large-language models (LLMs), they can produce plausible but ungrounded outputs, termed hallucination. Existing benchmarks focus on environmental sounds (e.g., dog barking) to indicate event occurrence. In contrast, human speech carries fundamentally different, rich semantics and temporal structures, yet it remains unexplored whether current models can accurately align speech content with corresponding visual signals. In this work, we show that speech content can induce hallucinations in audio-visual LLMs. To systematically study this, we introduce SVHalluc, the first comprehensive benchmark for evaluating speech-vision hallucination in audio-visual LLMs. 

**Method-oriented passage (PDF p. 4)**

To systematically study speech-vision hallucinations in audio-visual LLMs, we propose an automated dataset con- struction pipeline with human verification. Specifically, our pipeline transforms well-aligned speech-video pairs (A, V ) into controlled variations that correspond to semantic or temporal conditions. For clarity, for two-choice questions, we term samples with ground-truth labels “yes” as positive samples, while those labeled “no” as negative samples. Video collection and preprocessing. We collect syn- chronized speech-video pairs from the widely-applied YouCook2 dataset [42], where the narrations well align with visual actions. We 

**Results-oriented passage (PDF p. 6)**

Semantic hallucination. Semantic hallucination tasks evaluate whether the model can identify what speech con- tent is supported by visual evidence. As shown in Table 2, all open-source models show severe failure modes in our benchmark. For the global semantic alignment (GSA) task, most models achieve an accuracy of around 50%, close to random guess results. This indicates that models tend to believe that the speech describes visual scenes, without re- ally reasoning about their alignment. Therefore, even in the cases that speech and video describe two distinctly different scenes, e.g., boiling noodles and frying meat patties, mod- els still c

**Caveat-oriented passage (PDF p. 2)**

veys rich information, such as instructions or even irrele- vant commentary. This introduces a complex semantic re- lationship between speech content and visual scene, yet is overlooked by existing benchmarks. Third, speech can de- scribe events that happen in the past, present or future, while previous benchmarks only use environmental sounds to i

## 255. Multilingual Long-Form Speech Instruction Following: KIT's Submission to IWSLT 2026

ID: `2606.04730` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2606.04730

Snapshot SHA-256: `2802c2e89f854198c0215ec081bc5a537196f9f30b2936b3c222451e6171c40b`

Abstract extract: With the advent of Large Language Models, single-task and token-based multi-task models have evolved into instruction-based systems that infer task and target language implicitly from natural language prompts. This trend is reflected in IWSLT's Instruction Following Track, which this year introduced new tasks including an unknown surprise task, posing a genuine challenge against overfitting to known tasks. We present KIT's submission to the Long and Short Instruction Following tracks in the unconstrained setting. Our approach combines a general data augmentation pipeline that converts short-form corpora into long-form training data through segment concatenation, LLM-based label generation, a

**Method-oriented passage (PDF p. 1)**

With the advent of Large Language Models, single-task and token-based multi-task mod- els have evolved into instruction-based systems that infer task and target language implicitly from natural language prompts. This trend is re- flected in IWSLT’s Instruction Following Track, which this year introduced new tasks including an unknown surprise task, posing a genuine challenge against overfitting to known tasks. We present KIT’s submission to the Long and Short Instruction Following tracks in the un- constrained setting. Our approach combines a general data augmentation pipeline that con- verts short-form corpora into long-form train- ing data 

**Results-oriented passage (PDF p. 6)**

Baselines. The cascaded baseline demonstrates the advantage of using an ASR model specifically optimized for long-form audio, achieving 5.88% WER and 80.81% COMET score on translation. In contrast, the end-to-end baseline outperforms the cascaded approach on SQA and SSUM, but its inferior ASR and ST performance (53.40% WER, 68.65% COMET) reveals that it was not specifi- cally designed for long-form audio.

**Caveat-oriented passage (PDF p. 2)**

This year’s IWSLT instruction-following task cov- ered six tasks: Automatic Speech Recognition (ASR), Speech Translation (ST), Spoken Ques- tion Answering (SQA), Speech Summarization (SSUM), Audio Chaptering (ACHAP), and a sur- prise task. All tasks except ASR support the lan- guage pairs en–en, de, it, zh; however, not all task–language combinatio

## 256. Enhancing Audio Captioning with Auxiliary AudioSet Semantics

ID: `2606.05717` | Theme: Captioning/grounding | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2606.05717

Snapshot SHA-256: `846b3fd1b9c4c2c4d6902203602b6f0f673e6c98a53b1ed9c5521beba1e6de99`

Abstract extract: Automatic Audio Captioning (AAC) seeks to generate natural language descriptions of complex acoustic scenes, bridging auditory perception and language understanding. However, word-selection indeterminacy and increasing reliance on large-scale sequence-to-sequence or LLM-based models limit practical deployment. We propose a resource-efficient AAC framework that explicitly grounds caption generation in auxiliary AudioSet semantics. Frame-level acoustic representations extracted using a ConvNeXt encoder are augmented with top-$K$ predicted AudioSet keywords, providing structured contextual cues for decoding. A compact six-layer BART-style decoder conditions on this joint acoustic-semantic repre

**Method-oriented passage (PDF p. 1)**

Automatic Audio Captioning (AAC) seeks to generate natural language descriptions of complex acoustic scenes, bridging au- ditory perception and language understanding. However, word- selection indeterminacy and increasing reliance on large-scale sequence-to-sequence or LLM-based models limit practical de- ployment. We propose a resource-efficient AAC framework that explicitly grounds caption generation in auxiliary AudioSet se- mantics. Frame-level acoustic representations extracted using a ConvNeXt encoder are augmented with top-K predicted Au- dioSet keywords, providing structured contextual cues for de- coding. A compact six-layer BART-sty

**Results-oriented passage (PDF p. 3)**

Table 1: Evaluation on Clotho. Methods are grouped based on training source. (i) Clotho, (ii) AudioCaps and (iii) Large pretrained or prompt-based methods. † Results are directly quoted from the original papers, or we trained the models using the publicly available codes otherwise. Best results are shown in bold, and the second-best results are underlined within settings (i) and (ii) only.

**Caveat-oriented passage (PDF p. 2)**

More recent approaches have shifted toward leveraging large language models (LLMs) and large audio-language mod- els (LALMs). Kim et al. [6] introduced GPT-based decod- ing via prefix tuning, enabling adaptation to AAC with re- duced fine-tuning cost but still relying on large-scale pretrained language models. Pengi [7] extended this paradigm by tr

## 257. An Analysis of the Effectiveness of Synthetic Speech Data for ASR Fine-tuning in Selected Indic Languages

ID: `2606.17662` | Theme: Loop/data selection | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2606.17662

Snapshot SHA-256: `05aa4f7a302cfc9b7d9732941363499f1a19b21f7e73759ecd71f83a71894705`

Abstract extract: Synthetic data has the potential to be a valuable resource for training machine learning models, particularly Automatic Speech Recognition (ASR) Systems; however, its effectiveness requires systematic evaluation. In this study, we investigate the impact of incorporating synthetic speech data alongside real-world recordings for three Indic languages: Hindi, Kannada, and Telugu. We analyze the performance gains achieved by augmenting synthetic data with real data and independently examine how ASR performance varies with the sources of scripts used to generate synthetic speech. In addition, we evaluate the effect of synthetic speech generated using different speech synthesis models. Finally, we

**Method-oriented passage (PDF p. 3)**

performance across diverse recording conditions, collection methodologies, and speaker demographics. This multi-dataset evaluation strategy allows for a robust analysis of model gener- alization in realistic deployment scenarios. The Hindi models were evaluated on GramVaani[23], FLEURS[24], MUCS[25], Common Voice[26], Kathbath (including its noisy variant), Vaani, and RESPIN. The Telugu models were evaluated on FLEURS, Kathbath (including its noisy variant), Vaani, and RESPIN. The Kannada models were evaluated on FLEURS, Kathbath (including its noisy variant), and Vaani. To analyze the impact of the number of speakers used dur- ing the voice 

**Results-oriented passage (PDF p. 3)**

As shown in Table 1, the fine-tuned models consistently show performance improvements when augmented with synthetically generated data. For models trained on Vaani data, adding syn- thetic speech generated using RESPIN transcriptions reduces the average Word Error Rate (WER) by 15.06% for Hindi, 9.27% for Kannada, and 13.19% for Telugu. Although the gains achieved through synthetic data augmentation are slightly lower than those obtained by incorporating additional real speech data, they remain substantial across all languages. Notably, training with synthetic data alone also leads to measurable im- provements, reducing WER by 62.68% for Hind

**Caveat-oriented passage (PDF p. 3)**

From the performance of models trained with varying num- bers of speakers in the voice cloning process, as shown in table 2 we observe a decrease in WER when increasing the number of speakers from 1 to 10. Beyond this point, no further reduc- tion in WER is observed. This behavior suggests that limited speaker diversity is sufficient to capture the

## 258. FineCombo-TTS: Collaborative and Precise Controllable Speech Synthesis Using Text Descriptions and Reference Speech

ID: `2606.19209` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2606.19209

Snapshot SHA-256: `83b149fe54b305e97b599f502ad766d2ceee6be885f00bf33869db07585034cd`

Abstract extract: Controllable text-to-speech (TTS) has become a key research focus. However, methods based on either reference speech or text descriptions lack flexibility and precise control, and recent joint approaches remain loosely coupled, with speech modeling timbre and text controlling global style. We propose FineCombo-TTS, a unified framework for speech synthesis grounded in reference speech and guided by text descriptions, enabling flexible and precise control over acoustic attributes. Instead of explicit attribute disentanglement, we learn a unified acoustic representation and introduce a Conditional Flow Matching (CFM)-based Speech Variance Predictor to model fine-grained reference-to-target tran

**Method-oriented passage (PDF p. 2)**

• We propose FineCombo-TTS, the first controllable TTS ar- chitecture that jointly leverages reference speech and text de- scriptions to enable flexible and precise control. • We introduce a CFM-based Speech Variance Predictor that operates in a unified acoustic attribute latent space, model- ing fine-grained reference-to-target attribute transformations conditioned on text descriptions. • We construct FineEdit, the first large-scale paired dataset of 〈source speech, control description, target speech〉triplets for relative attribute control. Experiments validate the effective- ness of both the dataset and the proposed framework.

**Results-oriented passage (PDF p. 4)**

We evaluate controllability on prosody, emotion, and timbre us- ing both reference speech and textual descriptions. Test data are sampled from FineEdit and unseen during training. Eval- uation combines subjective metrics—MOS-S (speaker simi- larity), MOS-I (instruction following), and MOS-P (prosodic consistency)—with objective metrics: WER4 for intelligibility, SECS5 for speaker encoder cosine similarity, FPC for pitch cor- relation, and Emotion-A/S6 for emotion accuracy and embed- ding similarity. For joint-control analysis, we also report Con- trolled Accuracy, which measures whether the synthesized at- tribute change matches the instructi

**Caveat-oriented passage (PDF p. 3)**

Existing speech–description datasets provide only isolated speech–text pairs describing absolute acoustic properties, which are insufficient for learning reference-conditioned attribute transformations. To address this limitation, we construct Fi- neEdit, a structured paired English speech dataset designed to model relative attribute variations. Ea

## 259. How Do Instructions Shape Speech? Cross-Attention Attribution for Style-Captioned Text-to-Speech

ID: `2606.20532` | Theme: Captioning/grounding | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2606.20532

Snapshot SHA-256: `cc5efd6829693390821c1de3bf669c53a150772c4903311445dfe09f7741a84e`

Abstract extract: Style-captioned text-to-speech systems use natural language to control voice characteristics, but how individual words influence acoustic output remains unclear. Understanding this is critical for diagnosing failure modes and improving controllability in expressive TTS. We propose cross-attention attribution for speech diffusion models, adapting the DAAM framework to the speech domain for the first time, and apply it to CapSpeech-TTS. Our method extracts per-token heatmaps across 25 layers and 24 ODE steps. We analyze 3,600 (style caption, text transcript) combinations comprising 120 style captions conditioning the generation of 30 text transcripts each, revealing how caption tokens shape wa

**Method-oriented passage (PDF p. 2)**

Figure 1 illustrates the CapSpeech pipeline and our DAAM at- tribution mechanism. The model comprises four components working in sequence to transform a style caption and text tran- script into a waveform. The pipeline begins with a T5 caption encoder [11], which maps the style caption c = (c1, . . . , cTc) to contextual embeddings Ec ∈RTc×d; T5’s pre-trained en- coder provides rich semantic representations that capture lin- guistic nuances in style descriptions. These text embeddings are complemented by a CLAP encoder [25], which produces a global style tag embedding eclap ∈Rd′ from a short style la- bel, providing acoustic grounding alongsi

**Results-oriented passage (PDF p. 3)**

We compute temporal variance, PMR, and entropy for each to- ken’s aggregated heatmap and group by category. To quantify effect magnitude beyond p-values, we report Cohen’s d [30] (standardized mean difference) alongside Mann–Whitney U p- values [31]: the former provides interpretable effect sizes, while the latter avoids parametric assumptions about the underlying distributions. Results are shown in Figure 2 and Table 1. Style tokens exhibit the lowest temporal variance (¯σ2 = 2.1 × 10−5), sig- nificantly lower than content tokens (7.0 × 10−5; p < 10−43, d = −1.16) and function tokens (19.2 × 10−5; p < 10−44, d = −0.72). The 9.2× variance rat

**Caveat-oriented passage (PDF p. 4)**

Our three experiments converge on a unified picture: style- captioned TTS implements cross-attention as a hierarchical global conditioning channel. Style tokens distribute attention uniformly across time (9.2× lower variance than function to- kens, d = −1.16), correlate with acoustic features in seman- tically coherent patterns (“loud” ↔energy, r =

## 260. Vaani Benchmark V1.0: An Inclusive Multimodal Benchmark Dataset for Hindi

ID: `2606.21408` | Theme: Evaluation/reliability | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2606.21408

Snapshot SHA-256: `c5a9a99de94755f9dd27b4937e6dcfe1d4bb391d5d7715b5e781b477092a9d5d`

Abstract extract: Benchmarking is critical for the systematic evaluation of machine learning systems. While several open-source datasets are available for Hindi, existing benchmarks remain limited in terms of modality, geographic diversity, demographic representation, and transcription robustness. We introduce an inclusive, multimodal Hindi benchmark dataset collected from 102 districts across India. The dataset consists of spontaneous speech elicited using image prompts and recorded under real-world acoustic conditions across diverse demographic groups. Each audio segment is associated with the image prompt that elicited it and is annotated with three independent transcriptions, enabling multi-reference eval

**Method-oriented passage (PDF p. 4)**

To probe whether recording acoustics contribute to the low speech-retrieval performance, we re-synthesise the test utterances as clean Hindi and English speech using Kokoro TTS [34], and evaluate them with jina-embeddings-v5-omni-nano [33]. English queries are machine translations of the same human transcriptions, produced with gpt-5.6-luna [35]. Speech-to-image performance remains similar across the three conditions: 1.49% R@1 for the original recordings, 1.70% for synthetic Hindi speech, and 1.64% for synthetic English speech, with no pair significantly different un- der a paired exact McNemar test on top-1 outcomes (p = 0.28 real vs. synth

**Results-oriented passage (PDF p. 3)**

only if it is inserted in all three; a reference word is a deletion only if deleted in all three. The denominator is N = C + S + D, the length of the implied (materialised) reference, with errors aggregated over the corpus. An error is thus counted only when the output matches no acceptable realisation in any reference. The three transcription sets exhibit pairwise WERs of 10.40–13.34%; scoring each set against the other two under Approach 3 yields 6.63%, quantifying inter-annotator variation and providing context for ASR WERs. After evaluation, the WERs obtained using Approaches 1, 2, and 3 are presented in Table 1. The differences across th

**Caveat-oriented passage (PDF p. 1)**

tives, such as IndicSUPERB [4], LAHAJA [5] and Vistaar [6]. LA- HAJA comprises both read and extemporaneous speech across a di- verse range of topics and use cases, totaling 12.5 hours of Hindi audio collected from 132 speakers spanning 83 districts of India. In addition, multiple data collection efforts—including FLEURS [7], MUCS [8] and GramVaani

## 261. DNSMOS-C: Improving End-to-end Speech Quality Models via Contrastive Learning

ID: `2606.26903` | Theme: Evaluation/reliability | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2606.26903

Snapshot SHA-256: `767c3de7a8b337097990778f435276bc72321265ed6476e04fdeb9b96ef6003d`

Abstract extract: We introduce DNSMOS-C, a compact end-to-end speech quality assessment model that extends the DNSMOS Pro framework by integrating a MOS-guided triplet-based contrastive loss. Applied directly to the intermediate embeddings, this contrastive supervision encourages the latent space to be better organized with respect to perceptual quality while preserving the simplicity and efficiency of DNSMOS Pro. Unlike prior methods that depend on large pre-trained self-supervised learning (SSL) encoders and multi-stage training, DNSMOS-C jointly learns speech representations and MOS regression within a single, unified framework. Experiments on multiple datasets show that DNSMOS-C consistently improves corr

**Method-oriented passage (PDF p. 2)**

The overall model architecture is illustrated in Figure 1, which we name DNSMOS-C. The model consists of an encoder module fenc and a head module fhead. The encoder has four convolutional layers followed by a global max-pooling layer, which maps each audio clip to a 64-dimensional embedding vector. The head module, composed of three fully-connected layers and a linear transformation, maps the embedding to the estimated MOS mean and variance. Here, we introduce the SCOREQ loss [16], a triplet-based contrastive regression loss, into the DNSMOS Pro framework. The original SCOREQ formulation is a multi-stage process: first, an encoder and a proje

**Results-oriented passage (PDF p. 3)**

We evaluate DNSMOS-C against DNSMOS Pro across test splits of the three training datasets and multiple unseen test datasets. We report the mean ± standard deviation over 10 inde- pendent runs to assess both performance and stability. Standard performance measures - mean square error (MSE), linear cor- relation coefficient (LCC) [24], and Spearman rank correlation coefficient (SRCC) [25] are used, and results are summarized in Table 2 and Table 3, respectively. In-domain performance. Table 2 shows that DNSMOS- C consistently outperforms DNSMOS Pro across all training datasets in terms of correlation-based metrics. While MSE re- mains comparabl

**Caveat-oriented passage (PDF p. 1)**

ment. However, a significant limitation of these models is their still limited ability to generalize to unseen distortions or record- ing conditions [12]. Recent advances in contrastive learning have demonstrated strong potential for learning well-structured and semantically meaningful embeddings [13, 14, 15]. In speech quality as- sessment, SCOREQ

## 262. Attacking UTMOS: Probing the Robustness of a Speech Quality Assessment Model

ID: `2606.31105` | Theme: Evaluation/reliability | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2606.31105

Snapshot SHA-256: `07710f6595ab12f6d299cc64a8da1c17c6da9501f9fa09e4c218d1302d663ea5`

Abstract extract: UTMOS has become one of the most commonly used deep neural network-based speech quality assessment (SQA) metrics in speech processing research. In this paper, we attack UTMOS to probe its robustness. Starting from high-quality speech samples, we optimize the input in two directions: a score-preserving attack, which degrades perceived quality while maintaining the predicted score, and a quality-preserving attack, which lowers the predicted score while maintaining perceived quality. We consider three input spaces: raw waveform, mel spectrogram with a HiFi-GAN vocoder, and the latent space of EnCodec, a neural audio codec. Experimental results show that score-preserving attacks are effective ag

**Method-oriented passage (PDF p. 1)**

Speech quality assessment (SQA) refers to the evaluation of speech quality [1], [2]. In this work, we are particularly interested in non-intrusive, deep neural network (DNN)-based methods trained with ⟨speech, quality label⟩pairs, where the quality labels are collected through mean opinion score (MOS)-style listening tests [3]–[6]1. One of the most popular SQA models is UTMOS [7], the winning system of the VoiceMOS Challenge 2022 [8]. Trained on the BVCC dataset [9], which contains synthetic speech samples from 187 text- to-speech (TTS) and voice conversion (VC) systems, UTMOS was shown to have a system-level Spearman’s rank correlation coeff

**Results-oriented passage (PDF p. 4)**

One way to view the attacks is that we add perturbations to the input in a specific way to reach a certain goal. It therefore raises a fundamental question: how do the perceived and predicted quality change if we add random noise to the input? This should be viewed as the “baseline”. To this end, we add Gaussian noises with different amplitude values to the three attack spaces. Figure 3 shows the results. It could be observed that as the noise amplitude increased, both PESQ and UTMOS scores dropped, which was in fact the desired behavior as depicted in Fig. 1. On the other hand, this result justifies our proposed attacks, as we aim to find sa

**Caveat-oriented passage (PDF p. 2)**

attack. The second attack minimizes the predicted quality score while preserving perceived quality, which we refer to as a quality-preserving attack. Neither attack should succeed against an ideal and robust SQA model. In the experiments, we instantiate the proposed attacks in three optimization spaces: the waveform space, the la- tent space of a n

## 263. TokAN: Accent Normalization Using Self-Supervised Speech Tokens

ID: `2607.03928` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2607.03928

Snapshot SHA-256: `eab9a4103df2fbb3cf3f0b6393b48c94f1697db79e24d0df080cd7064d106cc4`

Abstract extract: Accent normalization (AN) seeks to convert non-native (L2) accented speech into standard (L1) speech while preserving speaker identity. The current techniques either require naturally recorded parallel L1-L2 speech for training, or suffer from quality degradation when supervised by synthesized targets. In this paper, we present TokAN, a token-based accent normalization framework that operates on self-supervised discrete speech tokens extracted from a L1-L2 jointly trained vector-quantization (VQ) tokenizer, without the need of synthetic supervisory speech. An autoregressive encoder-decoder model performs token-to-token conversion, translating L2-accented token sequences into the tokens of st

**Method-oriented passage (PDF p. 2)**

1) We replace the conference-version HuBERT/K-Means tokenizer with a jointly trained VQ tokenizer coupled to a speech synthesizer and a CTC-based ASR module, and conduct a systematic tokenizer selection study over SSL backbone, layer choice, and codebook size. 2) We redesign the autoregressive conversion model by adding RoPE, replacing cross-attention with a self- attention-only decoder that treats encoder features as a prefix, and removing the source accent embedding in favor of an accent-universal architecture. 3) We introduce an RL post-training stage based on GRPO that directly optimizes content preservation and ac- centedness reduction, 

**Results-oriented passage (PDF p. 8)**

Table IV presents the main evaluation results. Intelligibility / Content preservation. TokAN achieves substantially better intelligibility than all baselines, with TokAN-1 reaching a WER of 9.23% and TokAN-2 at 9.40%—both far below CosyAccent-1 (12.40%) and FramAN (17.55%). This advantage is consistent across all accents (Table V). VEVO exhibits the highest WER (28.94%), sub- stantially worse than even the unconverted source (15.81%). We attribute this to its extremely small content tokenizer codebook (32 entries): while a small codebook may suffice for native speech, prior work has shown that at least 1000 codes are needed for robust content

**Caveat-oriented passage (PDF p. 2)**

Early deep-learning AN methods can be categorized by their dependence on reference speech and parallel data. Reference- based approaches use native speech samples at inference, gen- erating accent-neutral representations via PPG or bottleneck features [1], [5], [7], native TTS-generated references [6], or speech tokens for style transfer [8]. Refer

## 264. Large Audio Language Models for Spoofing-Aware Speaker Verification

ID: `2607.14753` | Theme: Evaluation/reliability | Status: `excluded_after_screening`

Source: https://arxiv.org/pdf/2607.14753

Snapshot SHA-256: `539e774e2f610f5d97edb781ed609518f131a7ab8140b85f66ee1dcbf88cae95`

Excluded: Spoof-aware authentication; not the competition diversity protocol

Abstract extract: Recent advances in text-to-speech and voice cloning make high-quality spoofing inexpensive and scalable, threatening voice authentication systems, especially automatic speaker verification (ASV). Existing defenses mainly address this threat through binary countermeasures (CMs) for deepfake detection or spoofing-aware speaker verification (SASV), where current systems are dominated by modular ASV-CM fusion and cascaded pipelines. Although large audio language models (LALMs) have shown promise on related audio tasks, including CM and ASV, their use for SASV remains unexplored, despite their capacity to produce natural-language rationales for auditing and robustness beyond discriminative predic

**Method-oriented passage (PDF p. 2)**

• We propose several methods to improve LALMs’ hard- label verification capabilities by combining task-specific losses to achieve a better CM-ASV trade-off. We demon- strate that LALMs can be a plausible solution, outper- forming strong baselines.

**Results-oriented passage (PDF p. 2)**

but they do not expose grounded evidence for the joint speaker- authenticity decision. This is the gap addressed by our work. In parallel, recent studies investigate LALMs for speaker verification and SDD. In [18], authors reformulate text- independent and text-dependent speaker verification as audio question answering over enrollment-trial pairs. They show that LALMs have limited zero-shot ASV ability and are sensitive to prompting, but Low-Rank Adaptation (LoRA) [36] fine-tuning with hard-pair sampling substantially improves performance and can approach conventional ECAPA-TDNN [6] or cascaded systems. However, these studies do not address j

**Caveat-oriented passage (PDF p. 6)**

However, proposed method has several limitations. Despite their strong performance, LALM-based SASV systems require substantially higher computational resources than conventional fusion models. In addition, although the generated reasoning traces appear plausible, they have not yet been systematically validated. Therefore, we leave human evaluation

## 265. Staged Depth-Pruning Distillation of a Flow-Matching Text-to-Speech Teacher: A Compact Hindi Speech Synthesizer

ID: `2607.18662` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2607.18662

Snapshot SHA-256: `feddc3985e762e27b8e8d2d8473cf47d99d1d246cb2323014361b83ad6d026b3`

Abstract extract: We present a practical recipe for building a compact Hindi text-to-speech (TTS) model by distilling a large flow-matching teacher (IndicF5, 337M-parameter DiT) under a severe data budget (~17.6 hours). Training a small model from scratch on this much data fails outright. Instead we warm-start the student from the teacher by pruning depth only: keeping the teacher's width, text dimension, attention heads, and mel/text I/O fixed so all non-block tensors copy one-to-one, and retaining an evenly-spaced subset of transformer blocks. We first measure how much depth the teacher tolerates (it remains near-functional at -27% blocks but collapses past -50%), then descend gradually (22 -> 16 -> 12 -> 8

**Method-oriented passage (PDF p. 3)**

Each stage fine-tunes with the conditional flow-matching objective on the teacher-generated corpus: learning rate 5×10−5, 500-step warmup, dynamic batches of 24,000 mel frames, an euler ODE solver, and exponential moving-average (EMA) weights. Each warm-start checkpoint carries only EMA weights (no optimizer state), so training resumes as a fresh fine-tune. The warm start is evident in optimization: stage A loss begins near 1.0 (vs. 2–4 for random init) and reaches ∼0.49 within one epoch; intelligible speech appears by step 2,000.

**Results-oriented passage (PDF p. 5)**

Table 4: Independent benchmark: 50 unseen FLEURS hi in sentences, identical inputs for all models. WER/CER via Vakyansh Hindi ASR (see footnote); SIM via ECAPA-TDNN vs. the reference speaker; UTMOS = predicted MOS; RTF = synthesis time ÷ audio duration (median, after warmup).

**Caveat-oriented passage (PDF p. 2)**

Compact and multilingual TTS. MMS-TTS [13] scales to 1000+ languages with small per- language VITS models; Parler-TTS [10] and its Indic variant target controllability; Kokoro [4] is a popular small model with limited Hindi support. We instead distill a strong Indic teacher into a small student to inherit its quality.

## 266. From Semantics to Readout: Mechanistic Understanding of Audio Tokens after Fine-Tuning for Temporal Audio Grounding

ID: `2607.25355` | Theme: Captioning/grounding | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2607.25355

Snapshot SHA-256: `ad90fd9963fd4913194fc396d03b5f859dc7f826ac62aefdc20eef3d33f3846e`

Abstract extract: Large audio-language models (LALMs) convey acoustic evidence to language decoders through native audio tokens, yet the internal roles of these tokens remain poorly understood. Using temporal audio grounding as a diagnostic setting, we examine how language-model fine-tuning affects the layerwise semantics, decoder accessibility, and temporal output alignment of native audio-token states through four complementary analyses: query-conditioned token semantics, calibrated token readout, temporal-window probes, and residual-delta erasure during generation. Alongside substantial improvements in temporal localization, semantic analysis of Qwen2.5-Omni shows that latent evidence for queried events is

**Method-oriented passage (PDF p. 2)**

objective. TimeAudio and SpotSound use temporal markers, time encodings, timestamp sequences, or specialized tempo- ral supervision (Wang et al. 2026; Sun et al. 2026); TimePro- RL injects timestamp embeddings and optimizes temporal alignment with rewards (Shi et al. 2026); and tool use at the frame level exposes finer temporal operations for audio- language models (An et al. 2026). These works mainly study how temporal coordinates should be represented, supervised, or generated. In contrast, we use temporal grounding as a di- agnostic setting for studying how task fine-tuning changes native audio-token semantics and decoder readout.

**Results-oriented passage (PDF p. 4)**

Positive ∆readout indicates that patching the audio-token state improves semantic readout of the target event beyond the no-patch diagnostic baseline. This calibrated variant differs from direct output inspec- tion: it asks whether a specific audio-token hidden state can be expressed by the language decoder as text semantically matching the queried event. Together with the semantics di- agnostic, it separates semantics in representation space from token readout by the decoder.

**Caveat-oriented passage (PDF p. 2)**

Audio Tokens as Interfaces LALMs follow a common multimodal design in which audio inputs are encoded, pro- jected into the hidden space of the language model, and placed in the decoder context as token representations. Acoustic encoders and projection modules produce native audio-token states that condition text generation, enabling audio question 

## 267. dots.tts.edit: Precisely Controlled Speech Editing with a Continuous Autoregressive Model

ID: `2608.02673` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2608.02673

Snapshot SHA-256: `85449894fce4d114a8bb0330ff72df4d0d8138bfa78ed29bd9f23f1a71799302`

Abstract extract: Speech editing for content creation requires precise control over both what an edit should do and where it should apply. Free-form natural language provides a flexible interface for expressing edit requests, but its ambiguity may leave the intended operation, parameters, or target region underspecified. We study a semi-formal transcript-grounded edit instruction that specifies operation categories and parameters and binds them to transcript spans or boundaries. This semantic timeline avoids explicit timestamp alignment and provides an externally inspectable contract for compositional edits. We instantiate the interface in dots$.$tts$.$edit, a speech editing model built on a continuous autore

**Method-oriented passage (PDF p. 2)**

Following advances in large language models such as GPT- 3 and LLaMA (Brown et al., 2020; Touvron et al., 2023), large-scale pretraining has also broadened the capabili- ties of speech generation models. VALL-E formulates TTS synthesis as conditional language modeling over au- dio codec tokens and supports unseen speakers through short acoustic prompts (Chen et al., 2025a). CosyVoice and Spark-TTS further develop this approach through speech token design and large-scale training (Du et al., 2024b; Wang et al., 2025). A complementary route uses diﬀu- sion or ﬂow matching to model continuous speech rep- resentations directly, including non-auto

**Results-oriented passage (PDF p. 10)**

Table 6: Compositional editing results. Component and All report operation-level and case-level success rates using category-speciﬁc criteria. The pipeline baseline uses multiple passes.

**Caveat-oriented passage (PDF p. 3)**

Realizing this formulation remains diﬃcult. The output must execute every requested operation, preserve non-target con- tent and acoustics, and remain coherent even when a local edit changes duration. Training such a model requires large amounts of corresponding paired data. However, natural record- ings rarely provide paired utterances that diﬀer 

## 268. SraVaani 1.0: Scaling Inclusive Speech Recognition for Indic Languages

ID: `2608.08235` | Theme: Data/Indic speech | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2608.08235

Snapshot SHA-256: `a0ac471e981912c716012ced89c0ec27d66653956f76a69ec5ac9bb5ac91fdfb`

Abstract extract: India's linguistic landscape spans over 700 languages and thousands of dialects, yet the vast majority of automatic speech recognition (ASR) systems support only a small fraction of this diversity. We present SraVaani-1.0, a multilingual ASR model covering 65 Indian languages and dialects, many of which currently have no publicly available or competing ASR system. SraVaani-1.0 is built on a FastConformer architecture and trained from scratch through a three stage the first stage, we perform self-supervised pretraining on 31,255 hours of unlabelled speech from the VAANI corpus using a contrastive learning objective. In the second stage, we introduce an audio-image representation alignment sta

**Method-oriented passage (PDF p. 1)**

India’s linguistic landscape spans over 700 languages and thousands of dialects, yet the vast majority of automatic speech recognition (ASR) systems support only a small fraction of this diversity. We present SraVaani-1.0, a multilingual ASR model covering 65 Indian languages and dialects, many of which currently have no publicly available or competing ASR system. SraVaani-1.0 is built on a FastConformer architecture and trained from scratch through a three-stage pipeline. In the first stage, we perform self-supervised pretraining on 31,255 hours of unlabelled speech from the VAANI corpus using a contrastive learning objective. In the second 

**Results-oriented passage (PDF p. 8)**

Not all baselines support every language; results are reported only where a model has an official release for that language, and unsupported language–dataset pairs are left blank rather than scored. Table 2 summarises the language coverage of each system.

**Caveat-oriented passage (PDF p. 10)**

The current version of SraVaani has several limitations. First, it does not support Urdu and Kashmiri, as these languages were not included in the finetuning process although we have used it in the pretraining stage. Second, for code-switched speech, the model generates the entire transcription in the script of the predicted primary language rather

## 269. Evaluating Pre-trained Speech Encoders for Spontaneous Speech Detection and Out of Domain Synthetic Speech Generalisation in Indic Languages

ID: `2608.12536` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2608.12536

Snapshot SHA-256: `8a0b4d9cde72378041117c89dbb807f4628458673bb63c79769ee7366edbb71d`

Abstract extract: Transformer-based models have shown strong accuracy in distinguishing spontaneous from scripted speech and natural from synthetic speech, but these results are established on a narrow set of well-resourced language benchmarks and have not been extended across Indic languages, nor has embedding geometry been used to explain encoder behaviour or deepfake generalisation failure. We address these gaps by evaluating five frozen transformer encoders, AST, Vaani-FastConformer, Wav2vec2, Whisper and BEATs, across 22 Indic languages, and by conducting a multi-system TTS generalisation experiment across four TTS models. Beyond accuracy, we present language isolation probing and centroid proximity anal

**Method-oriented passage (PDF p. 2)**

The acoustic differences between spontaneous and read speech have been studied for decades, with prosody consistently identified as a primary dis- criminating dimension. Early work by Batliner et al. (1995) showed pitch contours, articulation rate, and pause distribution carry signal, though no single feature dominates. Rouas et al. (2003) found these prosodic differences large enough to affect downstream task performance, and Naka- mura et al. (2008) showed ASR models trained on read speech degrade substantially on sponta- neous input. Christodoulides (2020) and Ryant and Liberman (2016) each built multidimensional char- acterisations of spe

**Results-oriented passage (PDF p. 4)**

Architectural progress in audio deepfake detec- tion has been led by end-to-end models such as RawNet2 (Tak et al., 2021) and AASIST (Jung et al., 2022), which set strong baselines on the ASVspoof (Wang et al., 2019; Yamagishi et al., 2021, 2023) benchmarks. However, their gen- eralisation to unseen languages is severely lim- ited: Sharma et al. (2025) benchmarked both models on IndicSynth without domain adapta- tion and observed EERs exceeding 50% across most Indic languages, compared to sub-1% EER on ASVspoof 2019, exposing a critical cross- lingual generalisation gap. Li et al. (2024) demon- strated through systematic analysis across multi

**Caveat-oriented passage (PDF p. 3)**

The analysis asks a complementary question about the internal structure of those embeddings: to what extent do they retain explicit language identity in- formation, and does that language-discriminability trade off against the model’s ability to classify spon- taneous speech? For each encoder’s feature store, all embedding matrices and their langua

## 270. Poly-InstructTTS: Learning In-the-Wild Expressive Speech Synthesis from Open-Ended Instructions

ID: `2608.20387` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2608.20387

Snapshot SHA-256: `93149798d0cf6706a41d4652ca028e85d873241a7fd32a56e1817c282e6a9494`

Abstract extract: While recent text-to-speech (TTS) models achieve high naturalness, controlling fine-grained expression via natural-language instructions remains challenging. We introduce Poly- InstructTTS, which learns expressive speech from open-ended instructions using in-the-wild audiovisual data. We build a scalable multi-modal pipeline to construct a 1,000-hour instruction-annotated corpus covering 1,000+ fine-grained emotions and styles. The framework uses a prompt-free GPT with attribute-based thinking tokens, followed by a flow-matching module that injects timbre from a reference audio. We also present a speaker fine-tuning procedure to transfer instruction control to specific speakers while preserv

**Method-oriented passage (PDF p. 3)**

While the base Poly-InstructTTS model is capable of generat- ing zero-shot style with arbitrary timbres, real-world applica- tions often require endowing a specific speaker with instruction- following capabilities while maintaining their intrinsic per- sona. For this scenario, we propose an Instruction-Conditioned Speaker Fine-Tuning (SFT) scheme to transfer the expressive variance from our cinematic dataset to target speakers. The training format of the GPT remains identical to the base stage, but we prepend a Speaker ID tag to the content text. For the cinematic data, the tag is set to <Unknown>, whereas SFT data utilizes specific IDs such 

**Results-oriented passage (PDF p. 4)**

To validate the core architectural designs, we conduct ablations in Table2. First, removing the attribute-based thinking tokens lowers subjective scores, indicating they provide a useful prior that helps align instructions with acoustic tokens. These tokens complement the free-form instruction text, leaving the GPT to achieve better expressiveness compared to direct generation. We also evaluate optional pretrained instruction encoders, in- cluding FlanT5 [33], instructor [34] and GTR-base [35], by conditioning the GPT on their frozen hidden representations of the instruction text (dashed lines in Figure1b). Across set- tings, these variants d

**Caveat-oriented passage (PDF p. 4)**

indicate that our system can handle diverse styles and scenarios and produce expressive speech with fine-grained emotions. Limitations and trade-offs: evaluations also reveal weak- nesses under challenging acoustic conditions (e.g., noise, echo), which appear more related to the FM than to the GPT instruction pathway. During post-training, we obser

## 271. Lost in Speech: Trilingual Spoken Hallucination Detection Across Audio and Transcripts

ID: `2608.24707` | Theme: Captioning/grounding | Status: `excluded_after_screening`

Source: https://arxiv.org/pdf/2608.24707

Snapshot SHA-256: `7e6af09a3162cff3ae6e83f2d4c90dac3beb3ae61a1bddfe5939ad253a6d980b`

Excluded: Factual alteration detection in spoken news differs from acoustic grounding

Abstract extract: While text-based hallucination detection is well studied, reference-free detection of factual alterations in speech remains underexplored, especially for low-resource languages. Our spoken benchmark comprises 12,013 English, Russian, and Kazakh news samples with three synthetic alteration types and three severity levels, pairing source articles with rewrites as text, synthesized audio, and ASR transcripts. We add 290 fact-checked misinformation items collected in Russian (225) and Kazakh (65), translated into the other language and rendered through the same TTS-ASR pipeline. We evaluate fine-tuned multilingual encoders and zero-shot multimodal decoders on text, transcripts, and audio. Detect

**Method-oriented passage (PDF p. 2)**

TTS and ASR are least mature (Chun et al., 2025). To our knowledge, no prior resource combines spo- ken input, a detection task, three languages includ- ing Kazakh, and controlled hallucination types at graded severity; existing work covers only subsets of these axes. For benchmark construction, we operationally define a spoken hallucination as a synthetically in- troduced factual or contextual alteration in a news article that is unsupported by, or contradictory to, its source article. The source article is used to generate and assign the benchmark labels but is not provided to the evaluated detectors. Thus, our experiments concern reference

**Results-oriented passage (PDF p. 6)**

We evaluate five decoder models (1.5B–8B) in a zero-shot setting, reporting ASR-transcript (Dd) results for all five and direct-audio (Dc) results for three (Table 3). We report direct prompting only.

**Caveat-oriented passage (PDF p. 8)**

coverage and output reliability, and only then by task granularity. 3) Low-resource conditions amplify pipeline challenges. For the fine-tuned encoders, Kazakh has the highest ASR error and pronounced down- stream degradation, consistent with compounded TTS→ASR noise. 4) Granularity increases difficulty. Binary classification is substantially easie

## 272. Note-Level Temporal Grounding of Musical Concepts in Large Audio-Language Models

ID: `2608.29480` | Theme: Captioning/grounding | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2608.29480

Snapshot SHA-256: `8ac3e15fa82be6083525604670a2d41e2b16f7dce08edef6a28e34dbad23ca13`

Abstract extract: Large audio-language models (LALMs) demonstrate growing music-understanding capabilities, but whether their responses are grounded in acoustic evidence remains unclear. Musical language often involves abstract concepts whose acoustic evidence is difficult to define and evaluate precisely. We introduce MusicGroundingBench, a controlled benchmark of algorithmically generated piano audio with exact symbolic alignment, comprising three-note and two-bar settings. We evaluate two complementary capabilities: grounding, which localizes the acoustic evidence for a musical query, and understanding, which answers questions about the same excerpts. Our experiments show that cross-modal fine-tuning enabl

**Method-oriented passage (PDF p. 3)**

We evaluate four model settings. The FiLM and XAttn proposal baselines [17, 18] use MERT features [19] and trainable text queries and are evaluated only on MGBench-3N. Music Flamingo [3] and Qwen2-Audio-7B-Instruct [20] are prompted directly without MG- Bench training and serve as zero-shot transfer references. The GT- note baseline gives Qwen2.5-7B-Instruct the query and ground-truth MIDI notes without MGBench training; it follows the same times- tamp format and evaluation pipeline.

**Results-oriented passage (PDF p. 3)**

Table 1: Grounding results on MGBench-3N and MGBench-2B grounding test sets. We report instruction following rate (IFR), MergedIoU computed over the unions of predicted and ground-truth time spans, and precision, recall, F1, onset/offset MAE under greedy matching at IoU thresholds of 0.5 and 0.7, where 0.7 is the stricter criterion. MAE is computed over matched spans only and reported in milliseconds. The GT-note baseline supplies zero-shot Qwen2.5-7B-Instruct with exact MIDI note identities and boundaries but no audio. External LALMs are evaluated zero-shot without MGBench-specific training. The remaining models receive task-specific supervi

**Caveat-oriented passage (PDF p. 1)**

Large audio-language models (LALMs) are increasingly used for music captioning, question answering, and instruction following [1, 2, 3]. However, evaluations reveal limitations in perceptual under- standing and susceptibility to textual cues [4, 5]. Answer accuracy does not tell us how precisely a model can locate the notes or pas- sages described 

## 273. TAG-Bench: Benchmarking Temporal Audio Grounding in Large Audio Language Models

ID: `2609.01542` | Theme: Evaluation/reliability | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2609.01542

Snapshot SHA-256: `1f56925aa5c21a63fbc8627899192e36e7527fa31f5cba7f716f56821db38bb4`

Abstract extract: Large audio language models (LALMs) can describe what is heard, but their ability to localize when queried content occurs remains less systematically evaluated. We present TAG-Bench, a benchmark for temporal audio grounding in which a model returns every time interval that matches a natural-language query. TAG-Bench contains 1,750 human-verified query-recording pairs covering 149.5 hours, with eight source-dependent subsets spanning query categories and audio durations from 7 s to 20 min; 22.1% of the queries have multiple ground-truth intervals. Across 21 evaluated systems, the best-performing model achieves 31.2 mIoU and is the only system above 20 mIoU on the two long subsets, yet even th

**Method-oriented passage (PDF p. 2)**

Audio understanding benchmarks. MMAU [1], MMAU-Pro [2], and MMAR [3] assess multi-task audio reasoning through ques- tion answering; their published task descriptions emphasize ques- tion answering and reasoning rather than timestamp-output evalua- tion. Text-to-audio grounding was formalized on AudioCaps-style clips [16]. AudioTime [17] and TACOS [18] provide temporally aligned data on clips no longer than 30 seconds, principally for temporal-control or language–audio representation research. TAG- Bench differs in query diversity (covering speech content, semantics, and emotion in addition to acoustic events), in audio length (up to 20 minut

**Results-oriented passage (PDF p. 5)**

only 21.7, and FireRedAudio fails to produce a recoverable times- tamp on 20.8% of long acoustic-description queries. Because the long and short subsets also differ in source and query distribution, these results establish performance in the 17–20-minute regime but do not isolate duration as the cause of the gap. One-to-many queries are harder for the leading systems. One- to-many mIoU falls below one-to-one mIoU for FireRedAudio (34.1 vs. 21.0), MOSS-Audio-8B-Thinking (31.4 vs. 23.6), and Gemini- 3.1-Pro (27.9 vs. 20.9). At the stricter threshold, the best R@0.7 across the evaluated models falls from 24.9 on one-to-one queries to 10.1 on one

**Caveat-oriented passage (PDF p. 3)**

Answer parsing. We evaluate a free-form-output track. Timestamps are recovered by a deterministic rule-based cascade that matches in- terval expressions, start/end patterns, and timestamp arrays, normal- izing formats such as hh:mm:ss, mm:ss, millisecond fields, and spelled-out time words into seconds. Model-specific deterministic normalization han

## 274. VAANI Noise Event Dataset: A curated spontaneous speech dataset annotated with timestamps for noise events

ID: `2609.02474` | Theme: Data/Indic speech | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2609.02474

Snapshot SHA-256: `e382cf16e73fa962a1fbc83d721b00092173719a61677e720de7d00d95c4d184`

Abstract extract: Most public sound-event corpora are optimized either for general audio tagging or for clean speech separation, and comparatively few provide strong timestamped noise annotations layered directly on top of spontaneous, real-world speech. We present the VAANI Noise Event Timestamp Dataset, a derived annotation layer built on Project VAANI field recordings of spontaneous speech collected across 165 Indian districts in 105 languages. Unlike synthetically mixed corpora, VAANI captures speech and ambient noise in situ and simultaneously, and annotates each recording with fine-grained start/end timestamps for overlapping background noise events organized into a compact seven-class semantic taxonomy

**Method-oriented passage (PDF p. 2)**

WHAM! [1] takes the WSJ0-2mix speech-separation benchmark and adds a synthetic ambient-noise channel. WSJ0-2mix itself comprises 20,000, 5,000, and 3,000 in- stantaneous two-speaker mixtures in its 30-, 10-, and 5- hour train, validation, and test sets respectively (45 hours of clean, read WSJ0 speech in total); training and validation share speakers, while the test speakers are disjoint from both. WHAM! mixes this speech with roughly 80 hours of urban background audio, independently recorded with binaural microphones at San Francisco Bay Area cafes, bars, and offices, algorithmically combined at controlled SNRs to produce 28,000 two-speaker 

**Results-oriented passage (PDF p. 2)**

Two India-specific resources address the domain mis- match identified above but not the annotation gap. iN- oise [8] is a database of ten Indian environmental noise- type categories—five outdoor (autorickshaw, bus, highway, railway station, street) and five indoor (airport, cafeteria, home, train, workplace)—recorded specifically because en- vironmental noise in Indian conditions differs substantially from the noise typically studied in Western corpora. It is, however, a noise-only recording set: it contains no co- occurring speech and no annotation of when a noise event occurs relative to an utterance, so it is typically used to syntheticall

**Caveat-oriented passage (PDF p. 1)**

Abstract—Most public sound-event corpora are optimised either for general audio tagging or for clean speech separation, and comparatively few provide strong (timestamped) noise annotations layered directly on top of spontaneous, real- world speech. We present the VAANI Noise Event Timestamp Dataset , a derived annotation layer built on Project VAAN

## 275. Alignment-Free Text-Audiobox for Voice Dubbing and Full-Duplex Dialogue Synthesis

ID: `2609.03992` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2609.03992

Snapshot SHA-256: `ed306dff7de1e39f8e0fd8a39e8c42e8ec33b13197aba6f8c04da8654baa517a`

Abstract extract: We present Alignment-Free Text-Audiobox (Text-AB), a unified framework for high-quality voice dubbing and full-duplex dialogue synthesis. Building on a Diffusion Transformer trained with a flow-matching objective, Text-AB departs from the Audiobox system along three dimensions. First, it operates in a latent diffusion framework using DAC-VAE features that encode 48 kHz waveforms into a 25 Hz latent sequence, giving over 10x higher compression than previous EnCodec representations while improving resynthesis quality. Second, Text-AB is alignment-free: it consumes raw text via an off-the-shelf text encoder and learns text-speech alignment through cross-attention, removing the need for forced a

**Method-oriented passage (PDF p. 13)**

We introduced Text-AB, an alignment-free TTS framework for voice dubbing, full-duplex dialogue synthesis, and emotional full-duplex dialogue synthesis that unifies single- and two-channel speech generation within a single flow-matching-based DiT architecture. Text-AB successfully simplified the modeling stack while improving expressivity and scalability by operating in a high-fidelity latent diffusion space with DAC-VAE features, directly conditioning on raw text via cross-attention, and substantially scaling model and data size. We first pretrained Text-AB on a large-scale multilingual monologue dataset, then fine-tuned on three downstream t

**Results-oriented passage (PDF p. 9)**

Ablation Study. Table 2 shows an ablation on model size for the voice dubbing task. We observe strong scalability—performance of Text-AB consistently improves when increasing the model size from 300M to 1B to 3B parameters. Specifically, compared to the 300M model, the 3B model achieves relative improvements of 69%, 19% and 4% on content accuracy, speaker similarity and audio quality, respectively.

**Caveat-oriented passage (PDF p. 2)**

generates the target speech (Yang et al., 2020; Federico et al., 2020; Artioli et al., 2025). In this work we focus on the last component. From a modeling perspective, voice dubbing can be viewed as a cross-lingual zero-shot TTS problem: the input speech serves as an audio prompt, and the model aims to generate target-language speech conditioned on

## 276. What Did the MLLM Hear? Token-Level Spectro-Temporal Grounding for Audio MLLM Explainability

ID: `2609.12663` | Theme: Captioning/grounding | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/html/2609.12663

Snapshot SHA-256: `fc9559352aff55d635c9befcab836a73319bfd2fefad84775f7e663716a7a2b3`

Abstract extract: Audio-based Multimodal Large Language Models (MLLMs) can generate detailed natural-language descriptions of complex acoustic scenes, yet it remains unclear which parts of the input audio support each generated token. This is particularly challenging because acoustic evidence is distributed across time and frequency, and concurrent sound events may overlap temporally while occupying different spectral regions. We introduce STAG, to our knowledge the first post-hoc framework for token-level spectro-temporal grounding of captions generated by audio-based MLLMs. STAG estimates the temporal support for each generated token using target-token-specific vocabulary projections of the encoded audio re

**Method-oriented passage (HTML / no PDF page)**

STAG estimates temporal support using targeted white-box attribution, combined with black-box Frequency-Band Occlusion.

**Results-oriented passage (HTML / no PDF page)**

Conclusion


We introduced STAG, a post-hoc framework for token-level
spectro-temporal grounding of captions generated by audio MLLMs. By combining
white-box temporal attribution with black-box Frequency-Band Occlusion,
STAG produces token-specific time-frequency relevance maps without
retraining or modifying the underlying model. These maps can be aggregated into
event-level explanations through a shared attribution and evaluation pipeline
applicable across heterogeneous audio-language architectures. Across four grounding benchmarks, combining temporal attribution with
frequency-band evidence yields more accurate grounding than ten post-hoc
explanation methods. The configuration analysis supports the complementarity
of spectral and temporal evidence, and shows limited sensitivity to the final
projection rule. Cross-model and qualitative analyses further reveal that
similar captions and 

**Caveat-oriented passage (HTML / no PDF page)**

HTML fallback; no PDF page references. Post-hoc explanation is not itself a calibrated correctness probability.

## 277. Augmenting Large Audio-Language Models with Frame-Level Grounding for Fine-Grained Temporal Perception

ID: `2609.15215` | Theme: Captioning/grounding | Status: `selected_fulltext_review_plus_scoped_core_crosscheck`

Source: https://arxiv.org/pdf/2609.15215

Snapshot SHA-256: `d3118873ed3824fa031c53fcd2501d061894fe6faa154cbc326ac44e629a3777`

Abstract extract: Large Audio-Language Models (LALMs) have substantially advanced general audio understanding, yet they remain limited in fine-grained temporal perception, particularly in precise event localization. Existing approaches primarily post-train LALMs to predict event boundaries as timestamp tokens. However, this generative formulation lacks explicit correspondence between the timestamp predictions and fine-grained acoustic evidence, limiting the precision and reliability of temporal localization. To address this issue, we augment the LALM with a dedicated frame-level grounding model while leveraging its semantic modeling capability to represent the event query. Specifically, the frozen LALM encode

**Method-oriented passage (PDF p. 4)**

Table 2 summarizes the ablation results using Qwen3-Omni as the LALM backbone. To examine the role of LALM-based query mod- eling in our framework, we compare alternative query representa- tions for conditioning the grounding model while keeping the re- maining setup unchanged. MGA-CLAP serves as a standalone query encoder in place of the LALM, as it is pretrained via audio-text contrastive learning and provides word-level features [27]. To iso- late the contribution of audio contextualization within the LALM, we further remove the audio input to Qwen3-Omni while retaining the same textual input. The results show that the w/o audio context va

**Results-oriented passage (PDF p. 3)**

Table 1 presents the main temporal grounding results. All base- lines are evaluated on the same test sets using their publicly re- leased checkpoints. For FineLAP and DASM, longer recordings are split into non-overlapping 10s windows to match their input length. The strong results of TimeAudio and SpotSound confirm that task- specific post-training can effectively improve the temporal localiza- tion capability of LALMs. Our framework further improves perfor- mance with both LALM backbones, particularly at the stricter R@.7 threshold, with gains of 15.1 points on DESED and 8.1 points on AG over the best LALM baselines. The proposed framework a

**Caveat-oriented passage (PDF p. 1)**

Large Audio-Language Models (LALMs) have significantly ad- vanced general audio understanding by integrating acoustic per- ception with the semantic knowledge and reasoning capabilities of large language models [1, 2, 3]. Through multimodal pretraining and instruction tuning, LALMs acquire the ability to interpret di- verse acoustic content, includ

Additional interpretation and limitations: [core findings](CORE_FINDINGS.md).

## 278. Music Hallucination in Audio-Language Models: A Hierarchical Formulation and Empirical Study

ID: `2609.20195` | Theme: Captioning/grounding | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2609.20195

Snapshot SHA-256: `6ae56c0346b64aa163daff15f11cc6ef4292ef5d2cbde0fd1aa642bd2b008b40`

Abstract extract: Audio-language models increasingly generate confident music descriptions that are unsupported by the input audio. We present, to our knowledge, the first music-specific, layer-wise, multi-paradigm empirical study of hallucination in audio-language models and formulate it as a hierarchical perceptual grounding failure across five layers: sound events, temporal properties, tonal attributes, style, and emotion. We introduce MuseDiag, a multi-paradigm diagnostic framework with contradiction-based verification, and evaluate nine models (four open-source and five closed-source). We find that (1) vocal misperception is a universal weakness across all nine models, tonal perception is a major axis of

**Method-oriented passage (PDF p. 4)**

The diagnostic findings above suggest that music hallucination of- ten emerges when models fall back to language priors under weak audio grounding. We use ADD-M and TPA as training-free mitiga- tion probes to test whether MuseDiag profiles predict intervention behavior. They operate at different points in the generation pipeline (Figure 3): ADD-M acts in logit space to amplify audio-sensitive token predictions, while TPA acts in context space to supply layer- specific perceptual context before final response generation.

**Results-oriented passage (PDF p. 5)**

Qwen2.5-Omni-7B [63] (all 7B-class, differing in encoder/projector design) and five closed-source API models: Gemini 2.5 Flash and Gemini 2.5 Pro [9], Gemini 3 Pro [20], GPT-4o Audio [45], and MiMo-V2-Omni [62]. • Metrics. We report layer-wise hallucination rates (HRℓ, HRhard, HRsoft) for free-form description, probing accuracy and yes-bias (YB = 𝑃( ˆ𝑦=yes | 𝑦∗=no)) for discriminative probing, and per- attribute accuracy for structured querying. These main diagnostic results include 95% confidence intervals: 10,000-resample percentile bootstrap for probing, free-form, L3 key, and per-sample structured means, and Wald intervals for the remaini

**Caveat-oriented passage (PDF p. 1)**

Audio-language models increasingly generate confident music de- scriptions that are unsupported by the input audio. We present, to our knowledge, the first music-specific, layer-wise, multi-paradigm empirical study of hallucination in audio-language models and for- mulate it as a hierarchical perceptual grounding failure across five layers: sound e

## 279. CycleSpeech: Reciprocal Alignment for Instruction-Controlled Speech Synthesis and Paralinguistic Understanding

ID: `2609.24771` | Theme: Speech/audio generation and control | Status: `selected_fulltext_review_plus_scoped_core_crosscheck`

Source: https://arxiv.org/pdf/2609.24771

Snapshot SHA-256: `2156fc92d29a6101cc2f0068cca2c89e91c7a23efcb55be7db5eb7d3bf770a90`

Abstract extract: Instruction-controlled speech synthesis and paralinguistic understanding are often trained independently, leaving reciprocal feedback between the two tasks underexplored. We introduce CycleSpeech, a framework that connects generation and understanding through a shared, structured voice profile that serves as a common target for supervision and reciprocal feedback. The forward cycle assesses whether synthesized speech expresses the intended attributes by comparing recovered and target profiles. The backward cycle evaluates whether profiles inferred from real speech can guide reconstruction of the source speaking style. To support both directions, we construct a bilingual dataset of 20,046 exa

**Method-oriented passage (PDF p. 2)**

to each other? We introduce CycleSpeech, which uses a structured voice profile as a common target for understanding supervision and generation verification. The profile describes speaker traits, prosody, affect, and context in a canonical schema, making recovered attributes comparable with their targets. Generation still takes natural-language instructions as input; the target profile provides training supervision rather than an additional inference-time requirement.

**Results-oriented passage (PDF p. 8)**

Table 3 Instruction-controlled TTS results. WER/CER and Style Acc. use the shared evaluation protocol in Sec- tion 4.1; brackets give signed 95% confidence-bound offsets. Best and second-best results are bolded and underlined.

**Caveat-oriented passage (PDF p. 3)**

Connecting generation and understanding requires a shared target that supports both generation and verifi- cation. Structured descriptions provide such an interface by mapping instructions to explicit paralinguistic attributes that can be recovered from speech. SpeakerCard-1M [20] organizes speaker and utterance traits into a typed schema, while Un

Additional interpretation and limitations: [core findings](CORE_FINDINGS.md).

## 280. MISHAP-Bench: A Hallucination Benchmark for Large Audio-Language Models

ID: `2609.33893` | Theme: Evaluation/reliability | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2609.33893

Snapshot SHA-256: `9198bb2e34ad8ba8e3be1963be9d105589530083830abfdfe7af953618995ed3`

Abstract extract: Large audio-language models (LALMs) produce fluent responses about audio but often hallucinate by making plausible yet ungrounded claims. Existing audio hallucination benchmarks mainly measure response correctness, leaving it unclear whether an LALM hallucinates or simply fails to understand the audio. We challenge correctness-based evaluation by defining two hallucination categories: (i) context, where claims are not grounded in the audio; and (ii) knowledge, where claims about audio-related topics lack support from externally verifiable facts. We introduce MISHAP-Bench, a comprehensive benchmark with 12,000 challenging open-ended question-audio pairs and a rigorous evaluation pipeline cove

**Method-oriented passage (PDF p. 2)**

Large audio-language models. LALMs build on text-only LLMs to process audio and generate natural-language responses (Luo et al., 2026). They typically pair an audio encoder with an adapter that maps acoustic features into the LLM’s embedding space. (Chu et al., 2024; LLM-Core Xiaomi, 2025; Wang et al., 2026). Qwen2.5-Omni (Xu et al., 2025) and Audio Flamingo 3 (Ghosh et al., 2025) use Whisper-derived encoders (Radford et al., 2023), while Kimi-Audio (KimiTeam et al., 2025) combines discrete semantic tokens with continuous acoustic features. These audio representations provide information beyond transcribed words, including prosody and non-spe

**Results-oriented passage (PDF p. 9)**

Table 2: Hallucination rates (%) of LALMs under four mitigation methods. W/O denotes the unmitigated baseline. Lower is better; best results are bolded. Full results are provided in Table 8.

**Caveat-oriented passage (PDF p. 2)**

Audio-language evaluation has begun using open-ended questions to reflect how users interact with LALMs (Yang et al., 2024b). However, recent audio hallucination benchmarks have relied only on binary or multiple-choice questions with correctness-based scoring (Cheng et al., 2025; Zhao et al., 2026). Such scoring may penalize uncertainty while overl

## 281. InstCharVoice: Grounding Natural-Language Instructions for Character-Level Control in Text-to-Speech

ID: `2609.36287` | Theme: Captioning/grounding | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2609.36287

Snapshot SHA-256: `8171f1c5b4960992b7b9926681ddb2dba6cb6f9edb07b1eb5d1b5a09b25c2552`

Abstract extract: Instruction-based text-to-speech (ITTS) systems enable natural-language control of expressive speech generation, but often offer limited transparency and fine-grained control over individual text units. Character-level controllable TTS systems provide explicit acoustic control, yet typically rely on user-specified acoustic attributes. To bridge this gap, we propose InstCharVoice, a unified framework that grounds natural-language instructions in character-level acoustic control. We first construct grounded instruction annotations on the WordVoice-5A-zh corpus using Qwen3-Omni. With this supervision, we train an autoregressive model to identify instruction-relevant characters and predict their

**Method-oriented passage (PDF p. 1)**

Instruction-based text-to-speech (ITTS) systems enable natural- language control of expressive speech generation, but often of- fer limited transparency and fine-grained control over individual text units. Character-level controllable TTS systems provide ex- plicit acoustic control, yet typically rely on user-specified acous- tic attributes. To bridge this gap, we propose InstCharVoice, a unified framework that grounds natural-language instructions in character-level acoustic control. We first construct grounded instruction annotations on the WordVoice-5A-zh corpus using Qwen3-Omni. With this supervision, we train an autoregressive model to i

**Results-oriented passage (PDF p. 3)**

We evaluate InstCharVoice against three representative ITTS sys- tems: FireRedTTS3 [9], Qwen3-TTS [20], and CosyVoice3 [19]. We follow the data split of WordVoice-5A and use the same evalua- tion texts and reference speech across the main comparison, ablation study, and explicit character-level control comparison. For subjective evaluation, we randomly select 14 instruction-text pairs from the test set and one reference speech sample for each pair. All systems use the same instruction-text pairs and reference speech. Since the selected Qwen3-TTS and FireRedTTS3 models do not support voice cloning in instruction mode, we convert their out- put

**Caveat-oriented passage (PDF p. 4)**

in both speech naturalness and character-level instruction follow- ing. In contrast, the other ITTS systems obtain keyword-level acous- tic results close to those of the w/o Instruction variant, suggest- ing limited ability to translate natural-language instructions into pre- cise character-level acoustic changes. InstCharVoice obtains lower SMOS t

## 282. How Robust Are Neural Audio Codecs for African Speech? A Multi-Task Benchmark and the Limits of Perceptual Quality

ID: `2610.00154` | Theme: Representations/codecs | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2610.00154

Snapshot SHA-256: `737985d82c5f50ac30d05ce67f68dc44f713de67e0d9014779e33f3dd07de867`

Abstract extract: Neural audio codecs enable low-bitrate speech compression and tokenization, yet their robustness on accented and multilingual speech remains under-evaluated. We benchmark seven open-source neural codecs (DAC, EnCodec, FocalCodec, LanguageCodec, SemantiCodec, UniCodec, WavTokenizer) on three African speech datasets afrinames, afrispeech dialog, afrispeech multilingual, reporting signal-level quality (NISQA, UTMOS, ViSQOL, STOI, F0-RMSE) alongside two downstream tasks: automatic speech recognition (ASR) and speaker verification (ASV). Our analysis yields four findings. First, signal metrics differ sharply in downstream validity: reference-based structural/intelligibility measures (ViSQOL, STOI

**Method-oriented passage (PDF p. 2)**

II. RELATED WORK Neural audio coding has shifted from psychoacoustic meth- ods toward data-driven architectures that use vector quanti- zation for high-fidelity compression at low bitrates [1], [2]. EnCodec [1] and DAC [2] use residual vector quantization (RVQ) for strong rate–distortion performance. More recent models such as WavTokenizer and SemantiCodec target ultra- low bitrates by extracting semantic tokens from pretrained speech models [11], [12], while FocalCodec and Language- Codec emphasize linguistic-feature preservation relevant to low-resource speech [13], [14]. Although early evaluations relied on signal-level quality, there is g

**Results-oriented passage (PDF p. 1)**

Abstract—Neural audio codecs enable low-bitrate speech com- pression and tokenization, yet their robustness on accented and multilingual speech remains under-evaluated. We benchmark seven open-source neural codecs (DAC, EnCodec, FocalCodec, LanguageCodec, SemantiCodec, UniCodec, WavTokenizer) on three African speech datasets (afrinames, afrispeech dialog, afrispeech multilingual), reporting signal-level quality (NISQA, UTMOS, ViSQOL, STOI, F0-RMSE) alongside two downstream tasks: automatic speech recognition (ASR) and speaker ver- ification (ASV). Our analysis yields four findings. First, sig- nal metrics differ sharply in downstream validity

**Caveat-oriented passage (PDF p. 5)**

Our primary ASV backend is ECAPA-TDNN; we report MFCC–GMM only to show backend sensitivity and do not in- clude further backends such as WavLM. ASR breadth is deep- est on conversational dialog; per-domain ASR for the names and multilingual sets is limited by recognizer coverage and transcript availability, so we report those domains primarily thro

## 283. Relevant Evidence Decoding for Audio-Visual Hallucination Mitigation

ID: `2610.02976` | Theme: Captioning/grounding | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2610.02976

Snapshot SHA-256: `a9bf14aaf32aafde4a2ea220b0dba3e613f020b5348257fd212c632fa2c0980a`

Abstract extract: Audio-Visual Large Language Models (AV-LLMs) remain prone to cross-modal hallucinations, where one modality incorrectly affects predictions about another. Although contrastive decoding reduces hallucinations in vision-language models, its direct extension to AV-LLMs overlooks a key challenge: different questions require different perceptual evidence, including audio, video, or their interaction. Notably, we observe that joint audio-visual inference can weaken the prediction even when a model can recover the correct answer from a single informative modality. For example, when asked which instrument is heard, a model may correctly predict violin from the audio alone. Once a video showing a gui

**Method-oriented passage (PDF p. 2)**

In this study, we introduce Relevant Evidence Decoding (RED), a training-free decoding method that identifies the evidence required by the question and aligns the decoding correction with the measured predictive support of that evidence. A question-only forward pass identifies the required evidence. Pointwise Mutual Information (PMI) (Church & Hanks, 1990) measures its predictive support beyond the question and language context by decomposing the joint audio-visual contribu- tion into audio, video, and residual interaction components. RED refines the original audio-visual prediction using the PMI contribution corresponding to the required evi

**Results-oriented passage (PDF p. 7)**

Results on SVHalluc. RED achieves the best SVHalluc accuracy across all three backbones, im- proving standard decoding from 53.3–60.5% to 57.1–63.4% and consistently outperforming com- peting decoding methods. Unlike prior audio-visual hallucination benchmarks that primarily rely on environmental sounds as indicators of event occurrence, SVHalluc requires grounding semanti- cally rich speech with corresponding visual evidence (Zhang et al., 2026). The consistent advantage of RED in this more challenging speech–vision setting suggests that selectively targeting question- required predictive contributions remains effective beyond simpler acoust

**Caveat-oriented passage (PDF p. 2)**

correlated visual evidence while the relevant audio evidence has little effect on the prediction, as shown in Figure 1(a). We argue that the required evidence should instead have a direct and selective influence on prediction: changing question-required evidence should alter the prediction, whereas changing irrelevant evidence should have substanti

## 284. Timestamped Hindi speech transcription using Whisper

ID: `2610.08847` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2610.08847

Snapshot SHA-256: `397446bc8c1213627f5f2bf51909f5401479ffbd395fde85e0dc21aed859b9e9`

Abstract extract: Time accurate speech transcription is essential in critical appli- cations, such as medical conversation transcription, reading as- sessment, and atypical speech recognition. Encoder-decoder auto- matic speech recognition models, such as Whisper, do not produce word-level timestamps out-of-the-box for all languages. Existing approaches to word-level time stamp estimation either use an exter- nal CTC model capable of frame level phoneme/character prediction which is computationally expensive, or use the cross attention scores internal to the model which gives coarse time stamps. We consider timestamped speech transcription for Hindi in this paper. We pro- pose a CTC-based approach, in which w

**Method-oriented passage (PDF p. 1)**

the second approach based on connectionist temporal classification (CTC) forced alignment. WhisperX [5] uses CTC-based wav2vec2.0 model [6], trained for character/phoneme level recognition, to force align the Whisper transcripts and derive the timestamps. Framelevel posterior available in CTC approach enables fine timestamp estima- tion. However, the use of a second model, which is also language specific in [5], limits the capabilities of the framework while in- creasing the complexity. Further, the timestamp accuracy depends jointly on the performance of Whisper and wav2vec2.0 models, which is not uniform across different acoustic environmen

**Results-oriented passage (PDF p. 3)**

by detaching the space (” ”) token from all tokens, (ii) finetuned the Hindi-Whisper model with the modified tokenizer, and (iii) re- estimated the 15 attention heads used for DTW on a calibration set of 300 utterances. The time stamps were additionally compared with wav2vec2.0 and Nemo forced aligner (NFA) [22]. For NFA, we used the CTC-based IndicConformer model4 to compute frame level posteriors. Inference. ASR inference uses the HuggingFace pipeline of Hindi-Whisper for every system with language="hi" and task="transcribe". We evaluate the models in both, greedy, and beam search (with a beam size of 5) conditions. Metrics. We report word 

**Caveat-oriented passage (PDF p. 2)**

Architecture and models. We used Whisper large-v2 [1] architec- ture in all our experiments with pretrained weights from a model finetuned for Hindi2, which we refer to as Hindi-Whisper in the rest of the paper. The encoder in the model generates 1280 dimensional representations every 20 ms for a fixed 30 s segment. In the pro- posed CTC-based appr

## 285. TiTok: Audio-Visual LLM for Multi-Segment Temporal Grounding

ID: `2610.09408` | Theme: Captioning/grounding | Status: `excluded_after_screening`

Source: https://arxiv.org/pdf/2610.09408

Snapshot SHA-256: `27388a2c3b37c12e66752c8864dd36020bbc45d28fc17eefaa903fb7c740fd65`

Excluded: Audio-visual multi-segment grounding; outside audio-only scope

Abstract extract: Audio-visual multi-segment grounding (AV-MSG) in untrimmed videos, reasoning over audio-visual evidence and predicting multiple segments for a query, is a fundamental problem but remains challenging. Visual-only models overlook complementary acoustic cues, while audio-visual models often fail to calibrate the number of events - a phenomenon we refer to as count miscalibration. We present TiTok, an audio-visual large language model (AV-LLM) that localizes an arbitrary number of temporal event segments for each query. For precise boundary prediction, we introduce the Time Token Interleaving (TTI) method, which explicitly injects special time tokens into the audio-visual stream to align input-s

**Method-oriented passage (PDF p. 2)**

This visual-centric design overlooks an important regime in which audio is indispensable. Many real-world events (e.g., a dog barking, a gunshot) are often more clearly delimited temporally by sound than by appearance, and may recur within a single video. Therefore, given a query event that can appear multiple times, Audio-Visual Multi-Segment Grounding (AV-MSG) identifies all of its temporal occurrences. Fig. 1 contrasts AV-MSG with dense event captioning [18]. The latter localizes all events with timestamps without a query, whereas our task determines which event instances match a given query. A growing line of work has extended temporal gr

**Results-oriented passage (PDF p. 3)**

– We propose TiTok, which introduces TTI to interleave absolute timestamps as special time tokens into the audio-visual stream, giving the model an explicit, generable time axis for localizing multiple events. – We design decoupled, multi-segment-oriented rewards optimized by a GDPO- based RL pipeline, which preserves the fine-grained localization signals that joint normalization would otherwise wash out. – We establish a UnAV-100-based evaluation protocol for AV-MSG that in- cludes CountF1 to quantify count miscalibration, on which TiTok attains the most accurate AV-MSG results among the compared models.

**Caveat-oriented passage (PDF p. 4)**

In MLLMs, time is handled along two axes: (i) on the input side, frame num- bers or indices are overlaid on the frames [9,35], representations of timestamps are fused with the visual tokens [25], or time is injected as natural-language text [3,4,40]. In AV-LLMs, audio and visual tokens can be interleaved along a shared temporal axis [29,36]. (ii) O

## 286. Beyond Speech Captions: Speech-Rewarded Style Planning for Conversational Text-to-Speech

ID: `2610.11461` | Theme: Captioning/grounding | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2610.11461

Snapshot SHA-256: `12714797cb5d0e9d4cdd3a295e5a94604bdb51a2f885a72c484ca32b6d2cf047`

Abstract extract: Natural-language style descriptions provide an interpretable interface between large language models (LLMs) and controllable text-to-speech (TTS). However, using descriptions as pseudo-labels compresses target acoustics into text, and descriptive fidelity need not imply effective control of a particular synthesizer. We empirically show that speech-text alignment only weakly predicts downstream acoustic similarity among candidate instructions for the same utterance. We therefore propose Speech-Rewarded Style Planning (SRSP), which trains a text-based style planner through a frozen downstream TTS model. Given dialogue history and response text, the planner generates candidate instructions and 

**Method-oriented passage (PDF p. 2)**

Let H be text-only dialogue history, y the response text, p a same- speaker prompt utterance, and s = (s1, . . . , sT ) the target speech tokens. The style policy generates a natural-language instruction z ∼πθ(z | H, y). During training, s is used only to construct the reward. At inference, the planner receives only (H, y), and its instruction conditions the TTS model together with response text y and prompt audio p.

**Results-oriented passage (PDF p. 2)**

three S2S scores, we use emotion similarity, computed as the co- sine similarity between emotion2vec probability vectors [15], and MCD-DTW, the mel-cepstral distortion after dynamic time warping, as downstream acoustic metrics. To assess how T2S relates to downstream acoustic similarity, we compute within-utterance Spearman correlations across candidate instructions between each T2S score and each downstream acoustic metric, as well as pairwise correlations among the acoustic metrics. MCD is negated so that higher values consistently indicate better target matching, and the correlations are averaged across utterances. Figure 1 shows that T2S 

**Caveat-oriented passage (PDF p. 4)**

In the context-only setting (Fig. 3(c)), the judge receives the three preceding utterances as audio with transcripts and the current response text, and selects the candidate whose speaking style is more appropriate for the reply. In the target-reference setting (Fig. 3(d)), it receives the context transcripts, current response text, and ground- tru

## 287. HE-NAC: High-Efficiency Neural Audio Coding via Hierarchical and Residual Multi-Band Quantization

ID: `2610.15243` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2610.15243

Snapshot SHA-256: `e7ae0d2b19d51b267316445e534b0f5af7f9856b853aad572bd5a8141f479853`

Abstract extract: High-fidelity audio coding requires faithful reconstruction of perceptually important high-frequency components, which are often lost due to the aggressive temporal decimation and quantization of neural codecs. State-of-the-art neural audio coding methods rely on adversarial learning to hallucinate these missing components, yielding perceptually plausible but imprecise reconstructions; a limitation for high-fidelity music applications. As a remedy, we propose high-efficiency neural audio coding (HE-NAC), which provides a multi-band extension of the popular residual vector quantization (RVQ) scheme. HE-NAC introduces an effective training mechanism that harmonizes a bitrate-free blind upsampl

**Method-oriented passage (PDF p. 2)**

Although the combination of the highly decimated bot- tleneck features and RVQ is a robust choice, NAC systems with such architecture exhibit progressively more imprecise reconstruction in the higher frequencies. To address this limitation, we propose HE-NAC, which extends the conven- tional RVQ coding framework with a hierarchical multi-band residual quantization architecture. Rather than relying on a single bottleneck to represent the entire spectrum, HE-NAC progressively allocates quantization resources across frequency bands, enabling dedicated residual coding of higher-frequency content while preserving the scalability and coding efficie

**Results-oriented passage (PDF p. 13)**

substantially faster than real time (RTF ≪1). The HE- NAC(16,4,0) variant exhibits nearly identical inference speed to the parameter-matched DAC baseline while requiring approxi- mately 9% fewer GFLOPs. At the highest operating point, HE- NAC(16,4,2) incurs a moderate increase in computational cost (0.0165 vs. 0.0112 RTF and 491.7 vs. 426.7 GFLOPs/audio s), reflecting the additional computation associated with the dedicated high-band residual coding. Nevertheless, the pro- posed architecture maintains faster-than-real-time offline in- ference while delivering the perceptual quality improvements demonstrated in the previous sections; neither c

**Caveat-oriented passage (PDF p. 1)**

With the advent of deep learning, a novel type of audio coding technology has emerged, namely neural audio coding (NAC) [5]. NACs introduce data-driven approaches to various parts of a codec, e.g., to decode traditional speech codes in a generative way [6], [7], to learn highly compressed discrete tokens as a foundation model [8], [9], [10], or as 

## 288. RefTAG: Reflection-aware Temporal Audio Grounding in Large Audio Language Models

ID: `2610.16217` | Theme: Captioning/grounding | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2610.16217

Snapshot SHA-256: `e90d4f0e969e8ad9a33417910f060fe655d799ea478bb1a07bd8c92396926043`

Abstract extract: Temporal audio grounding requires locating every occurrence of a queried target, making both occurrence counts and interval boundaries essential. We propose RefTAG, a post-training framework for verifiable temporal self-correction. Its Reflection Chain-of-Thought (Re-CoT) protocol combines draft intervals, discrete count and boundary actions, and revised intervals in one response. Supervised fine-tuning on these trajectories (Re-CoT-SFT) teaches the protocol; reinforcement learning (RL) jointly rewards final localization and revision outcomes. Across 8,228 queries, Re-CoT-SFT improves query-weighted mIoU over final-answer SFT by 1.74 percentage points. RL further improves TAG-Bench multi-tar

**Method-oriented passage (PDF p. 2)**

Fig. 1. RefTAG data construction and training. Ground-truth-conditioned LLM generation and rule-based correction produce balanced Re- CoT-SFT trajectories. Re-CoT-RL generates fresh rollouts on 5K SFT examples. Ground truth guides data construction and rewards, never inference.

**Results-oriented passage (PDF p. 3)**

To assess grounding performance against open-source and com- mercial baselines, we compare RefTAG with MOSS-Audio-8B- Thinking [19], FireRedAudio [21], and Gemini-3.1-Pro [20]. The first two are open-source audio models; the third is a commercial multimodal model. SFT and Re-CoT-SFT share Qwen3-Omni-30B-A3B-Instruct initialization and source examples; their supervision differs only in response structure, as defined in Section 3. Both train for 500 steps with global batch size 32, maximum sequence length 16,384, and initial learning rate 5 × 10−6. Audio/vision towers and align- ers are frozen. Re-CoT-SFT-RL continues from the Re-CoT-SFT checkp

**Caveat-oriented passage (PDF p. 4)**

Table 2 separates draft informativeness from revision gain. Re- CoT-SFT drafts scored above a count- and width-matched random- position baseline (32 placements) on every dataset, by 0.2428 in aggregate Q. Revision raised Q from 0.6487 to 0.7526 and mIoU from 55.41% to 68.86%, complementing the final-answer comparison with SFT. LAT showed little cha

## 289. ATTEST: Evidence-Grounded Reinforcement Learning for Long-Audio Temporal Understanding

ID: `2610.17149` | Theme: Speech/audio generation and control | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2610.17149

Snapshot SHA-256: `dac12a04ba39316960d2339824fd6d933913e6b25dbaaf4f016187e0fa752bdc`

Abstract extract: Temporal grounding is fundamental to audio understanding, yet large audio language models (LALMs) remain weak at it on long audio, where hallucinations compound and annotated data is scarce. Existing benchmarks cover only short clips or offer coarse, synthetic annotations. We introduce EgoSCAPE, a manually verified benchmark created from Ego4D with 700 real audios of durations up to 5 minutes, annotated with dense captions, sound sources, audio timelines, and temporal grounding queries. We further propose ATTEST, a GRPO-based reinforcement learning framework that improves temporal grounding without changing the base model's architecture or token vocabulary. ATTEST combines (i) a counterfactu

**Method-oriented passage (PDF p. 2)**

To improve long-audio temporal understanding in LALMs, we propose ATTEST, a reinforcement learning framework that mitigates hallucinations and promotes encourages predictions grounded in the audio without altering the base model’s architecture or token vocabulary. ATTEST introduces three components: (i) a counterfactual reward that ensures predictions to be grounded in the acoustic events of the corresponding temporal region, (ii) an attention density reward that steers the model’s attention toward the audio tokens of the time span each prediction claims during generation, and (iii) a token-wise advantage that provides fine-grained supervisio

**Results-oriented passage (PDF p. 7)**

Table 1 Dense audio captioning results on EgoSCAPE and AudioSet-SL datasets comparing ATTEST to other audio and omni LLM baselines. EvtF1@0.5 and SegF1 are micro. Hal% and SrcF1@0.5 are macro. * denotes sliding-window evaluation described in §C.3. TimeAudio and AudioFlamingo 2 did not adhere to the instructions to produce segment-wise sound sources so we have omitted SrcF1 for them.

**Caveat-oriented passage (PDF p. 3)**

LLMs extend this recipe to accept multiple modalities including audio and text, showing better performance than audio-only models on various benchmarks (Xu et al., 2025a,b). Evaluation of these models has largely been using short audio benchmarks such as MMAR (Ma et al., 2025), MMAU (Sakshi et al., 2025) and MMSU (Wang et al., 2026a). There has bee

## 290. Quantizer Redundancy and Exact Index Recoding in a Frozen Neural Audio Codec

ID: `2610.20471` | Theme: Representations/codecs | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2610.20471

Snapshot SHA-256: `bd1024e9f75fafb3a6196c47cec1b8893a3595b8df70a2cfb1aef767b18e5d0f`

Abstract extract: Residual scalar quantization can produce highly dependent indices when successive stages reuse identical, unscaled grids. This case study examines that behavior in a frozen neural audio codec and develops an exact recoding procedure that reduces storage while preserving its decoder inputs. Analysis of the repeated-grid recurrence identifies predictable stage sequences; finite-precision checks motivate preserving every original index through explicit exception records. The model weights and reconstruction graph remain fixed. On the studied 62- and 512-file cohorts, a predictor, adaptive coding and explicit file selection reduce complete stored bytes. The final 512-file rate is 129.591 kbps in

**Method-oriented passage (PDF p. 2)**

codebook with low-dimensional scalar quantization and an implicit Cartesian-product code space [4]. The in- spected codec instead applies four scalar alphabet sizes across 128 channels per path, with symmetric, endpoint- inclusive uniform grids. Its nearest-grid rule differs from the shifted bounded-rounding construction in the original FSQ formulation. Parker et al. also describe post-training decomposition into scaled residual FSQ tokens [5]. The analysis below applies specifically to the present repeated, unscaled grids; it does not cover every FSQ or residual FSQ construction. Our literature review includes primary records avail- able thr

**Results-oriented passage (PDF p. 4)**

We exhaustively enumerate all qL tuples for each declared scalar configuration, at most 262144 per con- figuration. Table 1 gives the resulting class counts. Archived PyTorch decoding agrees bit-for-bit with in- dependent sequential NumPy float32 addition for every tuple. Every class representative reproduces its mem- bers’ decoded bits. These are complete results for the specified scalar code-decoding map, including tuples that may never be emitted by the encoder. With a shared mapping, a standalone fixed-width class identifier requires ⌈log2 K⌉bits. This does not specify an entropy rate or a complete file format. In particular, merging the 

**Caveat-oriented passage (PDF p. 6)**

After cohort selection, the two original inference runs es- tablish the index streams and compare original and pre- dictive fixed-field representations under the same zlib level 6. Subsequent compression development reuses those saved indices. A later saved-index comparison predefines 14 candidates: four representations each un- der zlib6, Zstandar

## 291. SNOAR: Self-training with Noise filtering, Observation adding, and Remixing for Speech Denoising Without Clean References

ID: `2610.20863` | Theme: Loop/data selection | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2610.20863

Snapshot SHA-256: `0015f60dc641b586b1b332979344f897bbe08d46462e70d1c0f697826cbe31b9`

Abstract extract: Unsupervised speech denoising methods such as MixIT and noisy-target training can be trained directly on noisy recordings, avoiding the sim-to-real gap of synthetic training data, but remain well below supervised performance. Teacher--student self-training, as in RemixIT, narrows this gap by remixing a teacher's estimates into new mixtures that supervise a student; however, since the student is trained only toward the teacher's estimates, teacher errors, in particular over-suppressed speech, are never recovered and propagate as the teacher is updated from the student. We propose SNOAR, a self-training framework that corrects the teacher's estimates before use: the noise leaked into its speec

**Method-oriented passage (PDF p. 1)**

we can currently achieve with supervised training on synthetic data, where perfectly clean references are available [11, 12]. Self-training pseudo-labeling frameworks such as RemixIT [13, 12] have been proposed to close more of this gap. RemixIT remixes a teacher model’s speech and noise estimates across recordings into mixtures whose targets are now known pseudo-labels, trains a stu- dent on them, and periodically replaces the teacher with the student or updates it by an exponential moving average [14]. The teacher can be trained in any of three ways: supervised, on synthetic mix- tures with clean references; unsupervised, on real recordings

**Results-oriented passage (PDF p. 4)**

both teachers, but its gains in PESQ and WER are markedly smaller than those of SNOAR while the two methods are much closer in SI- SDR. RemixIT thus removes noise about as well as SNOAR does, but at a higher cost to the speech itself. Table 2 reports the decomposition of Sec. 2 for the MixIT teacher and its two students, and confirms this interpretation. We report the least-squares fit ˆs ≈αs + βn on each test utterance, with λ = β/α the noise coefficient relative to the speech one and r = ∥ˆs −αs −βn∥2/∥ˆs∥2 the artifact energy as a fraction of the estimate’s, averaged over utterances. Both students reduce the teacher’s residual noise from λ

**Caveat-oriented passage (PDF p. 2)**

referred to as observation adding (OA) [17], originally proposed as an inference-time post-processing technique to improve speech recognition. We instead apply it here to the self-supervision. Any speech estimate can be decomposed as ˆs = αs + λn + a, with αs the retained speech, λn the residual noise, and a the component orthogonal to the subspace

## 292. Probing Neural Audio Codecs with Speaker Traits and Speech Characteristics

ID: `2610.20955` | Theme: Representations/codecs | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2610.20955

Snapshot SHA-256: `b23886fec83154fc5d6d95e4f97e4114186f3ef0a27e24ad195c8d5734d4b656`

Abstract extract: Neural audio codecs are increasingly used for low-bitrate speech coding and serve as tokenizers for speech language models, yet it remains unclear how their codebook hierarchies encode speaker traits and speech characteristics. We systematically study 17 multi-codebook neural audio codecs across seven traits: sex, age, accent, voice quality, emotion, speech flow, and non-verbal sounds. For each codec, we reconstruct speech using partial codebooks and use machine listeners to compare trait predictions on each reconstruction. We measure prediction agreement with reweighted Cohen's \k{appa}, and define trait depth as a proxy for the codebook depth by which each trait is encoded and recoverable.

**Method-oriented passage (PDF p. 2)**

Neural audio codecs represent audio using discrete codebooks, often arranged hierarchically. In RVQ, each codebook quantizes the residual left by the preceding codebooks, allowing reconstruction from the first k codebooks at a lower bitrate (Zeghidour et al., 2022; Défossez et al., 2023; Kumar et al., 2023). Other codecs quantize at multiple temporal resolutions or replace RVQ with a single codebook or finite scalar quantization (Siuzdak et al., 2024; Xin et al., 2024; Della Libera et al., 2025; Parker et al., 2025; Casanova et al., 2025). Recent codecs train the first codebook through teacher distillation. SpeechTokenizer and Mimi dis- till 

**Results-oriented passage (PDF p. 9)**

Several limitations exist given our experimental protocol. First, the evaluation aims to measure how closely a machine listener’s predictions on a partial reconstruction match its predictions on the origi- nal audio, and therefore it does not imply that the reconstruction preserves the trait as perceived by people. For example, a partial reconstruction might retain pitch cues but lose timbre information. As a result, a biological sex classifier from speech could then keep the same prediction as for the original audio, even if human listeners perceive the recon- structed voice differently. Moreover, decoding can reduce overall audio quality, s

**Caveat-oriented passage (PDF p. 2)**

2023b), yet which information is encoded at each depth remains unclear. Earlier codebooks are gen- erally assumed to capture coarse properties such as speaker identity and recording conditions, while later codebooks recover finer acoustic details (Bor- sos et al., 2023a; Chen et al., 2025). Teacher distil- lation places linguistic content in the fi

## 293. Query-Conditioned Liquid Temporal Grounding for Long-Form Audio

ID: `2610.31252` | Theme: Captioning/grounding | Status: `abstract_and_selected_fulltext_passages_reviewed`

Source: https://arxiv.org/pdf/2610.31252

Snapshot SHA-256: `53f018b53853b5c942b3ec19fea5516f91c59bed8e1a9ad6b8d0dd98ae733894`

Abstract extract: Long-form temporal audio grounding (TAG) is challenging because target events often occupy only a small portion of a recording, while queries may impose multiple semantic constraints over a large temporal search space. We propose a query-conditioned liquid temporal grounding framework that injects query semantics through FiLM before a closed-form continuous-time (CfC) network models long-range temporal dependencies. Multiple query-relevant candidates are generated, from which a frozen large audio-language model selects the most compatible one for lightweight local boundary refinement. The pretrained backbone remains frozen, with only lightweight grounding modules optimized. Experiments on th

**Method-oriented passage (PDF p. 1)**

Long-form temporal audio grounding (TAG) is challenging because target events often occupy only a small portion of a recording, while queries may impose multiple semantic con- straints over a large temporal search space. We propose a query-conditioned liquid temporal grounding framework that injects query semantics through FiLM before a closed-form continuous-time (CfC) network models long-range temporal dependencies. Multiple query-relevant candidates are gen- erated, from which a frozen large audio-language model se- lects the most compatible one for lightweight local boundary refinement. The pretrained backbone remains frozen, with only li

**Results-oriented passage (PDF p. 3)**

4.1. Main Localization Results We evaluate the proposed framework with two audio-language backbones, MOSS-Audio and Qwen3-Omni. For reference, we also include the official English TAG results reported in Listening with Time [5]. The results are summarized in Table 1. The proposed framework consistently improves tempo- ral grounding across both audio-language backbones. With MOSS-Audio, our method achieves 38.52 mIoU and 40.61 R@0.5, outperforming direct localization, sliding-window

**Caveat-oriented passage (PDF p. 3)**

where the λ coefficients control the contributions of the in- dividual losses. These losses optimize the temporal evidence predictor, while candidate extraction remains parameter-free. They do not directly supervise candidate-level ranking; se- mantic candidate selection is subsequently performed by the frozen LALM.

## 294. RVG-Bench: A Benchmark for Reasoning-Driven Audio-Visual Temporal Grounding

ID: `2610.32268` | Theme: Evaluation/reliability | Status: `excluded_after_screening`

Source: https://arxiv.org/pdf/2610.32268

Snapshot SHA-256: `8f5444096f1a38b1d9db2824afac2e57e593290afe16ad873e33022e4871d389`

Excluded: Video-grounding benchmark; outside audio-only scope

Abstract extract: Existing temporal video grounding (TVG) benchmarks primarily focus on localizing target video segments according to descriptive text queries of the visual content. However, real-world queries are more diverse and often require the model to first understand the user's intent before localization, such as finding visual evidence, identifying the cause of an event, or recalling a remembered moment, yet such queries remain largely overlooked. To mitigate this gap, we introduce RVG-Bench, a benchmark for reasoning-driven audio-visual temporal grounding, where every query is constructed such that the target segment can only be identified through reasoning about the query's underlying intent. We car

**Method-oriented passage (PDF p. 2)**

However, real-world video grounding rarely follows this pattern. Users typically do not describe what a segment looks like; instead, they express an intent: locating evidence for a question, identifying the cause of an observed outcome, or recalling a moment from a vague memory. Such queries are inherently indirect. For example, “Locate the action that caused the burglar to fall” in Fig. 1 requires tracing the fall back to the boy pouring water on the stairs, then localizing that earlier action. This reasoning-driven grounding is a core capability required by many downstream video understanding tasks, yet it remains unevaluated by existing be

**Results-oriented passage (PDF p. 9)**

that study, respectively—achieve average mIoUs of 60.4 and 58.0 [35]. The gap between these leading models is only 2.5 points, or 4.2% relative. In contrast, Gemini-3-Pro and TimeLens-8B achieve 44.4 and 30.1 mIoU on RVG-Bench, respectively, with a substantially larger gap of 14.3 points, or 47.5% relative to TimeLens-8B (Tab. 8). This comparison motivates complementing descriptive grounding with reasoning-driven queries that remain challenging for strong models. RVG-Bench requires genuine audio-visual understanding. To examine modality reliance, we conduct modality ablation on three strong omni-modal models by removing audio to obtain V-only

**Caveat-oriented passage (PDF p. 4)**

Despite this progress, existing TVG benchmarks share a common limitation: their queries are predominantly descriptive, requiring only surface-level matching between the query text and video content, while reasoning-driven localization re- mains largely unexplored. Grounded Video QA datasets such as NEXT-GQA [27] and REXTIME [6] attempt to bridge th

## 295. TAC2: Timestamped Audio Captioning as composable functions

ID: `2610.36568` | Theme: Captioning/grounding | Status: `selected_fulltext_review_plus_scoped_core_crosscheck`

Source: https://arxiv.org/pdf/2610.36568

Snapshot SHA-256: `ac44a2414d61510bf380be0a676dd767bc42400475e8d8c46664f9f1460d92b2`

Abstract extract: Real-world audio applications require precise, queryable representations grounded in physical time. Yet modern Large Audio-Language Models (LALMs) increasingly favor conversational generation, producing free-form descriptions that conflate acoustic perception with higher-level reasoning and lack precise temporal grounding. We introduce TAC2, a foundation model that casts timestamped audio captioning as composable functions to construct granular, speaker-attributed acoustic timelines directly from in-the-wild audio. To avoid prohibitively expensive manual annotation, we programmatically fuse complementary predictions from specialized weak teachers through time-registered IoU matching. We mode

**Method-oriented passage (PDF p. 2)**

We propose TAC2, a foundation model that constructs granular, speaker-attributed acoustic time- lines directly from in-the-wild audio. To avoid manually annotating such structured timelines at scale, we introduce a multi-view fusion pipeline that temporally aligns complementary predictions from off-the-shelf sound event detectors, diarizers, and captioners over a large real-world corpus, producing high-fidelity structural training targets. To construct this richer schema while retaining modular control, we introduce an Instruction-Input-Output (IIO) completion format that decom- poses the structured caption into conditionable completion tasks

**Results-oriented passage (PDF p. 7)**

TAC2-E, the teacher cascade (82.9). The gain is concentrated in perception (Table 1): TAC2-S reaches 77.8 on MMSU perception, compared with 68.7 for Gemini-3.7 Flash, 63.8 for TAC, and 63.5 for Qwen3Omni-Captioner, while retaining strong reasoning performance (86.4). The attribute buildup in Figure 4 further localizes these gains, whereby adding individual schema attributes pref- erentially improves their associated perception tasks while leaving transcript-driven semantic tasks comparatively stable. This advantage is specific to fine-grained acoustic representation rather than general audio QnA alone. Frontier OmniLLMs remain weaker on fine-

**Caveat-oriented passage (PDF p. 3)**

Audio-Language Models and Grounded Perception. Recent Large Audio-Language Models (LALMs) (Tang et al., 2024; Chu et al., 2024; Kong et al., 2024; Zhang et al., 2025) demonstrate strong instruction-following, yet benchmarks reveal a persistent gap between high-level reasoning and fine-grained acoustic perception (Wang et al., 2026a; Sakshi et al., 

Additional interpretation and limitations: [core findings](CORE_FINDINGS.md).

## 296. Fugatto 1: Foundational Generative Audio Transformer Opus 1

ID: `fugatto` | Theme: Speech/audio generation and control | Status: `selected_fulltext_review_plus_scoped_core_crosscheck`

Source: https://fugatto.github.io/FUGATTO_ICLR_2025.pdf

Snapshot SHA-256: `ebee7fc41d28f92ed3df401a383006b51985450c38c8381a10b526a0b7e1465b`

Abstract extract: Official Fugatto project PDF; see scoped core findings.

Additional interpretation and limitations: [core findings](CORE_FINDINGS.md).
