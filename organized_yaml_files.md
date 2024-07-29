## chart/Chart.yaml
```yaml
apiVersion: v2
description: A Helm chart for Gatekeeper
name: gatekeeper
keywords:
- open policy agent
version: 3.16.3-bb.0
home: https://github.com/open-policy-agent/gatekeeper
sources:
- https://github.com/open-policy-agent/gatekeeper.git
appVersion: v3.16.3
dependencies:
- name: gluon
  version: 0.5.0
  repository: oci://registry1.dso.mil/bigbang
annotations:
  bigbang.dev/applicationVersions: '- Gatekeeper: v3.16.3

    '
  helm.sh/images: "- name: gatekeeper\n  image: registry1.dso.mil/ironbank/opensource/openpolicyagent/gatekeeper:v3.16.3\n\
    - name: kubectl\n  image: registry1.dso.mil/ironbank/opensource/kubernetes/kubectl:v1.29.5\n\
    - name: base\n  image: registry1.dso.mil/ironbank/big-bang/base:2.1.0\n"
```

## chart/crds/assign-customresourcedefinition.yaml
```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  annotations:
    controller-gen.kubebuilder.io/version: v0.14.0
  labels:
    gatekeeper.sh/system: 'yes'
  name: assign.mutations.gatekeeper.sh
spec:
  group: mutations.gatekeeper.sh
  names:
    kind: Assign
    listKind: AssignList
    plural: assign
    singular: assign
  preserveUnknownFields: false
  scope: Cluster
  versions:
  - name: v1
    schema:
      openAPIV3Schema:
        description: Assign is the Schema for the assign API.
        properties:
          apiVersion:
            description: 'APIVersion defines the versioned schema of this representation
              of an object.

              Servers should convert recognized schemas to the latest internal value,
              and

              may reject unrecognized values.

              More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources'
            type: string
          kind:
            description: 'Kind is a string value representing the REST resource this
              object represents.

              Servers may infer this from the endpoint the client submits requests
              to.

              Cannot be updated.

              In CamelCase.

              More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds'
            type: string
          metadata:
            properties:
              name:
                maxLength: 63
                type: string
            type: object
          spec:
            description: AssignSpec defines the desired state of Assign.
            properties:
              applyTo:
                description: 'ApplyTo lists the specific groups, versions and kinds
                  a mutation will be applied to.

                  This is necessary because every mutation implies part of an object
                  schema and object

                  schemas are associated with specific GVKs.'
                items:
                  description: 'ApplyTo determines what GVKs items the mutation should
                    apply to.

                    Globs are not allowed.'
                  properties:
                    groups:
                      items:
                        type: string
                      type: array
                    kinds:
                      items:
                        type: string
                      type: array
                    versions:
                      items:
                        type: string
                      type: array
                  type: object
                type: array
              location:
                description: 'Location describes the path to be mutated, for example:
                  `spec.containers[name: main]`.'
                type: string
              match:
                description: 'Match allows the user to limit which resources get mutated.

                  Individual match criteria are AND-ed together. An undefined

                  match criteria matches everything.'
                properties:
                  excludedNamespaces:
                    description: 'ExcludedNamespaces is a list of namespace names.
                      If defined, a

                      constraint only applies to resources not in a listed namespace.

                      ExcludedNamespaces also supports a prefix or suffix based glob.  For
                      example,

                      `excludedNamespaces: [kube-*]` matches both `kube-system` and

                      `kube-public`, and `excludedNamespaces: [*-system]` matches
                      both `kube-system` and

                      `gatekeeper-system`.'
                    items:
                      description: 'A string that supports globbing at its front and
                        end. Ex: "kube-*" will match "kube-system" or

                        "kube-public", "*-system" will match "kube-system" or "gatekeeper-system",
                        "*system*" will

                        match "system-kube" or "kube-system".  The asterisk is required
                        for wildcard matching.'
                      pattern: ^\*?[-:a-z0-9]*\*?$
                      type: string
                    type: array
                  kinds:
                    items:
                      description: 'Kinds accepts a list of objects with apiGroups
                        and kinds fields

                        that list the groups/kinds of objects to which the mutation
                        will apply.

                        If multiple groups/kinds objects are specified,

                        only one match is needed for the resource to be in scope.'
                      properties:
                        apiGroups:
                          description: 'APIGroups is the API groups the resources
                            belong to. ''*'' is all groups.

                            If ''*'' is present, the length of the slice must be one.

                            Required.'
                          items:
                            type: string
                          type: array
                        kinds:
                          items:
                            type: string
                          type: array
                      type: object
                    type: array
                  labelSelector:
                    description: 'LabelSelector is the combination of two optional
                      fields: `matchLabels`

                      and `matchExpressions`.  These two fields provide different
                      methods of

                      selecting or excluding k8s objects based on the label keys and
                      values

                      included in object metadata.  All selection expressions from
                      both

                      sections are ANDed to determine if an object meets the cumulative

                      requirements of the selector.'
                    properties:
                      matchExpressions:
                        description: matchExpressions is a list of label selector
                          requirements. The requirements are ANDed.
                        items:
                          description: 'A label selector requirement is a selector
                            that contains values, a key, and an operator that

                            relates the key and values.'
                          properties:
                            key:
                              description: key is the label key that the selector
                                applies to.
                              type: string
                            operator:
                              description: 'operator represents a key''s relationship
                                to a set of values.

                                Valid operators are In, NotIn, Exists and DoesNotExist.'
                              type: string
                            values:
                              description: 'values is an array of string values. If
                                the operator is In or NotIn,

                                the values array must be non-empty. If the operator
                                is Exists or DoesNotExist,

                                the values array must be empty. This array is replaced
                                during a strategic

                                merge patch.'
                              items:
                                type: string
                              type: array
                          required:
                          - key
                          - operator
                          type: object
                        type: array
                      matchLabels:
                        additionalProperties:
                          type: string
                        description: 'matchLabels is a map of {key,value} pairs. A
                          single {key,value} in the matchLabels

                          map is equivalent to an element of matchExpressions, whose
                          key field is "key", the

                          operator is "In", and the values array contains only "value".
                          The requirements are ANDed.'
                        type: object
                    type: object
                    x-kubernetes-map-type: atomic
                  name:
                    description: 'Name is the name of an object.  If defined, it will
                      match against objects with the specified

                      name.  Name also supports a prefix or suffix glob.  For example,
                      `name: pod-*` would match

                      both `pod-a` and `pod-b`, and `name: *-pod` would match both
                      `a-pod` and `b-pod`.'
                    pattern: ^\*?[-:a-z0-9]*\*?$
                    type: string
                  namespaceSelector:
                    description: 'NamespaceSelector is a label selector against an
                      object''s containing

                      namespace or the object itself, if the object is a namespace.'
                    properties:
                      matchExpressions:
                        description: matchExpressions is a list of label selector
                          requirements. The requirements are ANDed.
                        items:
                          description: 'A label selector requirement is a selector
                            that contains values, a key, and an operator that

                            relates the key and values.'
                          properties:
                            key:
                              description: key is the label key that the selector
                                applies to.
                              type: string
                            operator:
                              description: 'operator represents a key''s relationship
                                to a set of values.

                                Valid operators are In, NotIn, Exists and DoesNotExist.'
                              type: string
                            values:
                              description: 'values is an array of string values. If
                                the operator is In or NotIn,

                                the values array must be non-empty. If the operator
                                is Exists or DoesNotExist,

                                the values array must be empty. This array is replaced
                                during a strategic

                                merge patch.'
                              items:
                                type: string
                              type: array
                          required:
                          - key
                          - operator
                          type: object
                        type: array
                      matchLabels:
                        additionalProperties:
                          type: string
                        description: 'matchLabels is a map of {key,value} pairs. A
                          single {key,value} in the matchLabels

                          map is equivalent to an element of matchExpressions, whose
                          key field is "key", the

                          operator is "In", and the values array contains only "value".
                          The requirements are ANDed.'
                        type: object
                    type: object
                    x-kubernetes-map-type: atomic
                  namespaces:
                    description: 'Namespaces is a list of namespace names. If defined,
                      a constraint only

                      applies to resources in a listed namespace.  Namespaces also
                      supports a

                      prefix or suffix based glob.  For example, `namespaces: [kube-*]`
                      matches both

                      `kube-system` and `kube-public`, and `namespaces: [*-system]`
                      matches both

                      `kube-system` and `gatekeeper-system`.'
                    items:
                      description: 'A string that supports globbing at its front and
                        end. Ex: "kube-*" will match "kube-system" or

                        "kube-public", "*-system" will match "kube-system" or "gatekeeper-system",
                        "*system*" will

                        match "system-kube" or "kube-system".  The asterisk is required
                        for wildcard matching.'
                      pattern: ^\*?[-:a-z0-9]*\*?$
                      type: string
                    type: array
                  scope:
                    description: 'Scope determines if cluster-scoped and/or namespaced-scoped
                      resources

                      are matched.  Accepts `*`, `Cluster`, or `Namespaced`. (defaults
                      to `*`)'
                    type: string
                  source:
                    description: 'Source determines whether generated or original
                      resources are matched.

                      Accepts `Generated`|`Original`|`All` (defaults to `All`). A
                      value of

                      `Generated` will only match generated resources, while `Original`
                      will only

                      match regular resources.'
                    enum:
                    - All
                    - Generated
                    - Original
                    type: string
                type: object
              parameters:
                description: Parameters define the behavior of the mutator.
                properties:
                  assign:
                    description: Assign.value holds the value to be assigned
                    properties:
                      externalData:
                        description: ExternalData describes the external data provider
                          to be used for mutation.
                        properties:
                          dataSource:
                            default: ValueAtLocation
                            description: 'DataSource specifies where to extract the
                              data that will be sent

                              to the external data provider as parameters.'
                            enum:
                            - ValueAtLocation
                            - Username
                            type: string
                          default:
                            description: 'Default specifies the default value to use
                              when the external data

                              provider returns an error and the failure policy is
                              set to "UseDefault".'
                            type: string
                          failurePolicy:
                            default: Fail
                            description: 'FailurePolicy specifies the policy to apply
                              when the external data

                              provider returns an error.'
                            enum:
                            - UseDefault
                            - Ignore
                            - Fail
                            type: string
                          provider:
                            description: Provider is the name of the external data
                              provider.
                            type: string
                        type: object
                      fromMetadata:
                        description: FromMetadata assigns a value from the specified
                          metadata field.
                        properties:
                          field:
                            description: Field specifies which metadata field provides
                              the assigned value. Valid fields are `namespace` and
                              `name`.
                            type: string
                        type: object
                      value:
                        description: Value is a constant value that will be assigned
                          to `location`
                        x-kubernetes-preserve-unknown-fields: true
                    type: object
                  pathTests:
                    items:
                      description: 'PathTest allows the user to customize how the
                        mutation works if parent

                        paths are missing. It traverses the list in order. All sub
                        paths are

                        tested against the provided condition, if the test fails,
                        the mutation is

                        not applied. All `subPath` entries must be a prefix of `location`.
                        Any

                        glob characters will take on the same value as was used to

                        expand the matching glob in `location`.



                        Available Tests:

                        * MustExist    - the path must exist or do not mutate

                        * MustNotExist - the path must not exist or do not mutate.'
                      properties:
                        condition:
                          description: Condition describes whether the path either
                            MustExist or MustNotExist in the original object
                          enum:
                          - MustExist
                          - MustNotExist
                          type: string
                        subPath:
                          type: string
                      type: object
                    type: array
                type: object
            type: object
          status:
            description: AssignStatus defines the observed state of Assign.
            properties:
              byPod:
                items:
                  description: MutatorPodStatusStatus defines the observed state of
                    MutatorPodStatus.
                  properties:
                    enforced:
                      type: boolean
                    errors:
                      items:
                        description: MutatorError represents a single error caught
                          while adding a mutator to a system.
                        properties:
                          message:
                            type: string
                          type:
                            description: 'Type indicates a specific class of error
                              for use by controller code.

                              If not present, the error should be treated as not matching
                              any known type.'
                            type: string
                        required:
                        - message
                        type: object
                      type: array
                    id:
                      type: string
                    mutatorUID:
                      description: 'Storing the mutator UID allows us to detect drift,
                        such as

                        when a mutator has been recreated after its CRD was deleted

                        out from under it, interrupting the watch'
                      type: string
                    observedGeneration:
                      format: int64
                      type: integer
                    operations:
                      items:
                        type: string
                      type: array
                  type: object
                type: array
            type: object
        type: object
    served: true
    storage: true
    subresources:
      status: {}
  - name: v1alpha1
    schema:
      openAPIV3Schema:
        description: Assign is the Schema for the assign API.
        properties:
          apiVersion:
            description: 'APIVersion defines the versioned schema of this representation
              of an object.

              Servers should convert recognized schemas to the latest internal value,
              and

              may reject unrecognized values.

              More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources'
            type: string
          kind:
            description: 'Kind is a string value representing the REST resource this
              object represents.

              Servers may infer this from the endpoint the client submits requests
              to.

              Cannot be updated.

              In CamelCase.

              More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds'
            type: string
          metadata:
            type: object
          spec:
            description: AssignSpec defines the desired state of Assign.
            properties:
              applyTo:
                description: 'ApplyTo lists the specific groups, versions and kinds
                  a mutation will be applied to.

                  This is necessary because every mutation implies part of an object
                  schema and object

                  schemas are associated with specific GVKs.'
                items:
                  description: 'ApplyTo determines what GVKs items the mutation should
                    apply to.

                    Globs are not allowed.'
                  properties:
                    groups:
                      items:
                        type: string
                      type: array
                    kinds:
                      items:
                        type: string
                      type: array
                    versions:
                      items:
                        type: string
                      type: array
                  type: object
                type: array
              location:
                description: 'Location describes the path to be mutated, for example:
                  `spec.containers[name: main]`.'
                type: string
              match:
                description: 'Match allows the user to limit which resources get mutated.

                  Individual match criteria are AND-ed together. An undefined

                  match criteria matches everything.'
                properties:
                  excludedNamespaces:
                    description: 'ExcludedNamespaces is a list of namespace names.
                      If defined, a

                      constraint only applies to resources not in a listed namespace.

                      ExcludedNamespaces also supports a prefix or suffix based glob.  For
                      example,

                      `excludedNamespaces: [kube-*]` matches both `kube-system` and

                      `kube-public`, and `excludedNamespaces: [*-system]` matches
                      both `kube-system` and

                      `gatekeeper-system`.'
                    items:
                      description: 'A string that supports globbing at its front and
                        end. Ex: "kube-*" will match "kube-system" or

                        "kube-public", "*-system" will match "kube-system" or "gatekeeper-system",
                        "*system*" will

                        match "system-kube" or "kube-system".  The asterisk is required
                        for wildcard matching.'
                      pattern: ^\*?[-:a-z0-9]*\*?$
                      type: string
                    type: array
                  kinds:
                    items:
                      description: 'Kinds accepts a list of objects with apiGroups
                        and kinds fields

                        that list the groups/kinds of objects to which the mutation
                        will apply.

                        If multiple groups/kinds objects are specified,

                        only one match is needed for the resource to be in scope.'
                      properties:
                        apiGroups:
                          description: 'APIGroups is the API groups the resources
                            belong to. ''*'' is all groups.

                            If ''*'' is present, the length of the slice must be one.

                            Required.'
                          items:
                            type: string
                          type: array
                        kinds:
                          items:
                            type: string
                          type: array
                      type: object
                    type: array
                  labelSelector:
                    description: 'LabelSelector is the combination of two optional
                      fields: `matchLabels`

                      and `matchExpressions`.  These two fields provide different
                      methods of

                      selecting or excluding k8s objects based on the label keys and
                      values

                      included in object metadata.  All selection expressions from
                      both

                      sections are ANDed to determine if an object meets the cumulative

                      requirements of the selector.'
                    properties:
                      matchExpressions:
                        description: matchExpressions is a list of label selector
                          requirements. The requirements are ANDed.
                        items:
                          description: 'A label selector requirement is a selector
                            that contains values, a key, and an operator that

                            relates the key and values.'
                          properties:
                            key:
                              description: key is the label key that the selector
                                applies to.
                              type: string
                            operator:
                              description: 'operator represents a key''s relationship
                                to a set of values.

                                Valid operators are In, NotIn, Exists and DoesNotExist.'
                              type: string
                            values:
                              description: 'values is an array of string values. If
                                the operator is In or NotIn,

                                the values array must be non-empty. If the operator
                                is Exists or DoesNotExist,

                                the values array must be empty. This array is replaced
                                during a strategic

                                merge patch.'
                              items:
                                type: string
                              type: array
                          required:
                          - key
                          - operator
                          type: object
                        type: array
                      matchLabels:
                        additionalProperties:
                          type: string
                        description: 'matchLabels is a map of {key,value} pairs. A
                          single {key,value} in the matchLabels

                          map is equivalent to an element of matchExpressions, whose
                          key field is "key", the

                          operator is "In", and the values array contains only "value".
                          The requirements are ANDed.'
                        type: object
                    type: object
                    x-kubernetes-map-type: atomic
                  name:
                    description: 'Name is the name of an object.  If defined, it will
                      match against objects with the specified

                      name.  Name also supports a prefix or suffix glob.  For example,
                      `name: pod-*` would match

                      both `pod-a` and `pod-b`, and `name: *-pod` would match both
                      `a-pod` and `b-pod`.'
                    pattern: ^\*?[-:a-z0-9]*\*?$
                    type: string
                  namespaceSelector:
                    description: 'NamespaceSelector is a label selector against an
                      object''s containing

                      namespace or the object itself, if the object is a namespace.'
                    properties:
                      matchExpressions:
                        description: matchExpressions is a list of label selector
                          requirements. The requirements are ANDed.
                        items:
                          description: 'A label selector requirement is a selector
                            that contains values, a key, and an operator that

                            relates the key and values.'
                          properties:
                            key:
                              description: key is the label key that the selector
                                applies to.
                              type: string
                            operator:
                              description: 'operator represents a key''s relationship
                                to a set of values.

                                Valid operators are In, NotIn, Exists and DoesNotExist.'
                              type: string
                            values:
                              description: 'values is an array of string values. If
                                the operator is In or NotIn,

                                the values array must be non-empty. If the operator
                                is Exists or DoesNotExist,

                                the values array must be empty. This array is replaced
                                during a strategic

                                merge patch.'
                              items:
                                type: string
                              type: array
                          required:
                          - key
                          - operator
                          type: object
                        type: array
                      matchLabels:
                        additionalProperties:
                          type: string
                        description: 'matchLabels is a map of {key,value} pairs. A
                          single {key,value} in the matchLabels

                          map is equivalent to an element of matchExpressions, whose
                          key field is "key", the

                          operator is "In", and the values array contains only "value".
                          The requirements are ANDed.'
                        type: object
                    type: object
                    x-kubernetes-map-type: atomic
                  namespaces:
                    description: 'Namespaces is a list of namespace names. If defined,
                      a constraint only

                      applies to resources in a listed namespace.  Namespaces also
                      supports a

                      prefix or suffix based glob.  For example, `namespaces: [kube-*]`
                      matches both

                      `kube-system` and `kube-public`, and `namespaces: [*-system]`
                      matches both

                      `kube-system` and `gatekeeper-system`.'
                    items:
                      description: 'A string that supports globbing at its front and
                        end. Ex: "kube-*" will match "kube-system" or

                        "kube-public", "*-system" will match "kube-system" or "gatekeeper-system",
                        "*system*" will

                        match "system-kube" or "kube-system".  The asterisk is required
                        for wildcard matching.'
                      pattern: ^\*?[-:a-z0-9]*\*?$
                      type: string
                    type: array
                  scope:
                    description: 'Scope determines if cluster-scoped and/or namespaced-scoped
                      resources

                      are matched.  Accepts `*`, `Cluster`, or `Namespaced`. (defaults
                      to `*`)'
                    type: string
                  source:
                    description: 'Source determines whether generated or original
                      resources are matched.

                      Accepts `Generated`|`Original`|`All` (defaults to `All`). A
                      value of

                      `Generated` will only match generated resources, while `Original`
                      will only

                      match regular resources.'
                    enum:
                    - All
                    - Generated
                    - Original
                    type: string
                type: object
              parameters:
                description: Parameters define the behavior of the mutator.
                properties:
                  assign:
                    description: Assign.value holds the value to be assigned
                    properties:
                      externalData:
                        description: ExternalData describes the external data provider
                          to be used for mutation.
                        properties:
                          dataSource:
                            default: ValueAtLocation
                            description: 'DataSource specifies where to extract the
                              data that will be sent

                              to the external data provider as parameters.'
                            enum:
                            - ValueAtLocation
                            - Username
                            type: string
                          default:
                            description: 'Default specifies the default value to use
                              when the external data

                              provider returns an error and the failure policy is
                              set to "UseDefault".'
                            type: string
                          failurePolicy:
                            default: Fail
                            description: 'FailurePolicy specifies the policy to apply
                              when the external data

                              provider returns an error.'
                            enum:
                            - UseDefault
                            - Ignore
                            - Fail
                            type: string
                          provider:
                            description: Provider is the name of the external data
                              provider.
                            type: string
                        type: object
                      fromMetadata:
                        description: FromMetadata assigns a value from the specified
                          metadata field.
                        properties:
                          field:
                            description: Field specifies which metadata field provides
                              the assigned value. Valid fields are `namespace` and
                              `name`.
                            type: string
                        type: object
                      value:
                        description: Value is a constant value that will be assigned
                          to `location`
                        x-kubernetes-preserve-unknown-fields: true
                    type: object
                  pathTests:
                    items:
                      description: 'PathTest allows the user to customize how the
                        mutation works if parent

                        paths are missing. It traverses the list in order. All sub
                        paths are

                        tested against the provided condition, if the test fails,
                        the mutation is

                        not applied. All `subPath` entries must be a prefix of `location`.
                        Any

                        glob characters will take on the same value as was used to

                        expand the matching glob in `location`.



                        Available Tests:

                        * MustExist    - the path must exist or do not mutate

                        * MustNotExist - the path must not exist or do not mutate.'
                      properties:
                        condition:
                          description: Condition describes whether the path either
                            MustExist or MustNotExist in the original object
                          enum:
                          - MustExist
                          - MustNotExist
                          type: string
                        subPath:
                          type: string
                      type: object
                    type: array
                type: object
            type: object
          status:
            description: AssignStatus defines the observed state of Assign.
            properties:
              byPod:
                items:
                  description: MutatorPodStatusStatus defines the observed state of
                    MutatorPodStatus.
                  properties:
                    enforced:
                      type: boolean
                    errors:
                      items:
                        description: MutatorError represents a single error caught
                          while adding a mutator to a system.
                        properties:
                          message:
                            type: string
                          type:
                            description: 'Type indicates a specific class of error
                              for use by controller code.

                              If not present, the error should be treated as not matching
                              any known type.'
                            type: string
                        required:
                        - message
                        type: object
                      type: array
                    id:
                      type: string
                    mutatorUID:
                      description: 'Storing the mutator UID allows us to detect drift,
                        such as

                        when a mutator has been recreated after its CRD was deleted

                        out from under it, interrupting the watch'
                      type: string
                    observedGeneration:
                      format: int64
                      type: integer
                    operations:
                      items:
                        type: string
                      type: array
                  type: object
                type: array
            type: object
        type: object
    served: true
    storage: false
    subresources:
      status: {}
  - name: v1beta1
    schema:
      openAPIV3Schema:
        description: Assign is the Schema for the assign API.
        properties:
          apiVersion:
            description: 'APIVersion defines the versioned schema of this representation
              of an object.

              Servers should convert recognized schemas to the latest internal value,
              and

              may reject unrecognized values.

              More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources'
            type: string
          kind:
            description: 'Kind is a string value representing the REST resource this
              object represents.

              Servers may infer this from the endpoint the client submits requests
              to.

              Cannot be updated.

              In CamelCase.

              More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds'
            type: string
          metadata:
            type: object
          spec:
            description: AssignSpec defines the desired state of Assign.
            properties:
              applyTo:
                description: 'ApplyTo lists the specific groups, versions and kinds
                  a mutation will be applied to.

                  This is necessary because every mutation implies part of an object
                  schema and object

                  schemas are associated with specific GVKs.'
                items:
                  description: 'ApplyTo determines what GVKs items the mutation should
                    apply to.

                    Globs are not allowed.'
                  properties:
                    groups:
                      items:
                        type: string
                      type: array
                    kinds:
                      items:
                        type: string
                      type: array
                    versions:
                      items:
                        type: string
                      type: array
                  type: object
                type: array
              location:
                description: 'Location describes the path to be mutated, for example:
                  `spec.containers[name: main]`.'
                type: string
              match:
                description: 'Match allows the user to limit which resources get mutated.

                  Individual match criteria are AND-ed together. An undefined

                  match criteria matches everything.'
                properties:
                  excludedNamespaces:
                    description: 'ExcludedNamespaces is a list of namespace names.
                      If defined, a

                      constraint only applies to resources not in a listed namespace.

                      ExcludedNamespaces also supports a prefix or suffix based glob.  For
                      example,

                      `excludedNamespaces: [kube-*]` matches both `kube-system` and

                      `kube-public`, and `excludedNamespaces: [*-system]` matches
                      both `kube-system` and

                      `gatekeeper-system`.'
                    items:
                      description: 'A string that supports globbing at its front and
                        end. Ex: "kube-*" will match "kube-system" or

                        "kube-public", "*-system" will match "kube-system" or "gatekeeper-system",
                        "*system*" will

                        match "system-kube" or "kube-system".  The asterisk is required
                        for wildcard matching.'
                      pattern: ^\*?[-:a-z0-9]*\*?$
                      type: string
                    type: array
                  kinds:
                    items:
                      description: 'Kinds accepts a list of objects with apiGroups
                        and kinds fields

                        that list the groups/kinds of objects to which the mutation
                        will apply.

                        If multiple groups/kinds objects are specified,

                        only one match is needed for the resource to be in scope.'
                      properties:
                        apiGroups:
                          description: 'APIGroups is the API groups the resources
                            belong to. ''*'' is all groups.

                            If ''*'' is present, the length of the slice must be one.

                            Required.'
                          items:
                            type: string
                          type: array
                        kinds:
                          items:
                            type: string
                          type: array
                      type: object
                    type: array
                  labelSelector:
                    description: 'LabelSelector is the combination of two optional
                      fields: `matchLabels`

                      and `matchExpressions`.  These two fields provide different
                      methods of

                      selecting or excluding k8s objects based on the label keys and
                      values

                      included in object metadata.  All selection expressions from
                      both

                      sections are ANDed to determine if an object meets the cumulative

                      requirements of the selector.'
                    properties:
                      matchExpressions:
                        description: matchExpressions is a list of label selector
                          requirements. The requirements are ANDed.
                        items:
                          description: 'A label selector requirement is a selector
                            that contains values, a key, and an operator that

                            relates the key and values.'
                          properties:
                            key:
                              description: key is the label key that the selector
                                applies to.
                              type: string
                            operator:
                              description: 'operator represents a key''s relationship
                                to a set of values.

                                Valid operators are In, NotIn, Exists and DoesNotExist.'
                              type: string
                            values:
                              description: 'values is an array of string values. If
                                the operator is In or NotIn,

                                the values array must be non-empty. If the operator
                                is Exists or DoesNotExist,

                                the values array must be empty. This array is replaced
                                during a strategic

                                merge patch.'
                              items:
                                type: string
                              type: array
                          required:
                          - key
                          - operator
                          type: object
                        type: array
                      matchLabels:
                        additionalProperties:
                          type: string
                        description: 'matchLabels is a map of {key,value} pairs. A
                          single {key,value} in the matchLabels

                          map is equivalent to an element of matchExpressions, whose
                          key field is "key", the

                          operator is "In", and the values array contains only "value".
                          The requirements are ANDed.'
                        type: object
                    type: object
                    x-kubernetes-map-type: atomic
                  name:
                    description: 'Name is the name of an object.  If defined, it will
                      match against objects with the specified

                      name.  Name also supports a prefix or suffix glob.  For example,
                      `name: pod-*` would match

                      both `pod-a` and `pod-b`, and `name: *-pod` would match both
                      `a-pod` and `b-pod`.'
                    pattern: ^\*?[-:a-z0-9]*\*?$
                    type: string
                  namespaceSelector:
                    description: 'NamespaceSelector is a label selector against an
                      object''s containing

                      namespace or the object itself, if the object is a namespace.'
                    properties:
                      matchExpressions:
                        description: matchExpressions is a list of label selector
                          requirements. The requirements are ANDed.
                        items:
                          description: 'A label selector requirement is a selector
                            that contains values, a key, and an operator that

                            relates the key and values.'
                          properties:
                            key:
                              description: key is the label key that the selector
                                applies to.
                              type: string
                            operator:
                              description: 'operator represents a key''s relationship
                                to a set of values.

                                Valid operators are In, NotIn, Exists and DoesNotExist.'
                              type: string
                            values:
                              description: 'values is an array of string values. If
                                the operator is In or NotIn,

                                the values array must be non-empty. If the operator
                                is Exists or DoesNotExist,

                                the values array must be empty. This array is replaced
                                during a strategic

                                merge patch.'
                              items:
                                type: string
                              type: array
                          required:
                          - key
                          - operator
                          type: object
                        type: array
                      matchLabels:
                        additionalProperties:
                          type: string
                        description: 'matchLabels is a map of {key,value} pairs. A
                          single {key,value} in the matchLabels

                          map is equivalent to an element of matchExpressions, whose
                          key field is "key", the

                          operator is "In", and the values array contains only "value".
                          The requirements are ANDed.'
                        type: object
                    type: object
                    x-kubernetes-map-type: atomic
                  namespaces:
                    description: 'Namespaces is a list of namespace names. If defined,
                      a constraint only

                      applies to resources in a listed namespace.  Namespaces also
                      supports a

                      prefix or suffix based glob.  For example, `namespaces: [kube-*]`
                      matches both

                      `kube-system` and `kube-public`, and `namespaces: [*-system]`
                      matches both

                      `kube-system` and `gatekeeper-system`.'
                    items:
                      description: 'A string that supports globbing at its front and
                        end. Ex: "kube-*" will match "kube-system" or

                        "kube-public", "*-system" will match "kube-system" or "gatekeeper-system",
                        "*system*" will

                        match "system-kube" or "kube-system".  The asterisk is required
                        for wildcard matching.'
                      pattern: ^\*?[-:a-z0-9]*\*?$
                      type: string
                    type: array
                  scope:
                    description: 'Scope determines if cluster-scoped and/or namespaced-scoped
                      resources

                      are matched.  Accepts `*`, `Cluster`, or `Namespaced`. (defaults
                      to `*`)'
                    type: string
                  source:
                    description: 'Source determines whether generated or original
                      resources are matched.

                      Accepts `Generated`|`Original`|`All` (defaults to `All`). A
                      value of

                      `Generated` will only match generated resources, while `Original`
                      will only

                      match regular resources.'
                    enum:
                    - All
                    - Generated
                    - Original
                    type: string
                type: object
              parameters:
                description: Parameters define the behavior of the mutator.
                properties:
                  assign:
                    description: Assign.value holds the value to be assigned
                    properties:
                      externalData:
                        description: ExternalData describes the external data provider
                          to be used for mutation.
                        properties:
                          dataSource:
                            default: ValueAtLocation
                            description: 'DataSource specifies where to extract the
                              data that will be sent

                              to the external data provider as parameters.'
                            enum:
                            - ValueAtLocation
                            - Username
                            type: string
                          default:
                            description: 'Default specifies the default value to use
                              when the external data

                              provider returns an error and the failure policy is
                              set to "UseDefault".'
                            type: string
                          failurePolicy:
                            default: Fail
                            description: 'FailurePolicy specifies the policy to apply
                              when the external data

                              provider returns an error.'
                            enum:
                            - UseDefault
                            - Ignore
                            - Fail
                            type: string
                          provider:
                            description: Provider is the name of the external data
                              provider.
                            type: string
                        type: object
                      fromMetadata:
                        description: FromMetadata assigns a value from the specified
                          metadata field.
                        properties:
                          field:
                            description: Field specifies which metadata field provides
                              the assigned value. Valid fields are `namespace` and
                              `name`.
                            type: string
                        type: object
                      value:
                        description: Value is a constant value that will be assigned
                          to `location`
                        x-kubernetes-preserve-unknown-fields: true
                    type: object
                  pathTests:
                    items:
                      description: 'PathTest allows the user to customize how the
                        mutation works if parent

                        paths are missing. It traverses the list in order. All sub
                        paths are

                        tested against the provided condition, if the test fails,
                        the mutation is

                        not applied. All `subPath` entries must be a prefix of `location`.
                        Any

                        glob characters will take on the same value as was used to

                        expand the matching glob in `location`.



                        Available Tests:

                        * MustExist    - the path must exist or do not mutate

                        * MustNotExist - the path must not exist or do not mutate.'
                      properties:
                        condition:
                          description: Condition describes whether the path either
                            MustExist or MustNotExist in the original object
                          enum:
                          - MustExist
                          - MustNotExist
                          type: string
                        subPath:
                          type: string
                      type: object
                    type: array
                type: object
            type: object
          status:
            description: AssignStatus defines the observed state of Assign.
            properties:
              byPod:
                items:
                  description: MutatorPodStatusStatus defines the observed state of
                    MutatorPodStatus.
                  properties:
                    enforced:
                      type: boolean
                    errors:
                      items:
                        description: MutatorError represents a single error caught
                          while adding a mutator to a system.
                        properties:
                          message:
                            type: string
                          type:
                            description: 'Type indicates a specific class of error
                              for use by controller code.

                              If not present, the error should be treated as not matching
                              any known type.'
                            type: string
                        required:
                        - message
                        type: object
                      type: array
                    id:
                      type: string
                    mutatorUID:
                      description: 'Storing the mutator UID allows us to detect drift,
                        such as

                        when a mutator has been recreated after its CRD was deleted

                        out from under it, interrupting the watch'
                      type: string
                    observedGeneration:
                      format: int64
                      type: integer
                    operations:
                      items:
                        type: string
                      type: array
                  type: object
                type: array
            type: object
        type: object
    served: true
    storage: false
    subresources:
      status: {}
```

