# Time Tracking Tool

## UI画面

![Top Page](C:\Users\81801\Documents\GitHub\django_practice\time tracking tool document\image\Top Page.png)

## DB構成

| 項目             | 項目名     | 型        | 最大桁 | 備考   |
| ---------------- | ---------- | --------- | ------ | ------ |
| タスク名         | TaskName   | String    | 50     |        |
| 作業開始時間     | TimeStart  | Timestamp | ?      |        |
| 作業終了時間     | TimeEnd    | Timestamp | ?      |        |
| 作業中判定フラグ | OnWrokFlag | int       | 1      | 0 or 1 |