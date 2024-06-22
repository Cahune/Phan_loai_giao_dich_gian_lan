import streamlit as st
import base64

def Home():
    st.image('./images/title.png')
    st.markdown("Ứng dụng Web này được thiết kế để giúp người dùng (chủ yếu là nhân viên ngân hàng) dự đoán khả năng một giao dịch có hợp lệ hay không dựa trên các đặc điểm đầu vào của giao dịch đó. Với việc sử dụng các mô hình máy học đã được đào tạo và thử nghiệm, chúng tôi sẽ đưa ra dự đoán một cách chính xác, nhanh chóng và tiện lợi.")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.image("./images/chinhxac.png", width=200)
        st.markdown("<p style='margin-left: 69px;'>Chính xác</p>", unsafe_allow_html=True)    
        
    with col2:
        st.image("./images/nhanhchong.png",width=200)
        st.markdown("<p style='margin-left: 75px;'>Nhanh chóng</p>", unsafe_allow_html=True)
        
    with col3:
        st.image("./images/tienloi.png",width=140)
        st.markdown("<p style='margin-left: 78px;'>Tiện lợi</p>", unsafe_allow_html=True)
        
    st.markdown("### *Cách sử dụng:*")
    st.markdown("""
    - Điều hướng đến Menu chính(>) nằm ở góc trên bên trái của màn hình.
    - Nhấn vào tab đăng nhập và thực hiện việc đăng nhập để có quyền xem kết quả dự đoán.
    - Truy cập tab kết quả dự đoán.
    - Nhập thông tin liên quan theo yêu cầu vào các trường đầu vào và nhận kết quả.
    """)
    
    st.markdown("### *Tuyên bố từ chối trách nhiệm:*")
    st.markdown("""
    - Ứng dụng web này có thể không phải lúc nào cũng cung cấp dự đoán chính xác. Khi nghi ngờ, vui lòng nhập lại các giá trị và xác minh dự đoán.
    - Bạn được yêu cầu đăng nhập để nhận thông tin chi tiết về kết quả kiểm tra của bạn. Hãy yên tâm, thông tin của bạn được an toàn và sẽ được giữ bí mật.
    - Điều quan trọng cần lưu ý là những cá nhân có các yếu tố nguy cơ hoặc mối lo ngại cụ thể nên tham khảo ý kiến ​​của các chuyên gia để được tư vấn.
    """)