## chart/crds/assignimage-customresourcedefinition.yaml
```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  annotations:
    controller-gen.kubebuilder.io/version: v0.14.0
  labels:
    gatekeeper.sh/system: 'yes'
  name: assignimage.mutations.gatekeeper.sh
spec:
  group: mutations.gatekeeper.sh
  names:
    kind: AssignImage
    listKind: AssignImageList
    plural: assignimage
    singular: assignimage
  preserveUnknownFields: false
  scope: Cluster
  versions:
  - name: v1alpha1
    schema:
      openAPIV3Schema:
        description: AssignImage is the Schema for the assignimage API.
        properties:
          apiVersion:
            description: 'APIVersion defines the versioned schema of this representation
              of an object.

              Servers should convert recognized schemas to the latest internal value,
              and

              may reject unrecognized values.

              More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources'
            type: string
          kind:
            description: 'Kind is a string value representing the REST resource this
              object represents.

              Servers may infer this from the endpoint the client submits requests
              to.

              Cannot be updated.

              In CamelCase.

              More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds'
            type: string
          metadata:
            properties:
              name:
                maxLength: 63
                type: string
            type: object
          spec:
            description: AssignImageSpec defines the desired state of AssignImage.
            properties:
              applyTo:
                description: 'ApplyTo lists the specific groups, versions and kinds
                  a mutation will be applied to.

                  This is necessary because every mutation implies part of an object
                  schema and object

                  schemas are associated with specific GVKs.'
                items:
                  description: 'ApplyTo determines what GVKs items the mutation should
                    apply to.

                    Globs are not allowed.'
                  properties:
                    groups:
                      items:
                        type: string
                      type: array
                    kinds:
                      items:
                        type: string
                      type: array
                    versions:
                      items:
                        type: string
                      type: array
                  type: object
                type: array
              location:
                description: 'Location describes the path to be mutated, for example:
                  `spec.containers[name: main].image`.'
                type: string
              match:
                description: 'Match allows the user to limit which resources get mutated.

                  Individual match criteria are AND-ed together. An undefined

                  match criteria matches everything.'
                properties:
                  excludedNamespaces:
                    description: 'ExcludedNamespaces is a list of namespace names.
                      If defined, a

                      constraint only applies to resources not in a listed namespace.

                      ExcludedNamespaces also supports a prefix or suffix based glob.  For
                      example,

                      `excludedNamespaces: [kube-*]` matches both `kube-system` and

                      `kube-public`, and `excludedNamespaces: [*-system]` matches
                      both `kube-system` and

                      `gatekeeper-system`.'
                    items:
                      description: 'A string that supports globbing at its front and
                        end. Ex: "kube-*" will match "kube-system" or

                        "kube-public", "*-system" will match "kube-system" or "gatekeeper-system",
                        "*system*" will

                        match "system-kube" or "kube-system".  The asterisk is required
                        for wildcard matching.'
                      pattern: ^\*?[-:a-z0-9]*\*?$
                      type: string
                    type: array
                  kinds:
                    items:
                      description: 'Kinds accepts a list of objects with apiGroups
                        and kinds fields

                        that list the groups/kinds of objects to which the mutation
                        will apply.

                        If multiple groups/kinds objects are specified,

                        only one match is needed for the resource to be in scope.'
                      properties:
                        apiGroups:
                          description: 'APIGroups is the API groups the resources
                            belong to. ''*'' is all groups.

                            If ''*'' is present, the length of the slice must be one.

                            Required.'
                          items:
                            type: string
                          type: array
                        kinds:
                          items:
                            type: string
                          type: array
                      type: object
                    type: array
                  labelSelector:
                    description: 'LabelSelector is the combination of two optional
                      fields: `matchLabels`

                      and `matchExpressions`.  These two fields provide different
                      methods of

                      selecting or excluding k8s objects based on the label keys and
                      values

                      included in object metadata.  All selection expressions from
                      both

                      sections are ANDed to determine if an object meets the cumulative

                      requirements of the selector.'
                    properties:
                      matchExpressions:
                        description: matchExpressions is a list of label selector
                          requirements. The requirements are ANDed.
                        items:
                          description: 'A label selector requirement is a selector
                            that contains values, a key, and an operator that

                            relates the key and values.'
                          properties:
                            key:
                              description: key is the label key that the selector
                                applies to.
                              type: string
                            operator:
                              description: 'operator represents a key''s relationship
                                to a set of values.

                                Valid operators are In, NotIn, Exists and DoesNotExist.'
                              type: string
                            values:
                              description: 'values is an array of string values. If
                                the operator is In or NotIn,

                                the values array must be non-empty. If the operator
                                is Exists or DoesNotExist,

                                the values array must be empty. This array is replaced
                                during a strategic

                                merge patch.'
                              items:
                                type: string
                              type: array
                          required:
                          - key
                          - operator
                          type: object
                        type: array
                      matchLabels:
                        additionalProperties:
                          type: string
                        description: 'matchLabels is a map of {key,value} pairs. A
                          single {key,value} in the matchLabels

                          map is equivalent to an element of matchExpressions, whose
                          key field is "key", the

                          operator is "In", and the values array contains only "value".
                          The requirements are ANDed.'
                        type: object
                    type: object
                    x-kubernetes-map-type: atomic
                  name:
                    description: 'Name is the name of an object.  If defined, it will
                      match against objects with the specified

                      name.  Name also supports a prefix or suffix glob.  For example,
                      `name: pod-*` would match

                      both `pod-a` and `pod-b`, and `name: *-pod` would match both
                      `a-pod` and `b-pod`.'
                    pattern: ^\*?[-:a-z0-9]*\*?$
                    type: string
                  namespaceSelector:
                    description: 'NamespaceSelector is a label selector against an
                      object''s containing

                      namespace or the object itself, if the object is a namespace.'
                    properties:
                      matchExpressions:
                        description: matchExpressions is a list of label selector
                          requirements. The requirements are ANDed.
                        items:
                          description: 'A label selector requirement is a selector
                            that contains values, a key, and an operator that

                            relates the key and values.'
                          properties:
                            key:
                              description: key is the label key that the selector
                                applies to.
                              type: string
                            operator:
                              description: 'operator represents a key''s relationship
                                to a set of values.

                                Valid operators are In, NotIn, Exists and DoesNotExist.'
                              type: string
                            values:
                              description: 'values is an array of string values. If
                                the operator is In or NotIn,

                                the values array must be non-empty. If the operator
                                is Exists or DoesNotExist,

                                the values array must be empty. This array is replaced
                                during a strategic

                                merge patch.'
                              items:
                                type: string
                              type: array
                          required:
                          - key
                          - operator
                          type: object
                        type: array
                      matchLabels:
                        additionalProperties:
                          type: string
                        description: 'matchLabels is a map of {key,value} pairs. A
                          single {key,value} in the matchLabels

                          map is equivalent to an element of matchExpressions, whose
                          key field is "key", the

                          operator is "In", and the values array contains only "value".
                          The requirements are ANDed.'
                        type: object
                    type: object
                    x-kubernetes-map-type: atomic
                  namespaces:
                    description: 'Namespaces is a list of namespace names. If defined,
                      a constraint only

                      applies to resources in a listed namespace.  Namespaces also
                      supports a

                      prefix or suffix based glob.  For example, `namespaces: [kube-*]`
                      matches both

                      `kube-system` and `kube-public`, and `namespaces: [*-system]`
                      matches both

                      `kube-system` and `gatekeeper-system`.'
                    items:
                      description: 'A string that supports globbing at its front and
                        end. Ex: "kube-*" will match "kube-system" or

                        "kube-public", "*-system" will match "kube-system" or "gatekeeper-system",
                        "*system*" will

                        match "system-kube" or "kube-system".  The asterisk is required
                        for wildcard matching.'
                      pattern: ^\*?[-:a-z0-9]*\*?$
                      type: string
                    type: array
                  scope:
                    description: 'Scope determines if cluster-scoped and/or namespaced-scoped
                      resources

                      are matched.  Accepts `*`, `Cluster`, or `Namespaced`. (defaults
                      to `*`)'
                    type: string
                  source:
                    description: 'Source determines whether generated or original
                      resources are matched.

                      Accepts `Generated`|`Original`|`All` (defaults to `All`). A
                      value of

                      `Generated` will only match generated resources, while `Original`
                      will only

                      match regular resources.'
                    enum:
                    - All
                    - Generated
                    - Original
                    type: string
                type: object
              parameters:
                description: Parameters define the behavior of the mutator.
                properties:
                  assignDomain:
                    description: 'AssignDomain sets the domain component on an image
                      string. The trailing

                      slash should not be included.'
                    type: string
                  assignPath:
                    description: AssignPath sets the domain component on an image
                      string.
                    type: string
                  assignTag:
                    description: 'AssignImage sets the image component on an image
                      string. It must start

                      with a `:` or `@`.'
                    type: string
                  pathTests:
                    items:
                      description: 'PathTest allows the user to customize how the
                        mutation works if parent

                        paths are missing. It traverses the list in order. All sub
                        paths are

                        tested against the provided condition, if the test fails,
                        the mutation is

                        not applied. All `subPath` entries must be a prefix of `location`.
                        Any

                        glob characters will take on the same value as was used to

                        expand the matching glob in `location`.



                        Available Tests:

                        * MustExist    - the path must exist or do not mutate

                        * MustNotExist - the path must not exist or do not mutate.'
                      properties:
                        condition:
                          description: Condition describes whether the path either
                            MustExist or MustNotExist in the original object
                          enum:
                          - MustExist
                          - MustNotExist
                          type: string
                        subPath:
                          type: string
                      type: object
                    type: array
                type: object
            type: object
          status:
            description: AssignImageStatus defines the observed state of AssignImage.
            properties:
              byPod:
                items:
                  description: MutatorPodStatusStatus defines the observed state of
                    MutatorPodStatus.
                  properties:
                    enforced:
                      type: boolean
                    errors:
                      items:
                        description: MutatorError represents a single error caught
                          while adding a mutator to a system.
                        properties:
                          message:
                            type: string
                          type:
                            description: 'Type indicates a specific class of error
                              for use by controller code.

                              If not present, the error should be treated as not matching
                              any known type.'
                            type: string
                        required:
                        - message
                        type: object
                      type: array
                    id:
                      type: string
                    mutatorUID:
                      description: 'Storing the mutator UID allows us to detect drift,
                        such as

                        when a mutator has been recreated after its CRD was deleted

                        out from under it, interrupting the watch'
                      type: string
                    observedGeneration:
                      format: int64
                      type: integer
                    operations:
                      items:
                        type: string
                      type: array
                  type: object
                type: array
            type: object
        type: object
    served: true
    storage: true
    subresources:
      status: {}
```

