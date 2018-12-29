$("body").ready(function () {
    top_video_type_click_even();
    backstage_menu_list_hover();
    backstage_url_check();

});


function top_video_type_click_even() {
    var top_video_type_first = $("#top-video-type li:nth-of-type(1)");
    var top_video_type_second = $("#top-video-type li:nth-of-type(2)");
    var span = $("#top-video-type li span");
    top_video_type_first.click(function () {
        top_video_type_first.addClass("active");
        top_video_type_second.removeClass("active");
        span.css({"left": "0", "width": "auto"});
        $("#top-video-upload p:first-child").removeClass("d-none");
        $("#top-video-upload p:last-child").addClass("d-none");
    });
    top_video_type_second.click(function () {
        top_video_type_first.removeClass("active");
        top_video_type_second.addClass("active");
        span.css({"left": "135px", "width": "121.83px"});
        $("#top-video-upload p:first-child").addClass("d-none");
        $("#top-video-upload p:last-child").removeClass("d-none");
    })
}

function backstage_menu_list_hover() {
    var backstage_menu_list = $("#backstage-menu-list a");
    backstage_menu_list.append("<span></span>");
}

function backstage_url_check() {
    var pathname = window.location.pathname;
    var backstage_menu_list_main = $('#backstage-menu-list a:nth-of-type(1)');
    var backstage_menu_list_main_span = $('#backstage-menu-list a:nth-of-type(1) span');
    var backstage_menu_list_favorite = $('#backstage-menu-list a:nth-of-type(2)');
    var backstage_menu_list_favorite_span = $('#backstage-menu-list a:nth-of-type(2) span');
    var backstage_menu_list_videos = $('#backstage-menu-list a:nth-of-type(3)');
    var backstage_menu_list_videos_span = $('#backstage-menu-list a:nth-of-type(3) span');
    var backstage_menu_list_channel = $('#backstage-menu-list a:nth-of-type(4)');
    var backstage_menu_list_channel_span = $('#backstage-menu-list a:nth-of-type(4) span');
    pathname === "/backstage/" ? (
        backstage_menu_list_main_span.css('transform', 'scaleX(1)'),
            backstage_menu_list_main.css('background-color', '#f8f9fa')
    ) : (
        pathname === "/backstage/favorite/" ? (
            backstage_menu_list_favorite.css('background-color', '#f8f9fa'),
                backstage_menu_list_favorite_span.css('transform', 'scaleX(1)')
        ) : (
            pathname === "/backstage/my-videos/" ? (
                backstage_menu_list_videos.css('background-color', '#f8f9fa'),
                    backstage_menu_list_videos_span.css('transform', 'scaleX(1)')
            ) : (
                pathname === "/backstage/channel/" ? (
                    backstage_menu_list_channel.css('background-color', '#f8f9fa'),
                        backstage_menu_list_channel_span.css('transform', 'scaleX(1)')
                ) : (
                    null
                )
            )
        )
    );
//    if (pathname === "/backstage") {
//      backstage_menu_list_main_span.css("transform", "scaleX(1)");
//      backstage_menu_list_main.css("background-color", "#f8f9fa")
// } else {
//      if (pathname === "/backstage/favorite") {
//        backstage_menu_list_favorite.css('background-color', '#f8f9fa'),
//        backstage_menu_list_favorite_span.css('transform', 'scaleX(1)')
//      } else {
//          if (pathname === "/backstage/my-videos") {
//              backstage_menu_list_videos.css('background-color', '#f8f9fa'),
//              backstage_menu_list_videos_span.css(menu_list_span_css_change)
//          } else {
//              if (pathname === "/backstage/channel") {
//                  backstage_menu_list_channel.css('background-color', '#f8f9fa'),
//                  backstage_menu_list_channel_span.css('transform', 'scaleX(1)')
//      }
// }
// }

// }
}
