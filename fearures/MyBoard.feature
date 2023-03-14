Feature: My board  test case

  Scenario Outline: Thực hiện login vào trang cá nhân và thực hiện thay đổi tên
    Given Thực hiện mở trang web
    When Thực hiện nhập "<username>" và "<password>"
    And Thực hiện bấm vào nút Login
#    những case ở trên đã có ở file login
    And Thực hiên truy cập vào trang cá nhân
    And thực hiện bấm vào change name
    And thực hiện nhập tên "<user_fristname>" và "<user_lastname>" mới
    Then thực hiện kiểm tra tên đã thay đổi

    Examples:
    |username         |password        | user_fristname  |user_lastname      |
    |kyodanh@gmail.com|Dannguyen0803  |   panda         |   danh             |





#    run chạy sử dụng commine line python -m behave fearures/MyBoard.feature web sử dụng là https://magento.softwaretestingboard.com/
