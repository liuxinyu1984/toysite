# Teaching App Design

用于 `tutor` 用户管理自己所教课程

- view all course taught by me
- view single course taught by me: list all lectures, documents, videos in the course
- add/delete/update lectures in course
- add/delete/update documents/videos in lecture

Tutor 只对 `lecture` 进行增删改查, 不能操作 `course`, course 仅由 admin 提前创建并指定 instructor.

## 1. View: `ViewMyCourses`

Tutor 用户查看自己所教所有课程, 仅用于 read

- view current courses: 当前所教的所有课程
- view past courses: 以前教过的课程

每一个 course 有一个 link 进入该课程的 `CourseDetail` view

## 2. View: `CourseDetail`

Tutor 查看单一课程内容, 用于 read, 不要 create/delete/update, 只有 instructor 本人能查看

- create lecture 入口: 进入 `CreateLecture` view
- 列出所有 lecture 的 week/title/syllabus, document 下载链接, video 观看入口
- 各个 lecture 有 `LectureDetail` 入口

## 3. View: `LectureDetail`

Tutor 查看单一 lecture 内容, 用于 read, 以及 create/update/delete 入口

- lecture detail page display week/title/syllabus/documents/videows
- lecture detail page 有 update/delete lecture 入口
- lecture detail page 有 create/update/delete documents 入口
- lecture detail page 有 create/update/delete videos 入口
