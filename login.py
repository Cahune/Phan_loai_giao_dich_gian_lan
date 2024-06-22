import streamlit as st
import pandas as pd

def Login():
    # Đọc dữ liệu từ file CSV vào DataFrame
    @st.cache_resource  # Caching để tối ưu hiệu suất khi đọc dữ liệu
    def load_data(filename):
        data = pd.read_csv(filename)
        return data
    
    data = load_data('user.csv')  # Tên file CSV chứa thông tin đăng nhập

    # Khởi tạo biến session state nếu chưa có
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
        st.session_state.user_name = ""
    
    # Kiểm tra xem người dùng đã đăng nhập chưa
    if not st.session_state.logged_in:
        st.title("Đăng nhập")
        with st.form("HỆ THỐNG ĐĂNG NHẬP"):
            user_name = st.text_input("Tên đăng nhập")
            password = st.text_input("Mật khẩu", type='password')
            if st.form_submit_button("Đăng Nhập"):
                # Kiểm tra thông tin đăng nhập
                if check_credentials(user_name, password, data):
                    st.success("Đăng nhập thành công")
                    st.session_state.logged_in = True
                    st.session_state.user_name = user_name
                else:
                    st.warning("Tên đăng nhập hoặc mật khẩu không đúng")
    
    # Nếu đã đăng nhập thành công, ẩn form đăng nhập và hiển thị nội dung người dùng
    if st.session_state.logged_in:
        st.title(f"Xin chào, {st.session_state.user_name}!")
        st.image('./images/avt.png', width=200)
       
        # Thêm nội dung cho người dùng đã đăng nhập
        st.write("Bây giờ bạn đã có thể xem kết quả dự đoán!")
        
        # Nút đăng xuất
        if st.button("Đăng Xuất"):
            st.session_state.logged_in = False
            st.session_state.user_name = ""
            st.success("Đã đăng xuất")

# Hàm kiểm tra thông tin đăng nhập từ file CSV
def check_credentials(username, password, data):
    # Chuẩn hóa username và password trước khi so sánh
    username = str(username).strip()
    password = str(password).strip()
    # Loại bỏ khoảng trắng ở đầu và cuối
    
    for index, row in data.iterrows():
        # Chuẩn hóa dữ liệu từ DataFrame trước khi so sánh
        db_username = str(row['username']).strip()  # Loại bỏ khoảng trắng ở đầu và cuối
        db_password = str(row['password']).strip()  # Loại bỏ khoảng trắng ở đầu và cuối
        
        if username == db_username and password == db_password:
            return True
    
    return False


