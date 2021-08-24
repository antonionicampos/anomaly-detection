# Autoencoders para Detecção de Anomalias em Equipamentos e Processos

#### Aluno: [Antonioni Barros Campos](https://github.com/antonionicampos)
#### Orientadora: [Manoela Kohler](https://github.com/manoelakohler)

---

Trabalho apresentado ao curso [BI MASTER](https://ica.puc-rio.ai/bi-master) como pré-requisito para conclusão de curso e obtenção de crédito na disciplina "Projetos de Sistemas Inteligentes de Apoio à Decisão".

- [Link para o código](https://github.com/antonionicampos/anomaly-detection).

---

### Resumo

Na indústria, sempre houve uma necessidade constante de aumento da produção com o mínimo de paradas nos processos. Somado a isso, nos últimos anos, com o aumento de poder computacional e capacidade de armazenamento, o volume de dados disponível aumentou consideravelmente abrindo espaço para o consequente aumento da utilização de métodos de *Machine Learning* e *Deep Learning* para a detecção e diagnóstico de falhas (anomalias) em equipamentos e processos.

O presente trabalho utiliza-se de modelos de Redes Neurais do tipo Autoencoder e LSTM-Autoencoder (arquitetura Autoencoder utilizando camadas LSTM) para criar uma representação dos dados de operação normal de uma [planta de processo (Tennessee Eastman Process)](./dataset.md) em um subespaço resultante do espaço original da base de dados e, a partir dessa representação, utiliza-se de um modelo SVM (Support Vector Machine) para classificar o vetor resultante (codificação do Autoencoder) em **normal** ou **falha**.

### Abstract <!-- Opcional! Caso não aplicável, remover esta seção -->

In industry, there has always been a constant need to increase production with minimal process limits. Added to this, in recent years, with the increase in computational power and storage capacity, the volume of available data has increased considerably, making room for the consequent increase in the use of Machine Learning and Deep Learning methods for detection and diagnosis of failures (anomalies) in equipment and processes.

The present work uses Autoencoder and LSTM-Autoencoder (Autoencoder architecture using LSTM layers) Neural Network models to create a representation of the normal operation data of a [process plant (Tennessee Eastman Process)](.\dataset.md) in a subspace resulting from the original space of the database and, from this representation, a SVM (Support Vector Machine) model is used to classify the resulting vector (obtained from the Autoencoder) in **normal** or **failure**. 

---

Matrícula: **192.671.130**

Pontifícia Universidade Católica do Rio de Janeiro

Curso de Pós Graduação *Business Intelligence Master*
