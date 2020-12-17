# Django Blog project!

So far we can create posts, but only when associated with a user

## TODO LIST Lab 28

- [x] Create blog_project Django project
- [x] Create blog app
- [x] Create Post model
- [x] title field
- [x] author field
- [x] body field
- [x] Register model with admin
- [x] Create BlogListView that extends appropriate generic view
- [x] associated url path is an empty string
- [x] Create BlogDetailView that extends appropriate generic view
- [x] associated url path is post/<int:pk>/
- [x] Create BlogCreateView that extends appropriate generic view
- [x] associated url path is post/new/
- [x] Create BlogUpdateView that extends appropriate generic view
- [x] associated url path is post/<int:pk>/edit/
- [x] Create BlogDeleteView that extends appropriate generic view
- [x] associated url path is post/<int:pk>/delete/
- [x] Add urls to support all views, with appropriate names
- [x] Add templates to support all views
- [x] Add navigation links in appropriate locations to access all pages
- [x] Make all necessary changes to project level files for project to run
- [x] In other words, make it work

## TODO LIST Lab 27

- [x] create blog_project project
- [x] create blog app
- [x] migrate data
- [x] create Post model
- [x] add title as a CharField with maximum length of 64 characters.
- [x] add author ForeignKey related to Django’s built in user model with CASCADE delete option.
- [x] add body TextField
- [x] add model to admin
- [x] modify Post model have user friendly display in admin
- [x] create migrations and migrate data
- [x] create a super user
- [x] Add a few posts via Admin panel
- [x] Addtemplates folder in root of project
- [x] register templates folder in project settings
- [x] create HomePageView
- [x] extend ListView
- [x] give a template of home.html
- [x] associate Post model
- [x] create home.html template
- [x] use Django Templating Language to display each post’s title
- [x] create base.html ancestor template
- [x] add main html document
- [x] use Django Templating Language to allow child templates to insert content
- [x] update url patterns for app and project
- [x] view home page and confirm posts showing properly
- [x] add detail view
- [x] link post_detail.html template
- [x] associate Post model
- [x] create post_detail.html template
- [x] template should extend base
- [x] content should display post title and body
- [x] update app urlpatterns to handle detail view
- [x] account for primary key in url
- [x] add link in home page template to related post detail page
