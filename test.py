# Tạo một dictionary có tên là base_dictionary với các keys là các agents và các values là các list rỗng
base_dictionary = {}
aspects = <predefine aspect here> 
# Duyệt qua từng dòng trong bộ dữ liệu
for each_line in dataset:
    # Tạo một dictionary tạm thời để lưu trữ các giá trị cho mỗi khía cạnh\

    temp_dict = {}
    for aspect in aspects:
        temp_dict[aspect] = []
    
    # Duyệt qua mỗi từ trong dòng
    for each_word in each_line:
        # Kiểm tra xem từ đó có trong sensing_agents_list hay không
        if each_word in sensing_agents_list:
            # Lấy window từ đằng trước và đằng sau từ đó
            window = get_window_around_word(each_line, each_word)
            
            # Thêm các giá trị của window vào temp_list tương ứng của khía cạnh
            temp_dict[sensing_agents_list[each_word]].extend(window)
    
    # Thêm temp_dict vào base_dictionary với keys là các khía cạnh
    for key, value in temp_dict.items():
        base_dictionary[key].append(value)

# Kết quả là base_dictionary chứa các list các giá trị tương ứng với từng khía cạnh
