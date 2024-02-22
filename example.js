// NodeJS example with Request
const request = require('request');

const URL = 'https://docs.google.com/forms/u/0/d/e/1FAIpQLSedOOgjiO5TmoG9b3PaaPVG9XT-s3ZNoVtxqTD_TVG1ewHjXg/formResponse';
const DATA = {
    'entry.656363207':' Không',
    'entry.1431340234': 'Đã từng',
    'entry.1491472049': 'Thỉnh thoảng',
    'entry.561335718': 'Qua mạng xã hội (facebook, reddit, instagram, ...)',
    'entry.561335718': 'Qua các nền tảng mua sắm trực tuyến',
    'entry.561335718': 'Nhắn tin, đăng bài vào các hội nhóm, cộng đồng',
    'entry.831075124': 'Không tìm được người mua',
    'entry.831075124': 'Không có sản phẩm cần mua',
    'entry.831075124': 'Spam comment',
    'entry.636174439': 'Lừa đảo',
    'entry.636174439': 'Sản phẩm không đảm bảo chất lượng',
    'entry.636174439': 'Giá cả',
    'dlut': '1708525804203',
    'entry.1431340234_sentinel': '',
    'entry.1491472049_sentinel': '',
    'entry.561335718_sentinel': '',
    'entry.831075124_sentinel': '',
    'entry.636174439_sentinel': '',
    'fvv': '1',
    'partialResponse': '[[[null,306678031,["18 - 25"],0],[null,576255298,["Thiết kế đồ họa"],0],[null,1570761028,["Đại học FPT"],0],[null,1500790156,["Năm 3"],0],[null,286922039,["Phần mềm thiết kế (Adobe Photoshop, Illustrator, ...)","Thiết kế đồ họa 2D, 3D cho web, mobile app, in ấn, ...","UI/UX Design","Branding và Identity"],0],[null,535942190,["Cộng Đồng Thiết Kế Đồ Họa (Graphic Design Community) (Facebook)","https://congdongdesigner.com (website)","https://designervn.net (website)"],0],[null,1303245396,["Bình thường"],0],[null,1371405968,["Đọc bài viết","Đọc comment","Tham gia thảo luận","Tìm kiếm tài nguyên","Giao lưu vui vẻ","Tham khảo sản phẩm tốt phục vụ công việc"],0],[null,2055220752,["Giao diện và trải nghiệm người dùng","Diễn đàn và thảo luận","Hỗ trợ và phản hồi","Cung cấp những kiến thức và tài nguyên chất lượng","Cung cấp các công cụ và dịch vụ hỗ trợ cho công việc"],0],[null,1049214840,["Nội dung hay ho"],0]],null,"-5950930480261770097"]',
    'pageHistory': '0,1',
    'fbzx': '-5950930480261770097',
}

request({
    url:URL,
    method:'POST',
    form:DATA,
}, function (error, res) {
    if (error) console.error(error)
    else console.log(res.statusCode, res.statusMessage)
})
