$(function () {
    pageInitModule.setWidth();
    pageInitModule.setSidebar();
});
$(window).resize(function () {
    pageInitModule.setWidth();
});


/*
* init page when page load
*/
var pageInitModule = (function (mod) {
    mod.setWidth = function () {
        if ($(window).width() < 768) {
            $(".sidebar").css({ left: -200 });
            $(".all").css({ marginLeft: 0 });
        } else {
            $(".sidebar").animate({ left: 0 });
            $(".all").animate({ marginLeft: 200 });
        }
    };  //设置主内容区的div到左边框的距离

    mod.setSidebar = function () {
        $('[data-target="sidebar"]').click(function () {
            var asideleft = $(".sidebar").offset().left;
            if (asideleft == 0) {
                $(".sidebar").animate({ left: -180 });
                $(".all").animate({ marginLeft: 0 });
            }
            else {
                $(".sidebar").animate({ left: 0 });
                $(".all").animate({ marginLeft: 180 });
            }
        });  //点击按钮收起左边导航栏

        $(".has-sub>a").click(function () {
            $(this).parent().siblings().find(".sub-menu").slideUp();  //查找父元素的所有同级元素中包含类名为"sub-menu"的元素，slideUp以滑动方式隐藏找到的元素，点击一个下拉菜单时，关闭其他下拉菜单
            $(this).parent().find(".sub-menu").slideToggle();   //找到父元素下面的元素中包含类名为"sub-menu"的元素，以滑动效果在显示和隐藏状态之间切换元素，如果被选元素是可见的，则隐藏这些元素，如果被选元素是隐藏的，则显示这些元素。
        });   //展开、关闭菜单


        var _strcurrenturl = window.location.href.toLowerCase();
        $(".navbar-nav a[href],.sidebar a[href]").each(function () {
            var href = $(this).attr("href").toLowerCase();
            var isActive = false;
            $(".breadcrumb>li a[href]").each(function (index) {
                if (href == $(this).attr("href").toLowerCase()) {
                    isActive = true;
                    return false;
                }
            });
            if (_strcurrenturl.indexOf(href) > -1 || isActive) {
                $(this).parent().addClass("active");
                if ($(this).parents("ul").attr("class") == "sub-menu") {
                    $(this).parents("ul").slideDown();
                    $(this).parents(".has-sub").addClass("active");
                }
            }
        })   //选择菜单时，添加active
    };
    return mod;
})(window.pageInitModule || {});



