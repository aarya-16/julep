# generated by datamodel-codegen:
#   filename:  openapi-1.0.0.yaml

from __future__ import annotations

from typing import Annotated, Literal
from uuid import UUID

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field, RootModel

from .Tools import (
    ChosenBash20241022,
    ChosenComputer20241022,
    ChosenFunctionCall,
    ChosenTextEditor20241022,
    Tool,
    ToolResponse,
)


class BaseEntry(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    role: Literal[
        "user",
        "assistant",
        "system",
        "function",
        "function_response",
        "function_call",
        "auto",
    ]
    """
    ChatML role (system|assistant|user|function_call|function|function_response|auto)
    """
    name: str | None = None
    content: (
        list[Content | ContentModel]
        | Tool
        | ChosenFunctionCall
        | ChosenComputer20241022
        | ChosenTextEditor20241022
        | ChosenBash20241022
        | str
        | ToolResponse
        | list[
            list[Content | ContentModel]
            | Tool
            | ChosenFunctionCall
            | ChosenComputer20241022
            | ChosenTextEditor20241022
            | ChosenBash20241022
            | str
            | ToolResponse
        ]
    )
    source: Literal[
        "api_request", "api_response", "tool_response", "internal", "summarizer", "meta"
    ]
    tokenizer: str
    token_count: int
    timestamp: Annotated[float, Field(ge=0.0)]
    """
    This is the time that this event refers to.
    """


class ChatMLRole(
    RootModel[
        Literal[
            "user",
            "assistant",
            "system",
            "function",
            "function_response",
            "function_call",
            "auto",
        ]
    ]
):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    root: Literal[
        "user",
        "assistant",
        "system",
        "function",
        "function_response",
        "function_call",
        "auto",
    ]
    """
    ChatML role (system|assistant|user|function_call|function|function_response|auto)
    """


class Content(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    text: str
    type: Literal["text"] = "text"
    """
    The type (fixed to 'text')
    """


class ContentModel(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    image_url: ImageUrl
    """
    The image URL
    """
    type: Literal["image_url"] = "image_url"
    """
    The type (fixed to 'image_url')
    """


class Entry(BaseEntry):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    created_at: Annotated[AwareDatetime, Field(json_schema_extra={"readOnly": True})]
    """
    When this resource was created as UTC date-time
    """
    id: Annotated[UUID, Field(json_schema_extra={"readOnly": True})]


class History(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    entries: list[Entry]
    relations: list[Relation]
    session_id: Annotated[UUID, Field(json_schema_extra={"readOnly": True})]
    created_at: Annotated[AwareDatetime, Field(json_schema_extra={"readOnly": True})]
    """
    When this resource was created as UTC date-time
    """


class ImageDetail(RootModel[Literal["low", "high", "auto"]]):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    root: Literal["low", "high", "auto"]
    """
    Image detail level
    """


class ImageUrl(BaseModel):
    """
    The image URL
    """

    model_config = ConfigDict(
        populate_by_name=True,
    )
    url: str
    """
    Image URL or base64 data url (e.g. `data:image/jpeg;base64,<the base64 encoded image>`)
    """
    detail: Literal["low", "high", "auto"] = "auto"
    """
    The detail level of the image
    """


class Relation(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    head: UUID
    relation: str
    tail: UUID