## chart/crds/assignmetadata-customresourcedefinition.yaml
```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  annotations:
    controller-gen.kubebuilder.io/version: v0.14.0
  labels:
    gatekeeper.sh/system: 'yes'
  name: assignmetadata.mutations.gatekeeper.sh
spec:
  group: mutations.gatekeeper.sh
  names:
    kind: AssignMetadata
    listKind: AssignMetadataList
    plural: assignmetadata
    singular: assignmetadata
  preserveUnknownFields: false
  scope: Cluster
  versions:
  - name: v1
    schema:
      openAPIV3Schema:
        description: AssignMetadata is the Schema for the assignmetadata API.
        properties:
          apiVersion:
            description: 'APIVersion defines the versioned schema of this representation
              of an object.

              Servers should convert recognized schemas to the latest internal value,
              and

              may reject unrecognized values.

              More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources'
            type: string
          kind:
            description: 'Kind is a string value representing the REST resource this
              object represents.

              Servers may infer this from the endpoint the client submits requests
              to.

              Cannot be updated.

              In CamelCase.

              More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds'
            type: string
          metadata:
            properties:
              name:
                maxLength: 63
                type: string
            type: object
          spec:
            description: AssignMetadataSpec defines the desired state of AssignMetadata.
            properties:
              location:
                type: string
              match:
                description: Match selects which objects are in scope.
                properties:
                  excludedNamespaces:
                    description: 'ExcludedNamespaces is a list of namespace names.
                      If defined, a

                      constraint only applies to resources not in a listed namespace.

                      ExcludedNamespaces also supports a prefix or suffix based glob.  For
                      example,

                      `excludedNamespaces: [kube-*]` matches both `kube-system` and

                      `kube-public`, and `excludedNamespaces: [*-system]` matches
                      both `kube-system` and

                      `gatekeeper-system`.'
                    items:
                      description: 'A string that supports globbing at its front and
                        end. Ex: "kube-*" will match "kube-system" or

                        "kube-public", "*-system" will match "kube-system" or "gatekeeper-system",
                        "*system*" will

                        match "system-kube" or "kube-system".  The asterisk is required
                        for wildcard matching.'
                      pattern: ^\*?[-:a-z0-9]*\*?$
                      type: string
                    type: array
                  kinds:
                    items:
                      description: 'Kinds accepts a list of objects with apiGroups
                        and kinds fields

                        that list the groups/kinds of objects to which the mutation
                        will apply.

                        If multiple groups/kinds objects are specified,

                        only one match is needed for the resource to be in scope.'
                      properties:
                        apiGroups:
                          description: 'APIGroups is the API groups the resources
                            belong to. ''*'' is all groups.

                            If ''*'' is present, the length of the slice must be one.

                            Required.'
                          items:
                            type: string
                          type: array
                        kinds:
                          items:
                            type: string
                          type: array
                      type: object
                    type: array
                  labelSelector:
                    description: 'LabelSelector is the combination of two optional
                      fields: `matchLabels`

                      and `matchExpressions`.  These two fields provide different
                      methods of

                      selecting or excluding k8s objects based on the label keys and
                      values

                      included in object metadata.  All selection expressions from
                      both

                      sections are ANDed to determine if an object meets the cumulative

                      requirements of the selector.'
                    properties:
                      matchExpressions:
                        description: matchExpressions is a list of label selector
                          requirements. The requirements are ANDed.
                        items:
                          description: 'A label selector requirement is a selector
                            that contains values, a key, and an operator that

                            relates the key and values.'
                          properties:
                            key:
                              description: key is the label key that the selector
                                applies to.
                              type: string
                            operator:
                              description: 'operator represents a key''s relationship
                                to a set of values.

                                Valid operators are In, NotIn, Exists and DoesNotExist.'
                              type: string
                            values:
                              description: 'values is an array of string values. If
                                the operator is In or NotIn,

                                the values array must be non-empty. If the operator
                                is Exists or DoesNotExist,

                                the values array must be empty. This array is replaced
                                during a strategic

                                merge patch.'
                              items:
                                type: string
                              type: array
                          required:
                          - key
                          - operator
                          type: object
                        type: array
                      matchLabels:
                        additionalProperties:
                          type: string
                        description: 'matchLabels is a map of {key,value} pairs. A
                          single {key,value} in the matchLabels

                          map is equivalent to an element of matchExpressions, whose
                          key field is "key", the

                          operator is "In", and the values array contains only "value".
                          The requirements are ANDed.'
                        type: object
                    type: object
                    x-kubernetes-map-type: atomic
                  name:
                    description: 'Name is the name of an object.  If defined, it will
                      match against objects with the specified

                      name.  Name also supports a prefix or suffix glob.  For example,
                      `name: pod-*` would match

                      both `pod-a` and `pod-b`, and `name: *-pod` would match both
                      `a-pod` and `b-pod`.'
                    pattern: ^\*?[-:a-z0-9]*\*?$
                    type: string
                  namespaceSelector:
                    description: 'NamespaceSelector is a label selector against an
                      object''s containing

                      namespace or the object itself, if the object is a namespace.'
                    properties:
                      matchExpressions:
                        description: matchExpressions is a list of label selector
                          requirements. The requirements are ANDed.
                        items:
                          description: 'A label selector requirement is a selector
                            that contains values, a key, and an operator that

                            relates the key and values.'
                          properties:
                            key:
                              description: key is the label key that the selector
                                applies to.
                              type: string
                            operator:
                              description: 'operator represents a key''s relationship
                                to a set of values.

                                Valid operators are In, NotIn, Exists and DoesNotExist.'
                              type: string
                            values:
                              description: 'values is an array of string values. If
                                the operator is In or NotIn,

                                the values array must be non-empty. If the operator
                                is Exists or DoesNotExist,

                                the values array must be empty. This array is replaced
                                during a strategic

                                merge patch.'
                              items:
                                type: string
                              type: array
                          required:
                          - key
                          - operator
                          type: object
                        type: array
                      matchLabels:
                        additionalProperties:
                          type: string
                        description: 'matchLabels is a map of {key,value} pairs. A
                          single {key,value} in the matchLabels

                          map is equivalent to an element of matchExpressions, whose
                          key field is "key", the

                          operator is "In", and the values array contains only "value".
                          The requirements are ANDed.'
                        type: object
                    type: object
                    x-kubernetes-map-type: atomic
                  namespaces:
                    description: 'Namespaces is a list of namespace names. If defined,
                      a constraint only

                      applies to resources in a listed namespace.  Namespaces also
                      supports a

                      prefix or suffix based glob.  For example, `namespaces: [kube-*]`
                      matches both

                      `kube-system` and `kube-public`, and `namespaces: [*-system]`
                      matches both

                      `kube-system` and `gatekeeper-system`.'
                    items:
                      description: 'A string that supports globbing at its front and
                        end. Ex: "kube-*" will match "kube-system" or

                        "kube-public", "*-system" will match "kube-system" or "gatekeeper-system",
                        "*system*" will

                        match "system-kube" or "kube-system".  The asterisk is required
                        for wildcard matching.'
                      pattern: ^\*?[-:a-z0-9]*\*?$
                      type: string
                    type: array
                  scope:
                    description: 'Scope determines if cluster-scoped and/or namespaced-scoped
                      resources

                      are matched.  Accepts `*`, `Cluster`, or `Namespaced`. (defaults
                      to `*`)'
                    type: string
                  source:
                    description: 'Source determines whether generated or original
                      resources are matched.

                      Accepts `Generated`|`Original`|`All` (defaults to `All`). A
                      value of

                      `Generated` will only match generated resources, while `Original`
                      will only

                      match regular resources.'
                    enum:
                    - All
                    - Generated
                    - Original
                    type: string
                type: object
              parameters:
                properties:
                  assign:
                    description: Assign.value holds the value to be assigned
                    properties:
                      externalData:
                        description: ExternalData describes the external data provider
                          to be used for mutation.
                        properties:
                          dataSource:
                            default: ValueAtLocation
                            description: 'DataSource specifies where to extract the
                              data that will be sent

                              to the external data provider as parameters.'
                            enum:
                            - ValueAtLocation
                            - Username
                            type: string
                          default:
                            description: 'Default specifies the default value to use
                              when the external data

                              provider returns an error and the failure policy is
                              set to "UseDefault".'
                            type: string
                          failurePolicy:
                            default: Fail
                            description: 'FailurePolicy specifies the policy to apply
                              when the external data

                              provider returns an error.'
                            enum:
                            - UseDefault
                            - Ignore
                            - Fail
                            type: string
                          provider:
                            description: Provider is the name of the external data
                              provider.
                            type: string
                        type: object
                      fromMetadata:
                        description: FromMetadata assigns a value from the specified
                          metadata field.
                        properties:
                          field:
                            description: Field specifies which metadata field provides
                              the assigned value. Valid fields are `namespace` and
                              `name`.
                            type: string
                        type: object
                      value:
                        description: Value is a constant value that will be assigned
                          to `location`
                        x-kubernetes-preserve-unknown-fields: true
                    type: object
                type: object
            type: object
          status:
            description: AssignMetadataStatus defines the observed state of AssignMetadata.
            properties:
              byPod:
                description: 'INSERT ADDITIONAL STATUS FIELD - define observed state
                  of cluster

                  Important: Run "make" to regenerate code after modifying this file'
                items:
                  description: MutatorPodStatusStatus defines the observed state of
                    MutatorPodStatus.
                  properties:
                    enforced:
                      type: boolean
                    errors:
                      items:
                        description: MutatorError represents a single error caught
                          while adding a mutator to a system.
                        properties:
                          message:
                            type: string
                          type:
                            description: 'Type indicates a specific class of error
                              for use by controller code.

                              If not present, the error should be treated as not matching
                              any known type.'
                            type: string
                        required:
                        - message
                        type: object
                      type: array
                    id:
                      type: string
                    mutatorUID:
                      description: 'Storing the mutator UID allows us to detect drift,
                        such as

                        when a mutator has been recreated after its CRD was deleted

                        out from under it, interrupting the watch'
                      type: string
                    observedGeneration:
                      format: int64
                      type: integer
                    operations:
                      items:
                        type: string
                      type: array
                  type: object
                type: array
            type: object
        type: object
    served: true
    storage: true
    subresources:
      status: {}
  - name: v1alpha1
    schema:
      openAPIV3Schema:
        description: AssignMetadata is the Schema for the assignmetadata API.
        properties:
          apiVersion:
            description: 'APIVersion defines the versioned schema of this representation
              of an object.

              Servers should convert recognized schemas to the latest internal value,
              and

              may reject unrecognized values.

              More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources'
            type: string
          kind:
            description: 'Kind is a string value representing the REST resource this
              object represents.

              Servers may infer this from the endpoint the client submits requests
              to.

              Cannot be updated.

              In CamelCase.

              More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds'
            type: string
          metadata:
            type: object
          spec:
            description: AssignMetadataSpec defines the desired state of AssignMetadata.
            properties:
              location:
                type: string
              match:
                description: Match selects which objects are in scope.
                properties:
                  excludedNamespaces:
                    description: 'ExcludedNamespaces is a list of namespace names.
                      If defined, a

                      constraint only applies to resources not in a listed namespace.

                      ExcludedNamespaces also supports a prefix or suffix based glob.  For
                      example,

                      `excludedNamespaces: [kube-*]` matches both `kube-system` and

                      `kube-public`, and `excludedNamespaces: [*-system]` matches
                      both `kube-system` and

                      `gatekeeper-system`.'
                    items:
                      description: 'A string that supports globbing at its front and
                        end. Ex: "kube-*" will match "kube-system" or

                        "kube-public", "*-system" will match "kube-system" or "gatekeeper-system",
                        "*system*" will

                        match "system-kube" or "kube-system".  The asterisk is required
                        for wildcard matching.'
                      pattern: ^\*?[-:a-z0-9]*\*?$
                      type: string
                    type: array
                  kinds:
                    items:
                      description: 'Kinds accepts a list of objects with apiGroups
                        and kinds fields

                        that list the groups/kinds of objects to which the mutation
                        will apply.

                        If multiple groups/kinds objects are specified,

                        only one match is needed for the resource to be in scope.'
                      properties:
                        apiGroups:
                          description: 'APIGroups is the API groups the resources
                            belong to. ''*'' is all groups.

                            If ''*'' is present, the length of the slice must be one.

                            Required.'
                          items:
                            type: string
                          type: array
                        kinds:
                          items:
                            type: string
                          type: array
                      type: object
                    type: array
                  labelSelector:
                    description: 'LabelSelector is the combination of two optional
                      fields: `matchLabels`

                      and `matchExpressions`.  These two fields provide different
                      methods of

                      selecting or excluding k8s objects based on the label keys and
                      values

                      included in object metadata.  All selection expressions from
                      both

                      sections are ANDed to determine if an object meets the cumulative

                      requirements of the selector.'
                    properties:
                      matchExpressions:
                        description: matchExpressions is a list of label selector
                          requirements. The requirements are ANDed.
                        items:
                          description: 'A label selector requirement is a selector
                            that contains values, a key, and an operator that

                            relates the key and values.'
                          properties:
                            key:
                              description: key is the label key that the selector
                                applies to.
                              type: string
                            operator:
                              description: 'operator represents a key''s relationship
                                to a set of values.

                                Valid operators are In, NotIn, Exists and DoesNotExist.'
                              type: string
                            values:
                              description: 'values is an array of string values. If
                                the operator is In or NotIn,

                                the values array must be non-empty. If the operator
                                is Exists or DoesNotExist,

                                the values array must be empty. This array is replaced
                                during a strategic

                                merge patch.'
                              items:
                                type: string
                              type: array
                          required:
                          - key
                          - operator
                          type: object
                        type: array
                      matchLabels:
                        additionalProperties:
                          type: string
                        description: 'matchLabels is a map of {key,value} pairs. A
                          single {key,value} in the matchLabels

                          map is equivalent to an element of matchExpressions, whose
                          key field is "key", the

                          operator is "In", and the values array contains only "value".
                          The requirements are ANDed.'
                        type: object
                    type: object
                    x-kubernetes-map-type: atomic
                  name:
                    description: 'Name is the name of an object.  If defined, it will
                      match against objects with the specified

                      name.  Name also supports a prefix or suffix glob.  For example,
                      `name: pod-*` would match

                      both `pod-a` and `pod-b`, and `name: *-pod` would match both
                      `a-pod` and `b-pod`.'
                    pattern: ^\*?[-:a-z0-9]*\*?$
                    type: string
                  namespaceSelector:
                    description: 'NamespaceSelector is a label selector against an
                      object''s containing

                      namespace or the object itself, if the object is a namespace.'
                    properties:
                      matchExpressions:
                        description: matchExpressions is a list of label selector
                          requirements. The requirements are ANDed.
                        items:
                          description: 'A label selector requirement is a selector
                            that contains values, a key, and an operator that

                            relates the key and values.'
                          properties:
                            key:
                              description: key is the label key that the selector
                                applies to.
                              type: string
                            operator:
                              description: 'operator represents a key''s relationship
                                to a set of values.

                                Valid operators are In, NotIn, Exists and DoesNotExist.'
                              type: string
                            values:
                              description: 'values is an array of string values. If
                                the operator is In or NotIn,

                                the values array must be non-empty. If the operator
                                is Exists or DoesNotExist,

                                the values array must be empty. This array is replaced
                                during a strategic

                                merge patch.'
                              items:
                                type: string
                              type: array
                          required:
                          - key
                          - operator
                          type: object
                        type: array
                      matchLabels:
                        additionalProperties:
                          type: string
                        description: 'matchLabels is a map of {key,value} pairs. A
                          single {key,value} in the matchLabels

                          map is equivalent to an element of matchExpressions, whose
                          key field is "key", the

                          operator is "In", and the values array contains only "value".
                          The requirements are ANDed.'
                        type: object
                    type: object
                    x-kubernetes-map-type: atomic
                  namespaces:
                    description: 'Namespaces is a list of namespace names. If defined,
                      a constraint only

                      applies to resources in a listed namespace.  Namespaces also
                      supports a

                      prefix or suffix based glob.  For example, `namespaces: [kube-*]`
                      matches both

                      `kube-system` and `kube-public`, and `namespaces: [*-system]`
                      matches both

                      `kube-system` and `gatekeeper-system`.'
                    items:
                      description: 'A string that supports globbing at its front and
                        end. Ex: "kube-*" will match "kube-system" or

                        "kube-public", "*-system" will match "kube-system" or "gatekeeper-system",
                        "*system*" will

                        match "system-kube" or "kube-system".  The asterisk is required
                        for wildcard matching.'
                      pattern: ^\*?[-:a-z0-9]*\*?$
                      type: string
                    type: array
                  scope:
                    description: 'Scope determines if cluster-scoped and/or namespaced-scoped
                      resources

                      are matched.  Accepts `*`, `Cluster`, or `Namespaced`. (defaults
                      to `*`)'
                    type: string
                  source:
                    description: 'Source determines whether generated or original
                      resources are matched.

                      Accepts `Generated`|`Original`|`All` (defaults to `All`). A
                      value of

                      `Generated` will only match generated resources, while `Original`
                      will only

                      match regular resources.'
                    enum:
                    - All
                    - Generated
                    - Original
                    type: string
                type: object
              parameters:
                properties:
                  assign:
                    description: Assign.value holds the value to be assigned
                    properties:
                      externalData:
                        description: ExternalData describes the external data provider
                          to be used for mutation.
                        properties:
                          dataSource:
                            default: ValueAtLocation
                            description: 'DataSource specifies where to extract the
                              data that will be sent

                              to the external data provider as parameters.'
                            enum:
                            - ValueAtLocation
                            - Username
                            type: string
                          default:
                            description: 'Default specifies the default value to use
                              when the external data

                              provider returns an error and the failure policy is
                              set to "UseDefault".'
                            type: string
                          failurePolicy:
                            default: Fail
                            description: 'FailurePolicy specifies the policy to apply
                              when the external data

                              provider returns an error.'
                            enum:
                            - UseDefault
                            - Ignore
                            - Fail
                            type: string
                          provider:
                            description: Provider is the name of the external data
                              provider.
                            type: string
                        type: object
                      fromMetadata:
                        description: FromMetadata assigns a value from the specified
                          metadata field.
                        properties:
                          field:
                            description: Field specifies which metadata field provides
                              the assigned value. Valid fields are `namespace` and
                              `name`.
                            type: string
                        type: object
                      value:
                        description: Value is a constant value that will be assigned
                          to `location`
                        x-kubernetes-preserve-unknown-fields: true
                    type: object
                type: object
            type: object
          status:
            description: AssignMetadataStatus defines the observed state of AssignMetadata.
            properties:
              byPod:
                description: 'INSERT ADDITIONAL STATUS FIELD - define observed state
                  of cluster

                  Important: Run "make" to regenerate code after modifying this file'
                items:
                  description: MutatorPodStatusStatus defines the observed state of
                    MutatorPodStatus.
                  properties:
                    enforced:
                      type: boolean
                    errors:
                      items:
                        description: MutatorError represents a single error caught
                          while adding a mutator to a system.
                        properties:
                          message:
                            type: string
                          type:
                            description: 'Type indicates a specific class of error
                              for use by controller code.

                              If not present, the error should be treated as not matching
                              any known type.'
                            type: string
                        required:
                        - message
                        type: object
                      type: array
                    id:
                      type: string
                    mutatorUID:
                      description: 'Storing the mutator UID allows us to detect drift,
                        such as

                        when a mutator has been recreated after its CRD was deleted

                        out from under it, interrupting the watch'
                      type: string
                    observedGeneration:
                      format: int64
                      type: integer
                    operations:
                      items:
                        type: string
                      type: array
                  type: object
                type: array
            type: object
        type: object
    served: true
    storage: false
    subresources:
      status: {}
  - name: v1beta1
    schema:
      openAPIV3Schema:
        description: AssignMetadata is the Schema for the assignmetadata API.
        properties:
          apiVersion:
            description: 'APIVersion defines the versioned schema of this representation
              of an object.

              Servers should convert recognized schemas to the latest internal value,
              and

              may reject unrecognized values.

              More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources'
            type: string
          kind:
            description: 'Kind is a string value representing the REST resource this
              object represents.

              Servers may infer this from the endpoint the client submits requests
              to.

              Cannot be updated.

              In CamelCase.

              More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds'
            type: string
          metadata:
            type: object
          spec:
            description: AssignMetadataSpec defines the desired state of AssignMetadata.
            properties:
              location:
                type: string
              match:
                description: Match selects which objects are in scope.
                properties:
                  excludedNamespaces:
                    description: 'ExcludedNamespaces is a list of namespace names.
                      If defined, a

                      constraint only applies to resources not in a listed namespace.

                      ExcludedNamespaces also supports a prefix or suffix based glob.  For
                      example,

                      `excludedNamespaces: [kube-*]` matches both `kube-system` and

                      `kube-public`, and `excludedNamespaces: [*-system]` matches
                      both `kube-system` and

                      `gatekeeper-system`.'
                    items:
                      description: 'A string that supports globbing at its front and
                        end. Ex: "kube-*" will match "kube-system" or

                        "kube-public", "*-system" will match "kube-system" or "gatekeeper-system",
                        "*system*" will

                        match "system-kube" or "kube-system".  The asterisk is required
                        for wildcard matching.'
                      pattern: ^\*?[-:a-z0-9]*\*?$
                      type: string
                    type: array
                  kinds:
                    items:
                      description: 'Kinds accepts a list of objects with apiGroups
                        and kinds fields

                        that list the groups/kinds of objects to which the mutation
                        will apply.

                        If multiple groups/kinds objects are specified,

                        only one match is needed for the resource to be in scope.'
                      properties:
                        apiGroups:
                          description: 'APIGroups is the API groups the resources
                            belong to. ''*'' is all groups.

                            If ''*'' is present, the length of the slice must be one.

                            Required.'
                          items:
                            type: string
                          type: array
                        kinds:
                          items:
                            type: string
                          type: array
                      type: object
                    type: array
                  labelSelector:
                    description: 'LabelSelector is the combination of two optional
                      fields: `matchLabels`

                      and `matchExpressions`.  These two fields provide different
                      methods of

                      selecting or excluding k8s objects based on the label keys and
                      values

                      included in object metadata.  All selection expressions from
                      both

                      sections are ANDed to determine if an object meets the cumulative

                      requirements of the selector.'
                    properties:
                      matchExpressions:
                        description: matchExpressions is a list of label selector
                          requirements. The requirements are ANDed.
                        items:
                          description: 'A label selector requirement is a selector
                            that contains values, a key, and an operator that

                            relates the key and values.'
                          properties:
                            key:
                              description: key is the label key that the selector
                                applies to.
                              type: string
                            operator:
                              description: 'operator represents a key''s relationship
                                to a set of values.

                                Valid operators are In, NotIn, Exists and DoesNotExist.'
                              type: string
                            values:
                              description: 'values is an array of string values. If
                                the operator is In or NotIn,

                                the values array must be non-empty. If the operator
                                is Exists or DoesNotExist,

                                the values array must be empty. This array is replaced
                                during a strategic

                                merge patch.'
                              items:
                                type: string
                              type: array
                          required:
                          - key
                          - operator
                          type: object
                        type: array
                      matchLabels:
                        additionalProperties:
                          type: string
                        description: 'matchLabels is a map of {key,value} pairs. A
                          single {key,value} in the matchLabels

                          map is equivalent to an element of matchExpressions, whose
                          key field is "key", the

                          operator is "In", and the values array contains only "value".
                          The requirements are ANDed.'
                        type: object
                    type: object
                    x-kubernetes-map-type: atomic
                  name:
                    description: 'Name is the name of an object.  If defined, it will
                      match against objects with the specified

                      name.  Name also supports a prefix or suffix glob.  For example,
                      `name: pod-*` would match

                      both `pod-a` and `pod-b`, and `name: *-pod` would match both
                      `a-pod` and `b-pod`.'
                    pattern: ^\*?[-:a-z0-9]*\*?$
                    type: string
                  namespaceSelector:
                    description: 'NamespaceSelector is a label selector against an
                      object''s containing

                      namespace or the object itself, if the object is a namespace.'
                    properties:
                      matchExpressions:
                        description: matchExpressions is a list of label selector
                          requirements. The requirements are ANDed.
                        items:
                          description: 'A label selector requirement is a selector
                            that contains values, a key, and an operator that

                            relates the key and values.'
                          properties:
                            key:
                              description: key is the label key that the selector
                                applies to.
                              type: string
                            operator:
                              description: 'operator represents a key''s relationship
                                to a set of values.

                                Valid operators are In, NotIn, Exists and DoesNotExist.'
                              type: string
                            values:
                              description: 'values is an array of string values. If
                                the operator is In or NotIn,

                                the values array must be non-empty. If the operator
                                is Exists or DoesNotExist,

                                the values array must be empty. This array is replaced
                                during a strategic

                                merge patch.'
                              items:
                                type: string
                              type: array
                          required:
                          - key
                          - operator
                          type: object
                        type: array
                      matchLabels:
                        additionalProperties:
                          type: string
                        description: 'matchLabels is a map of {key,value} pairs. A
                          single {key,value} in the matchLabels

                          map is equivalent to an element of matchExpressions, whose
                          key field is "key", the

                          operator is "In", and the values array contains only "value".
                          The requirements are ANDed.'
                        type: object
                    type: object
                    x-kubernetes-map-type: atomic
                  namespaces:
                    description: 'Namespaces is a list of namespace names. If defined,
                      a constraint only

                      applies to resources in a listed namespace.  Namespaces also
                      supports a

                      prefix or suffix based glob.  For example, `namespaces: [kube-*]`
                      matches both

                      `kube-system` and `kube-public`, and `namespaces: [*-system]`
                      matches both

                      `kube-system` and `gatekeeper-system`.'
                    items:
                      description: 'A string that supports globbing at its front and
                        end. Ex: "kube-*" will match "kube-system" or

                        "kube-public", "*-system" will match "kube-system" or "gatekeeper-system",
                        "*system*" will

                        match "system-kube" or "kube-system".  The asterisk is required
                        for wildcard matching.'
                      pattern: ^\*?[-:a-z0-9]*\*?$
                      type: string
                    type: array
                  scope:
                    description: 'Scope determines if cluster-scoped and/or namespaced-scoped
                      resources

                      are matched.  Accepts `*`, `Cluster`, or `Namespaced`. (defaults
                      to `*`)'
                    type: string
                  source:
                    description: 'Source determines whether generated or original
                      resources are matched.

                      Accepts `Generated`|`Original`|`All` (defaults to `All`). A
                      value of

                      `Generated` will only match generated resources, while `Original`
                      will only

                      match regular resources.'
                    enum:
                    - All
                    - Generated
                    - Original
                    type: string
                type: object
              parameters:
                properties:
                  assign:
                    description: Assign.value holds the value to be assigned
                    properties:
                      externalData:
                        description: ExternalData describes the external data provider
                          to be used for mutation.
                        properties:
                          dataSource:
                            default: ValueAtLocation
                            description: 'DataSource specifies where to extract the
                              data that will be sent

                              to the external data provider as parameters.'
                            enum:
                            - ValueAtLocation
                            - Username
                            type: string
                          default:
                            description: 'Default specifies the default value to use
                              when the external data

                              provider returns an error and the failure policy is
                              set to "UseDefault".'
                            type: string
                          failurePolicy:
                            default: Fail
                            description: 'FailurePolicy specifies the policy to apply
                              when the external data

                              provider returns an error.'
                            enum:
                            - UseDefault
                            - Ignore
                            - Fail
                            type: string
                          provider:
                            description: Provider is the name of the external data
                              provider.
                            type: string
                        type: object
                      fromMetadata:
                        description: FromMetadata assigns a value from the specified
                          metadata field.
                        properties:
                          field:
                            description: Field specifies which metadata field provides
                              the assigned value. Valid fields are `namespace` and
                              `name`.
                            type: string
                        type: object
                      value:
                        description: Value is a constant value that will be assigned
                          to `location`
                        x-kubernetes-preserve-unknown-fields: true
                    type: object
                type: object
            type: object
          status:
            description: AssignMetadataStatus defines the observed state of AssignMetadata.
            properties:
              byPod:
                description: 'INSERT ADDITIONAL STATUS FIELD - define observed state
                  of cluster

                  Important: Run "make" to regenerate code after modifying this file'
                items:
                  description: MutatorPodStatusStatus defines the observed state of
                    MutatorPodStatus.
                  properties:
                    enforced:
                      type: boolean
                    errors:
                      items:
                        description: MutatorError represents a single error caught
                          while adding a mutator to a system.
                        properties:
                          message:
                            type: string
                          type:
                            description: 'Type indicates a specific class of error
                              for use by controller code.

                              If not present, the error should be treated as not matching
                              any known type.'
                            type: string
                        required:
                        - message
                        type: object
                      type: array
                    id:
                      type: string
                    mutatorUID:
                      description: 'Storing the mutator UID allows us to detect drift,
                        such as

                        when a mutator has been recreated after its CRD was deleted

                        out from under it, interrupting the watch'
                      type: string
                    observedGeneration:
                      format: int64
                      type: integer
                    operations:
                      items:
                        type: string
                      type: array
                  type: object
                type: array
            type: object
        type: object
    served: true
    storage: false
    subresources:
      status: {}
```

