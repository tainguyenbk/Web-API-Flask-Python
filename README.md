# Xay dung REST API don gian voi Flask voi chuc nang
* Lay du lieu tu cac trang bao nhu Vnexpress, Vietnamnet: tieu de, noi dung, anh, url
* Them comment cho bai bao
* Luu vao co so du lieu SQLite

# FLASK PYTHON
## Định nghĩa
Là một micro-framework ứng dụng cho website được tạo ra từ ngôn ngữ python

Cài đặt
```
pip install Flask
```
## Chương trình Hello World

```python
from flask import Flask
app = Flask(__name__)
 
@app.route('/')
def hello_world():
    return 'Hello, World!'
 
if __name__ == '__main__':
    app.run()
```

***@app.route('/')*** chỉ định hàm phía dưới nó, hàm ***hello_world()*** được thực thi khi truy cập tới root url của website.
Trong hàm main, dòng code app.run() yêu cầu flask thực thi và lắng nghe các request của người dùng
Sau khi chạy chương trình, sẽ có dòng log:

```
Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

## Hướng dẫn Flask Python
### Định tuyến
Cách định tuyến url tới các phần khác nhau của trang web

Sử dụng route() chỉ định mỗi url của người dùng sẽ trỏ tới hàm nhất định

Ví dụ:
```python
@app.route('/user')
def user():
    return 'User page'
```
Bạn sẽ nhận được dòng chữ User page khi truy cập vào địa chỉ http://localhost:5000/user

### Quy tắc dùng tham số
Cú pháp dùng tham số là <kiểu_dũ_liệu:tên_biến>
 Ví dụ:
 ```python
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id
```

### Methods
Để sử dụng Methods, ta import request

Mặc định, một request sẽ sử dụng method GET nếu không chỉ định
Ví dụ:

```python
from flask import request
 
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
```



