Feature: Product test case

#  Scenario Outline: Thực hiện login vvào hệ thống và kiểm tra thông tin ở màn hình trang chủ
#    Given Thực hiện mở trang web
#    When Thực hiện nhập "<username>" và "<password>"
#    And Thực hiện bấm vào nút Login
#    And Thực hiện chuyển tới trang cuối của màn hình
#    And Kiểm tra 1 sản phẩm bất kì có trên trang
#    Then thực hiện kiểm tra màu "<color>" "<mau>" "<maucancheck>"sản phẩm
#
#    Examples:
#    |username         |password       |color                                   |mau                                                                                                                               |maucancheck|
#    |kyodanh@gmail.com|Dannguyen0803  |//*[@id='option-label-color-93-item-50']|https://magento.softwaretestingboard.com/pub/media/catalog/product/cache/7c4c1ed835fbbf2269f24539582c6d44/w/s/ws12-blue_main_1.jpg|     xanh  |


#    run chạy sử dụng commine line python -m behave fearures/Product.feature web sử dụng là https://magento.softwaretestingboard.com/


#   Scenario Outline: Thực hiện login vào hệ thống và thực hiện bám vào banner yoga để chuyển trang
#    Given Thực hiện mở trang web
#    When Thực hiện nhập "<username>" và "<password>"
#    And Thực hiện bấm vào nút Login
#    And Thực hiện chuyển tới trang cuối của màn hình
#    And Thực hiện chuyển lên đầu trang
#    And Thực hiện tại bấm vào banner yoga đầu trang
#    Then Hệ thống chuyển qua trang yoga và hệ thống hiển thị sản phẩm
#
#    Examples:
#    |username         |password       |
#    |kyodanh@gmail.com|Dannguyen0803  |



 Scenario Outline: Login và view chi tiết sản phẩm yoga
    Given Thực hiện mở trang web
    When Thực hiện nhập "<username>" và "<password>"
    And Thực hiện bấm vào nút Login
    And Thực hiện tại bấm vào banner yoga đầu trang
    And Bấm vào 1 sản phẩm "<product>" trên trang để xem chi tiết
    Then Hệ thống hiển thị thông tin chi tiết cho sản phẩm

    Examples:
    |username         |password       |product                     |
    |kyodanh@gmail.com|Dannguyen0803  |Gwen Drawstring Bike Short  |