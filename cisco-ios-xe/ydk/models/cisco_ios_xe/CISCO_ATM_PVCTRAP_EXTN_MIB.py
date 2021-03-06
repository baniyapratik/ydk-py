""" CISCO_ATM_PVCTRAP_EXTN_MIB 

This MIB Module is a supplement to the
CISCO\-IETF\-ATM2\-PVCTRAP\-MIB.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class CatmOAMFailureType(Enum):
    """
    CatmOAMFailureType

    Enums to indicate different types of OAM recoveries .

    catmLoopbackOAMFailure  \- The object in query is Loopback OAM

                              type of failure.

    catmSegmentCCOAMFailure \- The object in query is Segment CC

                              OAM type of failure.

    catmEndCCOAMFailure     \- The object in query is End\-to\-End 

                              CC OAM type of failure.

    catmAISRDIOAMFailure    \- The object in query is AISRDI OAM

                              type of failure.

    .. data:: catmLoopbackOAMFailure = 1

    .. data:: catmSegmentCCOAMFailure = 2

    .. data:: catmEndCCOAMFailure = 4

    .. data:: catmAISRDIOAMFailure = 8

    """

    catmLoopbackOAMFailure = Enum.YLeaf(1, "catmLoopbackOAMFailure")

    catmSegmentCCOAMFailure = Enum.YLeaf(2, "catmSegmentCCOAMFailure")

    catmEndCCOAMFailure = Enum.YLeaf(4, "catmEndCCOAMFailure")

    catmAISRDIOAMFailure = Enum.YLeaf(8, "catmAISRDIOAMFailure")


class CatmOAMRecoveryType(Enum):
    """
    CatmOAMRecoveryType

    Enums to indicate different types of OAM recoveries .

    catmLoopbackOAMRecover  \- The object in query is Loopback OAM

                              type of recovery.

    catmSegmentCCOAMRecover \- The object in query is Segment CC

                              OAM type of recovery.

    catmEndCCOAMRecover     \- The object in query is End\-to\-End 

                              CC OAM type of recovery.

    catmAISRDIOAMRecover    \- The object in query is AISRDI OAM

                              type of recovery.

    .. data:: catmLoopbackOAMRecover = 1

    .. data:: catmSegmentCCOAMRecover = 2

    .. data:: catmEndCCOAMRecover = 4

    .. data:: catmAISRDIOAMRecover = 8

    """

    catmLoopbackOAMRecover = Enum.YLeaf(1, "catmLoopbackOAMRecover")

    catmSegmentCCOAMRecover = Enum.YLeaf(2, "catmSegmentCCOAMRecover")

    catmEndCCOAMRecover = Enum.YLeaf(4, "catmEndCCOAMRecover")

    catmAISRDIOAMRecover = Enum.YLeaf(8, "catmAISRDIOAMRecover")



class CISCOATMPVCTRAPEXTNMIB(Entity):
    """
    
    
    .. attribute:: catmcurstatchangepvcltable
    
    	A table indicating all VCLs for which there is an active row in the atmVclTable having an atmVclConnKind value of `pvc' and atmVclOperStatus to have changed in the last corresponding PVC notification
    	**type**\:  :py:class:`Catmcurstatchangepvcltable <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.Catmcurstatchangepvcltable>`
    
    .. attribute:: catmstatuschangepvclrangetable
    
    	A table indicating more than one VCLs in a consecutive  range and for each VCL there is an active row in the  atmVclTable having an atmVclConnKind value of `pvc' and atmVclOperStatus to have changed in the same direction in the last corresponding PVC notification 
    	**type**\:  :py:class:`Catmstatuschangepvclrangetable <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.Catmstatuschangepvclrangetable>`
    
    .. attribute:: catmsegccstatuschpvclrangetable
    
    	A table indicating more than one VCLs in a consecutive  range and for each VCL there is an active row in the  atmVclTable having an atmVclConnKind value of `pvc' and atmVclOperStatus to have changed due to segment CC  failure in the same direction in the last PVC  corresponding notification 
    	**type**\:  :py:class:`Catmsegccstatuschpvclrangetable <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.Catmsegccstatuschpvclrangetable>`
    
    .. attribute:: catmendccstatuschpvclrangetable
    
    	A table indicating more than one VCLs in a consecutive  range and for each VCL there is an active row in the  atmVclTable having an atmVclConnKind value of `pvc' and atmVclOperStatus to have changed due to End CC failure in the same direction in the last PVC notification  interval
    	**type**\:  :py:class:`Catmendccstatuschpvclrangetable <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.Catmendccstatuschpvclrangetable>`
    
    .. attribute:: catmaisrdistatuschpvclrangetable
    
    	A table indicating more than one VCLs in a consecutive  range and for each VCL there is an active row in the  atmVclTable having an atmVclConnKind value of `pvc' and atmVclOperStatus to have changed due to AIS/RDI failure in the same direction in the last corresponding PVC  notification
    	**type**\:  :py:class:`Catmaisrdistatuschpvclrangetable <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.Catmaisrdistatuschpvclrangetable>`
    
    .. attribute:: catmdownpvclrangetable
    
    	A table indicating more than one VCLs in a consecutive  range and for each VCL there is an active row in the  atmVclTable having an atmVclConnKind value of `pvc' and atmVclOperStatus to have detected as Down in the last corresponding PVC notification 
    	**type**\:  :py:class:`Catmdownpvclrangetable <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.Catmdownpvclrangetable>`
    
    .. attribute:: catmcurstatusuppvcltable
    
    	A table indicating all VCLs for which there is an active row in the atmVclTable having an atmVclConnKind value of `pvc' and atmVclOperStatus to have changed to UP in the last corresponding PVC notification 
    	**type**\:  :py:class:`Catmcurstatusuppvcltable <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.Catmcurstatusuppvcltable>`
    
    .. attribute:: catmstatusuppvclrangetable
    
    	A table indicating more than one VCLs in a consecutive  range and for each VCL there is an active row in the  atmVclTable having an atmVclConnKind value of `pvc' and loopback OAM status to have detected as recovered in the last corresponding PVC notification 
    	**type**\:  :py:class:`Catmstatusuppvclrangetable <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.Catmstatusuppvclrangetable>`
    
    .. attribute:: catmsegccstatusuppvclrangetable
    
    	A table indicating more than one VCLs in a consecutive range and for each VCL there is an active row in the atmVclTable having an atmVclConnKind value of `pvc' and Segment CC OAM status to have detected as recovered in the last corresponding PVC notification 
    	**type**\:  :py:class:`Catmsegccstatusuppvclrangetable <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.Catmsegccstatusuppvclrangetable>`
    
    .. attribute:: catmendccstatusuppvclrangetable
    
    	A table indicating more than one VCLs in a consecutive range and for each VCL there is an active row in the atmVclTable having an atmVclConnKind value of `pvc' and End\-to\-End CC OAM status to have detected as recovered in the last corresponding PVC notification 
    	**type**\:  :py:class:`Catmendccstatusuppvclrangetable <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.Catmendccstatusuppvclrangetable>`
    
    .. attribute:: catmaisrdistatusuppvclrangetable
    
    	A table indicating more than one VCLs in a consecutive range and for each VCL there is an active row in the atmVclTable having an atmVclConnKind value of `pvc' and AISRDI OAM status to have detected as recovered in the last corresponding PVC notification 
    	**type**\:  :py:class:`Catmaisrdistatusuppvclrangetable <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.Catmaisrdistatusuppvclrangetable>`
    
    .. attribute:: catmuppvclrangetable
    
    	A table indicating more than one VCLs in a consecutive  range and for each VCL there is an active row in the  atmVclTable having an atmVclConnKind value of `pvc' and atmVclOperStatus to have detected as Up in the last corresponding PVC notification 
    	**type**\:  :py:class:`Catmuppvclrangetable <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.Catmuppvclrangetable>`
    
    

    """

    _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
    _revision = '2003-01-20'

    def __init__(self):
        super(CISCOATMPVCTRAPEXTNMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-ATM-PVCTRAP-EXTN-MIB"
        self.yang_parent_name = "CISCO-ATM-PVCTRAP-EXTN-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"catmCurStatChangePVclTable" : ("catmcurstatchangepvcltable", CISCOATMPVCTRAPEXTNMIB.Catmcurstatchangepvcltable), "catmStatusChangePVclRangeTable" : ("catmstatuschangepvclrangetable", CISCOATMPVCTRAPEXTNMIB.Catmstatuschangepvclrangetable), "catmSegCCStatusChPVclRangeTable" : ("catmsegccstatuschpvclrangetable", CISCOATMPVCTRAPEXTNMIB.Catmsegccstatuschpvclrangetable), "catmEndCCStatusChPVclRangeTable" : ("catmendccstatuschpvclrangetable", CISCOATMPVCTRAPEXTNMIB.Catmendccstatuschpvclrangetable), "catmAISRDIStatusChPVclRangeTable" : ("catmaisrdistatuschpvclrangetable", CISCOATMPVCTRAPEXTNMIB.Catmaisrdistatuschpvclrangetable), "catmDownPVclRangeTable" : ("catmdownpvclrangetable", CISCOATMPVCTRAPEXTNMIB.Catmdownpvclrangetable), "catmCurStatusUpPVclTable" : ("catmcurstatusuppvcltable", CISCOATMPVCTRAPEXTNMIB.Catmcurstatusuppvcltable), "catmStatusUpPVclRangeTable" : ("catmstatusuppvclrangetable", CISCOATMPVCTRAPEXTNMIB.Catmstatusuppvclrangetable), "catmSegCCStatusUpPVclRangeTable" : ("catmsegccstatusuppvclrangetable", CISCOATMPVCTRAPEXTNMIB.Catmsegccstatusuppvclrangetable), "catmEndCCStatusUpPVclRangeTable" : ("catmendccstatusuppvclrangetable", CISCOATMPVCTRAPEXTNMIB.Catmendccstatusuppvclrangetable), "catmAISRDIStatusUpPVclRangeTable" : ("catmaisrdistatusuppvclrangetable", CISCOATMPVCTRAPEXTNMIB.Catmaisrdistatusuppvclrangetable), "catmUpPVclRangeTable" : ("catmuppvclrangetable", CISCOATMPVCTRAPEXTNMIB.Catmuppvclrangetable)}
        self._child_list_classes = {}

        self.catmcurstatchangepvcltable = CISCOATMPVCTRAPEXTNMIB.Catmcurstatchangepvcltable()
        self.catmcurstatchangepvcltable.parent = self
        self._children_name_map["catmcurstatchangepvcltable"] = "catmCurStatChangePVclTable"
        self._children_yang_names.add("catmCurStatChangePVclTable")

        self.catmstatuschangepvclrangetable = CISCOATMPVCTRAPEXTNMIB.Catmstatuschangepvclrangetable()
        self.catmstatuschangepvclrangetable.parent = self
        self._children_name_map["catmstatuschangepvclrangetable"] = "catmStatusChangePVclRangeTable"
        self._children_yang_names.add("catmStatusChangePVclRangeTable")

        self.catmsegccstatuschpvclrangetable = CISCOATMPVCTRAPEXTNMIB.Catmsegccstatuschpvclrangetable()
        self.catmsegccstatuschpvclrangetable.parent = self
        self._children_name_map["catmsegccstatuschpvclrangetable"] = "catmSegCCStatusChPVclRangeTable"
        self._children_yang_names.add("catmSegCCStatusChPVclRangeTable")

        self.catmendccstatuschpvclrangetable = CISCOATMPVCTRAPEXTNMIB.Catmendccstatuschpvclrangetable()
        self.catmendccstatuschpvclrangetable.parent = self
        self._children_name_map["catmendccstatuschpvclrangetable"] = "catmEndCCStatusChPVclRangeTable"
        self._children_yang_names.add("catmEndCCStatusChPVclRangeTable")

        self.catmaisrdistatuschpvclrangetable = CISCOATMPVCTRAPEXTNMIB.Catmaisrdistatuschpvclrangetable()
        self.catmaisrdistatuschpvclrangetable.parent = self
        self._children_name_map["catmaisrdistatuschpvclrangetable"] = "catmAISRDIStatusChPVclRangeTable"
        self._children_yang_names.add("catmAISRDIStatusChPVclRangeTable")

        self.catmdownpvclrangetable = CISCOATMPVCTRAPEXTNMIB.Catmdownpvclrangetable()
        self.catmdownpvclrangetable.parent = self
        self._children_name_map["catmdownpvclrangetable"] = "catmDownPVclRangeTable"
        self._children_yang_names.add("catmDownPVclRangeTable")

        self.catmcurstatusuppvcltable = CISCOATMPVCTRAPEXTNMIB.Catmcurstatusuppvcltable()
        self.catmcurstatusuppvcltable.parent = self
        self._children_name_map["catmcurstatusuppvcltable"] = "catmCurStatusUpPVclTable"
        self._children_yang_names.add("catmCurStatusUpPVclTable")

        self.catmstatusuppvclrangetable = CISCOATMPVCTRAPEXTNMIB.Catmstatusuppvclrangetable()
        self.catmstatusuppvclrangetable.parent = self
        self._children_name_map["catmstatusuppvclrangetable"] = "catmStatusUpPVclRangeTable"
        self._children_yang_names.add("catmStatusUpPVclRangeTable")

        self.catmsegccstatusuppvclrangetable = CISCOATMPVCTRAPEXTNMIB.Catmsegccstatusuppvclrangetable()
        self.catmsegccstatusuppvclrangetable.parent = self
        self._children_name_map["catmsegccstatusuppvclrangetable"] = "catmSegCCStatusUpPVclRangeTable"
        self._children_yang_names.add("catmSegCCStatusUpPVclRangeTable")

        self.catmendccstatusuppvclrangetable = CISCOATMPVCTRAPEXTNMIB.Catmendccstatusuppvclrangetable()
        self.catmendccstatusuppvclrangetable.parent = self
        self._children_name_map["catmendccstatusuppvclrangetable"] = "catmEndCCStatusUpPVclRangeTable"
        self._children_yang_names.add("catmEndCCStatusUpPVclRangeTable")

        self.catmaisrdistatusuppvclrangetable = CISCOATMPVCTRAPEXTNMIB.Catmaisrdistatusuppvclrangetable()
        self.catmaisrdistatusuppvclrangetable.parent = self
        self._children_name_map["catmaisrdistatusuppvclrangetable"] = "catmAISRDIStatusUpPVclRangeTable"
        self._children_yang_names.add("catmAISRDIStatusUpPVclRangeTable")

        self.catmuppvclrangetable = CISCOATMPVCTRAPEXTNMIB.Catmuppvclrangetable()
        self.catmuppvclrangetable.parent = self
        self._children_name_map["catmuppvclrangetable"] = "catmUpPVclRangeTable"
        self._children_yang_names.add("catmUpPVclRangeTable")
        self._segment_path = lambda: "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB"


    class Catmcurstatchangepvcltable(Entity):
        """
        A table indicating all VCLs for which there is an
        active row in the atmVclTable having an atmVclConnKind
        value of `pvc' and atmVclOperStatus to have changed in the
        last corresponding PVC notification.
        
        .. attribute:: catmcurstatchangepvclentry
        
        	Each entry in the table represents a VCL for which there is an active row in the atmVclTable having an atmVclConnKind value of `pvc' and atmVclOperStatus to have changed in the last corresponding PVC notification
        	**type**\: list of  		 :py:class:`Catmcurstatchangepvclentry <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.Catmcurstatchangepvcltable.Catmcurstatchangepvclentry>`
        
        

        """

        _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
        _revision = '2003-01-20'

        def __init__(self):
            super(CISCOATMPVCTRAPEXTNMIB.Catmcurstatchangepvcltable, self).__init__()

            self.yang_name = "catmCurStatChangePVclTable"
            self.yang_parent_name = "CISCO-ATM-PVCTRAP-EXTN-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"catmCurStatChangePVclEntry" : ("catmcurstatchangepvclentry", CISCOATMPVCTRAPEXTNMIB.Catmcurstatchangepvcltable.Catmcurstatchangepvclentry)}

            self.catmcurstatchangepvclentry = YList(self)
            self._segment_path = lambda: "catmCurStatChangePVclTable"
            self._absolute_path = lambda: "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOATMPVCTRAPEXTNMIB.Catmcurstatchangepvcltable, [], name, value)


        class Catmcurstatchangepvclentry(Entity):
            """
            Each entry in the table represents a VCL for which
            there is an active row in the atmVclTable having an
            atmVclConnKind value of `pvc' and atmVclOperStatus
            to have changed in the last corresponding PVC notification.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: atmvclvpi  <key>
            
            	
            	**type**\: int
            
            	**range:** 0..4095
            
            	**refers to**\:  :py:class:`atmvclvpi <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.Atmvcltable.Atmvclentry>`
            
            .. attribute:: atmvclvci  <key>
            
            	
            	**type**\: int
            
            	**range:** 0..65535
            
            	**refers to**\:  :py:class:`atmvclvci <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.Atmvcltable.Atmvclentry>`
            
            .. attribute:: catmpvclstatustransition
            
            	The number of state transitions that has happened  on this PVCL in the last corresponding notification
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclstatuschangestart
            
            	The time stamp at which this PVCL changed state for the first time in  the last corresponding notification
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclstatuschangeend
            
            	The time stamp of the last state change of this PVCL in the last corresponding notification
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclsegccstatustransition
            
            	The number of state transitions that has happened  on this PVCL in the last corresponding notification due to Segment CC OAM failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclsegccstatuschangestart
            
            	The time stamp at which this PVCL changed state for the first time in  the last corresponding notification due to Segment CC OAM failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclsegccstatuschangeend
            
            	The time stamp of the last state change of this PVCL in the last corresponding notification due to Segment CC OAM failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclendccstatustransition
            
            	The number of state transitions that has happened  on this PVCL in the last corresponding notification due to End CC OAM failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclendccstatuschangestart
            
            	The time stamp at which this PVCL changed state for the first time in  the last corresponding notification due to End CC OAM failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclendccstatuschangeend
            
            	The time stamp of the last state change of this PVCL in the last corresponding notification due to End CC OAM failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclaisrdistatustransition
            
            	The number of state transitions that has happened  on this PVCL in the last corresponding notification due to AIS RDI OAM failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclaisrdistatuschangestart
            
            	The time stamp at which this PVCL changed state for the first time in  the last corresponding notification due to AIS RDI OAM failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclaisrdistatuschangeend
            
            	The time stamp of the last state change of this PVCL in the last corresponding notification due to AIS RDI OAM failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclcurfailtime
            
            	The time stamp at which this PVCL changed state to DOWN last time in the last corresponding notification 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclprevrecovertime
            
            	The time stamp at which this PVCL changed state to UP last time in the previous corresponding notification 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclfailurereason
            
            	Type of OAM failure
            	**type**\:  :py:class:`CatmOAMFailureType <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CatmOAMFailureType>`
            
            

            """

            _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
            _revision = '2003-01-20'

            def __init__(self):
                super(CISCOATMPVCTRAPEXTNMIB.Catmcurstatchangepvcltable.Catmcurstatchangepvclentry, self).__init__()

                self.yang_name = "catmCurStatChangePVclEntry"
                self.yang_parent_name = "catmCurStatChangePVclTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.atmvclvpi = YLeaf(YType.str, "atmVclVpi")

                self.atmvclvci = YLeaf(YType.str, "atmVclVci")

                self.catmpvclstatustransition = YLeaf(YType.uint32, "catmPVclStatusTransition")

                self.catmpvclstatuschangestart = YLeaf(YType.uint32, "catmPVclStatusChangeStart")

                self.catmpvclstatuschangeend = YLeaf(YType.uint32, "catmPVclStatusChangeEnd")

                self.catmpvclsegccstatustransition = YLeaf(YType.uint32, "catmPVclSegCCStatusTransition")

                self.catmpvclsegccstatuschangestart = YLeaf(YType.uint32, "catmPVclSegCCStatusChangeStart")

                self.catmpvclsegccstatuschangeend = YLeaf(YType.uint32, "catmPVclSegCCStatusChangeEnd")

                self.catmpvclendccstatustransition = YLeaf(YType.uint32, "catmPVclEndCCStatusTransition")

                self.catmpvclendccstatuschangestart = YLeaf(YType.uint32, "catmPVclEndCCStatusChangeStart")

                self.catmpvclendccstatuschangeend = YLeaf(YType.uint32, "catmPVclEndCCStatusChangeEnd")

                self.catmpvclaisrdistatustransition = YLeaf(YType.uint32, "catmPVclAISRDIStatusTransition")

                self.catmpvclaisrdistatuschangestart = YLeaf(YType.uint32, "catmPVclAISRDIStatusChangeStart")

                self.catmpvclaisrdistatuschangeend = YLeaf(YType.uint32, "catmPVclAISRDIStatusChangeEnd")

                self.catmpvclcurfailtime = YLeaf(YType.uint32, "catmPVclCurFailTime")

                self.catmpvclprevrecovertime = YLeaf(YType.uint32, "catmPVclPrevRecoverTime")

                self.catmpvclfailurereason = YLeaf(YType.enumeration, "catmPVclFailureReason")
                self._segment_path = lambda: "catmCurStatChangePVclEntry" + "[ifIndex='" + self.ifindex.get() + "']" + "[atmVclVpi='" + self.atmvclvpi.get() + "']" + "[atmVclVci='" + self.atmvclvci.get() + "']"
                self._absolute_path = lambda: "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/catmCurStatChangePVclTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOATMPVCTRAPEXTNMIB.Catmcurstatchangepvcltable.Catmcurstatchangepvclentry, ['ifindex', 'atmvclvpi', 'atmvclvci', 'catmpvclstatustransition', 'catmpvclstatuschangestart', 'catmpvclstatuschangeend', 'catmpvclsegccstatustransition', 'catmpvclsegccstatuschangestart', 'catmpvclsegccstatuschangeend', 'catmpvclendccstatustransition', 'catmpvclendccstatuschangestart', 'catmpvclendccstatuschangeend', 'catmpvclaisrdistatustransition', 'catmpvclaisrdistatuschangestart', 'catmpvclaisrdistatuschangeend', 'catmpvclcurfailtime', 'catmpvclprevrecovertime', 'catmpvclfailurereason'], name, value)


    class Catmstatuschangepvclrangetable(Entity):
        """
        A table indicating more than one VCLs in a consecutive 
        range and for each VCL there is an active row in the 
        atmVclTable having an atmVclConnKind value of `pvc'
        and atmVclOperStatus to have changed in the same
        direction in the last corresponding PVC notification .
        
        .. attribute:: catmstatuschangepvclrangeentry
        
        	Each entry in this table represents a range of VCLs and  for each VCL there is an active row in the atmVclTable having an atmVclConnKind value of 'pvc' and atmVclOperStatus to have changed in the same direction in the last notification  interval
        	**type**\: list of  		 :py:class:`Catmstatuschangepvclrangeentry <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.Catmstatuschangepvclrangetable.Catmstatuschangepvclrangeentry>`
        
        

        """

        _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
        _revision = '2003-01-20'

        def __init__(self):
            super(CISCOATMPVCTRAPEXTNMIB.Catmstatuschangepvclrangetable, self).__init__()

            self.yang_name = "catmStatusChangePVclRangeTable"
            self.yang_parent_name = "CISCO-ATM-PVCTRAP-EXTN-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"catmStatusChangePVclRangeEntry" : ("catmstatuschangepvclrangeentry", CISCOATMPVCTRAPEXTNMIB.Catmstatuschangepvclrangetable.Catmstatuschangepvclrangeentry)}

            self.catmstatuschangepvclrangeentry = YList(self)
            self._segment_path = lambda: "catmStatusChangePVclRangeTable"
            self._absolute_path = lambda: "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOATMPVCTRAPEXTNMIB.Catmstatuschangepvclrangetable, [], name, value)


        class Catmstatuschangepvclrangeentry(Entity):
            """
            Each entry in this table represents a range of VCLs and 
            for each VCL there is an active row in the atmVclTable having
            an atmVclConnKind value of 'pvc' and atmVclOperStatus to have
            changed in the same direction in the last notification 
            interval.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: atmvclvpi  <key>
            
            	
            	**type**\: int
            
            	**range:** 0..4095
            
            	**refers to**\:  :py:class:`atmvclvpi <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.Atmvcltable.Atmvclentry>`
            
            .. attribute:: catmstatuschangepvclrangeindex  <key>
            
            	Index to represent different ranges, the first range is indexed by value 0, the second by 1 and so on..
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: catmpvcllowerrangevalue
            
            	The first PVCL in a range of PVCLs for which the  atmVclOperStatus to have changed in the last  corresponding notification due to Loopback OAM failure
            	**type**\: int
            
            	**range:** 0..65536
            
            .. attribute:: catmpvclhigherrangevalue
            
            	The last PVCL in a range of PVCLs for which the  atmOperStatus to have changed in the last  corresponding notification due to Loopback OAM failure
            	**type**\: int
            
            	**range:** 0..65536
            
            .. attribute:: catmpvclrangestatuschangestart
            
            	The time stamp at which the first PVCL in the range changed state in the last corresponding notification due  to Loopback OAM failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclrangestatuschangeend
            
            	The time stamp at which the last PVCL in the range changed state in the last corresponding notification due  to Loopback OAM failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
            _revision = '2003-01-20'

            def __init__(self):
                super(CISCOATMPVCTRAPEXTNMIB.Catmstatuschangepvclrangetable.Catmstatuschangepvclrangeentry, self).__init__()

                self.yang_name = "catmStatusChangePVclRangeEntry"
                self.yang_parent_name = "catmStatusChangePVclRangeTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.atmvclvpi = YLeaf(YType.str, "atmVclVpi")

                self.catmstatuschangepvclrangeindex = YLeaf(YType.int32, "catmStatusChangePVclRangeIndex")

                self.catmpvcllowerrangevalue = YLeaf(YType.int32, "catmPVclLowerRangeValue")

                self.catmpvclhigherrangevalue = YLeaf(YType.int32, "catmPVclHigherRangeValue")

                self.catmpvclrangestatuschangestart = YLeaf(YType.uint32, "catmPVclRangeStatusChangeStart")

                self.catmpvclrangestatuschangeend = YLeaf(YType.uint32, "catmPVclRangeStatusChangeEnd")
                self._segment_path = lambda: "catmStatusChangePVclRangeEntry" + "[ifIndex='" + self.ifindex.get() + "']" + "[atmVclVpi='" + self.atmvclvpi.get() + "']" + "[catmStatusChangePVclRangeIndex='" + self.catmstatuschangepvclrangeindex.get() + "']"
                self._absolute_path = lambda: "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/catmStatusChangePVclRangeTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOATMPVCTRAPEXTNMIB.Catmstatuschangepvclrangetable.Catmstatuschangepvclrangeentry, ['ifindex', 'atmvclvpi', 'catmstatuschangepvclrangeindex', 'catmpvcllowerrangevalue', 'catmpvclhigherrangevalue', 'catmpvclrangestatuschangestart', 'catmpvclrangestatuschangeend'], name, value)


    class Catmsegccstatuschpvclrangetable(Entity):
        """
        A table indicating more than one VCLs in a consecutive 
        range and for each VCL there is an active row in the 
        atmVclTable having an atmVclConnKind value of `pvc'
        and atmVclOperStatus to have changed due to segment CC 
        failure in the same direction in the last PVC 
        corresponding notification .
        
        .. attribute:: catmsegccstatuschpvclrangeentry
        
        	Each entry in this table represents a range of VCLs and  for each VCL there is an active row in the atmVclTable having an atmVclConnKind value of 'pvc' and atmVclOperStatus to have changed due to segment CC failure in the same direction  in the last corresponding notification 
        	**type**\: list of  		 :py:class:`Catmsegccstatuschpvclrangeentry <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.Catmsegccstatuschpvclrangetable.Catmsegccstatuschpvclrangeentry>`
        
        

        """

        _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
        _revision = '2003-01-20'

        def __init__(self):
            super(CISCOATMPVCTRAPEXTNMIB.Catmsegccstatuschpvclrangetable, self).__init__()

            self.yang_name = "catmSegCCStatusChPVclRangeTable"
            self.yang_parent_name = "CISCO-ATM-PVCTRAP-EXTN-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"catmSegCCStatusChPVclRangeEntry" : ("catmsegccstatuschpvclrangeentry", CISCOATMPVCTRAPEXTNMIB.Catmsegccstatuschpvclrangetable.Catmsegccstatuschpvclrangeentry)}

            self.catmsegccstatuschpvclrangeentry = YList(self)
            self._segment_path = lambda: "catmSegCCStatusChPVclRangeTable"
            self._absolute_path = lambda: "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOATMPVCTRAPEXTNMIB.Catmsegccstatuschpvclrangetable, [], name, value)


        class Catmsegccstatuschpvclrangeentry(Entity):
            """
            Each entry in this table represents a range of VCLs and 
            for each VCL there is an active row in the atmVclTable having
            an atmVclConnKind value of 'pvc' and atmVclOperStatus to have
            changed due to segment CC failure in the same direction 
            in the last corresponding notification .
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: atmvclvpi  <key>
            
            	
            	**type**\: int
            
            	**range:** 0..4095
            
            	**refers to**\:  :py:class:`atmvclvpi <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.Atmvcltable.Atmvclentry>`
            
            .. attribute:: catmstatuschangepvclrangeindex  <key>
            
            	
            	**type**\: int
            
            	**range:** 0..65535
            
            	**refers to**\:  :py:class:`catmstatuschangepvclrangeindex <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.Catmstatuschangepvclrangetable.Catmstatuschangepvclrangeentry>`
            
            .. attribute:: catmpvclsegcclowerrangevalue
            
            	The first PVCL in a range of PVCLs for which the  atmVclOperStatus to have changed in the last  corresponding notification due to Segment CC OAM failure
            	**type**\: int
            
            	**range:** 0..65536
            
            .. attribute:: catmpvclsegcchigherrangevalue
            
            	The last PVCL in a range of PVCLs for which the  atmOperStatus to have changed in the last  corresponding notification due to Segment CC OAM failure
            	**type**\: int
            
            	**range:** 0..65536
            
            .. attribute:: catmpvclsegccrangestatuschstart
            
            	The time stamp at which the first PVCL in the range changed state in the last corresponding notification due  to Segment CC OAM failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclsegccrangestatuschend
            
            	The time stamp at which the last PVCL in the range changed state in the last corresponding notification due  to Segment CC OAM failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
            _revision = '2003-01-20'

            def __init__(self):
                super(CISCOATMPVCTRAPEXTNMIB.Catmsegccstatuschpvclrangetable.Catmsegccstatuschpvclrangeentry, self).__init__()

                self.yang_name = "catmSegCCStatusChPVclRangeEntry"
                self.yang_parent_name = "catmSegCCStatusChPVclRangeTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.atmvclvpi = YLeaf(YType.str, "atmVclVpi")

                self.catmstatuschangepvclrangeindex = YLeaf(YType.str, "catmStatusChangePVclRangeIndex")

                self.catmpvclsegcclowerrangevalue = YLeaf(YType.int32, "catmPVclSegCCLowerRangeValue")

                self.catmpvclsegcchigherrangevalue = YLeaf(YType.int32, "catmPVclSegCCHigherRangeValue")

                self.catmpvclsegccrangestatuschstart = YLeaf(YType.uint32, "catmPVclSegCCRangeStatusChStart")

                self.catmpvclsegccrangestatuschend = YLeaf(YType.uint32, "catmPVclSegCCRangeStatusChEnd")
                self._segment_path = lambda: "catmSegCCStatusChPVclRangeEntry" + "[ifIndex='" + self.ifindex.get() + "']" + "[atmVclVpi='" + self.atmvclvpi.get() + "']" + "[catmStatusChangePVclRangeIndex='" + self.catmstatuschangepvclrangeindex.get() + "']"
                self._absolute_path = lambda: "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/catmSegCCStatusChPVclRangeTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOATMPVCTRAPEXTNMIB.Catmsegccstatuschpvclrangetable.Catmsegccstatuschpvclrangeentry, ['ifindex', 'atmvclvpi', 'catmstatuschangepvclrangeindex', 'catmpvclsegcclowerrangevalue', 'catmpvclsegcchigherrangevalue', 'catmpvclsegccrangestatuschstart', 'catmpvclsegccrangestatuschend'], name, value)


    class Catmendccstatuschpvclrangetable(Entity):
        """
        A table indicating more than one VCLs in a consecutive 
        range and for each VCL there is an active row in the 
        atmVclTable having an atmVclConnKind value of `pvc'
        and atmVclOperStatus to have changed due to End CC failure
        in the same direction in the last PVC notification 
        interval.
        
        .. attribute:: catmendccstatuschpvclrangeentry
        
        	Each entry in this table represents a range of VCLs and  for each VCL there is an active row in the atmVclTable having an atmVclConnKind value of 'pvc' and atmVclOperStatus to have changed due to End CC failure in the same direction in the  last corresponding notification 
        	**type**\: list of  		 :py:class:`Catmendccstatuschpvclrangeentry <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.Catmendccstatuschpvclrangetable.Catmendccstatuschpvclrangeentry>`
        
        

        """

        _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
        _revision = '2003-01-20'

        def __init__(self):
            super(CISCOATMPVCTRAPEXTNMIB.Catmendccstatuschpvclrangetable, self).__init__()

            self.yang_name = "catmEndCCStatusChPVclRangeTable"
            self.yang_parent_name = "CISCO-ATM-PVCTRAP-EXTN-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"catmEndCCStatusChPVclRangeEntry" : ("catmendccstatuschpvclrangeentry", CISCOATMPVCTRAPEXTNMIB.Catmendccstatuschpvclrangetable.Catmendccstatuschpvclrangeentry)}

            self.catmendccstatuschpvclrangeentry = YList(self)
            self._segment_path = lambda: "catmEndCCStatusChPVclRangeTable"
            self._absolute_path = lambda: "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOATMPVCTRAPEXTNMIB.Catmendccstatuschpvclrangetable, [], name, value)


        class Catmendccstatuschpvclrangeentry(Entity):
            """
            Each entry in this table represents a range of VCLs and 
            for each VCL there is an active row in the atmVclTable having
            an atmVclConnKind value of 'pvc' and atmVclOperStatus to have
            changed due to End CC failure in the same direction in the 
            last corresponding notification .
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: atmvclvpi  <key>
            
            	
            	**type**\: int
            
            	**range:** 0..4095
            
            	**refers to**\:  :py:class:`atmvclvpi <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.Atmvcltable.Atmvclentry>`
            
            .. attribute:: catmstatuschangepvclrangeindex  <key>
            
            	
            	**type**\: int
            
            	**range:** 0..65535
            
            	**refers to**\:  :py:class:`catmstatuschangepvclrangeindex <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.Catmstatuschangepvclrangetable.Catmstatuschangepvclrangeentry>`
            
            .. attribute:: catmpvclendcclowerrangevalue
            
            	The first PVCL in a range of PVCLs for which the  atmVclOperStatus to have changed in the last  corresponding notification due to End CC OAM failure
            	**type**\: int
            
            	**range:** 0..65536
            
            .. attribute:: catmpvclendcchigherrangevalue
            
            	The last PVCL in a range of PVCLs for which the  atmOperStatus to have changed in the last  corresponding notification due to End CC OAM failure
            	**type**\: int
            
            	**range:** 0..65536
            
            .. attribute:: catmpvclendccrangestatuschstart
            
            	The time stamp at which the first PVCL in the range changed state in the last corresponding notification due  to End CC OAM failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclendccrangestatuschend
            
            	The time stamp at which the last PVCL in the range changed state in the last corresponding notification due  to End CC OAM failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
            _revision = '2003-01-20'

            def __init__(self):
                super(CISCOATMPVCTRAPEXTNMIB.Catmendccstatuschpvclrangetable.Catmendccstatuschpvclrangeentry, self).__init__()

                self.yang_name = "catmEndCCStatusChPVclRangeEntry"
                self.yang_parent_name = "catmEndCCStatusChPVclRangeTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.atmvclvpi = YLeaf(YType.str, "atmVclVpi")

                self.catmstatuschangepvclrangeindex = YLeaf(YType.str, "catmStatusChangePVclRangeIndex")

                self.catmpvclendcclowerrangevalue = YLeaf(YType.int32, "catmPVclEndCCLowerRangeValue")

                self.catmpvclendcchigherrangevalue = YLeaf(YType.int32, "catmPVclEndCCHigherRangeValue")

                self.catmpvclendccrangestatuschstart = YLeaf(YType.uint32, "catmPVclEndCCRangeStatusChStart")

                self.catmpvclendccrangestatuschend = YLeaf(YType.uint32, "catmPVclEndCCRangeStatusChEnd")
                self._segment_path = lambda: "catmEndCCStatusChPVclRangeEntry" + "[ifIndex='" + self.ifindex.get() + "']" + "[atmVclVpi='" + self.atmvclvpi.get() + "']" + "[catmStatusChangePVclRangeIndex='" + self.catmstatuschangepvclrangeindex.get() + "']"
                self._absolute_path = lambda: "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/catmEndCCStatusChPVclRangeTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOATMPVCTRAPEXTNMIB.Catmendccstatuschpvclrangetable.Catmendccstatuschpvclrangeentry, ['ifindex', 'atmvclvpi', 'catmstatuschangepvclrangeindex', 'catmpvclendcclowerrangevalue', 'catmpvclendcchigherrangevalue', 'catmpvclendccrangestatuschstart', 'catmpvclendccrangestatuschend'], name, value)


    class Catmaisrdistatuschpvclrangetable(Entity):
        """
        A table indicating more than one VCLs in a consecutive 
        range and for each VCL there is an active row in the 
        atmVclTable having an atmVclConnKind value of `pvc'
        and atmVclOperStatus to have changed due to AIS/RDI failure
        in the same direction in the last corresponding PVC 
        notification.
        
        .. attribute:: catmaisrdistatuschpvclrangeentry
        
        	Each entry in this table represents a range of VCLs and  for each VCL there is an active row in the atmVclTable having an atmVclConnKind value of 'pvc' and atmVclOperStatus to have changed due to AIS/RDI failure in the same direction in the  last corresponding notification 
        	**type**\: list of  		 :py:class:`Catmaisrdistatuschpvclrangeentry <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.Catmaisrdistatuschpvclrangetable.Catmaisrdistatuschpvclrangeentry>`
        
        

        """

        _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
        _revision = '2003-01-20'

        def __init__(self):
            super(CISCOATMPVCTRAPEXTNMIB.Catmaisrdistatuschpvclrangetable, self).__init__()

            self.yang_name = "catmAISRDIStatusChPVclRangeTable"
            self.yang_parent_name = "CISCO-ATM-PVCTRAP-EXTN-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"catmAISRDIStatusChPVclRangeEntry" : ("catmaisrdistatuschpvclrangeentry", CISCOATMPVCTRAPEXTNMIB.Catmaisrdistatuschpvclrangetable.Catmaisrdistatuschpvclrangeentry)}

            self.catmaisrdistatuschpvclrangeentry = YList(self)
            self._segment_path = lambda: "catmAISRDIStatusChPVclRangeTable"
            self._absolute_path = lambda: "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOATMPVCTRAPEXTNMIB.Catmaisrdistatuschpvclrangetable, [], name, value)


        class Catmaisrdistatuschpvclrangeentry(Entity):
            """
            Each entry in this table represents a range of VCLs and 
            for each VCL there is an active row in the atmVclTable having
            an atmVclConnKind value of 'pvc' and atmVclOperStatus to have
            changed due to AIS/RDI failure in the same direction in the 
            last corresponding notification .
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: atmvclvpi  <key>
            
            	
            	**type**\: int
            
            	**range:** 0..4095
            
            	**refers to**\:  :py:class:`atmvclvpi <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.Atmvcltable.Atmvclentry>`
            
            .. attribute:: catmstatuschangepvclrangeindex  <key>
            
            	
            	**type**\: int
            
            	**range:** 0..65535
            
            	**refers to**\:  :py:class:`catmstatuschangepvclrangeindex <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.Catmstatuschangepvclrangetable.Catmstatuschangepvclrangeentry>`
            
            .. attribute:: catmpvclaisrdilowerrangevalue
            
            	The first PVCL in a range of PVCLs for which the  atmVclOperStatus to have changed in the last  corresponding notification due to AISRDI OAM failure
            	**type**\: int
            
            	**range:** 0..65536
            
            .. attribute:: catmpvclaisrdihigherrangevalue
            
            	The last PVCL in a range of PVCLs for which the  atmOperStatus to have changed in the last  corresponding notification due to AISRDI OAM failure
            	**type**\: int
            
            	**range:** 0..65536
            
            .. attribute:: catmpvclaisrdirangestatuschstart
            
            	The time stamp at which the first PVCL in the range changed state in the last corresponding notification due  to AISRDI OAM failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclaisrdirangestatuschend
            
            	The time stamp at which the last PVCL in the range changed state in the last corresponding notification due  to AISRDI OAM failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
            _revision = '2003-01-20'

            def __init__(self):
                super(CISCOATMPVCTRAPEXTNMIB.Catmaisrdistatuschpvclrangetable.Catmaisrdistatuschpvclrangeentry, self).__init__()

                self.yang_name = "catmAISRDIStatusChPVclRangeEntry"
                self.yang_parent_name = "catmAISRDIStatusChPVclRangeTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.atmvclvpi = YLeaf(YType.str, "atmVclVpi")

                self.catmstatuschangepvclrangeindex = YLeaf(YType.str, "catmStatusChangePVclRangeIndex")

                self.catmpvclaisrdilowerrangevalue = YLeaf(YType.int32, "catmPVclAISRDILowerRangeValue")

                self.catmpvclaisrdihigherrangevalue = YLeaf(YType.int32, "catmPVclAISRDIHigherRangeValue")

                self.catmpvclaisrdirangestatuschstart = YLeaf(YType.uint32, "catmPVclAISRDIRangeStatusChStart")

                self.catmpvclaisrdirangestatuschend = YLeaf(YType.uint32, "catmPVclAISRDIRangeStatusChEnd")
                self._segment_path = lambda: "catmAISRDIStatusChPVclRangeEntry" + "[ifIndex='" + self.ifindex.get() + "']" + "[atmVclVpi='" + self.atmvclvpi.get() + "']" + "[catmStatusChangePVclRangeIndex='" + self.catmstatuschangepvclrangeindex.get() + "']"
                self._absolute_path = lambda: "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/catmAISRDIStatusChPVclRangeTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOATMPVCTRAPEXTNMIB.Catmaisrdistatuschpvclrangetable.Catmaisrdistatuschpvclrangeentry, ['ifindex', 'atmvclvpi', 'catmstatuschangepvclrangeindex', 'catmpvclaisrdilowerrangevalue', 'catmpvclaisrdihigherrangevalue', 'catmpvclaisrdirangestatuschstart', 'catmpvclaisrdirangestatuschend'], name, value)


    class Catmdownpvclrangetable(Entity):
        """
        A table indicating more than one VCLs in a consecutive 
        range and for each VCL there is an active row in the 
        atmVclTable having an atmVclConnKind value of `pvc'
        and atmVclOperStatus to have detected as Down
        in the last corresponding PVC notification .
        
        .. attribute:: catmdownpvclrangeentry
        
        	Each entry in this table represents a range of VCLs and  for each VCL there is an active row in the atmVclTable having an atmVclConnKind value of 'pvc' and  atmVclOperStatus to  have detected as Down in the last notification  interval
        	**type**\: list of  		 :py:class:`Catmdownpvclrangeentry <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.Catmdownpvclrangetable.Catmdownpvclrangeentry>`
        
        

        """

        _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
        _revision = '2003-01-20'

        def __init__(self):
            super(CISCOATMPVCTRAPEXTNMIB.Catmdownpvclrangetable, self).__init__()

            self.yang_name = "catmDownPVclRangeTable"
            self.yang_parent_name = "CISCO-ATM-PVCTRAP-EXTN-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"catmDownPVclRangeEntry" : ("catmdownpvclrangeentry", CISCOATMPVCTRAPEXTNMIB.Catmdownpvclrangetable.Catmdownpvclrangeentry)}

            self.catmdownpvclrangeentry = YList(self)
            self._segment_path = lambda: "catmDownPVclRangeTable"
            self._absolute_path = lambda: "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOATMPVCTRAPEXTNMIB.Catmdownpvclrangetable, [], name, value)


        class Catmdownpvclrangeentry(Entity):
            """
            Each entry in this table represents a range of VCLs and 
            for each VCL there is an active row in the atmVclTable having
            an atmVclConnKind value of 'pvc' and  atmVclOperStatus to 
            have detected as Down in the last notification 
            interval.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: atmvclvpi  <key>
            
            	
            	**type**\: int
            
            	**range:** 0..4095
            
            	**refers to**\:  :py:class:`atmvclvpi <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.Atmvcltable.Atmvclentry>`
            
            .. attribute:: catmstatuschangepvclrangeindex  <key>
            
            	
            	**type**\: int
            
            	**range:** 0..65535
            
            	**refers to**\:  :py:class:`catmstatuschangepvclrangeindex <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.Catmstatuschangepvclrangetable.Catmstatuschangepvclrangeentry>`
            
            .. attribute:: catmdownpvcllowerrangevalue
            
            	The first PVCL in a range of PVCLs for which the  atmVclOperStatus has been detected as Down in the  corresponding notification 
            	**type**\: int
            
            	**range:** 0..65536
            
            .. attribute:: catmdownpvclhigherrangevalue
            
            	The last PVCL in a range of PVCLs for which the  atmVclOperStatus has been detected as Down in the  corresponding notification 
            	**type**\: int
            
            	**range:** 0..65536
            
            .. attribute:: catmdownpvclrangestart
            
            	The time stamp at which the first atmVclOperStatus is detected as Down on any of the PVCLs in the range in the corresponding notification 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmdownpvclrangeend
            
            	The time stamp at which the last atmVclOperStatus is detected as Down on any of the PVCLs in the range in the corresponding notification 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmprevuppvclrangestart
            
            	The time stamp at which the first atmVclOperStatus is detected as Up on any of the PVCLs in the range in the previous catmIntfPvcUp2Trap notification
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmprevuppvclrangeend
            
            	The time stamp at which the last atmVclOperStatus is detected as Up on any of the PVCLs in the range in the previous catmIntfPvcUp2Trap notification
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclrangefailurereason
            
            	Type of OAM failure
            	**type**\:  :py:class:`CatmOAMFailureType <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CatmOAMFailureType>`
            
            

            """

            _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
            _revision = '2003-01-20'

            def __init__(self):
                super(CISCOATMPVCTRAPEXTNMIB.Catmdownpvclrangetable.Catmdownpvclrangeentry, self).__init__()

                self.yang_name = "catmDownPVclRangeEntry"
                self.yang_parent_name = "catmDownPVclRangeTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.atmvclvpi = YLeaf(YType.str, "atmVclVpi")

                self.catmstatuschangepvclrangeindex = YLeaf(YType.str, "catmStatusChangePVclRangeIndex")

                self.catmdownpvcllowerrangevalue = YLeaf(YType.int32, "catmDownPVclLowerRangeValue")

                self.catmdownpvclhigherrangevalue = YLeaf(YType.int32, "catmDownPVclHigherRangeValue")

                self.catmdownpvclrangestart = YLeaf(YType.uint32, "catmDownPVclRangeStart")

                self.catmdownpvclrangeend = YLeaf(YType.uint32, "catmDownPVclRangeEnd")

                self.catmprevuppvclrangestart = YLeaf(YType.uint32, "catmPrevUpPVclRangeStart")

                self.catmprevuppvclrangeend = YLeaf(YType.uint32, "catmPrevUpPVclRangeEnd")

                self.catmpvclrangefailurereason = YLeaf(YType.enumeration, "catmPVclRangeFailureReason")
                self._segment_path = lambda: "catmDownPVclRangeEntry" + "[ifIndex='" + self.ifindex.get() + "']" + "[atmVclVpi='" + self.atmvclvpi.get() + "']" + "[catmStatusChangePVclRangeIndex='" + self.catmstatuschangepvclrangeindex.get() + "']"
                self._absolute_path = lambda: "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/catmDownPVclRangeTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOATMPVCTRAPEXTNMIB.Catmdownpvclrangetable.Catmdownpvclrangeentry, ['ifindex', 'atmvclvpi', 'catmstatuschangepvclrangeindex', 'catmdownpvcllowerrangevalue', 'catmdownpvclhigherrangevalue', 'catmdownpvclrangestart', 'catmdownpvclrangeend', 'catmprevuppvclrangestart', 'catmprevuppvclrangeend', 'catmpvclrangefailurereason'], name, value)


    class Catmcurstatusuppvcltable(Entity):
        """
        A table indicating all VCLs for which there is an
        active row in the atmVclTable having an atmVclConnKind
        value of `pvc' and atmVclOperStatus to have changed to UP
        in the last corresponding PVC notification .
        
        .. attribute:: catmcurstatusuppvclentry
        
        	Each entry in the table represents a VCL for which there is an active row in the atmVclTable having an atmVclConnKind value of `pvc' and atmVclOperStatus to have changed to UP in the last PVC notification  interval
        	**type**\: list of  		 :py:class:`Catmcurstatusuppvclentry <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.Catmcurstatusuppvcltable.Catmcurstatusuppvclentry>`
        
        

        """

        _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
        _revision = '2003-01-20'

        def __init__(self):
            super(CISCOATMPVCTRAPEXTNMIB.Catmcurstatusuppvcltable, self).__init__()

            self.yang_name = "catmCurStatusUpPVclTable"
            self.yang_parent_name = "CISCO-ATM-PVCTRAP-EXTN-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"catmCurStatusUpPVclEntry" : ("catmcurstatusuppvclentry", CISCOATMPVCTRAPEXTNMIB.Catmcurstatusuppvcltable.Catmcurstatusuppvclentry)}

            self.catmcurstatusuppvclentry = YList(self)
            self._segment_path = lambda: "catmCurStatusUpPVclTable"
            self._absolute_path = lambda: "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOATMPVCTRAPEXTNMIB.Catmcurstatusuppvcltable, [], name, value)


        class Catmcurstatusuppvclentry(Entity):
            """
            Each entry in the table represents a VCL for which
            there is an active row in the atmVclTable having an
            atmVclConnKind value of `pvc' and atmVclOperStatus
            to have changed to UP in the last PVC notification 
            interval.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: atmvclvpi  <key>
            
            	
            	**type**\: int
            
            	**range:** 0..4095
            
            	**refers to**\:  :py:class:`atmvclvpi <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.Atmvcltable.Atmvclentry>`
            
            .. attribute:: atmvclvci  <key>
            
            	
            	**type**\: int
            
            	**range:** 0..65535
            
            	**refers to**\:  :py:class:`atmvclvci <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.Atmvcltable.Atmvclentry>`
            
            .. attribute:: catmpvclstatusuptransition
            
            	The number of Down to Up state transitions due to OAM loopback recovery that has happened on this PVCL  in the last corresponding notification 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclstatusupstart
            
            	The time stamp at which this PVCL changed state to UP  for the first time due to OAM loopback recovery in the last corresponding notification 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclstatusupend
            
            	The time stamp at which this PVCL changed state to UP  for the last time due to OAM loopback recovery in the last corresponding notification 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclsegccstatusuptransition
            
            	The number of Down to Up state transitions that has  happened on this PVCL in the last corresponding notification  due to Segment CC OAM recovery
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclsegccstatusupstart
            
            	The time stamp at which this PVCL changed state to Up for  the first time in the last corresponding notification due to Segment CC OAM recovery
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclsegccstatusupend
            
            	The time stamp of the last state change of this PVCL in the last corresponding notification due to Segment CC  OAM recovery
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclendccstatusuptransition
            
            	The number of Down to UP state transitions that has  happened on this PVCL in the last notification  interval due to End CC OAM recovery
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclendccstatusupstart
            
            	The time stamp at which this PVCL changed state to Up for the first time in the last corresponding notification  due to End CC OAM recovery
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclendccstatusupend
            
            	The time stamp at which this PVCL changed state to Up for the last time in the last corresponding notification  due to End CC OAM recovery
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclaisrdistatusuptransition
            
            	The number of Down to Up state transitions that  has happened on this PVCL in the last notification  interval due to AIS RDI OAM recovery
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclaisrdistatusupstart
            
            	The time stamp at which this PVCL changed state to Up for the first time in the last corresponding notification  due to AIS/RDI OAM recovery
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclaisrdistatusupend
            
            	The time stamp at which this PVCL changed state to Up for the last time in the last corresponding notification  due to AIS/RDI OAM recovery
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclcurrecovertime
            
            	The time stamp at which this PVCL changed state to UP last time in the last corresponding notification 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclprevfailtime
            
            	The time stamp at which this PVCL changed state to DOWN last time in the previous corresponding notification 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclrecoveryreason
            
            	Type of OAM Recovered
            	**type**\:  :py:class:`CatmOAMRecoveryType <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CatmOAMRecoveryType>`
            
            

            """

            _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
            _revision = '2003-01-20'

            def __init__(self):
                super(CISCOATMPVCTRAPEXTNMIB.Catmcurstatusuppvcltable.Catmcurstatusuppvclentry, self).__init__()

                self.yang_name = "catmCurStatusUpPVclEntry"
                self.yang_parent_name = "catmCurStatusUpPVclTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.atmvclvpi = YLeaf(YType.str, "atmVclVpi")

                self.atmvclvci = YLeaf(YType.str, "atmVclVci")

                self.catmpvclstatusuptransition = YLeaf(YType.uint32, "catmPVclStatusUpTransition")

                self.catmpvclstatusupstart = YLeaf(YType.uint32, "catmPVclStatusUpStart")

                self.catmpvclstatusupend = YLeaf(YType.uint32, "catmPVclStatusUpEnd")

                self.catmpvclsegccstatusuptransition = YLeaf(YType.uint32, "catmPVclSegCCStatusUpTransition")

                self.catmpvclsegccstatusupstart = YLeaf(YType.uint32, "catmPVclSegCCStatusUpStart")

                self.catmpvclsegccstatusupend = YLeaf(YType.uint32, "catmPVclSegCCStatusUpEnd")

                self.catmpvclendccstatusuptransition = YLeaf(YType.uint32, "catmPVclEndCCStatusUpTransition")

                self.catmpvclendccstatusupstart = YLeaf(YType.uint32, "catmPVclEndCCStatusUpStart")

                self.catmpvclendccstatusupend = YLeaf(YType.uint32, "catmPVclEndCCStatusUpEnd")

                self.catmpvclaisrdistatusuptransition = YLeaf(YType.uint32, "catmPVclAISRDIStatusUpTransition")

                self.catmpvclaisrdistatusupstart = YLeaf(YType.uint32, "catmPVclAISRDIStatusUpStart")

                self.catmpvclaisrdistatusupend = YLeaf(YType.uint32, "catmPVclAISRDIStatusUpEnd")

                self.catmpvclcurrecovertime = YLeaf(YType.uint32, "catmPVclCurRecoverTime")

                self.catmpvclprevfailtime = YLeaf(YType.uint32, "catmPVclPrevFailTime")

                self.catmpvclrecoveryreason = YLeaf(YType.enumeration, "catmPVclRecoveryReason")
                self._segment_path = lambda: "catmCurStatusUpPVclEntry" + "[ifIndex='" + self.ifindex.get() + "']" + "[atmVclVpi='" + self.atmvclvpi.get() + "']" + "[atmVclVci='" + self.atmvclvci.get() + "']"
                self._absolute_path = lambda: "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/catmCurStatusUpPVclTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOATMPVCTRAPEXTNMIB.Catmcurstatusuppvcltable.Catmcurstatusuppvclentry, ['ifindex', 'atmvclvpi', 'atmvclvci', 'catmpvclstatusuptransition', 'catmpvclstatusupstart', 'catmpvclstatusupend', 'catmpvclsegccstatusuptransition', 'catmpvclsegccstatusupstart', 'catmpvclsegccstatusupend', 'catmpvclendccstatusuptransition', 'catmpvclendccstatusupstart', 'catmpvclendccstatusupend', 'catmpvclaisrdistatusuptransition', 'catmpvclaisrdistatusupstart', 'catmpvclaisrdistatusupend', 'catmpvclcurrecovertime', 'catmpvclprevfailtime', 'catmpvclrecoveryreason'], name, value)


    class Catmstatusuppvclrangetable(Entity):
        """
        A table indicating more than one VCLs in a consecutive 
        range and for each VCL there is an active row in the 
        atmVclTable having an atmVclConnKind value of `pvc'
        and loopback OAM status to have detected as recovered
        in the last corresponding PVC notification .
        
        .. attribute:: catmstatusuppvclrangeentry
        
        	Each entry in this table represents a range of VCLs and  for each VCL there is an active row in the atmVclTable having an atmVclConnKind value of 'pvc' and  loopback OAM status to  have detected as recovered in the last notification  interval
        	**type**\: list of  		 :py:class:`Catmstatusuppvclrangeentry <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.Catmstatusuppvclrangetable.Catmstatusuppvclrangeentry>`
        
        

        """

        _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
        _revision = '2003-01-20'

        def __init__(self):
            super(CISCOATMPVCTRAPEXTNMIB.Catmstatusuppvclrangetable, self).__init__()

            self.yang_name = "catmStatusUpPVclRangeTable"
            self.yang_parent_name = "CISCO-ATM-PVCTRAP-EXTN-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"catmStatusUpPVclRangeEntry" : ("catmstatusuppvclrangeentry", CISCOATMPVCTRAPEXTNMIB.Catmstatusuppvclrangetable.Catmstatusuppvclrangeentry)}

            self.catmstatusuppvclrangeentry = YList(self)
            self._segment_path = lambda: "catmStatusUpPVclRangeTable"
            self._absolute_path = lambda: "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOATMPVCTRAPEXTNMIB.Catmstatusuppvclrangetable, [], name, value)


        class Catmstatusuppvclrangeentry(Entity):
            """
            Each entry in this table represents a range of VCLs and 
            for each VCL there is an active row in the atmVclTable having
            an atmVclConnKind value of 'pvc' and  loopback OAM status to 
            have detected as recovered in the last notification 
            interval.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: atmvclvpi  <key>
            
            	
            	**type**\: int
            
            	**range:** 0..4095
            
            	**refers to**\:  :py:class:`atmvclvpi <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.Atmvcltable.Atmvclentry>`
            
            .. attribute:: catmstatuschangepvclrangeindex  <key>
            
            	
            	**type**\: int
            
            	**range:** 0..65535
            
            	**refers to**\:  :py:class:`catmstatuschangepvclrangeindex <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.Catmstatuschangepvclrangetable.Catmstatuschangepvclrangeentry>`
            
            .. attribute:: catmpvcluplowerrangevalue
            
            	The first PVCL in a range of PVCLs for which the  Loopback OAM recovery has been detected in the last  corresponding notification 
            	**type**\: int
            
            	**range:** 0..65536
            
            .. attribute:: catmpvcluphigherrangevalue
            
            	The last PVCL in a range of PVCLs for which the  Loopback OAM recovery has been detected in the last  corresponding notification 
            	**type**\: int
            
            	**range:** 0..65536
            
            .. attribute:: catmpvclrangestatusupstart
            
            	The time stamp at which the first Loopback OAM recovery is detected on any of the PVCLs in the range in the last corresponding notification 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclrangestatusupend
            
            	The time stamp at which the last Loopback OAM recovery is detected on any of the PVCLs in the range in the last corresponding notification 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
            _revision = '2003-01-20'

            def __init__(self):
                super(CISCOATMPVCTRAPEXTNMIB.Catmstatusuppvclrangetable.Catmstatusuppvclrangeentry, self).__init__()

                self.yang_name = "catmStatusUpPVclRangeEntry"
                self.yang_parent_name = "catmStatusUpPVclRangeTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.atmvclvpi = YLeaf(YType.str, "atmVclVpi")

                self.catmstatuschangepvclrangeindex = YLeaf(YType.str, "catmStatusChangePVclRangeIndex")

                self.catmpvcluplowerrangevalue = YLeaf(YType.int32, "catmPVclUpLowerRangeValue")

                self.catmpvcluphigherrangevalue = YLeaf(YType.int32, "catmPVclUpHigherRangeValue")

                self.catmpvclrangestatusupstart = YLeaf(YType.uint32, "catmPVclRangeStatusUpStart")

                self.catmpvclrangestatusupend = YLeaf(YType.uint32, "catmPVclRangeStatusUpEnd")
                self._segment_path = lambda: "catmStatusUpPVclRangeEntry" + "[ifIndex='" + self.ifindex.get() + "']" + "[atmVclVpi='" + self.atmvclvpi.get() + "']" + "[catmStatusChangePVclRangeIndex='" + self.catmstatuschangepvclrangeindex.get() + "']"
                self._absolute_path = lambda: "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/catmStatusUpPVclRangeTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOATMPVCTRAPEXTNMIB.Catmstatusuppvclrangetable.Catmstatusuppvclrangeentry, ['ifindex', 'atmvclvpi', 'catmstatuschangepvclrangeindex', 'catmpvcluplowerrangevalue', 'catmpvcluphigherrangevalue', 'catmpvclrangestatusupstart', 'catmpvclrangestatusupend'], name, value)


    class Catmsegccstatusuppvclrangetable(Entity):
        """
        A table indicating more than one VCLs in a consecutive
        range and for each VCL there is an active row in the
        atmVclTable having an atmVclConnKind value of `pvc'
        and Segment CC OAM status to have detected as recovered
        in the last corresponding PVC notification .
        
        .. attribute:: catmsegccstatusuppvclrangeentry
        
        	Each entry in this table represents a range of VCLs and for each VCL there is an active row in the atmVclTable having an atmVclConnKind value of 'pvc' and Segment CC OAM status to have detected as recovered in the last notification interval
        	**type**\: list of  		 :py:class:`Catmsegccstatusuppvclrangeentry <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.Catmsegccstatusuppvclrangetable.Catmsegccstatusuppvclrangeentry>`
        
        

        """

        _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
        _revision = '2003-01-20'

        def __init__(self):
            super(CISCOATMPVCTRAPEXTNMIB.Catmsegccstatusuppvclrangetable, self).__init__()

            self.yang_name = "catmSegCCStatusUpPVclRangeTable"
            self.yang_parent_name = "CISCO-ATM-PVCTRAP-EXTN-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"catmSegCCStatusUpPVclRangeEntry" : ("catmsegccstatusuppvclrangeentry", CISCOATMPVCTRAPEXTNMIB.Catmsegccstatusuppvclrangetable.Catmsegccstatusuppvclrangeentry)}

            self.catmsegccstatusuppvclrangeentry = YList(self)
            self._segment_path = lambda: "catmSegCCStatusUpPVclRangeTable"
            self._absolute_path = lambda: "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOATMPVCTRAPEXTNMIB.Catmsegccstatusuppvclrangetable, [], name, value)


        class Catmsegccstatusuppvclrangeentry(Entity):
            """
            Each entry in this table represents a range of VCLs and
            for each VCL there is an active row in the atmVclTable having
            an atmVclConnKind value of 'pvc' and Segment CC OAM status to
            have detected as recovered in the last notification
            interval.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: atmvclvpi  <key>
            
            	
            	**type**\: int
            
            	**range:** 0..4095
            
            	**refers to**\:  :py:class:`atmvclvpi <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.Atmvcltable.Atmvclentry>`
            
            .. attribute:: catmstatuschangepvclrangeindex  <key>
            
            	
            	**type**\: int
            
            	**range:** 0..65535
            
            	**refers to**\:  :py:class:`catmstatuschangepvclrangeindex <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.Catmstatuschangepvclrangetable.Catmstatuschangepvclrangeentry>`
            
            .. attribute:: catmpvclsegccuplowerrangevalue
            
            	The first PVCL in a range of PVCLs for which the Segment CC OAM recovery has been detected in the last corresponding notification 
            	**type**\: int
            
            	**range:** 0..65536
            
            .. attribute:: catmpvclsegccuphigherrangevalue
            
            	The last PVCL in a range of PVCLs for which the Segment CC OAM recovery has been detected in the last corresponding notification 
            	**type**\: int
            
            	**range:** 0..65536
            
            .. attribute:: catmpvclsegccrangestatusupstart
            
            	The time stamp at which the first Segment CC OAM recovery is detected on any of the PVCLs in the range in the last corresponding notification 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclsegccrangestatusupend
            
            	The time stamp at which the last Segment CC OAM recovery is detected on any of the PVCLs in the range in the last corresponding notification 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
            _revision = '2003-01-20'

            def __init__(self):
                super(CISCOATMPVCTRAPEXTNMIB.Catmsegccstatusuppvclrangetable.Catmsegccstatusuppvclrangeentry, self).__init__()

                self.yang_name = "catmSegCCStatusUpPVclRangeEntry"
                self.yang_parent_name = "catmSegCCStatusUpPVclRangeTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.atmvclvpi = YLeaf(YType.str, "atmVclVpi")

                self.catmstatuschangepvclrangeindex = YLeaf(YType.str, "catmStatusChangePVclRangeIndex")

                self.catmpvclsegccuplowerrangevalue = YLeaf(YType.int32, "catmPVclSegCCUpLowerRangeValue")

                self.catmpvclsegccuphigherrangevalue = YLeaf(YType.int32, "catmPVclSegCCUpHigherRangeValue")

                self.catmpvclsegccrangestatusupstart = YLeaf(YType.uint32, "catmPVclSegCCRangeStatusUpStart")

                self.catmpvclsegccrangestatusupend = YLeaf(YType.uint32, "catmPVclSegCCRangeStatusUpEnd")
                self._segment_path = lambda: "catmSegCCStatusUpPVclRangeEntry" + "[ifIndex='" + self.ifindex.get() + "']" + "[atmVclVpi='" + self.atmvclvpi.get() + "']" + "[catmStatusChangePVclRangeIndex='" + self.catmstatuschangepvclrangeindex.get() + "']"
                self._absolute_path = lambda: "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/catmSegCCStatusUpPVclRangeTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOATMPVCTRAPEXTNMIB.Catmsegccstatusuppvclrangetable.Catmsegccstatusuppvclrangeentry, ['ifindex', 'atmvclvpi', 'catmstatuschangepvclrangeindex', 'catmpvclsegccuplowerrangevalue', 'catmpvclsegccuphigherrangevalue', 'catmpvclsegccrangestatusupstart', 'catmpvclsegccrangestatusupend'], name, value)


    class Catmendccstatusuppvclrangetable(Entity):
        """
        A table indicating more than one VCLs in a consecutive
        range and for each VCL there is an active row in the
        atmVclTable having an atmVclConnKind value of `pvc'
        and End\-to\-End CC OAM status to have detected as recovered
        in the last corresponding PVC notification .
        
        .. attribute:: catmendccstatusuppvclrangeentry
        
        	Each entry in this table represents a range of VCLs and for each VCL there is an active row in the atmVclTable having an atmVclConnKind value of 'pvc' and End\-to\-End CC OAM status  to have detected as recovered in the last notification interval
        	**type**\: list of  		 :py:class:`Catmendccstatusuppvclrangeentry <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.Catmendccstatusuppvclrangetable.Catmendccstatusuppvclrangeentry>`
        
        

        """

        _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
        _revision = '2003-01-20'

        def __init__(self):
            super(CISCOATMPVCTRAPEXTNMIB.Catmendccstatusuppvclrangetable, self).__init__()

            self.yang_name = "catmEndCCStatusUpPVclRangeTable"
            self.yang_parent_name = "CISCO-ATM-PVCTRAP-EXTN-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"catmEndCCStatusUpPVclRangeEntry" : ("catmendccstatusuppvclrangeentry", CISCOATMPVCTRAPEXTNMIB.Catmendccstatusuppvclrangetable.Catmendccstatusuppvclrangeentry)}

            self.catmendccstatusuppvclrangeentry = YList(self)
            self._segment_path = lambda: "catmEndCCStatusUpPVclRangeTable"
            self._absolute_path = lambda: "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOATMPVCTRAPEXTNMIB.Catmendccstatusuppvclrangetable, [], name, value)


        class Catmendccstatusuppvclrangeentry(Entity):
            """
            Each entry in this table represents a range of VCLs and
            for each VCL there is an active row in the atmVclTable having
            an atmVclConnKind value of 'pvc' and End\-to\-End CC OAM status 
            to have detected as recovered in the last notification
            interval.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: atmvclvpi  <key>
            
            	
            	**type**\: int
            
            	**range:** 0..4095
            
            	**refers to**\:  :py:class:`atmvclvpi <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.Atmvcltable.Atmvclentry>`
            
            .. attribute:: catmstatuschangepvclrangeindex  <key>
            
            	
            	**type**\: int
            
            	**range:** 0..65535
            
            	**refers to**\:  :py:class:`catmstatuschangepvclrangeindex <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.Catmstatuschangepvclrangetable.Catmstatuschangepvclrangeentry>`
            
            .. attribute:: catmpvclendccuplowerrangevalue
            
            	The first PVCL in a range of PVCLs for which the End\-to\-End CC OAM recovery has been detected in the last corresponding notification 
            	**type**\: int
            
            	**range:** 0..65536
            
            .. attribute:: catmpvclendccuphigherrangevalue
            
            	The last PVCL in a range of PVCLs for which the End\-to\-End CC OAM recovery has been detected in the last corresponding notification 
            	**type**\: int
            
            	**range:** 0..65536
            
            .. attribute:: catmpvclendccrangestatusupstart
            
            	The time stamp at which the first End\-to\-End CC OAM recovery is detected on any of the PVCLs in the range in the last corresponding notification 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclendccrangestatusupend
            
            	The time stamp at which the last End\-to\-End CC OAM recovery is detected on any of the PVCLs in the range in the last corresponding notification 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
            _revision = '2003-01-20'

            def __init__(self):
                super(CISCOATMPVCTRAPEXTNMIB.Catmendccstatusuppvclrangetable.Catmendccstatusuppvclrangeentry, self).__init__()

                self.yang_name = "catmEndCCStatusUpPVclRangeEntry"
                self.yang_parent_name = "catmEndCCStatusUpPVclRangeTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.atmvclvpi = YLeaf(YType.str, "atmVclVpi")

                self.catmstatuschangepvclrangeindex = YLeaf(YType.str, "catmStatusChangePVclRangeIndex")

                self.catmpvclendccuplowerrangevalue = YLeaf(YType.int32, "catmPVclEndCCUpLowerRangeValue")

                self.catmpvclendccuphigherrangevalue = YLeaf(YType.int32, "catmPVclEndCCUpHigherRangeValue")

                self.catmpvclendccrangestatusupstart = YLeaf(YType.uint32, "catmPVclEndCCRangeStatusUpStart")

                self.catmpvclendccrangestatusupend = YLeaf(YType.uint32, "catmPVclEndCCRangeStatusUpEnd")
                self._segment_path = lambda: "catmEndCCStatusUpPVclRangeEntry" + "[ifIndex='" + self.ifindex.get() + "']" + "[atmVclVpi='" + self.atmvclvpi.get() + "']" + "[catmStatusChangePVclRangeIndex='" + self.catmstatuschangepvclrangeindex.get() + "']"
                self._absolute_path = lambda: "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/catmEndCCStatusUpPVclRangeTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOATMPVCTRAPEXTNMIB.Catmendccstatusuppvclrangetable.Catmendccstatusuppvclrangeentry, ['ifindex', 'atmvclvpi', 'catmstatuschangepvclrangeindex', 'catmpvclendccuplowerrangevalue', 'catmpvclendccuphigherrangevalue', 'catmpvclendccrangestatusupstart', 'catmpvclendccrangestatusupend'], name, value)


    class Catmaisrdistatusuppvclrangetable(Entity):
        """
        A table indicating more than one VCLs in a consecutive
        range and for each VCL there is an active row in the
        atmVclTable having an atmVclConnKind value of `pvc'
        and AISRDI OAM status to have detected as recovered
        in the last corresponding PVC notification .
        
        .. attribute:: catmaisrdistatusuppvclrangeentry
        
        	Each entry in this table represents a range of VCLs and for each VCL there is an active row in the atmVclTable having an atmVclConnKind value of 'pvc' and AISRDI OAM status  to have detected as recovered in the last notification interval
        	**type**\: list of  		 :py:class:`Catmaisrdistatusuppvclrangeentry <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.Catmaisrdistatusuppvclrangetable.Catmaisrdistatusuppvclrangeentry>`
        
        

        """

        _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
        _revision = '2003-01-20'

        def __init__(self):
            super(CISCOATMPVCTRAPEXTNMIB.Catmaisrdistatusuppvclrangetable, self).__init__()

            self.yang_name = "catmAISRDIStatusUpPVclRangeTable"
            self.yang_parent_name = "CISCO-ATM-PVCTRAP-EXTN-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"catmAISRDIStatusUpPVclRangeEntry" : ("catmaisrdistatusuppvclrangeentry", CISCOATMPVCTRAPEXTNMIB.Catmaisrdistatusuppvclrangetable.Catmaisrdistatusuppvclrangeentry)}

            self.catmaisrdistatusuppvclrangeentry = YList(self)
            self._segment_path = lambda: "catmAISRDIStatusUpPVclRangeTable"
            self._absolute_path = lambda: "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOATMPVCTRAPEXTNMIB.Catmaisrdistatusuppvclrangetable, [], name, value)


        class Catmaisrdistatusuppvclrangeentry(Entity):
            """
            Each entry in this table represents a range of VCLs and
            for each VCL there is an active row in the atmVclTable having
            an atmVclConnKind value of 'pvc' and AISRDI OAM status 
            to have detected as recovered in the last notification
            interval.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: atmvclvpi  <key>
            
            	
            	**type**\: int
            
            	**range:** 0..4095
            
            	**refers to**\:  :py:class:`atmvclvpi <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.Atmvcltable.Atmvclentry>`
            
            .. attribute:: catmstatuschangepvclrangeindex  <key>
            
            	
            	**type**\: int
            
            	**range:** 0..65535
            
            	**refers to**\:  :py:class:`catmstatuschangepvclrangeindex <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.Catmstatuschangepvclrangetable.Catmstatuschangepvclrangeentry>`
            
            .. attribute:: catmpvclaisrdiuplowerrangevalue
            
            	The first PVCL in a range of PVCLs for which the AISRDI OAM recovery has been detected in the last corresponding notification 
            	**type**\: int
            
            	**range:** 0..65536
            
            .. attribute:: catmpvclaisrdiuphigherrangevalue
            
            	The last PVCL in a range of PVCLs for which the AISRDI OAM recovery has been detected in the last corresponding notification 
            	**type**\: int
            
            	**range:** 0..65536
            
            .. attribute:: catmpvclaisrdirangestatusupstart
            
            	The time stamp at which the first AISRDI OAM recovery is detected on any of the PVCLs in the range in the last corresponding notification 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclaisrdirangestatusupend
            
            	The time stamp at which the last AISRDI OAM recovery is detected on any of the PVCLs in the range in the last corresponding notification 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
            _revision = '2003-01-20'

            def __init__(self):
                super(CISCOATMPVCTRAPEXTNMIB.Catmaisrdistatusuppvclrangetable.Catmaisrdistatusuppvclrangeentry, self).__init__()

                self.yang_name = "catmAISRDIStatusUpPVclRangeEntry"
                self.yang_parent_name = "catmAISRDIStatusUpPVclRangeTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.atmvclvpi = YLeaf(YType.str, "atmVclVpi")

                self.catmstatuschangepvclrangeindex = YLeaf(YType.str, "catmStatusChangePVclRangeIndex")

                self.catmpvclaisrdiuplowerrangevalue = YLeaf(YType.int32, "catmPVclAISRDIUpLowerRangeValue")

                self.catmpvclaisrdiuphigherrangevalue = YLeaf(YType.int32, "catmPVclAISRDIUpHigherRangeValue")

                self.catmpvclaisrdirangestatusupstart = YLeaf(YType.uint32, "catmPVclAISRDIRangeStatusUpStart")

                self.catmpvclaisrdirangestatusupend = YLeaf(YType.uint32, "catmPVclAISRDIRangeStatusUpEnd")
                self._segment_path = lambda: "catmAISRDIStatusUpPVclRangeEntry" + "[ifIndex='" + self.ifindex.get() + "']" + "[atmVclVpi='" + self.atmvclvpi.get() + "']" + "[catmStatusChangePVclRangeIndex='" + self.catmstatuschangepvclrangeindex.get() + "']"
                self._absolute_path = lambda: "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/catmAISRDIStatusUpPVclRangeTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOATMPVCTRAPEXTNMIB.Catmaisrdistatusuppvclrangetable.Catmaisrdistatusuppvclrangeentry, ['ifindex', 'atmvclvpi', 'catmstatuschangepvclrangeindex', 'catmpvclaisrdiuplowerrangevalue', 'catmpvclaisrdiuphigherrangevalue', 'catmpvclaisrdirangestatusupstart', 'catmpvclaisrdirangestatusupend'], name, value)


    class Catmuppvclrangetable(Entity):
        """
        A table indicating more than one VCLs in a consecutive 
        range and for each VCL there is an active row in the 
        atmVclTable having an atmVclConnKind value of `pvc'
        and atmVclOperStatus to have detected as Up
        in the last corresponding PVC notification .
        
        .. attribute:: catmuppvclrangeentry
        
        	Each entry in this table represents a range of VCLs and  for each VCL there is an active row in the atmVclTable having an atmVclConnKind value of 'pvc' and  atmVclOperStatus to  have detected as Up in the last notification  interval
        	**type**\: list of  		 :py:class:`Catmuppvclrangeentry <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.Catmuppvclrangetable.Catmuppvclrangeentry>`
        
        

        """

        _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
        _revision = '2003-01-20'

        def __init__(self):
            super(CISCOATMPVCTRAPEXTNMIB.Catmuppvclrangetable, self).__init__()

            self.yang_name = "catmUpPVclRangeTable"
            self.yang_parent_name = "CISCO-ATM-PVCTRAP-EXTN-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"catmUpPVclRangeEntry" : ("catmuppvclrangeentry", CISCOATMPVCTRAPEXTNMIB.Catmuppvclrangetable.Catmuppvclrangeentry)}

            self.catmuppvclrangeentry = YList(self)
            self._segment_path = lambda: "catmUpPVclRangeTable"
            self._absolute_path = lambda: "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOATMPVCTRAPEXTNMIB.Catmuppvclrangetable, [], name, value)


        class Catmuppvclrangeentry(Entity):
            """
            Each entry in this table represents a range of VCLs and 
            for each VCL there is an active row in the atmVclTable having
            an atmVclConnKind value of 'pvc' and  atmVclOperStatus to 
            have detected as Up in the last notification 
            interval.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: atmvclvpi  <key>
            
            	
            	**type**\: int
            
            	**range:** 0..4095
            
            	**refers to**\:  :py:class:`atmvclvpi <ydk.models.cisco_ios_xe.ATM_MIB.ATMMIB.Atmvcltable.Atmvclentry>`
            
            .. attribute:: catmstatuschangepvclrangeindex  <key>
            
            	
            	**type**\: int
            
            	**range:** 0..65535
            
            	**refers to**\:  :py:class:`catmstatuschangepvclrangeindex <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CISCOATMPVCTRAPEXTNMIB.Catmstatuschangepvclrangetable.Catmstatuschangepvclrangeentry>`
            
            .. attribute:: catmuppvcllowerrangevalue
            
            	The first PVCL in a range of PVCLs for which the  atmVclOperStatus has been detected as Up in the  corresponding notification 
            	**type**\: int
            
            	**range:** 0..65536
            
            .. attribute:: catmuppvclhigherrangevalue
            
            	The last PVCL in a range of PVCLs for which the  atmVclOperStatus has been detected as Up in the  corresponding notification 
            	**type**\: int
            
            	**range:** 0..65536
            
            .. attribute:: catmuppvclrangestart
            
            	The time stamp at which the first atmVclOperStatus is detected as Up on any of the PVCLs in the range in the corresponding notification 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmuppvclrangeend
            
            	The time stamp at which the last atmVclOperStatus is detected as Up on any of the PVCLs in the range in the corresponding notification 
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmprevdownpvclrangestart
            
            	The time stamp at which the first atmVclOperStatus is detected as Down on any of the PVCLs in the range in the previous catmIntfPvcDownTrap notification
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmprevdownpvclrangeend
            
            	The time stamp at which the last atmVclOperStatus is detected as Down on any of the PVCLs in the range in the previous catmIntfPvcDownTrap notification
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: catmpvclrangerecoveryreason
            
            	Type of OAM Recovered
            	**type**\:  :py:class:`CatmOAMRecoveryType <ydk.models.cisco_ios_xe.CISCO_ATM_PVCTRAP_EXTN_MIB.CatmOAMRecoveryType>`
            
            

            """

            _prefix = 'CISCO-ATM-PVCTRAP-EXTN-MIB'
            _revision = '2003-01-20'

            def __init__(self):
                super(CISCOATMPVCTRAPEXTNMIB.Catmuppvclrangetable.Catmuppvclrangeentry, self).__init__()

                self.yang_name = "catmUpPVclRangeEntry"
                self.yang_parent_name = "catmUpPVclRangeTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.atmvclvpi = YLeaf(YType.str, "atmVclVpi")

                self.catmstatuschangepvclrangeindex = YLeaf(YType.str, "catmStatusChangePVclRangeIndex")

                self.catmuppvcllowerrangevalue = YLeaf(YType.int32, "catmUpPVclLowerRangeValue")

                self.catmuppvclhigherrangevalue = YLeaf(YType.int32, "catmUpPVclHigherRangeValue")

                self.catmuppvclrangestart = YLeaf(YType.uint32, "catmUpPVclRangeStart")

                self.catmuppvclrangeend = YLeaf(YType.uint32, "catmUpPVclRangeEnd")

                self.catmprevdownpvclrangestart = YLeaf(YType.uint32, "catmPrevDownPVclRangeStart")

                self.catmprevdownpvclrangeend = YLeaf(YType.uint32, "catmPrevDownPVclRangeEnd")

                self.catmpvclrangerecoveryreason = YLeaf(YType.enumeration, "catmPVclRangeRecoveryReason")
                self._segment_path = lambda: "catmUpPVclRangeEntry" + "[ifIndex='" + self.ifindex.get() + "']" + "[atmVclVpi='" + self.atmvclvpi.get() + "']" + "[catmStatusChangePVclRangeIndex='" + self.catmstatuschangepvclrangeindex.get() + "']"
                self._absolute_path = lambda: "CISCO-ATM-PVCTRAP-EXTN-MIB:CISCO-ATM-PVCTRAP-EXTN-MIB/catmUpPVclRangeTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOATMPVCTRAPEXTNMIB.Catmuppvclrangetable.Catmuppvclrangeentry, ['ifindex', 'atmvclvpi', 'catmstatuschangepvclrangeindex', 'catmuppvcllowerrangevalue', 'catmuppvclhigherrangevalue', 'catmuppvclrangestart', 'catmuppvclrangeend', 'catmprevdownpvclrangestart', 'catmprevdownpvclrangeend', 'catmpvclrangerecoveryreason'], name, value)

    def clone_ptr(self):
        self._top_entity = CISCOATMPVCTRAPEXTNMIB()
        return self._top_entity