## chart/crds/config-customresourcedefinition.yaml
```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  annotations:
    controller-gen.kubebuilder.io/version: v0.14.0
  labels:
    gatekeeper.sh/system: 'yes'
  name: configs.config.gatekeeper.sh
spec:
  group: config.gatekeeper.sh
  names:
    kind: Config
    listKind: ConfigList
    plural: configs
    singular: config
  preserveUnknownFields: false
  scope: Namespaced
  versions:
  - name: v1alpha1
    schema:
      openAPIV3Schema:
        description: Config is the Schema for the configs API.
        properties:
          apiVersion:
            description: 'APIVersion defines the versioned schema of this representation
              of an object.

              Servers should convert recognized schemas to the latest internal value,
              and

              may reject unrecognized values.

              More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources'
            type: string
          kind:
            description: 'Kind is a string value representing the REST resource this
              object represents.

              Servers may infer this from the endpoint the client submits requests
              to.

              Cannot be updated.

              In CamelCase.

              More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds'
            type: string
          metadata:
            type: object
          spec:
            description: ConfigSpec defines the desired state of Config.
            properties:
              match:
                description: Configuration for namespace exclusion
                items:
                  properties:
                    excludedNamespaces:
                      items:
                        description: 'A string that supports globbing at its front
                          and end. Ex: "kube-*" will match "kube-system" or

                          "kube-public", "*-system" will match "kube-system" or "gatekeeper-system",
                          "*system*" will

                          match "system-kube" or "kube-system".  The asterisk is required
                          for wildcard matching.'
                        pattern: ^\*?[-:a-z0-9]*\*?$
                        type: string
                      type: array
                    processes:
                      items:
                        type: string
                      type: array
                  type: object
                type: array
              readiness:
                description: Configuration for readiness tracker
                properties:
                  statsEnabled:
                    type: boolean
                type: object
              sync:
                description: Configuration for syncing k8s objects
                properties:
                  syncOnly:
                    description: If non-empty, only entries on this list will be replicated
                      into OPA
                    items:
                      properties:
                        group:
                          type: string
                        kind:
                          type: string
                        version:
                          type: string
                      type: object
                    type: array
                type: object
              validation:
                description: Configuration for validation
                properties:
                  traces:
                    description: List of requests to trace. Both "user" and "kinds"
                      must be specified
                    items:
                      properties:
                        dump:
                          description: Also dump the state of OPA with the trace.
                            Set to `All` to dump everything.
                          type: string
                        kind:
                          description: Only trace requests of the following GroupVersionKind
                          properties:
                            group:
                              type: string
                            kind:
                              type: string
                            version:
                              type: string
                          type: object
                        user:
                          description: Only trace requests from the specified user
                          type: string
                      type: object
                    type: array
                type: object
            type: object
          status:
            description: ConfigStatus defines the observed state of Config.
            type: object
        type: object
    served: true
    storage: true
```

## chart/crds/constraintpodstatus-customresourcedefinition.yaml
```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  annotations:
    controller-gen.kubebuilder.io/version: v0.14.0
  labels:
    gatekeeper.sh/system: 'yes'
  name: constraintpodstatuses.status.gatekeeper.sh
spec:
  group: status.gatekeeper.sh
  names:
    kind: ConstraintPodStatus
    listKind: ConstraintPodStatusList
    plural: constraintpodstatuses
    singular: constraintpodstatus
  preserveUnknownFields: false
  scope: Namespaced
  versions:
  - name: v1beta1
    schema:
      openAPIV3Schema:
        description: ConstraintPodStatus is the Schema for the constraintpodstatuses
          API.
        properties:
          apiVersion:
            description: 'APIVersion defines the versioned schema of this representation
              of an object.

              Servers should convert recognized schemas to the latest internal value,
              and

              may reject unrecognized values.

              More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources'
            type: string
          kind:
            description: 'Kind is a string value representing the REST resource this
              object represents.

              Servers may infer this from the endpoint the client submits requests
              to.

              Cannot be updated.

              In CamelCase.

              More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds'
            type: string
          metadata:
            type: object
          status:
            description: ConstraintPodStatusStatus defines the observed state of ConstraintPodStatus.
            properties:
              constraintUID:
                description: 'Storing the constraint UID allows us to detect drift,
                  such as

                  when a constraint has been recreated after its CRD was deleted

                  out from under it, interrupting the watch'
                type: string
              enforced:
                type: boolean
              errors:
                items:
                  description: Error represents a single error caught while adding
                    a constraint to engine.
                  properties:
                    code:
                      type: string
                    location:
                      type: string
                    message:
                      type: string
                  required:
                  - code
                  - message
                  type: object
                type: array
              id:
                type: string
              observedGeneration:
                format: int64
                type: integer
              operations:
                items:
                  type: string
                type: array
            type: object
        type: object
    served: true
    storage: true
```

