from collections import OrderedDict, namedtuple
from datetime import datetime
from decimal import Decimal
from typing import Any, Callable, Dict, Iterator, List, Optional, Set, Tuple, Type, Union
from uuid import UUID

from django.db.backends.sqlite3.base import DatabaseWrapper
from django.db.models.base import Model, ModelState
from django.db.models.expressions import Combinable, Expression, SQLiteNumericMixin
from django.db.models.fields import Field, TextField
from django.db.models.fields.mixins import FieldCacheMixin
from django.db.models.fields.related_lookups import MultiColSource
from django.db.models.fields.reverse_related import ForeignObjectRel, ManyToOneRel
from django.db.models.lookups import FieldGetDbPrepValueMixin, IntegerLessThan, Lookup, Transform
from django.db.models.options import Options
from django.db.models.query import QuerySet
from django.db.models.query_utils import FilteredRelation, PathInfo, Q
from django.db.models.sql.compiler import SQLCompiler
from django.db.models.sql.datastructures import BaseTable, Join
from django.db.models.sql.where import WhereNode

JoinInfo = namedtuple("JoinInfo", ["final_field", "targets", "opts", "joins", "path", "transform_function"])

class RawQuery:
    high_mark: None
    low_mark: int
    params: Union[Dict[str, str], List[datetime.datetime], List[decimal.Decimal], List[str], Set[str], Tuple] = ...
    sql: str = ...
    using: str = ...
    cursor: Optional[django.db.backends.utils.CursorWrapper] = ...
    extra_select: Dict[Any, Any] = ...
    annotation_select: Dict[Any, Any] = ...
    def __init__(
        self,
        sql: str,
        using: str,
        params: Optional[Union[Dict[str, str], List[datetime], List[Decimal], List[str], Set[str], Tuple[int]]] = ...,
    ) -> None: ...
    def chain(self, using: str) -> RawQuery: ...
    def clone(self, using: str) -> RawQuery: ...
    def get_columns(self) -> List[str]: ...
    def __iter__(self): ...
    @property
    def params_type(self) -> Type[Union[dict, tuple]]: ...

