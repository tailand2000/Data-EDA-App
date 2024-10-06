# Japanese
## データ分析EDAアプリケーション
- こちらのアプリを利用することでノートブックでコードを記載することなく簡単にEDAができるようになります
### 使い方
1. こちらのプロジェクトをクローン：git clone https://github.com/tailand2000/Data-EDA-App.git
2. .envファイルのLANGCHAIN_API_KEYにご自身のlangchainのAPIキー、OPENAI_API_KEYにご自身のOpenAIのAPIキーを入力。(1実行当たり、$0.0005程、料金がかかります。)
3. ファイルをアップロードしてください。csvファイルのみ対応しています。またcsvファイルの銭湯行にカラム名が含まれていることを確認。
4.  可視化したい内容をテキストエリアに記載。例：〇〇カラムごとの△△の平均値を棒グラフで可視化してください
5.  可視化ボタンを押す

# English
# Data Analysis EDA Application
- By using this application, you can easily perform Exploratory Data Analysis (EDA) without writing code in a notebook.

### How to Use
1. Clone this project: `git clone ~`
2. Enter your Langchain API key in the `LANGCHAIN_API_KEY` field and your OpenAI API key in the `OPENAI_API_KEY` field of the `.env` file. (It costs approximately $0.0005 per an execution.)
3. Upload your file. Only CSV files are supported. Please ensure that the CSV file includes column names in the first row.
4. Write the content you want to visualize in the text area. Example: "Visualize the average value of △△ by the 〇〇 column using a bar graph."
5. Press the "Visualize" button.
