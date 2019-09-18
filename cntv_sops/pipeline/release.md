# 0.9.0

- features:
    - 当引擎冻结时不再启动周期任务，并将当前启动记入失败历史
- bugs fix:
    - 修复节点超时强制失败操作执行失败时仍然发送节点执行失败的信号的 bug
    
# 0.9.1

- features:
    - 模板接口兼容 web 及 sdk 模式下的数据

# 0.9.2

- improvements:
    - 将 models 模块下与 web 层相关的代码移动到 pipeline_web 中

# 0.9.3

- features:
    - 流程模板在保存时设置是否韩有子流程的信息
    