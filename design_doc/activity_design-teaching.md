# Teaching Activities

用于 `tutor` 用户管理自己所教课程

- view all course taught by me: 一个列表页面
- view single course taught by me
- add lectures/topics: 创建新的 week lecture/topic, 上传文件/视频
- update course materials: 修改课程 material

Tutor 只对 `lecture` 进行增删改查, 不能操作 `course`. 建议集成在 `courses` app 里.

## 1. View all courses taught by me

Tutor 用户查看自己所教所有课程

- view name: `AllCoursesTaughtByMe`
- query 一次, `Course.objects.all()`, 用 `instructor` 做 filter
- 每门课一共入口链接, 进入该课程的 update view
- 需要 permission: 只能 tutor 用户查看

## 2. View single course taught by me

Tutor 查看自己所教单一课程

- view name: `SingleCourseTaughtByMe`, argument 需要 `course-id` or slug
- permission: 只有 course instructor 一人可以查看/修改/删除
- activities: create/update/delete lectures