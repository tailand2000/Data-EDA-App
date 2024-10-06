# Japanese
## データ分析EDAアプリケーション
- こちらのアプリを利用することでノートブックでコードを記載することなく簡単にEDAができるようになります

## ファイル構成
- app配下
    - code_generation.py：コードを生成する関数を格納
    - config.py：APIキーを設定する関数を格納
    - data_processing.py：データフレームに関する関数を格納
    - main.py：メインの処理を記載
- .env：APIの情報を記載


## 使い方
1. こちらのプロジェクトをクローン：git clone https://github.com/tailand2000/Data-EDA-App.git
2. ターミナルでpip install -r requirements.txt で必要なライブラリをインストール
3. .envファイルのLANGCHAIN_API_KEYにご自身のlangchainのAPIキー、OPENAI_API_KEYにご自身のOpenAIのAPIキーを入力。(1実行当たり、$0.0005程、料金がかかります。)
4. ターミナルでappフォルダまで移動し,streamlit run main.pyを実行し、アプリを立ち上げる
5. ファイルをアップロードしてください。csvファイルのみ対応しています。またcsvファイルの銭湯行にカラム名が含まれていることを確認。
6.  可視化したい内容をテキストエリアに記載。例：〇〇カラムごとの△△の平均値を棒グラフで可視化してください
7.  可視化ボタンを押す

# English
## Data Analysis EDA Application
- With this application, you can easily perform Exploratory Data Analysis (EDA) without writing code in a notebook.

## File Structure
- Inside the `app` directory:
    - `code_generation.py`: Contains functions for generating code.
    - `config.py`: Contains functions for setting API keys.
    - `data_processing.py`: Contains functions related to dataframes.
    - `main.py`: Contains the main logic of the application.
- `.env`: Stores API information.

## How to Use
1. Clone this project: `git clone https://github.com/tailand2000/Data-EDA-App.git`
2. Install the required libraries by running `pip install -r requirements.txt` in the terminal.
3. Enter your Langchain API key in the `LANGCHAIN_API_KEY` field and your OpenAI API key in the `OPENAI_API_KEY` field of the `.env` file. (Each execution costs approximately $0.0005.)
4. In the terminal, navigate to the `app` folder and run `streamlit run main.py` to launch the application.
5. Upload your file. Only CSV files are supported. Please ensure that the CSV file includes column names in the first row.
6. Write what you want to visualize in the text area. Example: "Visualize the average value of △△ by the 〇〇 column using a bar chart."
7. Press the "Visualize" button.