## chart/crds/constrainttemplate-customresourcedefinition.yaml
```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  annotations:
    controller-gen.kubebuilder.io/version: v0.14.0
  labels:
    gatekeeper.sh/system: 'yes'
  name: constrainttemplates.templates.gatekeeper.sh
spec:
  group: templates.gatekeeper.sh
  names:
    kind: ConstraintTemplate
    listKind: ConstraintTemplateList
    plural: constrainttemplates
    singular: constrainttemplate
  preserveUnknownFields: false
  scope: Cluster
  versions:
  - name: v1
    schema:
      openAPIV3Schema:
        description: ConstraintTemplate is the Schema for the constrainttemplates
          API
        properties:
          apiVersion:
            description: 'APIVersion defines the versioned schema of this representation
              of an object.

              Servers should convert recognized schemas to the latest internal value,
              and

              may reject unrecognized values.

              More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources'
            type: string
          kind:
            description: 'Kind is a string value representing the REST resource this
              object represents.

              Servers may infer this from the endpoint the client submits requests
              to.

              Cannot be updated.

              In CamelCase.

              More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds'
            type: string
          metadata:
            type: object
          spec:
            description: ConstraintTemplateSpec defines the desired state of ConstraintTemplate.
            properties:
              crd:
                properties:
                  spec:
                    properties:
                      names:
                        properties:
                          kind:
                            type: string
                          shortNames:
                            items:
                              type: string
                            type: array
                        type: object
                      validation:
                        default:
                          legacySchema: false
                        properties:
                          legacySchema:
                            default: false
                            type: boolean
                          openAPIV3Schema:
                            type: object
                            x-kubernetes-preserve-unknown-fields: true
                        type: object
                    type: object
                type: object
              targets:
                items:
                  properties:
                    code:
                      description: 'The source code options for the constraint template.
                        "Rego" can only

                        be specified in one place (either here or in the "rego" field)'
                      items:
                        properties:
                          engine:
                            description: 'The engine used to evaluate the code. Example:
                              "Rego". Required.'
                            type: string
                          source:
                            description: The source code for the template. Required.
                            x-kubernetes-preserve-unknown-fields: true
                        required:
                        - engine
                        - source
                        type: object
                      type: array
                      x-kubernetes-list-map-keys:
                      - engine
                      x-kubernetes-list-type: map
                    libs:
                      items:
                        type: string
                      type: array
                    rego:
                      type: string
                    target:
                      type: string
                  type: object
                type: array
            type: object
          status:
            description: ConstraintTemplateStatus defines the observed state of ConstraintTemplate.
            properties:
              byPod:
                items:
                  description: 'ByPodStatus defines the observed state of ConstraintTemplate
                    as seen by

                    an individual controller'
                  properties:
                    errors:
                      items:
                        description: CreateCRDError represents a single error caught
                          during parsing, compiling, etc.
                        properties:
                          code:
                            type: string
                          location:
                            type: string
                          message:
                            type: string
                        required:
                        - code
                        - message
                        type: object
                      type: array
                    id:
                      description: a unique identifier for the pod that wrote the
                        status
                      type: string
                    observedGeneration:
                      format: int64
                      type: integer
                  type: object
                  x-kubernetes-preserve-unknown-fields: true
                type: array
              created:
                type: boolean
            type: object
        type: object
    served: true
    storage: true
    subresources:
      status: {}
  - name: v1alpha1
    schema:
      openAPIV3Schema:
        description: ConstraintTemplate is the Schema for the constrainttemplates
          API
        properties:
          apiVersion:
            description: 'APIVersion defines the versioned schema of this representation
              of an object.

              Servers should convert recognized schemas to the latest internal value,
              and

              may reject unrecognized values.

              More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources'
            type: string
          kind:
            description: 'Kind is a string value representing the REST resource this
              object represents.

              Servers may infer this from the endpoint the client submits requests
              to.

              Cannot be updated.

              In CamelCase.

              More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds'
            type: string
          metadata:
            type: object
          spec:
            description: ConstraintTemplateSpec defines the desired state of ConstraintTemplate.
            properties:
              crd:
                properties:
                  spec:
                    properties:
                      names:
                        properties:
                          kind:
                            type: string
                          shortNames:
                            items:
                              type: string
                            type: array
                        type: object
                      validation:
                        default:
                          legacySchema: true
                        properties:
                          legacySchema:
                            default: true
                            type: boolean
                          openAPIV3Schema:
                            type: object
                            x-kubernetes-preserve-unknown-fields: true
                        type: object
                    type: object
                type: object
              targets:
                items:
                  properties:
                    code:
                      description: 'The source code options for the constraint template.
                        "Rego" can only

                        be specified in one place (either here or in the "rego" field)'
                      items:
                        properties:
                          engine:
                            description: 'The engine used to evaluate the code. Example:
                              "Rego". Required.'
                            type: string
                          source:
                            description: The source code for the template. Required.
                            x-kubernetes-preserve-unknown-fields: true
                        required:
                        - engine
                        - source
                        type: object
                      type: array
                      x-kubernetes-list-map-keys:
                      - engine
                      x-kubernetes-list-type: map
                    libs:
                      items:
                        type: string
                      type: array
                    rego:
                      type: string
                    target:
                      type: string
                  type: object
                type: array
            type: object
          status:
            description: ConstraintTemplateStatus defines the observed state of ConstraintTemplate.
            properties:
              byPod:
                items:
                  description: 'ByPodStatus defines the observed state of ConstraintTemplate
                    as seen by

                    an individual controller'
                  properties:
                    errors:
                      items:
                        description: CreateCRDError represents a single error caught
                          during parsing, compiling, etc.
                        properties:
                          code:
                            type: string
                          location:
                            type: string
                          message:
                            type: string
                        required:
                        - code
                        - message
                        type: object
                      type: array
                    id:
                      description: a unique identifier for the pod that wrote the
                        status
                      type: string
                    observedGeneration:
                      format: int64
                      type: integer
                  type: object
                  x-kubernetes-preserve-unknown-fields: true
                type: array
              created:
                type: boolean
            type: object
        type: object
    served: true
    storage: false
    subresources:
      status: {}
  - name: v1beta1
    schema:
      openAPIV3Schema:
        description: ConstraintTemplate is the Schema for the constrainttemplates
          API
        properties:
          apiVersion:
            description: 'APIVersion defines the versioned schema of this representation
              of an object.

              Servers should convert recognized schemas to the latest internal value,
              and

              may reject unrecognized values.

              More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources'
            type: string
          kind:
            description: 'Kind is a string value representing the REST resource this
              object represents.

              Servers may infer this from the endpoint the client submits requests
              to.

              Cannot be updated.

              In CamelCase.

              More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds'
            type: string
          metadata:
            type: object
          spec:
            description: ConstraintTemplateSpec defines the desired state of ConstraintTemplate.
            properties:
              crd:
                properties:
                  spec:
                    properties:
                      names:
                        properties:
                          kind:
                            type: string
                          shortNames:
                            items:
                              type: string
                            type: array
                        type: object
                      validation:
                        default:
                          legacySchema: true
                        properties:
                          legacySchema:
                            default: true
                            type: boolean
                          openAPIV3Schema:
                            type: object
                            x-kubernetes-preserve-unknown-fields: true
                        type: object
                    type: object
                type: object
              targets:
                items:
                  properties:
                    code:
                      description: 'The source code options for the constraint template.
                        "Rego" can only

                        be specified in one place (either here or in the "rego" field)'
                      items:
                        properties:
                          engine:
                            description: 'The engine used to evaluate the code. Example:
                              "Rego". Required.'
                            type: string
                          source:
                            description: The source code for the template. Required.
                            x-kubernetes-preserve-unknown-fields: true
                        required:
                        - engine
                        - source
                        type: object
                      type: array
                      x-kubernetes-list-map-keys:
                      - engine
                      x-kubernetes-list-type: map
                    libs:
                      items:
                        type: string
                      type: array
                    rego:
                      type: string
                    target:
                      type: string
                  type: object
                type: array
            type: object
          status:
            description: ConstraintTemplateStatus defines the observed state of ConstraintTemplate.
            properties:
              byPod:
                items:
                  description: 'ByPodStatus defines the observed state of ConstraintTemplate
                    as seen by

                    an individual controller'
                  properties:
                    errors:
                      items:
                        description: CreateCRDError represents a single error caught
                          during parsing, compiling, etc.
                        properties:
                          code:
                            type: string
                          location:
                            type: string
                          message:
                            type: string
                        required:
                        - code
                        - message
                        type: object
                      type: array
                    id:
                      description: a unique identifier for the pod that wrote the
                        status
                      type: string
                    observedGeneration:
                      format: int64
                      type: integer
                  type: object
                  x-kubernetes-preserve-unknown-fields: true
                type: array
              created:
                type: boolean
            type: object
        type: object
    served: true
    storage: false
    subresources:
      status: {}
```

## chart/crds/constrainttemplatepodstatus-customresourcedefinition.yaml
```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  annotations:
    controller-gen.kubebuilder.io/version: v0.14.0
  labels:
    gatekeeper.sh/system: 'yes'
  name: constrainttemplatepodstatuses.status.gatekeeper.sh
spec:
  group: status.gatekeeper.sh
  names:
    kind: ConstraintTemplatePodStatus
    listKind: ConstraintTemplatePodStatusList
    plural: constrainttemplatepodstatuses
    singular: constrainttemplatepodstatus
  preserveUnknownFields: false
  scope: Namespaced
  versions:
  - name: v1beta1
    schema:
      openAPIV3Schema:
        description: ConstraintTemplatePodStatus is the Schema for the constrainttemplatepodstatuses
          API.
        properties:
          apiVersion:
            description: 'APIVersion defines the versioned schema of this representation
              of an object.

              Servers should convert recognized schemas to the latest internal value,
              and

              may reject unrecognized values.

              More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources'
            type: string
          kind:
            description: 'Kind is a string value representing the REST resource this
              object represents.

              Servers may infer this from the endpoint the client submits requests
              to.

              Cannot be updated.

              In CamelCase.

              More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds'
            type: string
          metadata:
            type: object
          status:
            description: ConstraintTemplatePodStatusStatus defines the observed state
              of ConstraintTemplatePodStatus.
            properties:
              errors:
                items:
                  description: CreateCRDError represents a single error caught during
                    parsing, compiling, etc.
                  properties:
                    code:
                      type: string
                    location:
                      type: string
                    message:
                      type: string
                  required:
                  - code
                  - message
                  type: object
                type: array
              id:
                description: 'Important: Run "make" to regenerate code after modifying
                  this file'
                type: string
              observedGeneration:
                format: int64
                type: integer
              operations:
                items:
                  type: string
                type: array
              templateUID:
                description: 'UID is a type that holds unique ID values, including
                  UUIDs.  Because we

                  don''t ONLY use UUIDs, this is an alias to string.  Being a type
                  captures

                  intent and helps make sure that UIDs and names do not get conflated.'
                type: string
            type: object
        type: object
    served: true
    storage: true
```

## chart/crds/expansiontemplate-customresourcedefinition.yaml
```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  annotations:
    controller-gen.kubebuilder.io/version: v0.14.0
  labels:
    gatekeeper.sh/system: 'yes'
  name: expansiontemplate.expansion.gatekeeper.sh
spec:
  group: expansion.gatekeeper.sh
  names:
    kind: ExpansionTemplate
    listKind: ExpansionTemplateList
    plural: expansiontemplate
    singular: expansiontemplate
  preserveUnknownFields: false
  scope: Cluster
  versions:
  - name: v1alpha1
    schema:
      openAPIV3Schema:
        description: ExpansionTemplate is the Schema for the ExpansionTemplate API.
        properties:
          apiVersion:
            description: 'APIVersion defines the versioned schema of this representation
              of an object.

              Servers should convert recognized schemas to the latest internal value,
              and

              may reject unrecognized values.

              More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources'
            type: string
          kind:
            description: 'Kind is a string value representing the REST resource this
              object represents.

              Servers may infer this from the endpoint the client submits requests
              to.

              Cannot be updated.

              In CamelCase.

              More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds'
            type: string
          metadata:
            type: object
          spec:
            description: ExpansionTemplateSpec defines the desired state of ExpansionTemplate.
            properties:
              applyTo:
                description: 'ApplyTo lists the specific groups, versions and kinds
                  of generator resources

                  which will be expanded.'
                items:
                  description: 'ApplyTo determines what GVKs items the mutation should
                    apply to.

                    Globs are not allowed.'
                  properties:
                    groups:
                      items:
                        type: string
                      type: array
                    kinds:
                      items:
                        type: string
                      type: array
                    versions:
                      items:
                        type: string
                      type: array
                  type: object
                type: array
              enforcementAction:
                description: 'EnforcementAction specifies the enforcement action to
                  be used for resources

                  matching the ExpansionTemplate. Specifying an empty value will use
                  the

                  enforcement action specified by the Constraint in violation.'
                type: string
              generatedGVK:
                description: 'GeneratedGVK specifies the GVK of the resources which
                  the generator

                  resource creates.'
                properties:
                  group:
                    type: string
                  kind:
                    type: string
                  version:
                    type: string
                type: object
              templateSource:
                description: 'TemplateSource specifies the source field on the generator
                  resource to

                  use as the base for expanded resource. For Pod-creating generators,
                  this

                  is usually spec.template'
                type: string
            type: object
          status:
            description: ExpansionTemplateStatus defines the observed state of ExpansionTemplate.
            properties:
              byPod:
                items:
                  description: ExpansionTemplatePodStatusStatus defines the observed
                    state of ExpansionTemplatePodStatus.
                  properties:
                    errors:
                      items:
                        properties:
                          message:
                            type: string
                          type:
                            type: string
                        required:
                        - message
                        type: object
                      type: array
                    id:
                      description: 'Important: Run "make" to regenerate code after
                        modifying this file'
                      type: string
                    observedGeneration:
                      format: int64
                      type: integer
                    operations:
                      items:
                        type: string
                      type: array
                    templateUID:
                      description: 'UID is a type that holds unique ID values, including
                        UUIDs.  Because we

                        don''t ONLY use UUIDs, this is an alias to string.  Being
                        a type captures

                        intent and helps make sure that UIDs and names do not get
                        conflated.'
                      type: string
                  type: object
                type: array
            type: object
        type: object
    served: true
    storage: true
    subresources:
      status: {}
  - name: v1beta1
    schema:
      openAPIV3Schema:
        description: ExpansionTemplate is the Schema for the ExpansionTemplate API.
        properties:
          apiVersion:
            description: 'APIVersion defines the versioned schema of this representation
              of an object.

              Servers should convert recognized schemas to the latest internal value,
              and

              may reject unrecognized values.

              More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources'
            type: string
          kind:
            description: 'Kind is a string value representing the REST resource this
              object represents.

              Servers may infer this from the endpoint the client submits requests
              to.

              Cannot be updated.

              In CamelCase.

              More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds'
            type: string
          metadata:
            type: object
          spec:
            description: ExpansionTemplateSpec defines the desired state of ExpansionTemplate.
            properties:
              applyTo:
                description: 'ApplyTo lists the specific groups, versions and kinds
                  of generator resources

                  which will be expanded.'
                items:
                  description: 'ApplyTo determines what GVKs items the mutation should
                    apply to.

                    Globs are not allowed.'
                  properties:
                    groups:
                      items:
                        type: string
                      type: array
                    kinds:
                      items:
                        type: string
                      type: array
                    versions:
                      items:
                        type: string
                      type: array
                  type: object
                type: array
              enforcementAction:
                description: 'EnforcementAction specifies the enforcement action to
                  be used for resources

                  matching the ExpansionTemplate. Specifying an empty value will use
                  the

                  enforcement action specified by the Constraint in violation.'
                type: string
              generatedGVK:
                description: 'GeneratedGVK specifies the GVK of the resources which
                  the generator

                  resource creates.'
                properties:
                  group:
                    type: string
                  kind:
                    type: string
                  version:
                    type: string
                type: object
              templateSource:
                description: 'TemplateSource specifies the source field on the generator
                  resource to

                  use as the base for expanded resource. For Pod-creating generators,
                  this

                  is usually spec.template'
                type: string
            type: object
          status:
            description: ExpansionTemplateStatus defines the observed state of ExpansionTemplate.
            properties:
              byPod:
                items:
                  description: ExpansionTemplatePodStatusStatus defines the observed
                    state of ExpansionTemplatePodStatus.
                  properties:
                    errors:
                      items:
                        properties:
                          message:
                            type: string
                          type:
                            type: string
                        required:
                        - message
                        type: object
                      type: array
                    id:
                      description: 'Important: Run "make" to regenerate code after
                        modifying this file'
                      type: string
                    observedGeneration:
                      format: int64
                      type: integer
                    operations:
                      items:
                        type: string
                      type: array
                    templateUID:
                      description: 'UID is a type that holds unique ID values, including
                        UUIDs.  Because we

                        don''t ONLY use UUIDs, this is an alias to string.  Being
                        a type captures

                        intent and helps make sure that UIDs and names do not get
                        conflated.'
                      type: string
                  type: object
                type: array
            type: object
        type: object
    served: true
    storage: false
    subresources:
      status: {}
```

## chart/crds/expansiontemplatepodstatus-customresourcedefinition.yaml
```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  annotations:
    controller-gen.kubebuilder.io/version: v0.14.0
  labels:
    gatekeeper.sh/system: 'yes'
  name: expansiontemplatepodstatuses.status.gatekeeper.sh
spec:
  group: status.gatekeeper.sh
  names:
    kind: ExpansionTemplatePodStatus
    listKind: ExpansionTemplatePodStatusList
    plural: expansiontemplatepodstatuses
    singular: expansiontemplatepodstatus
  preserveUnknownFields: false
  scope: Namespaced
  versions:
  - name: v1beta1
    schema:
      openAPIV3Schema:
        description: ExpansionTemplatePodStatus is the Schema for the expansiontemplatepodstatuses
          API.
        properties:
          apiVersion:
            description: 'APIVersion defines the versioned schema of this representation
              of an object.

              Servers should convert recognized schemas to the latest internal value,
              and

              may reject unrecognized values.

              More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources'
            type: string
          kind:
            description: 'Kind is a string value representing the REST resource this
              object represents.

              Servers may infer this from the endpoint the client submits requests
              to.

              Cannot be updated.

              In CamelCase.

              More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds'
            type: string
          metadata:
            type: object
          status:
            description: ExpansionTemplatePodStatusStatus defines the observed state
              of ExpansionTemplatePodStatus.
            properties:
              errors:
                items:
                  properties:
                    message:
                      type: string
                    type:
                      type: string
                  required:
                  - message
                  type: object
                type: array
              id:
                description: 'Important: Run "make" to regenerate code after modifying
                  this file'
                type: string
              observedGeneration:
                format: int64
                type: integer
              operations:
                items:
                  type: string
                type: array
              templateUID:
                description: 'UID is a type that holds unique ID values, including
                  UUIDs.  Because we

                  don''t ONLY use UUIDs, this is an alias to string.  Being a type
                  captures

                  intent and helps make sure that UIDs and names do not get conflated.'
                type: string
            type: object
        type: object
    served: true
    storage: true
```

