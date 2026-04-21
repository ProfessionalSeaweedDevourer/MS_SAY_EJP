# Module ⑤ — AI Theory (Statistics · KNN · CNN · RNN)

> **[🇰🇷 한국어](#-한국어)** · **[🇺🇸 English](#-english)**

---

## 🇰🇷 한국어

수치 연산(numpy) · 데이터프레임(pandas) · 시각화(matplotlib) 를 거쳐 고전 ML(KNN) → 딥러닝(CNN·RNN) 으로 이어지는 AI 이론 구간입니다. `C01_python/` 1월분과 `C04_AI/` 전반을 묶습니다.

### 🗂 포함 디렉토리

**C01_python/ — 수치·통계·시각화 · 고전 ML**

| 경로 | 주제 |
|---|---|
| [../../C01_python/Jan14_numpy/](../../C01_python/Jan14_numpy/) | numpy 배열 연산 |
| [../../C01_python/Jan16_pd/](../../C01_python/Jan16_pd/) | pandas 기초 |
| [../../C01_python/Jan19_pd/](../../C01_python/Jan19_pd/) | pandas 심화 |
| [../../C01_python/Jan20/](../../C01_python/Jan20/) | pandas · matplotlib |
| [../../C01_python/Jan21/](../../C01_python/Jan21/) | matplotlib 차트 실습 (미세먼지·titanic·지하철·산점도) |
| [../../C01_python/Jan22_Backup/](../../C01_python/Jan22_Backup/) | 텍스트 처리 기초 (리스트·특수문자·단어 빈도) |
| [../../C01_python/Jan23_Backup/](../../C01_python/Jan23_Backup/) | 텍스트 · 이미지 처리 |
| [../../C01_python/Jan26_ML/](../../C01_python/Jan26_ML/) | KNN 등 고전 ML |

**C04_AI/ — 딥러닝 (TensorFlow)**

| 경로 | 주제 |
|---|---|
| [../../C04_AI/Jan27_base/](../../C04_AI/Jan27_base/) | 딥러닝 기초 |
| [../../C04_AI/Jan28/](../../C04_AI/Jan28/) | 신경망 이론 |
| [../../C04_AI/Jan29_tf/](../../C04_AI/Jan29_tf/) | TensorFlow 실습 (CNN) |
| [../../C04_AI/Jan30_tf/](../../C04_AI/Jan30_tf/) | TensorFlow 실습 (RNN) |

### 🎯 핵심 학습 주제

- numpy · pandas 로 벡터/프레임 단위 데이터 처리
- matplotlib 로 정적 시각화 — 막대·원·산점도·히스토그램
- 거리 기반 분류(KNN) 와 학습/검증 분할 · 성능 지표 개념
- CNN(합성곱·풀링) · RNN(순차 의존성) 기초 구조와 TensorFlow 구현

### 🔁 재현 주의

- TensorFlow 버전에 따라 API가 달라질 수 있습니다 (당시 학습은 TF 2.x 기준).
- 데이터셋이 외부에서 다운로드되는 경우 네트워크 접근이 필요합니다.

---

## 🇺🇸 English

The theory stretch — numerics (numpy), dataframes (pandas), visualization (matplotlib), classical ML (KNN), and deep learning (CNN · RNN). Draws from the January portion of `C01_python/` and the front half of `C04_AI/`.

### 🗂 Included Directories

**C01_python/ — Numerics · Statistics · Visualization · Classical ML**

| Path | Topic |
|---|---|
| [../../C01_python/Jan14_numpy/](../../C01_python/Jan14_numpy/) | numpy array operations |
| [../../C01_python/Jan16_pd/](../../C01_python/Jan16_pd/) | pandas basics |
| [../../C01_python/Jan19_pd/](../../C01_python/Jan19_pd/) | pandas advanced |
| [../../C01_python/Jan20/](../../C01_python/Jan20/) | pandas · matplotlib |
| [../../C01_python/Jan21/](../../C01_python/Jan21/) | matplotlib chart drills (air quality · titanic · subway · scatter) |
| [../../C01_python/Jan22_Backup/](../../C01_python/Jan22_Backup/) | Text-handling basics (lists · special chars · word count) |
| [../../C01_python/Jan23_Backup/](../../C01_python/Jan23_Backup/) | Text · image processing |
| [../../C01_python/Jan26_ML/](../../C01_python/Jan26_ML/) | Classical ML (KNN, etc.) |

**C04_AI/ — Deep Learning (TensorFlow)**

| Path | Topic |
|---|---|
| [../../C04_AI/Jan27_base/](../../C04_AI/Jan27_base/) | Deep-learning foundations |
| [../../C04_AI/Jan28/](../../C04_AI/Jan28/) | Neural-network theory |
| [../../C04_AI/Jan29_tf/](../../C04_AI/Jan29_tf/) | TensorFlow lab (CNN) |
| [../../C04_AI/Jan30_tf/](../../C04_AI/Jan30_tf/) | TensorFlow lab (RNN) |

### 🎯 Key Topics

- Vector- and frame-level data manipulation with numpy · pandas
- Static visualization with matplotlib — bar · pie · scatter · histogram
- Distance-based classification (KNN), train/validation split, performance metrics
- CNN (convolution · pooling) and RNN (sequential dependency) fundamentals in TensorFlow

### 🔁 Reproduction Notes

- APIs may differ across TensorFlow versions (course material targeted TF 2.x).
- Datasets downloaded on-the-fly require network access.
