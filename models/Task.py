from typing import Optional, List, Any
from uuid import UUID


class Creator:
    color: str
    email: str
    id: int
    initials: Optional[str]
    profile_picture: None
    username: str

    def __init__(self, color: str, email: str, id: int, initials: Optional[str], profile_picture: None, username: str) -> None:
        self.color = color
        self.email = email
        self.id = id
        self.initials = initials
        self.profile_picture = profile_picture
        self.username = username


class Option:
    color: str
    id: UUID
    name: str
    orderindex: int

    def __init__(self, color: str, id: UUID, name: str, orderindex: int) -> None:
        self.color = color
        self.id = id
        self.name = name
        self.orderindex = orderindex


class TypeConfig:
    default: Optional[int]
    new_drop_down: Optional[bool]
    options: Optional[List[Option]]
    placeholder: None

    def __init__(self, default: Optional[int], new_drop_down: Optional[bool], options: Optional[List[Option]], placeholder: None) -> None:
        self.default = default
        self.new_drop_down = new_drop_down
        self.options = options
        self.placeholder = placeholder


class CustomField:
    date_created: str
    hide_from_guests: bool
    id: UUID
    name: str
    required: bool
    type: str
    type_config: TypeConfig
    value: Optional[int]

    def __init__(self, date_created: str, hide_from_guests: bool, id: UUID, name: str, required: bool, type: str, type_config: TypeConfig, value: Optional[int]) -> None:
        self.date_created = date_created
        self.hide_from_guests = hide_from_guests
        self.id = id
        self.name = name
        self.required = required
        self.type = type
        self.type_config = type_config
        self.value = value


class Folder:
    access: bool
    hidden: Optional[bool]
    id: int
    name: str

    def __init__(self, access: bool, hidden: Optional[bool], id: int, name: str) -> None:
        self.access = access
        self.hidden = hidden
        self.id = id
        self.name = name


class Space:
    id: int

    def __init__(self, id: int) -> None:
        self.id = id


class Status:
    color: str
    orderindex: int
    status: str
    type: str

    def __init__(self, color: str, orderindex: int, status: str, type: str) -> None:
        self.color = color
        self.orderindex = orderindex
        self.status = status
        self.type = type


class Task:
    archived: bool
    assignees: List[Creator]
    checklists: List[Any]
    creator: Creator
    custom_fields: List[CustomField]
    custom_id: None
    date_closed: None
    date_created: str
    date_updated: str
    dependencies: List[Any]
    description: str
    due_date: str
    folder: Folder
    id: str
    linked_tasks: List[Any]
    list: Folder
    name: str
    orderindex: str
    parent: str
    permission_level: str
    points: int
    priority: None
    project: Folder
    space: Space
    start_date: str
    status: Status
    tags: List[Any]
    team_id: int
    text_content: str
    time_estimate: None
    time_spent: int
    url: str
    watchers: List[Any]

    def __init__(self, archived: bool, assignees: List[Creator], checklists: List[Any], creator: Creator, custom_fields: List[CustomField], custom_id: None, date_closed: None, date_created: str, date_updated: str, dependencies: List[Any], description: str, due_date: str, folder: Folder, id: str, linked_tasks: List[Any], list: Folder, name: str, orderindex: str, parent: str, permission_level: str, points: int, priority: None, project: Folder, space: Space, start_date: str, status: Status, tags: List[Any], team_id: int, text_content: str, time_estimate: None, time_spent: int, url: str, watchers: List[Any]) -> None:
        self.archived = archived
        self.assignees = assignees
        self.checklists = checklists
        self.creator = creator
        self.custom_fields = custom_fields
        self.custom_id = custom_id
        self.date_closed = date_closed
        self.date_created = date_created
        self.date_updated = date_updated
        self.dependencies = dependencies
        self.description = description
        self.due_date = due_date
        self.folder = folder
        self.id = id
        self.linked_tasks = linked_tasks
        self.list = list
        self.name = name
        self.orderindex = orderindex
        self.parent = parent
        self.permission_level = permission_level
        self.points = points
        self.priority = priority
        self.project = project
        self.space = space
        self.start_date = start_date
        self.status = status
        self.tags = tags
        self.team_id = team_id
        self.text_content = text_content
        self.time_estimate = time_estimate
        self.time_spent = time_spent
        self.url = url
        self.watchers = watchers
