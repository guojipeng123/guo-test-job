
(function () {
    $.atoms.cn_test = [
        {
            tag_code: "cntv_value1",
            type: "input",
            attrs: {
                name: gettext("数值1"),
                placeholder: gettext("数值1"),
                hookable: true
            },
            validation: [
                {
                    type: "required"
                }
            ]
        },
        {
            tag_code: "cntv_value2",
            type: "input",
            attrs: {
                name: gettext("数值2"),
                placeholder: gettext("数值2"),
                hookable: true
            },
            validation: [
                {
                    type: "required"
                }
            ]
        },
        {
            tag_code: "symbol",
            type: "input",
            attrs: {
                name: gettext("符号"),
                placeholder: gettext("请输入+、-、*、/，对应加、减、乘、除"),
                hookable: true
            },
            validation: [
                {
                    type: "required"
                }
            ]
        },
    ]
})();