## chart/crds/modifyset-customresourcedefinition.yaml
```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  annotations:
    controller-gen.kubebuilder.io/version: v0.14.0
  labels:
    gatekeeper.sh/system: 'yes'
  name: modifyset.mutations.gatekeeper.sh
spec:
  group: mutations.gatekeeper.sh
  names:
    kind: ModifySet
    listKind: ModifySetList
    plural: modifyset
    singular: modifyset
  preserveUnknownFields: false
  scope: Cluster
  versions:
  - name: v1
    schema:
      openAPIV3Schema:
        description: 'ModifySet allows the user to modify non-keyed lists, such as

          the list of arguments to a container.'
        properties:
          apiVersion:
            description: 'APIVersion defines the versioned schema of this representation
              of an object.

              Servers should convert recognized schemas to the latest internal value,
              and

              may reject unrecognized values.

              More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources'
            type: string
          kind:
            description: 'Kind is a string value representing the REST resource this
              object represents.

              Servers may infer this from the endpoint the client submits requests
              to.

              Cannot be updated.

              In CamelCase.

              More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds'
            type: string
          metadata:
            properties:
              name:
                maxLength: 63
                type: string
            type: object
          spec:
            description: ModifySetSpec defines the desired state of ModifySet.
            properties:
              applyTo:
                description: 'ApplyTo lists the specific groups, versions and kinds
                  a mutation will be applied to.

                  This is necessary because every mutation implies part of an object
                  schema and object

                  schemas are associated with specific GVKs.'
                items:
                  description: 'ApplyTo determines what GVKs items the mutation should
                    apply to.

                    Globs are not allowed.'
                  properties:
                    groups:
                      items:
                        type: string
                      type: array
                    kinds:
                      items:
                        type: string
                      type: array
                    versions:
                      items:
                        type: string
                      type: array
                  type: object
                type: array
              location:
                description: 'Location describes the path to be mutated, for example:
                  `spec.containers[name: main].args`.'
                type: string
              match:
                description: 'Match allows the user to limit which resources get mutated.

                  Individual match criteria are AND-ed together. An undefined

                  match criteria matches everything.'
                properties:
                  excludedNamespaces:
                    description: 'ExcludedNamespaces is a list of namespace names.
                      If defined, a

                      constraint only applies to resources not in a listed namespace.

                      ExcludedNamespaces also supports a prefix or suffix based glob.  For
                      example,

                      `excludedNamespaces: [kube-*]` matches both `kube-system` and

                      `kube-public`, and `excludedNamespaces: [*-system]` matches
                      both `kube-system` and

                      `gatekeeper-system`.'
                    items:
                      description: 'A string that supports globbing at its front and
                        end. Ex: "kube-*" will match "kube-system" or

                        "kube-public", "*-system" will match "kube-system" or "gatekeeper-system",
                        "*system*" will

                        match "system-kube" or "kube-system".  The asterisk is required
                        for wildcard matching.'
                      pattern: ^\*?[-:a-z0-9]*\*?$
                      type: string
                    type: array
                  kinds:
                    items:
                      description: 'Kinds accepts a list of objects with apiGroups
                        and kinds fields

                        that list the groups/kinds of objects to which the mutation
                        will apply.

                        If multiple groups/kinds objects are specified,

                        only one match is needed for the resource to be in scope.'
                      properties:
                        apiGroups:
                          description: 'APIGroups is the API groups the resources
                            belong to. ''*'' is all groups.

                            If ''*'' is present, the length of the slice must be one.

                            Required.'
                          items:
                            type: string
                          type: array
                        kinds:
                          items:
                            type: string
                          type: array
                      type: object
                    type: array
                  labelSelector:
                    description: 'LabelSelector is the combination of two optional
                      fields: `matchLabels`

                      and `matchExpressions`.  These two fields provide different
                      methods of

                      selecting or excluding k8s objects based on the label keys and
                      values

                      included in object metadata.  All selection expressions from
                      both

                      sections are ANDed to determine if an object meets the cumulative

                      requirements of the selector.'
                    properties:
                      matchExpressions:
                        description: matchExpressions is a list of label selector
                          requirements. The requirements are ANDed.
                        items:
                          description: 'A label selector requirement is a selector
                            that contains values, a key, and an operator that

                            relates the key and values.'
                          properties:
                            key:
                              description: key is the label key that the selector
                                applies to.
                              type: string
                            operator:
                              description: 'operator represents a key''s relationship
                                to a set of values.

                                Valid operators are In, NotIn, Exists and DoesNotExist.'
                              type: string
                            values:
                              description: 'values is an array of string values. If
                                the operator is In or NotIn,

                                the values array must be non-empty. If the operator
                                is Exists or DoesNotExist,

                                the values array must be empty. This array is replaced
                                during a strategic

                                merge patch.'
                              items:
                                type: string
                              type: array
                          required:
                          - key
                          - operator
                          type: object
                        type: array
                      matchLabels:
                        additionalProperties:
                          type: string
                        description: 'matchLabels is a map of {key,value} pairs. A
                          single {key,value} in the matchLabels

                          map is equivalent to an element of matchExpressions, whose
                          key field is "key", the

                          operator is "In", and the values array contains only "value".
                          The requirements are ANDed.'
                        type: object
                    type: object
                    x-kubernetes-map-type: atomic
                  name:
                    description: 'Name is the name of an object.  If defined, it will
                      match against objects with the specified

                      name.  Name also supports a prefix or suffix glob.  For example,
                      `name: pod-*` would match

                      both `pod-a` and `pod-b`, and `name: *-pod` would match both
                      `a-pod` and `b-pod`.'
                    pattern: ^\*?[-:a-z0-9]*\*?$
                    type: string
                  namespaceSelector:
                    description: 'NamespaceSelector is a label selector against an
                      object''s containing

                      namespace or the object itself, if the object is a namespace.'
                    properties:
                      matchExpressions:
                        description: matchExpressions is a list of label selector
                          requirements. The requirements are ANDed.
                        items:
                          description: 'A label selector requirement is a selector
                            that contains values, a key, and an operator that

                            relates the key and values.'
                          properties:
                            key:
                              description: key is the label key that the selector
                                applies to.
                              type: string
                            operator:
                              description: 'operator represents a key''s relationship
                                to a set of values.

                                Valid operators are In, NotIn, Exists and DoesNotExist.'
                              type: string
                            values:
                              description: 'values is an array of string values. If
                                the operator is In or NotIn,

                                the values array must be non-empty. If the operator
                                is Exists or DoesNotExist,

                                the values array must be empty. This array is replaced
                                during a strategic

                                merge patch.'
                              items:
                                type: string
                              type: array
                          required:
                          - key
                          - operator
                          type: object
                        type: array
                      matchLabels:
                        additionalProperties:
                          type: string
                        description: 'matchLabels is a map of {key,value} pairs. A
                          single {key,value} in the matchLabels

                          map is equivalent to an element of matchExpressions, whose
                          key field is "key", the

                          operator is "In", and the values array contains only "value".
                          The requirements are ANDed.'
                        type: object
                    type: object
                    x-kubernetes-map-type: atomic
                  namespaces:
                    description: 'Namespaces is a list of namespace names. If defined,
                      a constraint only

                      applies to resources in a listed namespace.  Namespaces also
                      supports a

                      prefix or suffix based glob.  For example, `namespaces: [kube-*]`
                      matches both

                      `kube-system` and `kube-public`, and `namespaces: [*-system]`
                      matches both

                      `kube-system` and `gatekeeper-system`.'
                    items:
                      description: 'A string that supports globbing at its front and
                        end. Ex: "kube-*" will match "kube-system" or

                        "kube-public", "*-system" will match "kube-system" or "gatekeeper-system",
                        "*system*" will

                        match "system-kube" or "kube-system".  The asterisk is required
                        for wildcard matching.'
                      pattern: ^\*?[-:a-z0-9]*\*?$
                      type: string
                    type: array
                  scope:
                    description: 'Scope determines if cluster-scoped and/or namespaced-scoped
                      resources

                      are matched.  Accepts `*`, `Cluster`, or `Namespaced`. (defaults
                      to `*`)'
                    type: string
                  source:
                    description: 'Source determines whether generated or original
                      resources are matched.

                      Accepts `Generated`|`Original`|`All` (defaults to `All`). A
                      value of

                      `Generated` will only match generated resources, while `Original`
                      will only

                      match regular resources.'
                    enum:
                    - All
                    - Generated
                    - Original
                    type: string
                type: object
              parameters:
                description: Parameters define the behavior of the mutator.
                properties:
                  operation:
                    default: merge
                    description: Operation describes whether values should be merged
                      in ("merge"), or pruned ("prune"). Default value is "merge"
                    enum:
                    - merge
                    - prune
                    type: string
                  pathTests:
                    description: 'PathTests are a series of existence tests that can
                      be checked

                      before a mutation is applied'
                    items:
                      description: 'PathTest allows the user to customize how the
                        mutation works if parent

                        paths are missing. It traverses the list in order. All sub
                        paths are

                        tested against the provided condition, if the test fails,
                        the mutation is

                        not applied. All `subPath` entries must be a prefix of `location`.
                        Any

                        glob characters will take on the same value as was used to

                        expand the matching glob in `location`.



                        Available Tests:

                        * MustExist    - the path must exist or do not mutate

                        * MustNotExist - the path must not exist or do not mutate.'
                      properties:
                        condition:
                          description: Condition describes whether the path either
                            MustExist or MustNotExist in the original object
                          enum:
                          - MustExist
                          - MustNotExist
                          type: string
                        subPath:
                          type: string
                      type: object
                    type: array
                  values:
                    description: Values describes the values provided to the operation
                      as `values.fromList`.
                    type: object
                    x-kubernetes-preserve-unknown-fields: true
                type: object
            type: object
          status:
            description: ModifySetStatus defines the observed state of ModifySet.
            properties:
              byPod:
                items:
                  description: MutatorPodStatusStatus defines the observed state of
                    MutatorPodStatus.
                  properties:
                    enforced:
                      type: boolean
                    errors:
                      items:
                        description: MutatorError represents a single error caught
                          while adding a mutator to a system.
                        properties:
                          message:
                            type: string
                          type:
                            description: 'Type indicates a specific class of error
                              for use by controller code.

                              If not present, the error should be treated as not matching
                              any known type.'
                            type: string
                        required:
                        - message
                        type: object
                      type: array
                    id:
                      type: string
                    mutatorUID:
                      description: 'Storing the mutator UID allows us to detect drift,
                        such as

                        when a mutator has been recreated after its CRD was deleted

                        out from under it, interrupting the watch'
                      type: string
                    observedGeneration:
                      format: int64
                      type: integer
                    operations:
                      items:
                        type: string
                      type: array
                  type: object
                type: array
            type: object
        type: object
    served: true
    storage: true
    subresources:
      status: {}
  - name: v1alpha1
    schema:
      openAPIV3Schema:
        description: 'ModifySet allows the user to modify non-keyed lists, such as

          the list of arguments to a container.'
        properties:
          apiVersion:
            description: 'APIVersion defines the versioned schema of this representation
              of an object.

              Servers should convert recognized schemas to the latest internal value,
              and

              may reject unrecognized values.

              More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources'
            type: string
          kind:
            description: 'Kind is a string value representing the REST resource this
              object represents.

              Servers may infer this from the endpoint the client submits requests
              to.

              Cannot be updated.

              In CamelCase.

              More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds'
            type: string
          metadata:
            type: object
          spec:
            description: ModifySetSpec defines the desired state of ModifySet.
            properties:
              applyTo:
                description: 'ApplyTo lists the specific groups, versions and kinds
                  a mutation will be applied to.

                  This is necessary because every mutation implies part of an object
                  schema and object

                  schemas are associated with specific GVKs.'
                items:
                  description: 'ApplyTo determines what GVKs items the mutation should
                    apply to.

                    Globs are not allowed.'
                  properties:
                    groups:
                      items:
                        type: string
                      type: array
                    kinds:
                      items:
                        type: string
                      type: array
                    versions:
                      items:
                        type: string
                      type: array
                  type: object
                type: array
              location:
                description: 'Location describes the path to be mutated, for example:
                  `spec.containers[name: main].args`.'
                type: string
              match:
                description: 'Match allows the user to limit which resources get mutated.

                  Individual match criteria are AND-ed together. An undefined

                  match criteria matches everything.'
                properties:
                  excludedNamespaces:
                    description: 'ExcludedNamespaces is a list of namespace names.
                      If defined, a

                      constraint only applies to resources not in a listed namespace.

                      ExcludedNamespaces also supports a prefix or suffix based glob.  For
                      example,

                      `excludedNamespaces: [kube-*]` matches both `kube-system` and

                      `kube-public`, and `excludedNamespaces: [*-system]` matches
                      both `kube-system` and

                      `gatekeeper-system`.'
                    items:
                      description: 'A string that supports globbing at its front and
                        end. Ex: "kube-*" will match "kube-system" or

                        "kube-public", "*-system" will match "kube-system" or "gatekeeper-system",
                        "*system*" will

                        match "system-kube" or "kube-system".  The asterisk is required
                        for wildcard matching.'
                      pattern: ^\*?[-:a-z0-9]*\*?$
                      type: string
                    type: array
                  kinds:
                    items:
                      description: 'Kinds accepts a list of objects with apiGroups
                        and kinds fields

                        that list the groups/kinds of objects to which the mutation
                        will apply.

                        If multiple groups/kinds objects are specified,

                        only one match is needed for the resource to be in scope.'
                      properties:
                        apiGroups:
                          description: 'APIGroups is the API groups the resources
                            belong to. ''*'' is all groups.

                            If ''*'' is present, the length of the slice must be one.

                            Required.'
                          items:
                            type: string
                          type: array
                        kinds:
                          items:
                            type: string
                          type: array
                      type: object
                    type: array
                  labelSelector:
                    description: 'LabelSelector is the combination of two optional
                      fields: `matchLabels`

                      and `matchExpressions`.  These two fields provide different
                      methods of

                      selecting or excluding k8s objects based on the label keys and
                      values

                      included in object metadata.  All selection expressions from
                      both

                      sections are ANDed to determine if an object meets the cumulative

                      requirements of the selector.'
                    properties:
                      matchExpressions:
                        description: matchExpressions is a list of label selector
                          requirements. The requirements are ANDed.
                        items:
                          description: 'A label selector requirement is a selector
                            that contains values, a key, and an operator that

                            relates the key and values.'
                          properties:
                            key:
                              description: key is the label key that the selector
                                applies to.
                              type: string
                            operator:
                              description: 'operator represents a key''s relationship
                                to a set of values.

                                Valid operators are In, NotIn, Exists and DoesNotExist.'
                              type: string
                            values:
                              description: 'values is an array of string values. If
                                the operator is In or NotIn,

                                the values array must be non-empty. If the operator
                                is Exists or DoesNotExist,

                                the values array must be empty. This array is replaced
                                during a strategic

                                merge patch.'
                              items:
                                type: string
                              type: array
                          required:
                          - key
                          - operator
                          type: object
                        type: array
                      matchLabels:
                        additionalProperties:
                          type: string
                        description: 'matchLabels is a map of {key,value} pairs. A
                          single {key,value} in the matchLabels

                          map is equivalent to an element of matchExpressions, whose
                          key field is "key", the

                          operator is "In", and the values array contains only "value".
                          The requirements are ANDed.'
                        type: object
                    type: object
                    x-kubernetes-map-type: atomic
                  name:
                    description: 'Name is the name of an object.  If defined, it will
                      match against objects with the specified

                      name.  Name also supports a prefix or suffix glob.  For example,
                      `name: pod-*` would match

                      both `pod-a` and `pod-b`, and `name: *-pod` would match both
                      `a-pod` and `b-pod`.'
                    pattern: ^\*?[-:a-z0-9]*\*?$
                    type: string
                  namespaceSelector:
                    description: 'NamespaceSelector is a label selector against an
                      object''s containing

                      namespace or the object itself, if the object is a namespace.'
                    properties:
                      matchExpressions:
                        description: matchExpressions is a list of label selector
                          requirements. The requirements are ANDed.
                        items:
                          description: 'A label selector requirement is a selector
                            that contains values, a key, and an operator that

                            relates the key and values.'
                          properties:
                            key:
                              description: key is the label key that the selector
                                applies to.
                              type: string
                            operator:
                              description: 'operator represents a key''s relationship
                                to a set of values.

                                Valid operators are In, NotIn, Exists and DoesNotExist.'
                              type: string
                            values:
                              description: 'values is an array of string values. If
                                the operator is In or NotIn,

                                the values array must be non-empty. If the operator
                                is Exists or DoesNotExist,

                                the values array must be empty. This array is replaced
                                during a strategic

                                merge patch.'
                              items:
                                type: string
                              type: array
                          required:
                          - key
                          - operator
                          type: object
                        type: array
                      matchLabels:
                        additionalProperties:
                          type: string
                        description: 'matchLabels is a map of {key,value} pairs. A
                          single {key,value} in the matchLabels

                          map is equivalent to an element of matchExpressions, whose
                          key field is "key", the

                          operator is "In", and the values array contains only "value".
                          The requirements are ANDed.'
                        type: object
                    type: object
                    x-kubernetes-map-type: atomic
                  namespaces:
                    description: 'Namespaces is a list of namespace names. If defined,
                      a constraint only

                      applies to resources in a listed namespace.  Namespaces also
                      supports a

                      prefix or suffix based glob.  For example, `namespaces: [kube-*]`
                      matches both

                      `kube-system` and `kube-public`, and `namespaces: [*-system]`
                      matches both

                      `kube-system` and `gatekeeper-system`.'
                    items:
                      description: 'A string that supports globbing at its front and
                        end. Ex: "kube-*" will match "kube-system" or

                        "kube-public", "*-system" will match "kube-system" or "gatekeeper-system",
                        "*system*" will

                        match "system-kube" or "kube-system".  The asterisk is required
                        for wildcard matching.'
                      pattern: ^\*?[-:a-z0-9]*\*?$
                      type: string
                    type: array
                  scope:
                    description: 'Scope determines if cluster-scoped and/or namespaced-scoped
                      resources

                      are matched.  Accepts `*`, `Cluster`, or `Namespaced`. (defaults
                      to `*`)'
                    type: string
                  source:
                    description: 'Source determines whether generated or original
                      resources are matched.

                      Accepts `Generated`|`Original`|`All` (defaults to `All`). A
                      value of

                      `Generated` will only match generated resources, while `Original`
                      will only

                      match regular resources.'
                    enum:
                    - All
                    - Generated
                    - Original
                    type: string
                type: object
              parameters:
                description: Parameters define the behavior of the mutator.
                properties:
                  operation:
                    default: merge
                    description: Operation describes whether values should be merged
                      in ("merge"), or pruned ("prune"). Default value is "merge"
                    enum:
                    - merge
                    - prune
                    type: string
                  pathTests:
                    description: 'PathTests are a series of existence tests that can
                      be checked

                      before a mutation is applied'
                    items:
                      description: 'PathTest allows the user to customize how the
                        mutation works if parent

                        paths are missing. It traverses the list in order. All sub
                        paths are

                        tested against the provided condition, if the test fails,
                        the mutation is

                        not applied. All `subPath` entries must be a prefix of `location`.
                        Any

                        glob characters will take on the same value as was used to

                        expand the matching glob in `location`.



                        Available Tests:

                        * MustExist    - the path must exist or do not mutate

                        * MustNotExist - the path must not exist or do not mutate.'
                      properties:
                        condition:
                          description: Condition describes whether the path either
                            MustExist or MustNotExist in the original object
                          enum:
                          - MustExist
                          - MustNotExist
                          type: string
                        subPath:
                          type: string
                      type: object
                    type: array
                  values:
                    description: Values describes the values provided to the operation
                      as `values.fromList`.
                    type: object
                    x-kubernetes-preserve-unknown-fields: true
                type: object
            type: object
          status:
            description: ModifySetStatus defines the observed state of ModifySet.
            properties:
              byPod:
                items:
                  description: MutatorPodStatusStatus defines the observed state of
                    MutatorPodStatus.
                  properties:
                    enforced:
                      type: boolean
                    errors:
                      items:
                        description: MutatorError represents a single error caught
                          while adding a mutator to a system.
                        properties:
                          message:
                            type: string
                          type:
                            description: 'Type indicates a specific class of error
                              for use by controller code.

                              If not present, the error should be treated as not matching
                              any known type.'
                            type: string
                        required:
                        - message
                        type: object
                      type: array
                    id:
                      type: string
                    mutatorUID:
                      description: 'Storing the mutator UID allows us to detect drift,
                        such as

                        when a mutator has been recreated after its CRD was deleted

                        out from under it, interrupting the watch'
                      type: string
                    observedGeneration:
                      format: int64
                      type: integer
                    operations:
                      items:
                        type: string
                      type: array
                  type: object
                type: array
            type: object
        type: object
    served: true
    storage: false
    subresources:
      status: {}
  - name: v1beta1
    schema:
      openAPIV3Schema:
        description: 'ModifySet allows the user to modify non-keyed lists, such as

          the list of arguments to a container.'
        properties:
          apiVersion:
            description: 'APIVersion defines the versioned schema of this representation
              of an object.

              Servers should convert recognized schemas to the latest internal value,
              and

              may reject unrecognized values.

              More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources'
            type: string
          kind:
            description: 'Kind is a string value representing the REST resource this
              object represents.

              Servers may infer this from the endpoint the client submits requests
              to.

              Cannot be updated.

              In CamelCase.

              More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds'
            type: string
          metadata:
            type: object
          spec:
            description: ModifySetSpec defines the desired state of ModifySet.
            properties:
              applyTo:
                description: 'ApplyTo lists the specific groups, versions and kinds
                  a mutation will be applied to.

                  This is necessary because every mutation implies part of an object
                  schema and object

                  schemas are associated with specific GVKs.'
                items:
                  description: 'ApplyTo determines what GVKs items the mutation should
                    apply to.

                    Globs are not allowed.'
                  properties:
                    groups:
                      items:
                        type: string
                      type: array
                    kinds:
                      items:
                        type: string
                      type: array
                    versions:
                      items:
                        type: string
                      type: array
                  type: object
                type: array
              location:
                description: 'Location describes the path to be mutated, for example:
                  `spec.containers[name: main].args`.'
                type: string
              match:
                description: 'Match allows the user to limit which resources get mutated.

                  Individual match criteria are AND-ed together. An undefined

                  match criteria matches everything.'
                properties:
                  excludedNamespaces:
                    description: 'ExcludedNamespaces is a list of namespace names.
                      If defined, a

                      constraint only applies to resources not in a listed namespace.

                      ExcludedNamespaces also supports a prefix or suffix based glob.  For
                      example,

                      `excludedNamespaces: [kube-*]` matches both `kube-system` and

                      `kube-public`, and `excludedNamespaces: [*-system]` matches
                      both `kube-system` and

                      `gatekeeper-system`.'
                    items:
                      description: 'A string that supports globbing at its front and
                        end. Ex: "kube-*" will match "kube-system" or

                        "kube-public", "*-system" will match "kube-system" or "gatekeeper-system",
                        "*system*" will

                        match "system-kube" or "kube-system".  The asterisk is required
                        for wildcard matching.'
                      pattern: ^\*?[-:a-z0-9]*\*?$
                      type: string
                    type: array
                  kinds:
                    items:
                      description: 'Kinds accepts a list of objects with apiGroups
                        and kinds fields

                        that list the groups/kinds of objects to which the mutation
                        will apply.

                        If multiple groups/kinds objects are specified,

                        only one match is needed for the resource to be in scope.'
                      properties:
                        apiGroups:
                          description: 'APIGroups is the API groups the resources
                            belong to. ''*'' is all groups.

                            If ''*'' is present, the length of the slice must be one.

                            Required.'
                          items:
                            type: string
                          type: array
                        kinds:
                          items:
                            type: string
                          type: array
                      type: object
                    type: array
                  labelSelector:
                    description: 'LabelSelector is the combination of two optional
                      fields: `matchLabels`

                      and `matchExpressions`.  These two fields provide different
                      methods of

                      selecting or excluding k8s objects based on the label keys and
                      values

                      included in object metadata.  All selection expressions from
                      both

                      sections are ANDed to determine if an object meets the cumulative

                      requirements of the selector.'
                    properties:
                      matchExpressions:
                        description: matchExpressions is a list of label selector
                          requirements. The requirements are ANDed.
                        items:
                          description: 'A label selector requirement is a selector
                            that contains values, a key, and an operator that

                            relates the key and values.'
                          properties:
                            key:
                              description: key is the label key that the selector
                                applies to.
                              type: string
                            operator:
                              description: 'operator represents a key''s relationship
                                to a set of values.

                                Valid operators are In, NotIn, Exists and DoesNotExist.'
                              type: string
                            values:
                              description: 'values is an array of string values. If
                                the operator is In or NotIn,

                                the values array must be non-empty. If the operator
                                is Exists or DoesNotExist,

                                the values array must be empty. This array is replaced
                                during a strategic

                                merge patch.'
                              items:
                                type: string
                              type: array
                          required:
                          - key
                          - operator
                          type: object
                        type: array
                      matchLabels:
                        additionalProperties:
                          type: string
                        description: 'matchLabels is a map of {key,value} pairs. A
                          single {key,value} in the matchLabels

                          map is equivalent to an element of matchExpressions, whose
                          key field is "key", the

                          operator is "In", and the values array contains only "value".
                          The requirements are ANDed.'
                        type: object
                    type: object
                    x-kubernetes-map-type: atomic
                  name:
                    description: 'Name is the name of an object.  If defined, it will
                      match against objects with the specified

                      name.  Name also supports a prefix or suffix glob.  For example,
                      `name: pod-*` would match

                      both `pod-a` and `pod-b`, and `name: *-pod` would match both
                      `a-pod` and `b-pod`.'
                    pattern: ^\*?[-:a-z0-9]*\*?$
                    type: string
                  namespaceSelector:
                    description: 'NamespaceSelector is a label selector against an
                      object''s containing

                      namespace or the object itself, if the object is a namespace.'
                    properties:
                      matchExpressions:
                        description: matchExpressions is a list of label selector
                          requirements. The requirements are ANDed.
                        items:
                          description: 'A label selector requirement is a selector
                            that contains values, a key, and an operator that

                            relates the key and values.'
                          properties:
                            key:
                              description: key is the label key that the selector
                                applies to.
                              type: string
                            operator:
                              description: 'operator represents a key''s relationship
                                to a set of values.

                                Valid operators are In, NotIn, Exists and DoesNotExist.'
                              type: string
                            values:
                              description: 'values is an array of string values. If
                                the operator is In or NotIn,

                                the values array must be non-empty. If the operator
                                is Exists or DoesNotExist,

                                the values array must be empty. This array is replaced
                                during a strategic

                                merge patch.'
                              items:
                                type: string
                              type: array
                          required:
                          - key
                          - operator
                          type: object
                        type: array
                      matchLabels:
                        additionalProperties:
                          type: string
                        description: 'matchLabels is a map of {key,value} pairs. A
                          single {key,value} in the matchLabels

                          map is equivalent to an element of matchExpressions, whose
                          key field is "key", the

                          operator is "In", and the values array contains only "value".
                          The requirements are ANDed.'
                        type: object
                    type: object
                    x-kubernetes-map-type: atomic
                  namespaces:
                    description: 'Namespaces is a list of namespace names. If defined,
                      a constraint only

                      applies to resources in a listed namespace.  Namespaces also
                      supports a

                      prefix or suffix based glob.  For example, `namespaces: [kube-*]`
                      matches both

                      `kube-system` and `kube-public`, and `namespaces: [*-system]`
                      matches both

                      `kube-system` and `gatekeeper-system`.'
                    items:
                      description: 'A string that supports globbing at its front and
                        end. Ex: "kube-*" will match "kube-system" or

                        "kube-public", "*-system" will match "kube-system" or "gatekeeper-system",
                        "*system*" will

                        match "system-kube" or "kube-system".  The asterisk is required
                        for wildcard matching.'
                      pattern: ^\*?[-:a-z0-9]*\*?$
                      type: string
                    type: array
                  scope:
                    description: 'Scope determines if cluster-scoped and/or namespaced-scoped
                      resources

                      are matched.  Accepts `*`, `Cluster`, or `Namespaced`. (defaults
                      to `*`)'
                    type: string
                  source:
                    description: 'Source determines whether generated or original
                      resources are matched.

                      Accepts `Generated`|`Original`|`All` (defaults to `All`). A
                      value of

                      `Generated` will only match generated resources, while `Original`
                      will only

                      match regular resources.'
                    enum:
                    - All
                    - Generated
                    - Original
                    type: string
                type: object
              parameters:
                description: Parameters define the behavior of the mutator.
                properties:
                  operation:
                    default: merge
                    description: Operation describes whether values should be merged
                      in ("merge"), or pruned ("prune"). Default value is "merge"
                    enum:
                    - merge
                    - prune
                    type: string
                  pathTests:
                    description: 'PathTests are a series of existence tests that can
                      be checked

                      before a mutation is applied'
                    items:
                      description: 'PathTest allows the user to customize how the
                        mutation works if parent

                        paths are missing. It traverses the list in order. All sub
                        paths are

                        tested against the provided condition, if the test fails,
                        the mutation is

                        not applied. All `subPath` entries must be a prefix of `location`.
                        Any

                        glob characters will take on the same value as was used to

                        expand the matching glob in `location`.



                        Available Tests:

                        * MustExist    - the path must exist or do not mutate

                        * MustNotExist - the path must not exist or do not mutate.'
                      properties:
                        condition:
                          description: Condition describes whether the path either
                            MustExist or MustNotExist in the original object
                          enum:
                          - MustExist
                          - MustNotExist
                          type: string
                        subPath:
                          type: string
                      type: object
                    type: array
                  values:
                    description: Values describes the values provided to the operation
                      as `values.fromList`.
                    type: object
                    x-kubernetes-preserve-unknown-fields: true
                type: object
            type: object
          status:
            description: ModifySetStatus defines the observed state of ModifySet.
            properties:
              byPod:
                items:
                  description: MutatorPodStatusStatus defines the observed state of
                    MutatorPodStatus.
                  properties:
                    enforced:
                      type: boolean
                    errors:
                      items:
                        description: MutatorError represents a single error caught
                          while adding a mutator to a system.
                        properties:
                          message:
                            type: string
                          type:
                            description: 'Type indicates a specific class of error
                              for use by controller code.

                              If not present, the error should be treated as not matching
                              any known type.'
                            type: string
                        required:
                        - message
                        type: object
                      type: array
                    id:
                      type: string
                    mutatorUID:
                      description: 'Storing the mutator UID allows us to detect drift,
                        such as

                        when a mutator has been recreated after its CRD was deleted

                        out from under it, interrupting the watch'
                      type: string
                    observedGeneration:
                      format: int64
                      type: integer
                    operations:
                      items:
                        type: string
                      type: array
                  type: object
                type: array
            type: object
        type: object
    served: true
    storage: false
    subresources:
      status: {}
```