class Query:
    base_table: str
    related_ids: None
    related_updates: Dict[Type[django.db.models.base.Model], List[Tuple[django.db.models.fields.Field, None, Union[int, str]]]]
    values: List[
        Tuple[django.db.models.fields.Field, Optional[Type[django.db.models.base.Model]], django.db.models.aggregates.Max]
    ]
    alias_prefix: str = ...
    subq_aliases: frozenset = ...
    compiler: str = ...
    model: Optional[Type[django.db.models.base.Model]] = ...
    alias_refcount: Dict[str, int] = ...
    alias_map: collections.OrderedDict = ...
    external_aliases: Set[str] = ...
    table_map: Dict[str, List[str]] = ...
    default_cols: bool = ...
    default_ordering: bool = ...
    standard_ordering: bool = ...
    used_aliases: Set[str] = ...
    filter_is_sticky: bool = ...
    subquery: bool = ...
    select: Union[List[django.db.models.expressions.Col], Tuple] = ...
    where: django.db.models.sql.where.WhereNode = ...
    where_class: Type[django.db.models.sql.where.WhereNode] = ...
    group_by: Optional[Union[Tuple, bool]] = ...
    order_by: Tuple = ...
    distinct: bool = ...
    distinct_fields: Tuple = ...
    select_for_update: bool = ...
    select_for_update_nowait: bool = ...
    select_for_update_skip_locked: bool = ...
    select_for_update_of: Tuple = ...
    select_related: Union[Dict[str, Dict[str, Dict[str, Dict[str, Dict[str, Dict[str, Dict[str, Dict[Any, Any]]]]]]]], bool] = ...
    max_depth: int = ...
    values_select: Tuple = ...
    annotation_select_mask: Optional[Set[str]] = ...
    combinator: Optional[str] = ...
    combinator_all: bool = ...
    combined_queries: Tuple = ...
    extra_select_mask: Optional[Set[str]] = ...
    extra_tables: Tuple = ...
    extra_order_by: Union[List[str], Tuple] = ...
    deferred_loading: Tuple[Union[Set[str], frozenset], bool] = ...
    explain_query: bool = ...
    explain_format: Optional[str] = ...
    explain_options: Dict[str, int] = ...
    def __init__(self, model: Optional[Type[Model]], where: Type[WhereNode] = ...) -> None: ...
    @property
    def extra(self) -> OrderedDict: ...
    @property
    def annotations(self) -> OrderedDict: ...
    @property
    def has_select_fields(self) -> bool: ...
    def base_table(self) -> str: ...
    def sql_with_params(self) -> Tuple[str, Tuple]: ...
    def __deepcopy__(
        self,
        memo: Dict[
            int,
            Union[
                Dict[str, Union[ModelState, int, str]], List[Union[Dict[str, Union[bool, str]], ModelState]], Model, ModelState
            ],
        ],
    ) -> Query: ...
    def get_compiler(self, using: Optional[str] = ..., connection: Optional[DatabaseWrapper] = ...) -> SQLCompiler: ...
    def get_meta(self) -> Options: ...
    def clone(self) -> Query: ...
    def chain(self, klass: Optional[Type[Query]] = ...) -> Query: ...
    def relabeled_clone(self, change_map: Union[Dict[Any, Any], OrderedDict]) -> Query: ...
    def rewrite_cols(
        self, annotation: Union[Expression, FieldGetDbPrepValueMixin, WhereNode], col_cnt: int
    ) -> Tuple[Union[Expression, IntegerLessThan], int]: ...
    def get_aggregation(
        self, using: str, added_aggregate_names: Union[Dict[str, SQLiteNumericMixin], List[str]]
    ) -> Dict[str, Optional[Union[datetime, Decimal, float]]]: ...
    def get_count(self, using: str) -> int: ...
    def has_filters(self) -> WhereNode: ...
    def has_results(self, using: str) -> bool: ...
    def explain(self, using: str, format: Optional[str] = ..., **options: Any) -> str: ...
    def combine(self, rhs: Query, connector: str) -> None: ...
    def deferred_to_data(self, target: Dict[Any, Any], callback: Callable) -> None: ...
    def table_alias(
        self, table_name: str, create: bool = ..., filtered_relation: Optional[FilteredRelation] = ...
    ) -> Tuple[str, bool]: ...
    def ref_alias(self, alias: str) -> None: ...
    def unref_alias(self, alias: str, amount: int = ...) -> None: ...
    def promote_joins(self, aliases: Set[str]) -> None: ...
    def demote_joins(self, aliases: Set[str]) -> None: ...
    def reset_refcounts(self, to_counts: Dict[str, int]) -> None: ...
    def change_aliases(self, change_map: Union[Dict[Any, Any], OrderedDict]) -> None: ...
    def bump_prefix(self, outer_query: Query) -> None: ...
    def get_initial_alias(self) -> str: ...
    def count_active_tables(self) -> int: ...
    def join(
        self, join: Union[BaseTable, Join], reuse: Optional[Set[str]] = ..., reuse_with_filtered_relation: bool = ...
    ) -> str: ...
    def join_parent_model(
        self, opts: Options, model: Optional[Type[Model]], alias: str, seen: Dict[Optional[Type[Model]], str]
    ) -> str: ...
    def add_annotation(self, annotation: Combinable, alias: str, is_summary: bool = ...) -> None: ...
    def resolve_expression(self, query: Query, *args: Any, **kwargs: Any) -> Query: ...
    def as_sql(self, compiler: SQLCompiler, connection: DatabaseWrapper) -> Tuple[str, Tuple]: ...
    def resolve_lookup_value(self, value: Any, can_reuse: Optional[Set[str]], allow_joins: bool) -> Any: ...
    def solve_lookup_type(self, lookup: str) -> Union[Tuple[List[str], List[str], bool], Tuple[List[str], Tuple, Expression]]: ...
    def check_query_object_type(self, value: Union[Model, int, str, UUID], opts: Options, field: FieldCacheMixin) -> None: ...
    def check_related_objects(self, field: Union[Field, reverse_related.ForeignObjectRel], value: Any, opts: Options) -> None: ...
    def build_lookup(self, lookups: List[str], lhs: Union[Expression, TextField, MultiColSource], rhs: Any) -> Lookup: ...
    def try_transform(self, lhs: Expression, name: str) -> Transform: ...
    def build_filter(
        self,
        filter_expr: Union[Dict[str, str], Tuple[str, Tuple[int, int]]],
        branch_negated: bool = ...,
        current_negated: bool = ...,
        can_reuse: Optional[Set[str]] = ...,
        allow_joins: bool = ...,
        split_subq: bool = ...,
        reuse_with_filtered_relation: bool = ...,
    ) -> Tuple[WhereNode, List[Any]]: ...
    def add_filter(self, filter_clause: Tuple[str, Union[List[int], List[str]]]) -> None: ...
    def add_q(self, q_object: Q) -> None: ...
    def build_filtered_relation_q(
        self, q_object: Q, reuse: Set[str], branch_negated: bool = ..., current_negated: bool = ...
    ) -> WhereNode: ...
    def add_filtered_relation(self, filtered_relation: FilteredRelation, alias: str) -> None: ...
    def names_to_path(
        self, names: List[str], opts: Options, allow_many: bool = ..., fail_on_missing: bool = ...
    ) -> Tuple[List[PathInfo], Union[Field, reverse_related.ForeignObjectRel], Tuple[Field], List[str]]: ...
    def setup_joins(
        self,
        names: List[str],
        opts: Options,
        alias: str,
        can_reuse: Optional[Set[str]] = ...,
        allow_many: bool = ...,
        reuse_with_filtered_relation: bool = ...,
    ) -> JoinInfo: ...
    def trim_joins(
        self, targets: Tuple[Field], joins: List[str], path: List[PathInfo]
    ) -> Tuple[Tuple[Field], str, List[str]]: ...
    def resolve_ref(
        self, name: str, allow_joins: bool = ..., reuse: Optional[Set[str]] = ..., summarize: bool = ...
    ) -> Expression: ...
    def split_exclude(
        self,
        filter_expr: Tuple[str, Union[QuerySet, int]],
        can_reuse: Set[str],
        names_with_path: List[Tuple[str, List[PathInfo]]],
    ) -> Tuple[WhereNode, Tuple]: ...
    def set_empty(self) -> None: ...
    def is_empty(self) -> bool: ...
    high_mark: Optional[int] = ...
    low_mark: int = ...
    def set_limits(self, low: Optional[int] = ..., high: Optional[int] = ...) -> None: ...
    def clear_limits(self) -> None: ...
    def has_limit_one(self) -> bool: ...
    def can_filter(self) -> bool: ...
    def clear_select_clause(self) -> None: ...
    def clear_select_fields(self) -> None: ...
    def set_select(self, cols: List[Expression]) -> None: ...
    def add_distinct_fields(self, *field_names: Any) -> None: ...
    def add_fields(self, field_names: Union[Iterator[Any], List[str]], allow_m2m: bool = ...) -> None: ...
    def add_ordering(self, *ordering: Any) -> None: ...
    def clear_ordering(self, force_empty: bool) -> None: ...
    def set_group_by(self) -> None: ...
    def add_select_related(self, fields: Tuple[str]) -> None: ...
    def add_extra(
        self,
        select: Optional[Union[Dict[str, int], Dict[str, str], OrderedDict]],
        select_params: Optional[Union[List[int], List[str], Tuple[int]]],
        where: Optional[List[str]],
        params: Optional[List[str]],
        tables: Optional[List[str]],
        order_by: Optional[Union[List[str], Tuple[str]]],
    ) -> None: ...
    def clear_deferred_loading(self) -> None: ...
    def add_deferred_loading(self, field_names: Tuple[str]) -> None: ...
    def add_immediate_loading(self, field_names: Tuple[str]) -> None: ...
    def get_loaded_field_names(self) -> Dict[Type[Model], Set[str]]: ...
    def get_loaded_field_names_cb(
        self,
        target: Dict[Type[Model], Set[str]],
        model: Type[Model],
        fields: Union[Set[Field], Set[reverse_related.ManyToOneRel]],
    ) -> None: ...
    def set_annotation_mask(self, names: Optional[Union[List[str], Set[str], Tuple]]) -> None: ...
    def append_annotation_mask(self, names: List[str]) -> None: ...
    def set_extra_mask(self, names: Union[List[str], Tuple]) -> None: ...
    def set_values(self, fields: Union[List[str], Tuple]) -> None: ...
    @property
    def annotation_select(self) -> Union[Dict[Any, Any], OrderedDict]: ...
    @property
    def extra_select(self) -> Union[Dict[Any, Any], OrderedDict]: ...
    def trim_start(self, names_with_path: List[Tuple[str, List[PathInfo]]]) -> Tuple[str, bool]: ...
    def is_nullable(self, field: Field) -> bool: ...

class JoinPromoter:
    connector: str = ...
    negated: bool = ...
    effective_connector: str = ...
    num_children: int = ...
    votes: collections.Counter = ...
    def __init__(self, connector: str, num_children: int, negated: bool) -> None: ...
    def add_votes(self, votes: Union[Iterator[Any], List[Any], Set[str], Tuple]) -> None: ...
    def update_join_types(self, query: Query) -> Set[str]: ...
