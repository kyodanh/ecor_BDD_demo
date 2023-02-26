Feature: Login test case

  Scenario Outline: Thực hiện login và hệ thống và kiểm tra user
    Given Thực hiện mở trang web
    When Thực hiện nhập username và password
    And Thực hiện bấm vào nút Login
    And Thực hiện kiểm tra xem username hiển thị đúng
    Then thực hiện kiểm tra có hiển thị avatar user

    Examples:
    |username|password|
    |dannguyen|tesst12|


#    run chạy sử dụng commine line python -m behave fearures/LoginTestCase.feature web sử dụng là https://magento.softwaretestingboard.com/