## chart/crds/mutatorpodstatus-customresourcedefinition.yaml
```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  annotations:
    controller-gen.kubebuilder.io/version: v0.14.0
  labels:
    gatekeeper.sh/system: 'yes'
  name: mutatorpodstatuses.status.gatekeeper.sh
spec:
  group: status.gatekeeper.sh
  names:
    kind: MutatorPodStatus
    listKind: MutatorPodStatusList
    plural: mutatorpodstatuses
    singular: mutatorpodstatus
  preserveUnknownFields: false
  scope: Namespaced
  versions:
  - name: v1beta1
    schema:
      openAPIV3Schema:
        description: MutatorPodStatus is the Schema for the mutationpodstatuses API.
        properties:
          apiVersion:
            description: 'APIVersion defines the versioned schema of this representation
              of an object.

              Servers should convert recognized schemas to the latest internal value,
              and

              may reject unrecognized values.

              More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources'
            type: string
          kind:
            description: 'Kind is a string value representing the REST resource this
              object represents.

              Servers may infer this from the endpoint the client submits requests
              to.

              Cannot be updated.

              In CamelCase.

              More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds'
            type: string
          metadata:
            type: object
          status:
            description: MutatorPodStatusStatus defines the observed state of MutatorPodStatus.
            properties:
              enforced:
                type: boolean
              errors:
                items:
                  description: MutatorError represents a single error caught while
                    adding a mutator to a system.
                  properties:
                    message:
                      type: string
                    type:
                      description: 'Type indicates a specific class of error for use
                        by controller code.

                        If not present, the error should be treated as not matching
                        any known type.'
                      type: string
                  required:
                  - message
                  type: object
                type: array
              id:
                type: string
              mutatorUID:
                description: 'Storing the mutator UID allows us to detect drift, such
                  as

                  when a mutator has been recreated after its CRD was deleted

                  out from under it, interrupting the watch'
                type: string
              observedGeneration:
                format: int64
                type: integer
              operations:
                items:
                  type: string
                type: array
            type: object
        type: object
    served: true
    storage: true
```

## chart/crds/provider-customresourcedefinition.yaml
```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  annotations:
    controller-gen.kubebuilder.io/version: v0.14.0
  labels:
    gatekeeper.sh/system: 'yes'
  name: providers.externaldata.gatekeeper.sh
spec:
  group: externaldata.gatekeeper.sh
  names:
    kind: Provider
    listKind: ProviderList
    plural: providers
    singular: provider
  preserveUnknownFields: false
  scope: Cluster
  versions:
  - deprecated: true
    deprecationWarning: externaldata.gatekeeper.sh/v1alpha1 is deprecated. Use externaldata.gatekeeper.sh/v1beta1
      instead.
    name: v1alpha1
    schema:
      openAPIV3Schema:
        description: Provider is the Schema for the Provider API
        properties:
          apiVersion:
            description: 'APIVersion defines the versioned schema of this representation
              of an object.

              Servers should convert recognized schemas to the latest internal value,
              and

              may reject unrecognized values.

              More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources'
            type: string
          kind:
            description: 'Kind is a string value representing the REST resource this
              object represents.

              Servers may infer this from the endpoint the client submits requests
              to.

              Cannot be updated.

              In CamelCase.

              More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds'
            type: string
          metadata:
            type: object
          spec:
            description: Spec defines the Provider specifications.
            properties:
              caBundle:
                description: 'CABundle is a base64-encoded string that contains the
                  TLS CA bundle in PEM format.

                  It is used to verify the signature of the provider''s certificate.'
                type: string
              timeout:
                description: Timeout is the timeout when querying the provider.
                type: integer
              url:
                description: URL is the url for the provider. URL is prefixed with
                  https://.
                type: string
            type: object
        type: object
    served: true
    storage: false
  - name: v1beta1
    schema:
      openAPIV3Schema:
        description: Provider is the Schema for the providers API
        properties:
          apiVersion:
            description: 'APIVersion defines the versioned schema of this representation
              of an object.

              Servers should convert recognized schemas to the latest internal value,
              and

              may reject unrecognized values.

              More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources'
            type: string
          kind:
            description: 'Kind is a string value representing the REST resource this
              object represents.

              Servers may infer this from the endpoint the client submits requests
              to.

              Cannot be updated.

              In CamelCase.

              More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds'
            type: string
          metadata:
            type: object
          spec:
            description: Spec defines the Provider specifications.
            properties:
              caBundle:
                description: 'CABundle is a base64-encoded string that contains the
                  TLS CA bundle in PEM format.

                  It is used to verify the signature of the provider''s certificate.'
                type: string
              timeout:
                description: Timeout is the timeout when querying the provider.
                type: integer
              url:
                description: URL is the url for the provider. URL is prefixed with
                  https://.
                type: string
            type: object
        type: object
    served: true
    storage: true
```

## chart/crds/syncset-customresourcedefinition.yaml
```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  annotations:
    controller-gen.kubebuilder.io/version: v0.14.0
  labels:
    gatekeeper.sh/system: 'yes'
  name: syncsets.syncset.gatekeeper.sh
spec:
  group: syncset.gatekeeper.sh
  names:
    kind: SyncSet
    listKind: SyncSetList
    plural: syncsets
    singular: syncset
  preserveUnknownFields: false
  scope: Cluster
  versions:
  - name: v1alpha1
    schema:
      openAPIV3Schema:
        description: SyncSet defines which resources Gatekeeper will cache. The union
          of all SyncSets plus the syncOnly field of Gatekeeper's Config resource
          defines the sets of resources that will be synced.
        properties:
          apiVersion:
            description: 'APIVersion defines the versioned schema of this representation
              of an object.

              Servers should convert recognized schemas to the latest internal value,
              and

              may reject unrecognized values.

              More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources'
            type: string
          kind:
            description: 'Kind is a string value representing the REST resource this
              object represents.

              Servers may infer this from the endpoint the client submits requests
              to.

              Cannot be updated.

              In CamelCase.

              More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds'
            type: string
          metadata:
            properties:
              name:
                maxLength: 63
                type: string
            type: object
          spec:
            properties:
              gvks:
                items:
                  properties:
                    group:
                      type: string
                    kind:
                      type: string
                    version:
                      type: string
                  type: object
                type: array
            type: object
        type: object
    served: true
    storage: true
```

