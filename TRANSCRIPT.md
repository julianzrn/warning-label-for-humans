# 制作记录 — Warning Label for Humans: One Line, Big Laugh

## 流程
1. 从 make.fun 官网接口（GET /api/competitions?status=open）读取本场 description，核对确切要求：一行至多 160 字符，印在人身上的安全警告标签。要求原文与候选清单见 candidates.md。
2. 按 $5 场次提高后的标准撰写候选：每场至少 8 个候选（见 candidates.md），逐一按"转折是否出人意料、朗读节奏、是否与常见老梗撞车"筛选，选定 1 个最佳。
3. 将选定内容写入 main.py 的命名常量 ENTRY_TEXT，程序运行时原样写入 /output/entry.txt，不带末尾换行。
4. 对 main.py 做一轮结构修订（拆出 render_entry() 以字节方式写入），修订前后各运行一次并逐字节对比输出，确认完全一致。
5. 自检：main.py 连续运行两次，输出一致；字符数合规；文件末尾无换行。

## 选定作品（135 字符）
WARNING: Requires 8 hours of charging nightly; will run on 4 and make it everyone's problem. Keep away from group chats after midnight.
