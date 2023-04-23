# User Design

---

## 1. Introduction

### 1.1 Types and Amounts of Users

We need 3 types of users:

- `admin`: 管理员用户, 数量约 10 人
- `tutor`: 教师用户, 数量 <=200 人, 活跃用户每学期 <=100 人
- `student`: 学生用户, 每学期活跃用户约 2000 人

### 1.2 Activities of `admin` Users

`admin` activities:

- manage courses
- manage tutors
- manage students
- manage announcements

### 1.3 Activities of `student` Users

`student` activities:

- manage personal profile
- browse courses
- register courses
- drop courses
- read announcements
- read course pages
- watch videos
- download files
- *ask questions (optional)
- *exercises and quizzes (optional)

### 1.4 Activities of `tutor` Users

`tutor` activities:

- manage personal profile
- manage courses: add/delete/edit `lecture` to `course`
- manage lectures: add/delete/edit `module` to `lecture`
- manage modules: upload files/videos, edit syllabus/summaries
- *manage quizzes (optional)
- *answer questions (optional)
- manage anouncements
- manage FAQs

### 1.5 Identification of Users

Fields of all users (创建账户时必填):

- username: required, unique
- password
- wechat id: required, unique. 用于和微信对照.
- email: required. 用于找回密码.

区分 administrative 和普通用户:

- use `is_staff`, `is_superuser` flag
- `admin` 用户数量极少, 仅在后台创建 superuser
- `student` 数量多, 从页面 create account
- `tutor` 数量较多, 从页面 create account

区分 `student` 和 `tutor` 用户:

- use `is_tutor` flag
- 页面 register 时, 用下拉菜单勾选“是否为tutor”选项
- 需要后台手动确认 tutor 账户
- `tutor` 用户需要一个 nickname, 便于客服识别
- `tutor` 用户需要添加 subject 域, 用于学科内检索