from typing import Optional, Dict, Any, List, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return { k: f(v) for (k, v) in x.items() }


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Payload:
    """消息内容
    
    未知，当messageType为0时
    
    文件消息，当messageType为1时
    
    语音消息，当messageType为2时
    
    名片消息，当messageType为3时
    
    聊天历史消息，当messageType为4时
    
    表情消息，当messageType为5时
    
    图片消息，当messageType为6时
    
    文字消息，当messageType为7时
    
    位置消息，当messageType为8时
    
    小程序消息，当messageType为9时
    
    钱相关消息，当messageType为10时
    
    撤回消息，当messageType为11时
    
    图文消息，当messageType为12时
    
    视频消息，当messageType为13时
    
    入群邀请，当messageType为9999时
    
    系统消息，当messageType为10000时
    
    企微系统消息，当messageType为10001时
    """
    """文件名，消息内容转成字符串
    
    消息内容转成字符串
    """
    content: Optional[str]
    """文件地址"""
    file_url: Optional[str]
    """文件名
    
    名字
    """
    name: Optional[str]
    """文件大小"""
    payload_size: Optional[float]
    """时长"""
    duration: Optional[float]
    """语音地址"""
    voice_url: Optional[str]
    """头像"""
    avatar: Optional[str]
    """是否为内部员工"""
    coworker: Optional[bool]
    """是否为好友"""
    friend: Optional[bool]
    """性别"""
    gender: Optional[float]
    """类型"""
    payload_type: Optional[float]
    """微信号/企业微信(名字全拼)"""
    weixin: Optional[str]
    """名片客户系统wxid"""
    wxid: Optional[str]
    """表情地址"""
    payload_image_url: Optional[str]
    """原图数据"""
    artwork: Optional[Dict[str, Any]]
    """原图高"""
    artwork_height: Optional[float]
    """原图宽"""
    artwork_width: Optional[str]
    """压缩图片地址"""
    image_url: Optional[str]
    """图片地址大小"""
    size: Optional[float]
    """被@的人的wxid"""
    mention: Optional[List[str]]
    """消息内容"""
    text: Optional[str]
    """关联的公众号ID"""
    appid: Optional[str]
    """小程序描述"""
    description: Optional[str]
    """icon地址"""
    icon_url: Optional[str]
    """封面图url"""
    nickname: Optional[str]
    """跳转路径"""
    page_path: Optional[str]
    """封面图加密数据"""
    thumb_key: Optional[str]
    """小程序标题"""
    title: Optional[str]
    """视频号地址"""
    url: Optional[str]
    """小程序ID"""
    username: Optional[str]
    """封面图地址"""
    thumbnail_url: Optional[str]
    """视频地址"""
    video_url: Optional[str]
    """群头像"""
    avatar_url: Optional[str]
    """邀请者名字"""
    invitater_name: Optional[str]
    """邀请者记录id"""
    invite_model_id: Optional[str]
    """邀请状态"""
    invite_status: Optional[float]
    """群名"""
    room_topic: Optional[str]
    """消息id"""
    recall_failed_payload_message_id: Optional[str]
    """邀请者姓名"""
    room_join_member_payload_inviter_name: Optional[str]
    """入群联系人名字"""
    room_join_member_payload_member_names: Optional[List[str]]
    """详情"""
    sub_payload: Optional[Dict[str, Any]]
    """类型"""
    type: Optional[float]
    """是否是bot自己"""
    contact_in_room_sysem_message_is_self: Optional[str]
    """展示名称"""
    contact_in_room_system_message_display_name: Optional[str]
    """群聊系统wxid"""
    contact_in_room_system_message_wxid: Optional[str]
    """被邀请者信息"""
    room_join_payload_invitee_list: Optional[List[str]]
    """邀请者信息"""
    room_join_payload_inviter: Optional[Dict[str, Any]]
    """时间戳"""
    room_join_payload_timestamp: Optional[float]
    """被踢者信息"""
    room_leave_payload_leaver_list: Optional[List[str]]
    """踢人者"""
    room_leave_payload_remover: Optional[Dict[str, Any]]
    """时间戳"""
    room_leave_payload_timestamp: Optional[float]
    """修改者信息"""
    room_topic_payload_changer: Optional[Dict[str, Any]]
    """新群名"""
    room_topic_payload_new_topic: Optional[str]
    """旧群名"""
    room_topic_payload_old_topic: Optional[str]
    """时间戳"""
    room_topic_payload_timestamp: Optional[float]
    wechat_system_payload_type: Optional[float]

    def __init__(self, content: Optional[str], file_url: Optional[str], name: Optional[str], payload_size: Optional[float], duration: Optional[float], voice_url: Optional[str], avatar: Optional[str], coworker: Optional[bool], friend: Optional[bool], gender: Optional[float], payload_type: Optional[float], weixin: Optional[str], wxid: Optional[str], payload_image_url: Optional[str], artwork: Optional[Dict[str, Any]], artwork_height: Optional[float], artwork_width: Optional[str], image_url: Optional[str], size: Optional[float], mention: Optional[List[str]], text: Optional[str], appid: Optional[str], description: Optional[str], icon_url: Optional[str], nickname: Optional[str], page_path: Optional[str], thumb_key: Optional[str], title: Optional[str], url: Optional[str], username: Optional[str], thumbnail_url: Optional[str], video_url: Optional[str], avatar_url: Optional[str], invitater_name: Optional[str], invite_model_id: Optional[str], invite_status: Optional[float], room_topic: Optional[str], recall_failed_payload_message_id: Optional[str], room_join_member_payload_inviter_name: Optional[str], room_join_member_payload_member_names: Optional[List[str]], sub_payload: Optional[Dict[str, Any]], type: Optional[float], contact_in_room_sysem_message_is_self: Optional[str], contact_in_room_system_message_display_name: Optional[str], contact_in_room_system_message_wxid: Optional[str], room_join_payload_invitee_list: Optional[List[str]], room_join_payload_inviter: Optional[Dict[str, Any]], room_join_payload_timestamp: Optional[float], room_leave_payload_leaver_list: Optional[List[str]], room_leave_payload_remover: Optional[Dict[str, Any]], room_leave_payload_timestamp: Optional[float], room_topic_payload_changer: Optional[Dict[str, Any]], room_topic_payload_new_topic: Optional[str], room_topic_payload_old_topic: Optional[str], room_topic_payload_timestamp: Optional[float], wechat_system_payload_type: Optional[float]) -> None:
        self.content = content
        self.file_url = file_url
        self.name = name
        self.payload_size = payload_size
        self.duration = duration
        self.voice_url = voice_url
        self.avatar = avatar
        self.coworker = coworker
        self.friend = friend
        self.gender = gender
        self.payload_type = payload_type
        self.weixin = weixin
        self.wxid = wxid
        self.payload_image_url = payload_image_url
        self.artwork = artwork
        self.artwork_height = artwork_height
        self.artwork_width = artwork_width
        self.image_url = image_url
        self.size = size
        self.mention = mention
        self.text = text
        self.appid = appid
        self.description = description
        self.icon_url = icon_url
        self.nickname = nickname
        self.page_path = page_path
        self.thumb_key = thumb_key
        self.title = title
        self.url = url
        self.username = username
        self.thumbnail_url = thumbnail_url
        self.video_url = video_url
        self.avatar_url = avatar_url
        self.invitater_name = invitater_name
        self.invite_model_id = invite_model_id
        self.invite_status = invite_status
        self.room_topic = room_topic
        self.recall_failed_payload_message_id = recall_failed_payload_message_id
        self.room_join_member_payload_inviter_name = room_join_member_payload_inviter_name
        self.room_join_member_payload_member_names = room_join_member_payload_member_names
        self.sub_payload = sub_payload
        self.type = type
        self.contact_in_room_sysem_message_is_self = contact_in_room_sysem_message_is_self
        self.contact_in_room_system_message_display_name = contact_in_room_system_message_display_name
        self.contact_in_room_system_message_wxid = contact_in_room_system_message_wxid
        self.room_join_payload_invitee_list = room_join_payload_invitee_list
        self.room_join_payload_inviter = room_join_payload_inviter
        self.room_join_payload_timestamp = room_join_payload_timestamp
        self.room_leave_payload_leaver_list = room_leave_payload_leaver_list
        self.room_leave_payload_remover = room_leave_payload_remover
        self.room_leave_payload_timestamp = room_leave_payload_timestamp
        self.room_topic_payload_changer = room_topic_payload_changer
        self.room_topic_payload_new_topic = room_topic_payload_new_topic
        self.room_topic_payload_old_topic = room_topic_payload_old_topic
        self.room_topic_payload_timestamp = room_topic_payload_timestamp
        self.wechat_system_payload_type = wechat_system_payload_type

    @staticmethod
    def from_dict(obj: Any) -> 'Payload':
        assert isinstance(obj, dict)
        content = from_union([from_str, from_none], obj.get("content"))
        file_url = from_union([from_str, from_none], obj.get("fileUrl"))
        name = from_union([from_str, from_none], obj.get("name"))
        payload_size = from_union([from_float, from_none], obj.get("size\t"))
        duration = from_union([from_float, from_none], obj.get("duration"))
        voice_url = from_union([from_str, from_none], obj.get("voiceUrl"))
        avatar = from_union([from_str, from_none], obj.get("avatar"))
        coworker = from_union([from_bool, from_none], obj.get("coworker\t"))
        friend = from_union([from_bool, from_none], obj.get("friend"))
        gender = from_union([from_float, from_none], obj.get("gender"))
        payload_type = from_union([from_float, from_none], obj.get("type\t"))
        weixin = from_union([from_str, from_none], obj.get("weixin"))
        wxid = from_union([from_str, from_none], obj.get("wxid"))
        payload_image_url = from_union([from_str, from_none], obj.get("imageUrl\t"))
        artwork = from_union([lambda x: from_dict(lambda x: x, x), from_none], obj.get("artwork"))
        artwork_height = from_union([from_float, from_none], obj.get("artwork.height"))
        artwork_width = from_union([from_str, from_none], obj.get("artwork.width"))
        image_url = from_union([from_str, from_none], obj.get("imageUrl"))
        size = from_union([from_float, from_none], obj.get("size"))
        mention = from_union([lambda x: from_list(from_str, x), from_none], obj.get("mention"))
        text = from_union([from_str, from_none], obj.get("text\t"))
        appid = from_union([from_str, from_none], obj.get("appid"))
        description = from_union([from_str, from_none], obj.get("description"))
        icon_url = from_union([from_str, from_none], obj.get("iconUrl"))
        nickname = from_union([from_str, from_none], obj.get("nickname"))
        page_path = from_union([from_str, from_none], obj.get("pagePath"))
        thumb_key = from_union([from_str, from_none], obj.get("thumbKey\t"))
        title = from_union([from_str, from_none], obj.get("title"))
        url = from_union([from_str, from_none], obj.get("url\t"))
        username = from_union([from_str, from_none], obj.get("username"))
        thumbnail_url = from_union([from_str, from_none], obj.get("thumbnailUrl"))
        video_url = from_union([from_str, from_none], obj.get("videoUrl"))
        avatar_url = from_union([from_str, from_none], obj.get("avatarUrl\t"))
        invitater_name = from_union([from_str, from_none], obj.get("invitaterName"))
        invite_model_id = from_union([from_str, from_none], obj.get("inviteModelId"))
        invite_status = from_union([from_float, from_none], obj.get("inviteStatus"))
        room_topic = from_union([from_str, from_none], obj.get("roomTopic"))
        recall_failed_payload_message_id = from_union([from_str, from_none], obj.get("RecallFailedPayload.messageId"))
        room_join_member_payload_inviter_name = from_union([from_str, from_none], obj.get("RoomJoinMemberPayload.inviterName"))
        room_join_member_payload_member_names = from_union([lambda x: from_list(from_str, x), from_none], obj.get("RoomJoinMemberPayload.memberNames"))
        sub_payload = from_union([lambda x: from_dict(lambda x: x, x), from_none], obj.get("subPayload"))
        type = from_union([from_float, from_none], obj.get("type"))
        contact_in_room_sysem_message_is_self = from_union([from_str, from_none], obj.get("ContactInRoomSysemMessage.isSelf\t"))
        contact_in_room_system_message_display_name = from_union([from_str, from_none], obj.get("ContactInRoomSystemMessage.displayName"))
        contact_in_room_system_message_wxid = from_union([from_str, from_none], obj.get("ContactInRoomSystemMessage.wxid"))
        room_join_payload_invitee_list = from_union([lambda x: from_list(from_str, x), from_none], obj.get("RoomJoinPayload.inviteeList"))
        room_join_payload_inviter = from_union([lambda x: from_dict(lambda x: x, x), from_none], obj.get("RoomJoinPayload.inviter"))
        room_join_payload_timestamp = from_union([from_float, from_none], obj.get("RoomJoinPayload.timestamp"))
        room_leave_payload_leaver_list = from_union([lambda x: from_list(from_str, x), from_none], obj.get("RoomLeavePayload.leaverList"))
        room_leave_payload_remover = from_union([lambda x: from_dict(lambda x: x, x), from_none], obj.get("RoomLeavePayload.remover"))
        room_leave_payload_timestamp = from_union([from_float, from_none], obj.get("RoomLeavePayload.timestamp"))
        room_topic_payload_changer = from_union([lambda x: from_dict(lambda x: x, x), from_none], obj.get("RoomTopicPayload.changer"))
        room_topic_payload_new_topic = from_union([from_str, from_none], obj.get("RoomTopicPayload.newTopic"))
        room_topic_payload_old_topic = from_union([from_str, from_none], obj.get("RoomTopicPayload.oldTopic"))
        room_topic_payload_timestamp = from_union([from_float, from_none], obj.get("RoomTopicPayload.timestamp"))
        wechat_system_payload_type = from_union([from_float, from_none], obj.get("wechatSystemPayloadType"))
        return Payload(content, file_url, name, payload_size, duration, voice_url, avatar, coworker, friend, gender, payload_type, weixin, wxid, payload_image_url, artwork, artwork_height, artwork_width, image_url, size, mention, text, appid, description, icon_url, nickname, page_path, thumb_key, title, url, username, thumbnail_url, video_url, avatar_url, invitater_name, invite_model_id, invite_status, room_topic, recall_failed_payload_message_id, room_join_member_payload_inviter_name, room_join_member_payload_member_names, sub_payload, type, contact_in_room_sysem_message_is_self, contact_in_room_system_message_display_name, contact_in_room_system_message_wxid, room_join_payload_invitee_list, room_join_payload_inviter, room_join_payload_timestamp, room_leave_payload_leaver_list, room_leave_payload_remover, room_leave_payload_timestamp, room_topic_payload_changer, room_topic_payload_new_topic, room_topic_payload_old_topic, room_topic_payload_timestamp, wechat_system_payload_type)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.content is not None:
            result["content"] = from_union([from_str, from_none], self.content)
        if self.file_url is not None:
            result["fileUrl"] = from_union([from_str, from_none], self.file_url)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.payload_size is not None:
            result["size\t"] = from_union([to_float, from_none], self.payload_size)
        if self.duration is not None:
            result["duration"] = from_union([to_float, from_none], self.duration)
        if self.voice_url is not None:
            result["voiceUrl"] = from_union([from_str, from_none], self.voice_url)
        if self.avatar is not None:
            result["avatar"] = from_union([from_str, from_none], self.avatar)
        if self.coworker is not None:
            result["coworker\t"] = from_union([from_bool, from_none], self.coworker)
        if self.friend is not None:
            result["friend"] = from_union([from_bool, from_none], self.friend)
        if self.gender is not None:
            result["gender"] = from_union([to_float, from_none], self.gender)
        if self.payload_type is not None:
            result["type\t"] = from_union([to_float, from_none], self.payload_type)
        if self.weixin is not None:
            result["weixin"] = from_union([from_str, from_none], self.weixin)
        if self.wxid is not None:
            result["wxid"] = from_union([from_str, from_none], self.wxid)
        if self.payload_image_url is not None:
            result["imageUrl\t"] = from_union([from_str, from_none], self.payload_image_url)
        if self.artwork is not None:
            result["artwork"] = from_union([lambda x: from_dict(lambda x: x, x), from_none], self.artwork)
        if self.artwork_height is not None:
            result["artwork.height"] = from_union([to_float, from_none], self.artwork_height)
        if self.artwork_width is not None:
            result["artwork.width"] = from_union([from_str, from_none], self.artwork_width)
        if self.image_url is not None:
            result["imageUrl"] = from_union([from_str, from_none], self.image_url)
        if self.size is not None:
            result["size"] = from_union([to_float, from_none], self.size)
        if self.mention is not None:
            result["mention"] = from_union([lambda x: from_list(from_str, x), from_none], self.mention)
        if self.text is not None:
            result["text\t"] = from_union([from_str, from_none], self.text)
        if self.appid is not None:
            result["appid"] = from_union([from_str, from_none], self.appid)
        if self.description is not None:
            result["description"] = from_union([from_str, from_none], self.description)
        if self.icon_url is not None:
            result["iconUrl"] = from_union([from_str, from_none], self.icon_url)
        if self.nickname is not None:
            result["nickname"] = from_union([from_str, from_none], self.nickname)
        if self.page_path is not None:
            result["pagePath"] = from_union([from_str, from_none], self.page_path)
        if self.thumb_key is not None:
            result["thumbKey\t"] = from_union([from_str, from_none], self.thumb_key)
        if self.title is not None:
            result["title"] = from_union([from_str, from_none], self.title)
        if self.url is not None:
            result["url\t"] = from_union([from_str, from_none], self.url)
        if self.username is not None:
            result["username"] = from_union([from_str, from_none], self.username)
        if self.thumbnail_url is not None:
            result["thumbnailUrl"] = from_union([from_str, from_none], self.thumbnail_url)
        if self.video_url is not None:
            result["videoUrl"] = from_union([from_str, from_none], self.video_url)
        if self.avatar_url is not None:
            result["avatarUrl\t"] = from_union([from_str, from_none], self.avatar_url)
        if self.invitater_name is not None:
            result["invitaterName"] = from_union([from_str, from_none], self.invitater_name)
        if self.invite_model_id is not None:
            result["inviteModelId"] = from_union([from_str, from_none], self.invite_model_id)
        if self.invite_status is not None:
            result["inviteStatus"] = from_union([to_float, from_none], self.invite_status)
        if self.room_topic is not None:
            result["roomTopic"] = from_union([from_str, from_none], self.room_topic)
        if self.recall_failed_payload_message_id is not None:
            result["RecallFailedPayload.messageId"] = from_union([from_str, from_none], self.recall_failed_payload_message_id)
        if self.room_join_member_payload_inviter_name is not None:
            result["RoomJoinMemberPayload.inviterName"] = from_union([from_str, from_none], self.room_join_member_payload_inviter_name)
        if self.room_join_member_payload_member_names is not None:
            result["RoomJoinMemberPayload.memberNames"] = from_union([lambda x: from_list(from_str, x), from_none], self.room_join_member_payload_member_names)
        if self.sub_payload is not None:
            result["subPayload"] = from_union([lambda x: from_dict(lambda x: x, x), from_none], self.sub_payload)
        if self.type is not None:
            result["type"] = from_union([to_float, from_none], self.type)
        if self.contact_in_room_sysem_message_is_self is not None:
            result["ContactInRoomSysemMessage.isSelf\t"] = from_union([from_str, from_none], self.contact_in_room_sysem_message_is_self)
        if self.contact_in_room_system_message_display_name is not None:
            result["ContactInRoomSystemMessage.displayName"] = from_union([from_str, from_none], self.contact_in_room_system_message_display_name)
        if self.contact_in_room_system_message_wxid is not None:
            result["ContactInRoomSystemMessage.wxid"] = from_union([from_str, from_none], self.contact_in_room_system_message_wxid)
        if self.room_join_payload_invitee_list is not None:
            result["RoomJoinPayload.inviteeList"] = from_union([lambda x: from_list(from_str, x), from_none], self.room_join_payload_invitee_list)
        if self.room_join_payload_inviter is not None:
            result["RoomJoinPayload.inviter"] = from_union([lambda x: from_dict(lambda x: x, x), from_none], self.room_join_payload_inviter)
        if self.room_join_payload_timestamp is not None:
            result["RoomJoinPayload.timestamp"] = from_union([to_float, from_none], self.room_join_payload_timestamp)
        if self.room_leave_payload_leaver_list is not None:
            result["RoomLeavePayload.leaverList"] = from_union([lambda x: from_list(from_str, x), from_none], self.room_leave_payload_leaver_list)
        if self.room_leave_payload_remover is not None:
            result["RoomLeavePayload.remover"] = from_union([lambda x: from_dict(lambda x: x, x), from_none], self.room_leave_payload_remover)
        if self.room_leave_payload_timestamp is not None:
            result["RoomLeavePayload.timestamp"] = from_union([to_float, from_none], self.room_leave_payload_timestamp)
        if self.room_topic_payload_changer is not None:
            result["RoomTopicPayload.changer"] = from_union([lambda x: from_dict(lambda x: x, x), from_none], self.room_topic_payload_changer)
        if self.room_topic_payload_new_topic is not None:
            result["RoomTopicPayload.newTopic"] = from_union([from_str, from_none], self.room_topic_payload_new_topic)
        if self.room_topic_payload_old_topic is not None:
            result["RoomTopicPayload.oldTopic"] = from_union([from_str, from_none], self.room_topic_payload_old_topic)
        if self.room_topic_payload_timestamp is not None:
            result["RoomTopicPayload.timestamp"] = from_union([to_float, from_none], self.room_topic_payload_timestamp)
        if self.wechat_system_payload_type is not None:
            result["wechatSystemPayloadType"] = from_union([to_float, from_none], self.wechat_system_payload_type)
        return result


