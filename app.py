from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random

def auto_fill_google_form():
    # Khởi tạo trình duyệt (ở đây là Chrome)
    driver = webdriver.Chrome()

    try:
        # Mở trang Google Form
        driver.get('https://docs.google.com/forms/d/e/1FAIpQLSedOOgjiO5TmoG9b3PaaPVG9XT-s3ZNoVtxqTD_TVG1ewHjXg/viewform')
        
        # Chọn ô checkbox
        # i5, i8, i11, i14: tuoi 18; 18-25; 26-35; >35
        my_array = ['i5', 'i8', 'i11', 'i14']
        random_element = random.choice(my_array)
        checkbox_element1 = driver.find_element(By.ID,random_element)
        checkbox_element1.click()

        my_array1 = ['GD', 'Thiết kế', 'Thiết kế đồ họa','Thiet ke do hoa', 'Graphic Design', 'đồ họa']
        random_element1 = random.choice(my_array1)
        # Xác định phần tử input bằng cách sử dụng aria-labelledby
        input_element2 = driver.find_element(By.CSS_SELECTOR, '[aria-labelledby="i17"]')
        # Gửi dữ liệu vào trường văn bản
        input_element2.send_keys(random_element1)


        my_array2 = ['fpt', 'Đại học FPT','fpt', 'Đại học FPT', 'Đại học FPT']
        random_element2 = random.choice(my_array2)
        my_array3 = ['FPT Edu','Multi Arena','FPT Software','Incamedia Vietnam', 'Công ty thiết kế đồ họa và in ấn Song Phước', 'Công ty VietBrands', 'Sao Kim', 'iColor Branding', 'ColorME', 'ColorME', 'ColorMe','Colorme']
        random_element3 = random.choice(my_array3)
        input_element3 = driver.find_element(By.CSS_SELECTOR, '[aria-labelledby="i21"]')
        # Gửi dữ liệu vào trường văn bản
        if random_element == 'i11' or random_element == 'i14':
            input_element3.send_keys(random_element3)
        else:
            input_element3.send_keys(random_element2)


        if random_element == 'i11' or random_element == 'i14':
            checkbox_element4 = driver.find_element(By.ID,'i41')
        else:
        # 29,32,35,38,41: nam 1 , 2, 3 ,4 di lam
            last2 = random.choice(['i29','i32','i35','i38','i41'])
            checkbox_element4 = driver.find_element(By.ID,last2)
        checkbox_element4.click()

        # Tạo danh sách các phần tử
        item_list = ['i52', 'i55', 'i58', 'i61', 'i64', 'i67', 'i70']
        # Random số từ 4 đến 7
        random_number = random.randint(1, 7)
        # Chọn ra số lượng phần tử random từ danh sách
        selected_items = random.sample(item_list, random_number)
        # Thực hiện click và xóa phần tử từ danh sách
        for item in selected_items:
            checkbox_element = driver.find_element(By.ID, item)
            checkbox_element.click()
            item_list.remove(item)

        # i52,i55,i58,i61,i64,i67,i70
        # checkbox_element5 = driver.find_element(By.ID,'i52')
        # checkbox_element5.click()
        # checkbox_element6 = driver.find_element(By.ID,'i55')
        # checkbox_element6.click()
        # checkbox_element7 = driver.find_element(By.ID,'i58')
        # checkbox_element7.click()
        # checkbox_element8 = driver.find_element(By.ID,'i61')
        # checkbox_element8.click()

        # 81, 84, 87 cong dong
        # checkbox_element9 = driver.find_element(By.ID,'i81')
        # checkbox_element9.click()
        # checkbox_element10 = driver.find_element(By.ID,'i84')
        # checkbox_element10.click()
        # checkbox_element11 = driver.find_element(By.ID,'i87')
        # checkbox_element11.click()
            
        # Tạo danh sách các phần tử
        item_list11 = ['i81','i84','i87']
        # Random số từ 4 đến 7
        random_number11 = random.randint(1, 3)
        # Chọn ra số lượng phần tử random từ danh sách
        selected_items11 = random.sample(item_list11, random_number11)
        # Thực hiện click và xóa phần tử từ danh sách
        for item in selected_items11:
            checkbox_element11 = driver.find_element(By.ID, item)
            checkbox_element11.click()
            item_list11.remove(item)

        # 97, 100, 103, 106, 109: ko baoh, hiem khi, thinh thoang, usually, ++usually
        # checkbox_element12 = driver.find_element(By.ID,'i106')
        # checkbox_element12.click()

        # Tạo danh sách các phần tử
        item_list12 = ['i97','i100', 'i103','i106','i109']
        random_element12 = random.choice(item_list12)
        checkbox_element12 = driver.find_element(By.ID,random_element12)
        checkbox_element12.click()


        # Tạo danh sách các phần tử
        item_list13 = ['i117', 'i120', 'i123', 'i126', 'i129', 'i132', 'i135', 'i138', 'i141']
        # Random số từ 4 đến 7
        random_number13 = random.randint(4, 9)
        # Chọn ra số lượng phần tử random từ danh sách
        selected_items13 = random.sample(item_list13, random_number13)
        # Thực hiện click và xóa phần tử từ danh sách
        for item in selected_items13:
            checkbox_element13 = driver.find_element(By.ID, item)
            checkbox_element13.click()
            item_list13.remove(item)

        # 117, 120, 123, 126, 129, 132, 135, 138, 141,144
        # checkbox_element13 = driver.find_element(By.ID,'i117')
        # checkbox_element13.click()
        # checkbox_element14 = driver.find_element(By.ID,'i120')
        # checkbox_element14.click()
        # checkbox_element15 = driver.find_element(By.ID,'i123')
        # checkbox_element15.click()
        # checkbox_element16 = driver.find_element(By.ID,'i126')
        # checkbox_element16.click()
        # checkbox_element17 = driver.find_element(By.ID,'i141')
        # checkbox_element17.click()
        # checkbox_element17 = driver.find_element(By.ID,'i144')
        # checkbox_element17.click()


        # Tạo danh sách các phần tử
        item_list14 = ['i155', 'i158', 'i161', 'i164', 'i167', 'i170', 'i173', 'i176']
        # Random số từ 4 đến 7
        random_number14 = random.randint(4, 8)
        # Chọn ra số lượng phần tử random từ danh sách
        selected_items14 = random.sample(item_list14, random_number14)
        # Thực hiện click và xóa phần tử từ danh sách
        for item in selected_items14:
            checkbox_element14 = driver.find_element(By.ID, item)
            checkbox_element14.click()
            item_list14.remove(item)

        # #155, 158, 161, 164, 167, 170, 173, 176
        # checkbox_element18 = driver.find_element(By.ID,'i155')
        # checkbox_element18.click()
        # checkbox_element19 = driver.find_element(By.ID,'i158')
        # checkbox_element19.click()
        # checkbox_element20 = driver.find_element(By.ID,'i161')
        # checkbox_element20.click()
        # checkbox_element21 = driver.find_element(By.ID,'i167')
        # checkbox_element21.click()
        # checkbox_element22 = driver.find_element(By.ID,'i173')
        # checkbox_element22.click()

        my_array98 = ['kỳ vọng sớm ra mắt', 'sớm ra mắt','có nhiều người dùng','có bài viết hay','Bài viết chất lượng','Bài viết tốt','tài nguyên tốt','tài nguyên hay','tài liệu hay','có mọi người vào thảo luận','có chức năng thảo luận','có dạy các môn học trên trường','dạy các môn học','có các môn học trên trường','fu ne va die','kỳ vọng ',' ok']
        random_element98 = random.choice(my_array98)
        # Xác định phần tử input bằng cách sử dụng aria-labelledby
        input_element98 = driver.find_element(By.CSS_SELECTOR, '[aria-labelledby="i182"]')
        # Gửi dữ liệu vào trường văn bản
        input_element98.send_keys(random_element98)

        # Xác định phần tử có nội dung là "Gửi" bằng cách sử dụng XPath
        button_element23 = driver.find_element(By.XPATH, '//span[text()="Tiếp"]')
        # Thực hiện click vào phần tử
        button_element23.click()
        time.sleep(2)

        #(i5), i8: chua baoh, da tung
        checkbox_element24 = driver.find_element(By.ID,random.choice(['i5', 'i8']))
        checkbox_element24.click()

        checkbox_element25 = driver.find_element(By.ID,random.choice(['i15','i18','i21','i24','i27'])) #(15),18,21,24,27: chua tung, hiem khi,...
        checkbox_element25.click()

        #35,38,41,44, (47): mxh, nen tang truc tuyen, nhan tin dang bai, rao ban truc tiep
        # Tạo danh sách các phần tử
        item_list15 = ['i35', 'i38', 'i41', 'i44','i47']
        # Random số
        random_number15 = random.randint(2, 5)
        # Chọn ra số lượng phần tử random từ danh sách
        selected_items15 = random.sample(item_list15, random_number15)
        # Thực hiện click và xóa phần tử từ danh sách
        for item in selected_items15:
            checkbox_element15 = driver.find_element(By.ID, item)
            checkbox_element15.click()
            item_list15.remove(item)


        # checkbox_element26 = driver.find_element(By.ID,'i35')
        # checkbox_element26.click()
        # checkbox_element27 = driver.find_element(By.ID,'i38')
        # checkbox_element27.click()
        # checkbox_element28 = driver.find_element(By.ID,'i41')
        # checkbox_element28.click()

        #58,61,64,67,(70): ko tim dc nguoi mua, ko co san pham can mua, bai viet bi troi, spam comment, chua tung su dung dich vu
            # Tạo danh sách các phần tử
        item_list16 = ['i58','i61','i64','i67','i70']
        # Random số từ 4 đến 7
        random_number16 = random.randint(1, 4)
        # Chọn ra số lượng phần tử random từ danh sách
        selected_items16 = random.sample(item_list16, random_number16)
        # Thực hiện click và xóa phần tử từ danh sách
        for item in selected_items16:
            checkbox_element16 = driver.find_element(By.ID, item)
            checkbox_element16.click()
            item_list16.remove(item)

        # checkbox_element29 = driver.find_element(By.ID,'i58')
        # checkbox_element29.click()
        # checkbox_element30 = driver.find_element(By.ID,'i61')
        # checkbox_element30.click()
        # checkbox_element31 = driver.find_element(By.ID,'i64')
        # checkbox_element31.click()
        # checkbox_element32 = driver.find_element(By.ID,'i67')
        # checkbox_element32.click()

        # 81, 84, 87, (90) 
        # Tạo danh sách các phần tử
        item_list17 = ['i81', 'i84', 'i87','i90']
        # Random số từ 4 đến 7
        random_number17 = random.randint(1, 4)
        # Chọn ra số lượng phần tử random từ danh sách
        selected_items17 = random.sample(item_list17, random_number17)
        # Thực hiện click và xóa phần tử từ danh sách
        for item in selected_items17:
            checkbox_element17 = driver.find_element(By.ID, item)
            checkbox_element17.click()
            item_list17.remove(item)

        # checkbox_element33 = driver.find_element(By.ID,'i81')
        # checkbox_element33.click()
        # checkbox_element34 = driver.find_element(By.ID,'i84')
        # checkbox_element34.click()
        # checkbox_element35 = driver.find_element(By.ID,'i87')
        # checkbox_element35.click()

        my_array99 = ['bao giờ có thế ạ','cố lên','yo bro','tuyệt vời','xuất sắc','web đẹp','biu ti phun','ố kề','web ngon đẹp xịn mịn nhé','cố lên các bạn','okkkk','OK','Ok','lolo','alo','1234','abcxyz','u','s','12jd','hqdz','hoangquan','okbabi']
        random_element99 = random.choice(my_array99)
        # Xác định phần tử input bằng cách sử dụng aria-labelledby
        input_element99 = driver.find_element(By.CSS_SELECTOR, '[aria-labelledby="i96"]')
        # Gửi dữ liệu vào trường văn bản
        input_element99.send_keys(random_element99)
        # Xác định phần tử có nội dung là "Gửi" bằng cách sử dụng XPath
        button_element36 = driver.find_element(By.XPATH, '//span[text()="Gửi"]')
        # Thực hiện click vào phần tử
        button_element36.click()

        # ... Điền dữ liệu vào các trường khác và tương tác với các nút khác nếu cần
        # Chờ cho form được gửi đi và xử lý kết quả nếu cần
        time.sleep(2)  # Chờ 5 giây, có thể điều chỉnh thời gian chờ theo cần thiết
    finally:
        # Đóng trình duyệt khi hoàn thành
        driver.quit()

if __name__ == "__main__":
    #Khai báo số lượng biểu mẫu muốn gửi tự động
    number_auto = 10
    
    for i in range(number_auto):
        auto_fill_google_form()
