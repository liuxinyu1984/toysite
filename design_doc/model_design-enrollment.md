# Enrollment Design

## 0. Activities

`Enrollment` class 建立 student 和 course 之间联系

- 一个 student 可以 enroll 多门课程, 每门课只能选一次
- 一个 course 可以有多个学生选课, 每个学生只选该课一次
  
建立 course object 之后可以开放 enrollment

- 学生从已创建的 course 中选择要 enroll 的 course
- enroll 需要从学生账户 create 一个 enrollment object, 暂时不处于激活状态, 等待缴费确认后由 admin 激活
- enroll 创建后要给 admin 发送通知, admin 激活待办
- 激活后发送通知给学生用户
- drop 需要确认, admin 收到 drop 请求, admin 将 enrollment object 改为未激活状态
- drop 后发送通知学生 drop 成功
- 收费确认功能: 每个 enrollment 创建时学生收到一个唯一认证码 string, 缴费 emt 时需要一并输入, 以便于 admin 确认收款, 之后才能激活 enrollment
- 激活期之内的学生有课程内容的访问权限: 学生有 enroll 课程的访问入口, 访问时验证是否激活

## 1. `Enrollment` class

Fields of `Enrollment` model

- `User`: student who enroll the course/create the enrollment
- `Course`: course that the student enrolled in
- `activated`: boolean field
- `register_date`: date that the enrollment is created, use `auto_now=True`
- `start_date`: starting date of enrollment, can access course materials from this date
- `drop_date`: dropping date of enrollment, deny the access from this date