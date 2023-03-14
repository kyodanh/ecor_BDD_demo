Feature: Product test case

  Scenario Outline: Thực hiện login vvào hệ thống và kiểm tra thông tin ở màn hình trang chủ
    Given Thực hiện mở trang web
    When Thực hiện nhập "<username>" và "<password>"
    And Thực hiện bấm vào nút Login
    And Thực hiện chuyển tới trang cuối của màn hình
    And Kiểm tra 1 sản phẩm bất kì có trên trang
    Then thực hiện kiểm tra màu sản phẩm


    Examples:
    |username |password |
    |kyodanh@gmail.com|Dannguyen0803  |


#    run chạy sử dụng commine line python -m behave fearures/Product.feature web sử dụng là https://magento.softwaretestingboard.com/