class ApifoxModel:
    """客户或者群头像"""
    avatar: str
    """bot的账号id"""
    bot_id: str
    """bot的企业微信userId"""
    bot_user_id: str
    """对话id（表示一个bot和一个客户）"""
    chat_id: str
    """客户姓名"""
    contact_name: str
    """客户的类型"""
    contact_type: float
    """是否为内部员工"""
    coworker: bool
    """客户的企业微信externalUserId"""
    external_user_id: str
    """托管账号对应成员的系统wxid"""
    im_bot_id: str
    """客户的系统wxid"""
    im_contact_id: Optional[str]
    """群聊的系统wxid"""
    im_room_id: Optional[str]
    """消息是否是托管账号自己发送的消息"""
    is_self: bool
    """消息id"""
    message_id: Optional[str]
    """消息的payload"""
    message_type: float
    """企业id"""
    org_id: str
    """消息内容"""
    payload: Optional[Payload]
    """群名"""
    room_topic: Optional[str]
    """群的企微chatId"""
    room_wecom_chat_id: Optional[str]
    """消息发送者的秒回id，仅当消息为消息为托管账号发送的，且消息来源为小组级控制台手动发消息时有效"""
    send_by: Optional[str]
    """消息来源，具体来源信息参考下面的枚举定义"""
    source: Optional[float]
    """企业级token"""
    token: str

    def __init__(self, avatar: str, bot_id: str, bot_user_id: str, chat_id: str, contact_name: str, contact_type: float, coworker: bool, external_user_id: str, im_bot_id: str, im_contact_id: Optional[str], im_room_id: Optional[str], is_self: bool, message_id: Optional[str], message_type: float, org_id: str, payload: Optional[Payload], room_topic: Optional[str], room_wecom_chat_id: Optional[str], send_by: Optional[str], source: Optional[float], token: str) -> None:
        self.avatar = avatar
        self.bot_id = bot_id
        self.bot_user_id = bot_user_id
        self.chat_id = chat_id
        self.contact_name = contact_name
        self.contact_type = contact_type
        self.coworker = coworker
        self.external_user_id = external_user_id
        self.im_bot_id = im_bot_id
        self.im_contact_id = im_contact_id
        self.im_room_id = im_room_id
        self.is_self = is_self
        self.message_id = message_id
        self.message_type = message_type
        self.org_id = org_id
        self.payload = payload
        self.room_topic = room_topic
        self.room_wecom_chat_id = room_wecom_chat_id
        self.send_by = send_by
        self.source = source
        self.token = token

    @staticmethod
    def from_dict(obj: Any) -> 'ApifoxModel':
        assert isinstance(obj, dict)
        avatar = from_str(obj.get("avatar"))
        bot_id = from_str(obj.get("botId"))
        bot_user_id = from_str(obj.get("botUserId"))
        chat_id = from_str(obj.get("chatId"))
        contact_name = from_str(obj.get("contactName"))
        contact_type = from_float(obj.get("contactType"))
        coworker = from_bool(obj.get("coworker"))
        external_user_id = from_str(obj.get("externalUserId"))
        im_bot_id = from_str(obj.get("imBotId\t"))
        im_contact_id = from_union([from_str, from_none], obj.get("imContactId\t"))
        im_room_id = from_union([from_str, from_none], obj.get("imRoomId\t"))
        is_self = from_bool(obj.get("isSelf"))
        message_id = from_union([from_str, from_none], obj.get("messageId"))
        message_type = from_float(obj.get("messageType"))
        org_id = from_str(obj.get("orgId"))
        payload = from_union([Payload.from_dict, from_none], obj.get("payload"))
        room_topic = from_union([from_str, from_none], obj.get("roomTopic"))
        room_wecom_chat_id = from_union([from_str, from_none], obj.get("roomWecomChatId\t"))
        send_by = from_union([from_str, from_none], obj.get("sendBy"))
        source = from_union([from_float, from_none], obj.get("source"))
        token = from_str(obj.get("token"))
        return ApifoxModel(avatar, bot_id, bot_user_id, chat_id, contact_name, contact_type, coworker, external_user_id, im_bot_id, im_contact_id, im_room_id, is_self, message_id, message_type, org_id, payload, room_topic, room_wecom_chat_id, send_by, source, token)

    def to_dict(self) -> dict:
        result: dict = {}
        result["avatar"] = from_str(self.avatar)
        result["botId"] = from_str(self.bot_id)
        result["botUserId"] = from_str(self.bot_user_id)
        result["chatId"] = from_str(self.chat_id)
        result["contactName"] = from_str(self.contact_name)
        result["contactType"] = to_float(self.contact_type)
        result["coworker"] = from_bool(self.coworker)
        result["externalUserId"] = from_str(self.external_user_id)
        result["imBotId\t"] = from_str(self.im_bot_id)
        if self.im_contact_id is not None:
            result["imContactId\t"] = from_union([from_str, from_none], self.im_contact_id)
        if self.im_room_id is not None:
            result["imRoomId\t"] = from_union([from_str, from_none], self.im_room_id)
        result["isSelf"] = from_bool(self.is_self)
        if self.message_id is not None:
            result["messageId"] = from_union([from_str, from_none], self.message_id)
        result["messageType"] = to_float(self.message_type)
        result["orgId"] = from_str(self.org_id)
        if self.payload is not None:
            result["payload"] = from_union([lambda x: to_class(Payload, x), from_none], self.payload)
        if self.room_topic is not None:
            result["roomTopic"] = from_union([from_str, from_none], self.room_topic)
        if self.room_wecom_chat_id is not None:
            result["roomWecomChatId\t"] = from_union([from_str, from_none], self.room_wecom_chat_id)
        if self.send_by is not None:
            result["sendBy"] = from_union([from_str, from_none], self.send_by)
        if self.source is not None:
            result["source"] = from_union([to_float, from_none], self.source)
        result["token"] = from_str(self.token)
        return result


def apifox_model_from_dict(s: Any) -> ApifoxModel:
    return ApifoxModel.from_dict(s)


def apifox_model_to_dict(x: ApifoxModel) -> Any:
    return to_class(ApifoxModel, x)
