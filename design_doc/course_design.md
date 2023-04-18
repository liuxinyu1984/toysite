# Course Design

---

## 1. Course-Lecture-Topic Structure

Course 由每周一个 lecture 组成, 每个 lecture 由若干个 topic 组成

- `course` object 代表一个学期的一门课整体
- `lecture` object 代表一次周课, 方便计算中途加入/退出的价格. 另外 midterm/final review 就由单一 lecture 组成
- `topic` object 由 tutor 定制, 包含 video, file, syllabus 等等. Topic 便于组织材料和内容

## 2. Course

`course` model attributes:

- `subject`: e.g. 'MATH', 'ECON', 'STAT'
- `course_number`: e.g. '101'
- `year`: e.g. '2023'. 可由 admin 在学期初期创建课程, 自动获取 `start_date` year
- `term`: e.g. 'spring', 'fall', 'summer', 可由 `created_at` 自动获得
- `section`: e.g. '103', '201', 'all' (代表不分 section 的课). Econ 等课程不同 section 区别较大需要区分
- `instructor`: 为 `user` 类 object, 需要在学期初由 admin 手动添加
- `start_date`, `end_date`: 学期开始/结束日期. 结束日期后访问终止
- `list_of_lectures`: lecture 列表 (`lecture` model 中用 ForeignKey 对应 `course`)
- slug: subject+course_number+year+term+section

`course` methods:

- `get_all_lectures()`: return a list of all `lecture` objects associated to the course

## 3. Lecture

`lecture` model attributes:

- course: 'ForeignKey' to `course` model
- week: 课程第几周
- syllabus: 'TextField' 简短介绍本周包含哪些知识点
- notes: PDF file. 以周为单位下载 notes
- is_midterm: boolean field 表示是否 midterm review
- is_final: boolean field 表示是否 final review
- created date: 创建日期
- modified on: 修改日期
- slug: course+week

`lecture` model methods:

- `get_all_topics()`: return a list of all `topic` objects associated to the lecture

## 4. Topic

`topic` model attributes:

- lecture: 'ForeignKey' to lecture
- title: 'CharField' 不能太长, 一目了然
- description: 'TextField' 可以详细一些介绍此小节 topic
- notes: PDF file. 可以独立于 lecture PDF 单独上传附加 notes
- video: 视频

## 5. Relation

Relation between 3 models/classes:

![course-lecture-topic](/design_doc/course_lecture_topic.png)

- `lecture` object 可以脱离 course 单独存在, 可以反复使用
- `topic` object 可以重复使用, 可以脱离 lecture

## 6. Permissions

Permissions on CRUD operations of `course`, `lecture`, `topic` on different types of users:

| operations | student      | tutor                       | admin    |
| ---------- | ------------ | --------------------------- | -------- |
| Create     | none         | `lecture`, `topic` teaching | `course` |
| Read       | all enrolled | all teaching                | all      |
| Update     | none         | `lecture`,`topic` teaching  | `course` |
| Delete     | none         | `lecture`, `topic` teaching | `course` |
