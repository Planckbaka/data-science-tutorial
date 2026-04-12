"""模拟数据生成器 — 生成 B站商业化场景的模拟数据用于学习。"""

import random
from datetime import datetime, timedelta


def generate_ad_events(n: int = 10000, seed: int = 42) -> list[dict]:
    """生成模拟的广告投放事件数据。

    字段: user_id, ad_id, advertiser_id, position, action (impression/click/convert),
          timestamp, device, cost

    适用于: SQL 练习, 漏斗分析, CTR 计算
    """
    random.seed(seed)
    positions = ["首页推荐", "搜索结果", "视频贴片", "信息流", "UP主合作"]
    devices = ["iOS", "Android", "PC", "iPad"]
    actions = ["impression"] * 70 + ["click"] * 25 + ["convert"] * 5  # 模拟转化漏斗

    base_time = datetime(2024, 1, 1)
    events = []
    for i in range(n):
        events.append({
            "event_id": i + 1,
            "user_id": f"u_{random.randint(1, n // 10)}",
            "ad_id": f"ad_{random.randint(1, 200)}",
            "advertiser_id": f"adv_{random.randint(1, 50)}",
            "position": random.choice(positions),
            "action": random.choice(actions),
            "timestamp": (base_time + timedelta(
                days=random.randint(0, 90),
                hours=random.randint(0, 23),
                minutes=random.randint(0, 59)
            )).isoformat(),
            "device": random.choice(devices),
            "cost": round(random.uniform(0.01, 5.0), 2) if random.random() > 0.3 else 0,
        })
    return events


def generate_ad_knowledge_base() -> list[dict]:
    """生成模拟的广告投放知识库文档 — 用于 RAG 练习。

    返回带有 title, content, category 的文档列表。
    """
    docs = [
        {
            "title": "B站广告投放入门指南",
            "content": "B站广告投放支持多种形式，包括信息流广告、搜索广告、开屏广告、UP主商业合作等。广告主可以通过B站广告平台自助投放，也可以联系销售团队进行定制化投放方案。投放前需要完成企业认证和账户充值。",
            "category": "入门"
        },
        {
            "title": "广告计费模式说明",
            "content": "B站广告支持 CPC（按点击付费）、CPM（按千次展示付费）、OCPC（智能出价）三种计费模式。CPC 适合效果类广告，CPM 适合品牌曝光，OCPC 则通过算法自动优化出价以达到目标转化成本。",
            "category": "计费"
        },
        {
            "title": "广告素材规范",
            "content": "广告素材需要符合以下规范：图片尺寸 1280x720 或 720x1280，文件大小不超过 2MB；视频时长建议 15-60 秒，分辨率不低于 720p；标题长度不超过 30 个字符；不得包含虚假宣传、低俗内容或违规信息。",
            "category": "素材"
        },
        {
            "title": "定向投放策略",
            "content": "B站支持多维度定向：人群定向（年龄、性别、地域）、兴趣定向（基于用户浏览和互动行为）、内容定向（投放到特定分区或UP主视频）、重定向（对已访问用户再次触达）。建议新手从宽泛定向开始，逐步收窄。",
            "category": "策略"
        },
        {
            "title": "广告数据报告解读",
            "content": "广告数据报告包含以下核心指标：展示量（Impression）、点击量（Click）、点击率（CTR = Click/Impression）、转化量、转化率、CPC（单次点击成本）、CPM（千次展示成本）、ROI（投资回报率）。建议每日关注 CTR 和转化率变化趋势。",
            "category": "数据"
        },
        {
            "title": "UP主商业合作流程",
            "content": "UP主商业合作通过花火平台进行。广告主在花火平台发布需求，UP主接单后进行内容创作。合作形式包括：定制视频、植入广告、直播带货、动态推广等。平台会对内容进行合规审核，确保符合广告法和平台规则。",
            "category": "合作"
        },
        {
            "title": "账户优化建议",
            "content": "账户优化的关键步骤：1) 合理设置日预算，避免预算过早耗尽；2) 分时段投放，B站用户活跃高峰为晚 8-11 点；3) A/B 测试不同素材和文案；4) 定期更新素材避免用户疲劳；5) 利用 DMP 人群包精准定向。",
            "category": "优化"
        },
    ]
    return docs


def generate_user_conversations(n: int = 100, seed: int = 42) -> list[dict]:
    """生成模拟的广告主客服对话数据 — 用于 Agent 对话练习。"""
    random.seed(seed)
    questions = [
        "我的广告审核没通过是什么原因？",
        "如何提高广告的点击率？",
        "OCPC 智能出价是怎么工作的？",
        "可以指定投放到某个UP主的视频吗？",
        "广告投放后多久能看到数据？",
        "如何设置重定向人群包？",
        "我想投放开屏广告，需要什么资质？",
        "广告费用可以开发票吗？",
        "为什么我的广告展示量突然下降了？",
        "花火平台怎么找合适的UP主？",
    ]

    conversations = []
    for i in range(n):
        conversations.append({
            "conversation_id": f"conv_{i+1}",
            "user_id": f"adv_{random.randint(1, 50)}",
            "question": random.choice(questions),
            "timestamp": (datetime(2024, 6, 1) + timedelta(
                days=random.randint(0, 30),
                hours=random.randint(9, 18)
            )).isoformat(),
            "channel": random.choice(["web", "app", "api"]),
        })
    return conversations