## chart/values.yaml
```yaml
openshift: false
replicas: 3
revisionHistoryLimit: 10
auditInterval: 60
metricsBackends:
- prometheus
auditMatchKindOnly: true
constraintViolationsLimit: 1000
auditFromCache: false
disableMutation: true
disableAudit: false
disableValidatingWebhook: false
validatingWebhookName: gatekeeper-validating-webhook-configuration
validatingWebhookTimeoutSeconds: 15
validatingWebhookFailurePolicy: Ignore
validatingWebhookAnnotations: {}
validatingWebhookExemptNamespacesLabels: {}
validatingWebhookObjectSelector: {}
validatingWebhookMatchConditions: []
validatingWebhookCheckIgnoreFailurePolicy: Fail
validatingWebhookCustomRules: {}
validatingWebhookURL: null
enableDeleteOperations: false
enableExternalData: true
enableGeneratorResourceExpansion: true
enableTLSHealthcheck: false
maxServingThreads: -1
mutatingWebhookName: gatekeeper-mutating-webhook-configuration
mutatingWebhookFailurePolicy: Ignore
mutatingWebhookReinvocationPolicy: Never
mutatingWebhookAnnotations: {}
mutatingWebhookExemptNamespacesLabels: {}
mutatingWebhookObjectSelector: {}
mutatingWebhookMatchConditions: []
mutatingWebhookTimeoutSeconds: 1
mutatingWebhookCustomRules: {}
mutatingWebhookURL: null
mutationAnnotations: false
auditChunkSize: 500
logLevel: INFO
logDenies: true
logMutations: true
emitAdmissionEvents: false
emitAuditEvents: false
admissionEventsInvolvedNamespace: false
auditEventsInvolvedNamespace: false
resourceQuota: true
externaldataProviderResponseCacheTTL: 3m
enableK8sNativeValidation: false
vapEnforcement: GATEKEEPER_DEFAULT
image:
  repository: registry1.dso.mil/ironbank/opensource/openpolicyagent/gatekeeper
  release: v3.16.3
  pullPolicy: IfNotPresent
  pullSecrets:
  - name: private-registry
  crdRepository: registry1.dso.mil/ironbank/opensource/kubernetes/kubectl
  crdRelease: v1.29.5
preInstall:
  crdRepository:
    image:
      repository: registry1.dso.mil/ironbank/opensource/kubernetes/kubectl
      tag: v1.29.5
  securityContext:
    allowPrivilegeEscalation: false
    capabilities:
      drop:
      - ALL
    readOnlyRootFilesystem: true
    runAsGroup: 999
    runAsNonRoot: true
    runAsUser: 1000
postUpgrade:
  labelNamespace:
    enabled: false
    image:
      repository: registry1.dso.mil/ironbank/opensource/kubernetes/kubectl
      tag: v1.29.5
      pullPolicy: IfNotPresent
      pullSecrets: []
    extraNamespaces: []
    podSecurity: []
    extraAnnotations: {}
    priorityClassName: ''
  affinity: {}
  tolerations: []
  nodeSelector:
    kubernetes.io/os: linux
  resources: {}
  securityContext:
    allowPrivilegeEscalation: false
    capabilities:
      drop:
      - ALL
    readOnlyRootFilesystem: true
    runAsGroup: 999
    runAsNonRoot: true
    runAsUser: 1000
postInstall:
  labelNamespace:
    enabled: true
    extraRules: []
    image:
      repository: registry1.dso.mil/ironbank/opensource/kubernetes/kubectl
      tag: v1.29.5
      pullPolicy: IfNotPresent
      pullSecrets: []
    extraNamespaces: []
    podSecurity: []
    extraAnnotations: {}
    priorityClassName: ''
  probeWebhook:
    enabled: true
    image:
      repository: registry1.dso.mil/ironbank/big-bang/base
      tag: 2.1.0
      pullPolicy: IfNotPresent
      pullSecrets: []
    waitTimeout: 60
    httpTimeout: 2
    insecureHTTPS: false
    priorityClassName: ''
  affinity: {}
  tolerations: []
  nodeSelector:
    kubernetes.io/os: linux
  securityContext:
    allowPrivilegeEscalation: false
    capabilities:
      drop:
      - ALL
    readOnlyRootFilesystem: true
    runAsGroup: 999
    runAsNonRoot: true
    runAsUser: 1000
preUninstall:
  deleteWebhookConfigurations:
    extraRules: []
    enabled: false
    image:
      repository: registry1.dso.mil/ironbank/opensource/kubernetes/kubectl
      tag: v1.29.5
      pullPolicy: IfNotPresent
      pullSecrets: []
    priorityClassName: ''
  affinity: {}
  tolerations: []
  nodeSelector:
    kubernetes.io/os: linux
  resources: {}
  securityContext:
    allowPrivilegeEscalation: false
    capabilities:
      drop:
      - ALL
    readOnlyRootFilesystem: true
    runAsGroup: 999
    runAsNonRoot: true
    runAsUser: 1000
podAnnotations:
  container.seccomp.security.alpha.kubernetes.io/manager: runtime/default
auditPodAnnotations: {}
podLabels: {}
podCountLimit: '100'
secretAnnotations: {}
enableRuntimeDefaultSeccompProfile: true
controllerManager:
  exemptNamespaces: []
  exemptNamespacePrefixes: []
  hostNetwork: false
  dnsPolicy: ClusterFirst
  port: 8443
  metricsPort: 8888
  healthPort: 9090
  readinessTimeout: 1
  livenessTimeout: 1
  priorityClassName: system-cluster-critical
  disableCertRotation: false
  tlsMinVersion: 1.3
  clientCertName: ''
  strategyType: RollingUpdate
  affinity:
    podAntiAffinity:
      preferredDuringSchedulingIgnoredDuringExecution:
      - podAffinityTerm:
          labelSelector:
            matchExpressions:
            - key: gatekeeper.sh/operation
              operator: In
              values:
              - webhook
          topologyKey: kubernetes.io/hostname
        weight: 100
  topologySpreadConstraints: []
  tolerations: []
  nodeSelector:
    kubernetes.io/os: linux
  resources:
    limits:
      cpu: 175m
      memory: 512Mi
    requests:
      cpu: 175m
      memory: 512Mi
  securityContext:
    allowPrivilegeEscalation: false
    capabilities:
      drop:
      - ALL
    readOnlyRootFilesystem: true
    runAsGroup: 999
    runAsNonRoot: true
    runAsUser: 1000
  podSecurityContext:
    fsGroup: 999
    supplementalGroups:
    - 999
  extraRules: []
  networkPolicy:
    enabled: false
    ingress: {}
audit:
  enablePubsub: false
  hostNetwork: false
  dnsPolicy: ClusterFirst
  metricsPort: 8888
  healthPort: 9090
  readinessTimeout: 1
  livenessTimeout: 1
  priorityClassName: system-cluster-critical
  disableCertRotation: false
  affinity: {}
  tolerations: []
  nodeSelector:
    kubernetes.io/os: linux
  resources:
    limits:
      cpu: 1.2
      memory: 768Mi
    requests:
      cpu: 1.2
      memory: 768Mi
  securityContext:
    allowPrivilegeEscalation: false
    capabilities:
      drop:
      - ALL
    readOnlyRootFilesystem: true
    runAsGroup: 999
    runAsNonRoot: true
    runAsUser: 1000
  podSecurityContext:
    fsGroup: 999
    supplementalGroups:
    - 999
  writeToRAMDisk: false
  extraRules: []
crds:
  affinity: {}
  tolerations: []
  nodeSelector:
    kubernetes.io/os: linux
  resources: {}
  securityContext:
    allowPrivilegeEscalation: false
    capabilities:
      drop:
      - ALL
    readOnlyRootFilesystem: true
    runAsGroup: 65532
    runAsNonRoot: true
    runAsUser: 65532
pdb:
  controllerManager:
    minAvailable: 1
service: {}
disabledBuiltins:
- '{http.send}'
psp:
  enabled: false
upgradeCRDs:
  enabled: true
  extraRules: []
  priorityClassName: ''
cleanupCRDs:
  enabled: true
  containerSecurityContext:
    allowPrivilegeEscalation: false
    capabilities:
      drop:
      - ALL
    readOnlyRootFilesystem: true
    runAsGroup: 999
    runAsNonRoot: true
    runAsUser: 1000
  securityContext:
    readOnlyRootFilesystem: true
    runAsGroup: 999
    runAsNonRoot: true
    runAsUser: 1000
    fsGroup: 999
    supplementalGroups:
    - 999
rbac:
  create: true
externalCertInjection:
  enabled: false
  secretName: gatekeeper-webhook-server-cert
violations:
  allowedAppArmorProfiles:
    enabled: false
    enforcementAction: dryrun
    kind: K8sPSPAppArmor
    name: allowed-app-armor-profiles
    match: {}
    parameters:
      allowedProfiles:
      - runtime/default
      excludedResources: []
  allowedCapabilities:
    enabled: true
    enforcementAction: dryrun
    kind: K8sPSPCapabilities
    name: allowed-capabilities
    match: {}
    parameters:
      allowedCapabilities: []
      requiredDropCapabilities:
      - all
      excludedResources: []
  allowedDockerRegistries:
    enabled: true
    enforcementAction: deny
    kind: K8sAllowedRepos
    name: allowed-docker-registries
    match: {}
    parameters:
      repos:
      - registry1.dso.mil
      excludedResources: []
  allowedFlexVolumes:
    enabled: true
    enforcementAction: deny
    kind: K8sPSPFlexVolumes
    name: allowed-flex-volumes
    match: {}
    parameters:
      allowedFlexVolumes: []
      excludedResources: []
  allowedHostFilesystem:
    enabled: true
    enforcementAction: deny
    kind: K8sPSPHostFilesystem
    name: allowed-host-filesystem
    match: {}
    parameters:
      allowedHostPaths: []
      excludedResources: []
  allowedIPs:
    enabled: true
    enforcementAction: deny
    kind: K8sExternalIPs
    name: allowed-ips
    match: {}
    parameters:
      allowedIPs: []
      excludedResources: []
  allowedProcMount:
    enabled: true
    enforcementAction: deny
    kind: K8sPSPProcMount
    name: allowed-proc-mount
    match: {}
    parameters:
      procMount: Default
      excludedResources: []
  allowedSecCompProfiles:
    enabled: true
    enforcementAction: dryrun
    kind: K8sPSPSeccomp
    name: allowed-sec-comp-profiles
    match: {}
    parameters:
      allowedProfiles:
      - runtime/default
      excludedResources: []
  allowedUsers:
    enabled: true
    enforcementAction: dryrun
    kind: K8sPSPAllowedUsers
    name: allowed-users
    match: {}
    parameters:
      runAsUser:
        rule: MustRunAsNonRoot
      fsGroup:
        rule: MustRunAs
        ranges:
        - min: 1000
          max: 65535
      runAsGroup:
        rule: MustRunAs
        ranges:
        - min: 1000
          max: 65535
      supplementalGroups:
        rule: MustRunAs
        ranges:
        - min: 1000
          max: 65535
      excludedResources: []
  bannedImageTags:
    enabled: true
    enforcementAction: deny
    kind: K8sBannedImageTags
    name: banned-image-tags
    match: {}
    parameters:
      tags:
      - latest
      excludedResources: []
  blockNodePort:
    enabled: true
    enforcementAction: dryrun
    kind: K8sBlockNodePort
    name: block-node-ports
    match: {}
    parameters:
      excludedResources: []
  containerRatio:
    enabled: true
    enforcementAction: dryrun
    kind: K8sContainerRatios
    name: container-ratios
    match: {}
    parameters:
      ratio: '2'
      excludedResources: []
  hostNetworking:
    enabled: true
    enforcementAction: deny
    kind: K8sPSPHostNetworkingPorts
    name: host-networking
    match: {}
    parameters:
      hostNetwork: false
      min: 0
      max: 0
      excludedResources: []
  httpsOnly:
    enabled: true
    enforcementAction: deny
    kind: K8sHttpsOnly2
    name: https-only
    match: {}
    parameters:
      excludedResources: []
  imageDigest:
    enabled: true
    enforcementAction: dryrun
    kind: K8sImageDigests2
    name: image-digest
    match: {}
    parameters:
      excludedResources: []
  namespacesHaveIstio:
    enabled: true
    enforcementAction: dryrun
    kind: K8sRequiredLabelValues
    name: namespaces-have-istio
    match:
      namespaceSelector:
        matchExpressions:
        - key: admission.gatekeeper.sh/ignore
          operator: DoesNotExist
    parameters:
      labels:
      - allowedRegex: ^enabled
        key: istio-injection
      excludedResources: []
  noBigContainers:
    enabled: true
    enforcementAction: dryrun
    kind: K8sContainerLimits
    name: no-big-container
    match: {}
    parameters:
      cpu: 2000m
      memory: 4G
      excludedResources: []
  noHostNamespace:
    enabled: true
    enforcementAction: deny
    kind: K8sPSPHostNamespace2
    name: no-host-namespace
    match: {}
    parameters:
      excludedResources: []
  noPrivilegedContainers:
    enabled: true
    enforcementAction: deny
    kind: K8sPSPPrivilegedContainer2
    name: no-privileged-containers
    match: {}
    parameters:
      excludedResources: []
  noDefaultServiceAccount:
    enabled: true
    enforcementAction: dryrun
    kind: K8sDenySADefault
    name: no-default-service-account
    match: {}
    parameters:
      excludedResources: []
  noPrivilegedEscalation:
    enabled: true
    enforcementAction: dryrun
    kind: K8sPSPAllowPrivilegeEscalationContainer2
    name: no-privileged-escalation
    match: {}
    parameters:
      excludedResources: []
  noSysctls:
    enabled: true
    enforcementAction: deny
    kind: K8sPSPForbiddenSysctls
    name: no-sysctls
    match: {}
    parameters:
      forbiddenSysctls:
      - '*'
      excludedResources: []
  podsHaveIstio:
    enabled: true
    enforcementAction: dryrun
    kind: K8sNoAnnotationValues
    name: pods-have-istio
    match: {}
    parameters:
      annotations:
      - disallowedRegex: ^false
        key: sidecar.istio.io/inject
      excludedResources: []
  readOnlyRoot:
    enabled: true
    enforcementAction: dryrun
    kind: K8sPSPReadOnlyRootFilesystem2
    name: read-only-root
    match: {}
    parameters:
      excludedResources: []
  requiredLabels:
    enabled: true
    enforcementAction: dryrun
    kind: K8sRequiredLabelValues
    name: required-labels
    match: {}
    parameters:
      labels:
      - allowedRegex: ''
        key: app.kubernetes.io/name
      - allowedRegex: ''
        key: app.kubernetes.io/instance
      - allowedRegex: ''
        key: app.kubernetes.io/version
      - allowedRegex: ''
        key: app.kubernetes.io/component
      - allowedRegex: ''
        key: app.kubernetes.io/part-of
      - allowedRegex: ''
        key: app.kubernetes.io/managed-by
      excludedResources: []
  requiredProbes:
    enabled: true
    enforcementAction: dryrun
    kind: K8sRequiredProbes
    name: required-probes
    match: {}
    parameters:
      probeTypes:
      - tcpSocket
      - httpGet
      - exec
      probes:
      - readinessProbe
      - livenessProbe
      excludedResources: []
  restrictedTaint:
    enabled: true
    enforcementAction: deny
    kind: RestrictedTaintToleration
    name: restricted-taint
    match: {}
    parameters:
      allowGlobalToleration: false
      restrictedTaint:
        effect: NoSchedule
        key: privileged
        value: 'true'
      excludedResources: []
  selinuxPolicy:
    enabled: true
    enforcementAction: deny
    kind: K8sPSPSELinuxV2
    name: selinux-policy
    match: {}
    parameters:
      allowedSELinuxOptions:
      - level: null
        role: null
        type: null
        user: null
      excludedResources: []
  uniqueIngressHost:
    enabled: true
    enforcementAction: deny
    kind: K8sUniqueIngressHost
    name: unique-ingress-hosts
    match: {}
    parameters:
      excludedResources: []
  volumeTypes:
    enabled: true
    enforcementAction: deny
    kind: K8sPSPVolumeTypes
    name: volume-types
    match: {}
    parameters:
      volumes:
      - configMap
      - emptyDir
      - projected
      - secret
      - downwardAPI
      - persistentVolumeClaim
      excludedResources: []
monitoring:
  enabled: false
networkPolicies:
  enabled: false
  controlPlaneCidr: 0.0.0.0/0
  additionalPolicies: []
bbtests:
  enabled: true
  scripts:
    image: registry1.dso.mil/ironbank/opensource/kubernetes/kubectl:v1.29.5
    securityContext:
      allowPrivilegeEscalation: false
      capabilities:
        drop:
        - ALL
      readOnlyRootFilesystem: true
      runAsGroup: 999
      runAsNonRoot: true
      runAsUser: 1000
    additionalVolumeMounts:
    - name: '{{ .Chart.Name }}-test-config'
      mountPath: /yaml
    - name: '{{ .Chart.Name }}-kube-cache'
      mountPath: /.kube/cache
    additionalVolumes:
    - name: '{{ .Chart.Name }}-test-config'
      configMap:
        name: '{{ .Chart.Name }}-test-config'
    - name: '{{ .Chart.Name }}-kube-cache'
      emptyDir: {}
```

## oscal-component.yaml
```yaml
component-definition:
  uuid: 558ddfa8-2642-4726-8a89-6b99fc4cbf6e
  metadata:
    title: Gatekeeper Component
    last-modified: '2021-10-19T12:00:00Z'
    version: '20211019'
    oscal-version: 1.1.1
    parties:
    - uuid: 72134592-08C2-4A77-ABAD-C880F109367A
      type: organization
      name: Platform One
      links:
      - href: https://p1.dso.mil
        rel: website
  components:
  - uuid: 8078c070-2d5b-44b8-8fd1-47797fa12c6d
    type: software
    title: OPA Gatekeeper
    description: "An application which assists in enforcing, monitoring, and remediating\
      \ policies in Kubernetes while strengthening governance of an environment. \n"
    purpose: Monitors existing clusters, detects policy violations, and also acts
      as a customizable Kubernetes Admission Webhook
    responsible-roles:
    - role-id: provider
      party-uuids:
      - 72134592-08C2-4A77-ABAD-C880F109367A
    control-implementations:
    - uuid: d2afb4c4-2cd8-5305-a6cc-d1bc7b388d0c
      source: https://raw.githubusercontent.com/GSA/fedramp-automation/93ca0e20ff5e54fc04140613476fba80f08e3c7d/dist/content/rev5/baselines/json/FedRAMP_rev5_HIGH-baseline-resolved-profile_catalog.json
      description: Controls implemented by <component> for inheritance by applications
      implemented-requirements:
      - uuid: c89a52f1-4d60-4d4e-9c4c-7c5eb04fe21a
        control-id: au-2
        description: OPA Gatekeeper provides policy violations events to Cluster Auditor
          for event logging.   The list of policies being audited is/will be captured
          by the Policy Document in Gatekeeper's chart.
      - uuid: c38f765f-b706-4810-96b6-2971f37122df
        control-id: au-3
        description: 'Gatekeeper provides the policy being violated, the timestamp
          of when it occurred, the location (cluster/namespace), the object causing
          the violation and whether it was in warn or deny mode. '
      - uuid: f856dc53-1c3a-428e-83ff-65723c325dac
        control-id: au-8
        description: Gatekeeper policies have timestamps associated to when the violation
          was found and identified.   By logging policy violations into log messages
          (via logDenies=true ),  these logs are also available in the logging framework.
      - uuid: 41b6ce08-5827-4e08-8ff4-1a61a2e378f8
        control-id: au-9
        description: Access to the Gatekeeper violations are managed by/inherited
          from the Kubernetes cluster.
      - uuid: ffb9f4b5-0bfe-4053-9e12-5657a1ceb0b9
        control-id: cm-7.5
        description: OPA Gatekeeper can prevent by default unauthorized changes to
          the system.
      - uuid: 07a4e16a-944b-4989-a6d8-057b545748d0
        control-id: cm-11
        description: Gatekeeper can provide the ability for end users to control the
          policies that allow for the installation of end-user software. It also provides
          the enforcement and monitoring.
```

## tests/test-values.yml
```yaml
replicas: 1
image:
  pullSecrets:
  - name: private-registry
postInstall:
  labelNamespace:
    image:
      pullSecrets:
      - name: private-registry
  probeWebhook:
    image:
      pullSecrets:
      - name: private-registry
postUpgrade:
  cleanupCRD:
    image:
      pullSecrets:
      - name: private-registry
violations:
  allowedAppArmorProfiles:
    enforcementAction: deny
    match:
      namespaces:
      - default
      - bad-pod-test-ns
      - good-pod-test-ns
  allowedCapabilities:
    enforcementAction: deny
    match:
      namespaces:
      - default
      - bad-pod-test-ns
      - good-pod-test-ns
  allowedDockerRegistries:
    enforcementAction: deny
    match:
      namespaces:
      - default
      - bad-pod-test-ns
      - good-pod-test-ns
  allowedFlexVolumes:
    enforcementAction: deny
    match:
      namespaces:
      - default
      - bad-pod-test-ns
      - good-pod-test-ns
  allowedHostFilesystem:
    enforcementAction: deny
    match:
      namespaces:
      - default
      - bad-pod-test-ns
      - good-pod-test-ns
  allowedIPs:
    enforcementAction: deny
    match:
      namespaces:
      - default
      - bad-pod-test-ns
      - good-pod-test-ns
  allowedProcMount:
    enabled: false
  allowedSecCompProfiles:
    enforcementAction: deny
    match:
      namespaces:
      - default
      - bad-pod-test-ns
      - good-pod-test-ns
  allowedUsers:
    enforcementAction: deny
    match:
      namespaces:
      - default
      - bad-pod-test-ns
      - good-pod-test-ns
  bannedImageTags:
    enforcementAction: deny
    match:
      namespaces:
      - default
      - bad-pod-test-ns
      - good-pod-test-ns
  blockNodePort:
    enforcementAction: deny
    match:
      namespaces:
      - default
      - bad-pod-test-ns
      - good-pod-test-ns
  containerRatio:
    enforcementAction: deny
    match:
      namespaces:
      - default
      - bad-pod-test-ns
      - good-pod-test-ns
  hostNetworking:
    enforcementAction: deny
    match:
      namespaces:
      - default
      - bad-pod-test-ns
      - good-pod-test-ns
    parameters:
      min: 8080
      max: 8080
  httpsOnly:
    enforcementAction: deny
    match:
      namespaces:
      - default
      - bad-pod-test-ns
      - good-pod-test-ns
  imageDigest:
    enforcementAction: deny
    match:
      namespaces:
      - default
      - bad-pod-test-ns
      - good-pod-test-ns
  namespacesHaveIstio:
    enforcementAction: deny
    match:
      namespaces:
      - default
      - bad-pod-test-ns
      - good-pod-test-ns
  noBigContainers:
    enforcementAction: deny
    match:
      namespaces:
      - default
      - bad-pod-test-ns
      - good-pod-test-ns
  noHostNamespace:
    enforcementAction: deny
    match:
      namespaces:
      - default
      - bad-pod-test-ns
      - good-pod-test-ns
  noPrivilegedContainers:
    enforcementAction: deny
    match:
      namespaces:
      - default
      - bad-pod-test-ns
      - good-pod-test-ns
  noPrivilegedEscalation:
    enforcementAction: deny
    match:
      namespaces:
      - default
      - bad-pod-test-ns
      - good-pod-test-ns
  noDefaultServiceAccount:
    enforcementAction: deny
    match:
      namespaces:
      - default
      - bad-pod-test-ns
      - good-pod-test-ns
  noSysctls:
    enforcementAction: deny
    match:
      namespaces:
      - default
      - bad-pod-test-ns
      - good-pod-test-ns
  podsHaveIstio:
    enforcementAction: deny
    match:
      namespaces:
      - default
      - bad-pod-test-ns
      - good-pod-test-ns
  readOnlyRoot:
    enforcementAction: deny
    match:
      namespaces:
      - default
      - bad-pod-test-ns
      - good-pod-test-ns
  requiredLabels:
    enforcementAction: deny
    match:
      namespaces:
      - default
      - bad-pod-test-ns
      - good-pod-test-ns
  requiredProbes:
    enforcementAction: deny
    match:
      namespaces:
      - default
      - bad-pod-test-ns
      - good-pod-test-ns
  restrictedTaint:
    enforcementAction: deny
    match:
      namespaces:
      - default
      - bad-pod-test-ns
      - good-pod-test-ns
  selinuxPolicy:
    enforcementAction: deny
    match:
      namespaces:
      - default
      - bad-pod-test-ns
      - good-pod-test-ns
  uniqueIngressHost:
    enforcementAction: deny
    match:
      namespaces:
      - default
      - bad-pod-test-ns
      - good-pod-test-ns
  volumeTypes:
    enforcementAction: deny
    match:
      namespaces:
      - default
      - bad-pod-test-ns
      - good-pod-test-ns
bbtests:
  enabled: true
networkPolicies:
  enabled: true
  controlPlaneCidr: 172.16.0.0/12
```

