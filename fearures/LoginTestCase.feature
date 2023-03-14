Feature: Login test case

  Scenario Outline: Thực hiện login và hệ thống và kiểm tra user
    Given Thực hiện mở trang web
    When Thực hiện nhập "<username>" và "<password>"
    And Thực hiện bấm vào nút Login
    And Thực hiện kiểm tra xem username hiển thị đúng
    Then thực hiện kiểm tra có hiển thị avatar user

    Examples:
    |username |password |
    |kyodanh@gmail.com|Dannguyen0803  |



    Scenario Outline: Thực hiện login và kiểm tra thông tin user ở trang cá nhân
    Given Thực hiện mở trang web
    When Thực hiện nhập "<username>" và "<password>"
    And Thực hiện bấm vào nút Login
    And Thực hiện kiểm tra xem username hiển thị đúng
    And Thực hiện bấm vào trang cá nhân của user
    Then thực hiện kiểm tra thông tin user có giống với menu

    Examples:
    |username |password |
    |kyodanh@gmail.com|Dannguyen0803  |

#    run chạy sử dụng commine line python -m behave fearures/LoginTestCase.feature web sử dụng là https://magento.softwaretestingboard.com/
