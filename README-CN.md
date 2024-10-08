# 角色扮演对话生成器

[English](README.md) | 简体中文 | [繁體中文](README-ZH-HANT.md) | [日本語](README-JA.md)


这个项目是一个基于 Python 的工具，用于生成两个角色之间的角色扮演对话。虽然最初设置为模拟唐纳德·特朗普和乔·拜登之间的对话，但可以轻松修改为使用任何两个您选择的角色。

## 功能特性

- **可自定义角色**：虽然最初为特朗普和拜登设置，但您可以轻松修改角色描述，以创建任何两个角色之间的对话。
- **角色生成**：根据提供的描述创建详细的角色简介，包括性格特征、背景、目标和说话风格。
- **动态对话生成**：在角色之间生成逼真的、具有上下文意识的对话。
- **双语支持**：支持英语和中文两种语言进行角色生成和对话。
- **自定义主题**：允许用户输入自定义主题或场景，供角色讨论。
- **上下文感知**：保持对话上下文，实现连贯的多轮对话。
- **JSON 输出**：将生成的对话和角色简介以 JSON 格式保存，便于解析和分析。
- **交互模式**：提供交互式命令行界面，让用户引导对话方向。
- **灵活的角色切换**：在对话生成过程中自动在角色之间切换。
- **可配置参数**：允许调整模型参数（如 temperature），以生成多样化的对话。

## 要求

- Python 3.7+
- `zhipuai` 库
- GLM-4 API 密钥

## 安装

1. 克隆此仓库：
   ```
   git clone https://github.com/o1xhack/glm-role-agent
   cd glm-role-agent
   ```

2. 安装所需的包：
   ```
   pip install -r requirements.txt
   ```

3. 设置您的 GLM-4 API 密钥：
   
   建议在本地环境变量中设置您的 API 密钥。您可以通过在 `~/.bashrc`、`~/.zshrc` 或等效的 shell 配置文件中添加以下行来实现：

   ```
   export ZHIPUAI_API_KEY='your-api-key-here'
   ```

   添加此行后，记得重新加载您的 shell 配置或重启终端。

   或者，如果您还没有设置环境变量，可以在运行脚本之前临时导出它：

   ```
   export ZHIPUAI_API_KEY='your-api-key-here'
   python main.py --lan=zh
   ```

   注意：将 'your-api-key-here' 替换为您实际的 GLM-4 API 密钥。

## 使用方法

使用所需的语言选项运行主脚本：

```
python main.py --lan=en  # 英语
python main.py --lan=zh  # 中文
```

按照提示输入对话主题。输入 'quit' 结束对话生成。

## 自定义角色

要更改对话中使用的角色：

1. 打开 `main.py` 文件。
2. 找到 `text1` 和 `text2` 变量（大约在第20行左右）。
3. 将这些变量的内容替换为您想要的角色描述。
4. 保存文件并像往常一样运行脚本。

例如，要创建爱因斯坦和牛顿之间的对话，您可以将描述更改为：

```python
text1 = """
阿尔伯特·爱因斯坦，著名的物理学家，以相对论理论而闻名。
他彻底改变了我们对空间、时间和引力的理解。
爱因斯坦以他的思想实验和将复杂想法用简单术语解释的能力而著称。
"""

text2 = """
艾萨克·牛顿爵士，英国物理学家和数学家，奠定了经典力学的基础。
他发现了运动定律和万有引力定律，发展了微积分，并在光学方面取得了突破性进展。
牛顿以其有条不紊的方法而闻名，他的名言是"如果我看得更远，是因为我站在巨人的肩膀上。"
"""
```

## 文件结构

- `main.py`：运行对话生成器的主脚本
- `character_generator.py`：生成角色简介
- `dialogue_generator.py`：处理对话生成逻辑
- `model_interaction.py`：管理与 GLM-4 模型的交互
- `data_saver.py`：处理对话的保存和格式化

## 贡献

欢迎贡献！请随时提交 Pull Request。

## 许可证

该项目根据Apache-2.0许可证的条款进行许可。详情请参见[LICENSE](LICENSE)文件。