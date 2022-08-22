#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This is CCmath software. 
CCmath Website: https://www.ccmath.com/
Erlang Calculator User Manual: https://erlangaddin.ccmath.com/manual/
"""


# =============================================================================
# REQUIRED PACKAGES
# =============================================================================

import requests

# =============================================================================
# POST REQUEST
# This function sends a post request to given URL and encodes the return in JSON.
# =============================================================================
URL = 'http://software.ccmath.com/cgi-bin/erlang4.fcgi'
def request(output):
    response = requests.post(URL, json=output)
    result = float(response.json())
    return result


#UID=str(input('Enter user ID: '))
UID='2d735398-18b2-11ed-861d-0242ac120002'
output={'UID':UID}
    

# =============================================================================
# ERLANG X FUNCTIONS
# Depending on their values, either the Erlang C, Erlang X, or a combination of 
# the two models is used in the following functions. Note that some parameters in
# the Erlang X functions are optional, these parameters are filled in with default
# values. If an optional parameter is used, all other optional parameters 
# must also be filled in.
# =============================================================================     
    
class X:
    def __init__(self):
        return None
    
    class SLA:
        """
        Parameters
        ----------
        Forecast : float
            The average number of arrivals per unit of time. (Forecast ≥ 0)
        AHT : float
            The Average Handling Time of a call. (AHT > 0)
        Agents : float
            Represents the number of agents; it can be real. (Agents ≥ 0)
        Awt : float
            The Acceptable Waiting Time is the maximum allowed waiting time.
            Customers that wait shorter than the Awt have received, per definition,
            a good service. The service level is defined as the percentage of 
            customers that are served within the Awt. The time unit is the same as 
            the others and, hence, is not necessarily in seconds! (Awt ≥ 0)
        Lines : int
            The Lines parameter is the limit on the total number of customers that 
            can be in the system at the same time, consisting of: lines in use by 
            customers in service, and lines in use by customers that wait. A new 
            arriving customer will be blocked if all lines are occupied. 
            (Lines ≥ Agents, integer). 
            Note: setting a default of 5* your top interval arrival # is good 
            practice, but remember it’s really about the capacity your company has 
            bought from the telephony provider.
        Patience : float
            The average time a customer is willing to wait in the queue. A simple 
            estimator for the patience is calculated by dividing the total waiting 
            time (including the waiting times of the abandoned customers) by the 
            number of abandonments. It is important to filter out extreme values 
            in advance. (Patience ≥ 0)
        Retrials : float
            The probability that a customer who abandons, redials. (0 ≤ Retrials ≤ 1)
        Definition : int
            A flag to switch between different modes of calculating the service level. 
            0 = virtual service level; 1 = answered; 2 = offered (default).
        Variance : float
            The variance of the forecast. All models take fluctuations in the number of 
            arrivals into account. This is characterized by the Poisson distribution, 
            for which the variance is equal to the expectation. The Variance parameter 
            can be used in case the variance is bigger than the expectation. 
            (Variance ≥ Forecast)
        
        Returns
        -------
        float
            The expected service level.
        """
        def __init__(self,Forecast:float,AHT:float,Agents:float,Awt:float,Lines:int=None,Patience:float=None,Retrials:float=None,Definition:int=None,Variance:float=None):
            for var in list(locals().keys())[1:]:
                self.var=locals()[var]   
            return None
        
        def __new__(cls,Forecast:float,AHT:float,Agents:float,Awt:float,Lines:int=None,Patience:float=None,Retrials:float=None,Definition:int=None,Variance:float=None):
            if Lines!=None and Patience!=None and Retrials!=None and Variance!=None and Definition!=None:
                output['function']='serviceLevelErlangXDV'
            elif Lines!=None and Patience!=None and Retrials!=None and Definition==None and Variance!=None:
                output['function']='serviceLevelErlangXV'
            elif Lines!=None and Patience!=None and Retrials!=None and Definition!=None and Variance==None:
                output['function']='serviceLevelErlangXD'
            elif Lines!=None and Patience!=None and Retrials!=None and Definition==None and Variance==None:
                output['function']='serviceLevelErlangX'
            elif (Lines!=None and Patience==None and Retrials==None and Definition==None and Variance==None):
                output['function']='serviceLevelErlangCL'
            elif Lines==None and Patience==None and Retrials==None and Definition==None and Variance==None:
                output['function']='serviceLevelErlangC'      
            else:
                output['function']=None      
            for i in X.SLA.__new__.__annotations__:
                output[i]=locals()[i]
            return request(output)
                    
      
    class AGENTS_SLA():
        """
        Parameters
        ----------
        SL : float
            The expected Service Level of an arbitrary non-blocked customer. (0 < SL < 1)
        Forecast : float
            The average number of arrivals per unit of time. (Forecast ≥ 0)
        AHT : float
            The Average Handling Time of a call. (AHT > 0)
        Awt : float
            The Acceptable Waiting Time is the maximum allowed waiting time.
            Customers that wait shorter than the Awt have received, per definition,
            a good service. The service level is defined as the percentage of 
            customers that are served within the Awt. The time unit is the same as 
            the others and, hence, is not necessarily in seconds! (Awt ≥ 0)
        Lines : int
            The Lines parameter is the limit on the total number of customers that 
            can be in the system at the same time, consisting of: lines in use by 
            customers in service, and lines in use by customers that wait. A new 
            arriving customer will be blocked if all lines are occupied. 
            (Lines ≥ Agents, integer). 
            Note: setting a default of 5* your top interval arrival # is good 
            practice, but remember it’s really about the capacity your company has 
            bought from the telephony provider.
        Patience : float
            The average time a customer is willing to wait in the queue. A simple 
            estimator for the patience is calculated by dividing the total waiting 
            time (including the waiting times of the abandoned customers) by the 
            number of abandonments. It is important to filter out extreme values 
            in advance. (Patience ≥ 0)
        Retrials : float
            The probability that a customer who abandons, redials. (0 ≤ Retrials ≤ 1)
        Definition : int
            A flag to switch between different modes of calculating the service level. 
            0 = virtual service level; 1 = answered; 2 = offered (default).
        Variance : float
            The variance of the forecast. All models take fluctuations in the number of 
            arrivals into account. This is characterized by the Poisson distribution, 
            for which the variance is equal to the expectation. The Variance parameter 
            can be used in case the variance is bigger than the expectation. 
            (Variance ≥ Forecast)
        
        Returns
        -------
        float
            The optimal number of agents such that the service-level objective is satisfied.
        """
        def __init__(self,SL:float,Forecast:float,AHT:float,Awt:float,Lines:int=None,Patience:float=None,Retrials:float=None,Definition:int=None,Variance:float=None):
            for var in list(locals().keys())[1:]:
                self.var=locals()[var]   
            return None
       
        
        def __new__(cls,SL:float,Forecast:float,AHT:float,Awt:float,Lines:int=None,Patience:float=None,Retrials:float=None,Definition:int=None,Variance:float=None):
            if Lines!=None and Patience!=None and Retrials!=None and Variance!=None and Definition!=None:
                output['function']='agentsServiceLevelErlangXDV'
            elif Lines!=None and Patience!=None and Retrials!=None and Definition==None and Variance!=None:
                output['function']='agentsServiceLevelErlangXV'
            elif Lines!=None and Patience!=None and Retrials!=None and Definition!=None and Variance==None:
                output['function']='agentsServiceLevelErlangXD'
            elif Lines!=None and Patience!=None and Retrials!=None and Definition==None and Variance==None:
                output['function']='agentsServiceLevelErlangX'
            elif (Lines!=None and Patience==None and Retrials==None and Definition==None and Variance==None):
                output['function']='agentsServiceLevelErlangCL'
            elif Lines==None and Patience==None and Retrials==None and Variance==None  and Definition==None:
                output['function']='agentsServiceLevelErlangC'
            else:
                output['function']=None    
            for i in X.AGENTS_SLA.__new__.__annotations__:
                output[i]=locals()[i]
            return request(output)  
        
    class FORECAST():
        """
        Parameters
        ----------
        SL : float
            The expected Service Level of an arbitrary non-blocked customer. (0 < SL < 1)
        AHT : float
            The Average Handling Time of a call. (AHT > 0)
        Agents : float
            Represents the number of agents; it can be real. (Agents ≥ 0)
        Awt : float
            The Acceptable Waiting Time is the maximum allowed waiting time.
            Customers that wait shorter than the Awt have received, per definition,
            a good service. The service level is defined as the percentage of 
            customers that are served within the Awt. The time unit is the same as 
            the others and, hence, is not necessarily in seconds! (Awt ≥ 0)
        Lines : int
            The Lines parameter is the limit on the total number of customers that 
            can be in the system at the same time, consisting of: lines in use by 
            customers in service, and lines in use by customers that wait. A new 
            arriving customer will be blocked if all lines are occupied. 
            (Lines ≥ Agents, integer). 
            Note: setting a default of 5* your top interval arrival # is good 
            practice, but remember it’s really about the capacity your company has 
            bought from the telephony provider.
        Patience : float
            The average time a customer is willing to wait in the queue. A simple 
            estimator for the patience is calculated by dividing the total waiting 
            time (including the waiting times of the abandoned customers) by the 
            number of abandonments. It is important to filter out extreme values 
            in advance. (Patience ≥ 0)
        Retrials : float
            The probability that a customer who abandons, redials. (0 ≤ Retrials ≤ 1)
        Definition : int
            A flag to switch between different modes of calculating the service level. 
            0 = virtual service level; 1 = answered; 2 = offered (default).
        
        Returns
        -------
        float
            The maximum average number of arrivals per unit of time such that the 
            service-level objective is satisfied.
        """
        def __init__(self,SL:float,AHT:float,Agents:float,Awt:float,Lines:int=None,Patience:float=None,Retrials:float=None,Definition:int=None):
            for var in list(locals().keys())[1:]:
                self.var=locals()[var]   
            return None
        
        def __new__(cls,SL:float,AHT:float,Agents:float,Awt:float,Lines:int=None,Patience:float=None,Retrials:float=None,Definition:int=None):
            if Lines!=None and Patience!=None and Retrials!=None and Definition!=None:
                output['function']='forecastServiceLevelErlangXD'
            elif Lines!=None and Patience!=None and Retrials!=None and Definition==None:
                output['function']='forecastServiceLevelErlangX'
            elif (Lines!=None and Patience==None and Retrials==None and Definition==None):
                output['function']='forecastServiceLevelErlangCL'
            elif Lines==None and Patience==None and Retrials==None and Definition==None:
                output['function']='forecastServiceLevelErlangC'
            else:
                output['function']=None    
            for i in X.FORECAST.__new__.__annotations__:
                output[i]=locals()[i]
            return request(output) 
    
    class ASA():
        """
        Parameters
        ----------
        Forecast : float
            The average number of arrivals per unit of time. (Forecast ≥ 0)
        AHT : float
            The Average Handling Time of a call. (AHT > 0)
        Agents : float
            Represents the number of agents; it can be real. (Agents ≥ 0)
        Lines : int
            The Lines parameter is the limit on the total number of customers that 
            can be in the system at the same time, consisting of: lines in use by 
            customers in service, and lines in use by customers that wait. A new 
            arriving customer will be blocked if all lines are occupied. 
            (Lines ≥ Agents, integer). 
            Note: setting a default of 5* your top interval arrival # is good 
            practice, but remember it’s really about the capacity your company has 
            bought from the telephony provider.
        Patience : float
            The average time a customer is willing to wait in the queue. A simple 
            estimator for the patience is calculated by dividing the total waiting 
            time (including the waiting times of the abandoned customers) by the 
            number of abandonments. It is important to filter out extreme values 
            in advance. (Patience ≥ 0)
        Retrials : float
            The probability that a customer who abandons, redials. (0 ≤ Retrials ≤ 1)
        
        Returns
        -------
        float
            The average speed of answer.
        """
        def __init__(self,Forecast:float,AHT:float,Agents:float,Lines:int=None,Patience:float=None,Retrials:float=None):
            for var in list(locals().keys())[1:]:
                self.var=locals()[var]   
            return None
        def __new__(cls,Forecast:float,AHT:float,Agents:float,Lines:int=None,Patience:float=None,Retrials:float=None):
            if Lines!=None and Patience!=None and Retrials!=None:
                output['function']='waitingtimeErlangX'
            elif Lines!=None and Patience==None and Retrials==None:
                output['function']='waitingtimeErlangCL'
            elif Lines==None and Patience==None and Retrials==None:
                output['function']='waitingtimeErlangC'
            else:
                output['function']=None    
            for i in X.ASA.__new__.__annotations__:
                output[i]=locals()[i]
            return request(output) 
    
    class AGENTS_ASA():
        """
        Parameters
        ----------
        W : float
            The Average Speed of Answer (also known as average waiting time) is the time
            that an arbitrary customer with infinite patience would incur. (W > 0)
        Forecast : float
            The average number of arrivals per unit of time. (Forecast ≥ 0)
        AHT:AHT : list
            The Average Handling Time of a call. (AHT > 0). The difference between 
            this and the previous AHT parameter is that the AHT should be a range 
            of cells instead of a single number. The number of elements in the range
            determines the maximum number of concurrent chats that an agent can do. 
            This parameter is exclusively used in the Chat functions.
        Lines : int
            The Lines parameter is the limit on the total number of customers that 
            can be in the system at the same time, consisting of: lines in use by 
            customers in service, and lines in use by customers that wait. A new 
            arriving customer will be blocked if all lines are occupied. 
            (Lines ≥ Agents, integer). 
            Note: setting a default of 5* your top interval arrival # is good 
            practice, but remember it’s really about the capacity your company has 
            bought from the telephony provider.
        Patience : float
            The average time a customer is willing to wait in the queue. A simple 
            estimator for the patience is calculated by dividing the total waiting 
            time (including the waiting times of the abandoned customers) by the 
            number of abandonments. It is important to filter out extreme values 
            in advance. (Patience ≥ 0)
            
        Returns
        -------
        float
            The average speed of answer.
        """
        def __init__(self,W:float,Forecast:float,AHT:float,Lines:int=None,Patience:float=None,Retrials:float=None):
            for var in list(locals().keys())[1:]:
                self.var=locals()[var]   
            return None
        def __new__(cls,W:float,Forecast:float,AHT:float,Lines:int=None,Patience:float=None,Retrials:float=None):
            if Lines!=None and Patience!=None and Retrials!=None:
                output['function']='agentsWaitingTimeErlangX'
            elif Lines!=None and Patience==None and Retrials==None:
                output['function']='agentsWaitingTimeErlangCL'
            elif Lines==None and Patience==None and Retrials==None:
                output['function']='agentsWaitingTimeErlangC'
            else:
                output['function']=None    
            for i in X.AGENTS_ASA.__new__.__annotations__:
                output[i]=locals()[i]
            return request(output)
    
    class ABANDON():
        """
        Parameters
        ----------
        Forecast : float
            The average number of arrivals per unit of time. (Forecast ≥ 0)
        AHT : float
            The Average Handling Time of a call. (AHT > 0)
        Agents : float
            Represents the number of agents; it can be real. (Agents ≥ 0)
        Lines : int
            The Lines parameter is the limit on the total number of customers that 
            can be in the system at the same time, consisting of: lines in use by 
            customers in service, and lines in use by customers that wait. A new 
            arriving customer will be blocked if all lines are occupied. 
            (Lines ≥ Agents, integer). 
            Note: setting a default of 5* your top interval arrival # is good 
            practice, but remember it’s really about the capacity your company has 
            bought from the telephony provider.
        Patience : float
            The average time a customer is willing to wait in the queue. A simple 
            estimator for the patience is calculated by dividing the total waiting 
            time (including the waiting times of the abandoned customers) by the 
            number of abandonments. It is important to filter out extreme values 
            in advance. (Patience ≥ 0)
        Retrials : float
            The probability that a customer who abandons, redials. (0 ≤ Retrials ≤ 1)
        Variance : float
            The variance of the forecast. All models take fluctuations in the number of 
            arrivals into account. This is characterized by the Poisson distribution, 
            for which the variance is equal to the expectation. The Variance parameter 
            can be used in case the variance is bigger than the expectation. 
            (Variance ≥ Forecast)
        
        Returns
        -------
        float
            The fraction of customers that abandon.
        """
        def __init__(self,Forecast:float,AHT:float,Agents:float,Lines:int,Patience:float,Retrials:float,Variance:float=None):
            for var in list(locals().keys())[1:]:
                self.var=locals()[var]   
            return None
        def __new__(cls,Forecast:float,AHT:float,Agents:float,Lines:int,Patience:float,Retrials:float,Variance:float=None):
            if Variance!=None:
                output['function']='abandonmentsErlangXV'
            elif Variance==None:
                output['function']='abandonmentsErlangX'
                
            for i in X.ABANDON.__new__.__annotations__:
                output[i]=locals()[i]
            return request(output) 
    
    class AGENTS_ABANDON():
        """
        Parameters
        ----------
        Ab : float
            The probability that an arbitrary customer will abandon. 
            (0 < Ab < 1)
        Forecast : float
            The average number of arrivals per unit of time. (Forecast ≥ 0)
        AHT : float
            The Average Handling Time of a call. (AHT > 0)
        Lines : int
            The Lines parameter is the limit on the total number of customers that 
            can be in the system at the same time, consisting of: lines in use by 
            customers in service, and lines in use by customers that wait. A new 
            arriving customer will be blocked if all lines are occupied. 
            (Lines ≥ Agents, integer). 
            Note: setting a default of 5* your top interval arrival # is good 
            practice, but remember it’s really about the capacity your company has 
            bought from the telephony provider.
        Patience : float
            The average time a customer is willing to wait in the queue. A simple 
            estimator for the patience is calculated by dividing the total waiting 
            time (including the waiting times of the abandoned customers) by the 
            number of abandonments. It is important to filter out extreme values 
            in advance. (Patience ≥ 0)
        Retrials : float
            The probability that a customer who abandons, redials. (0 ≤ Retrials ≤ 1)
            
        Returns
        -------
        float
            The optimal number of agents such that the abandonment objective is satisfied.
        """
        def __init__(self,ab:float,Forecast:float,AHT:float,Lines:int,Patience:float,Retrials:float):      
            for var in list(locals().keys())[1:]:
                self.var=locals()[var]   
            return None
        def __new__(cls,ab:float,Forecast:float,AHT:float,Lines:int,Patience:float,Retrials:float):      
            output['function']='agentsAbandonmentErlangX'
            for i in X.AGENTS_ABANDON.__new__.__annotations__:
                output[i]=locals()[i]
            return request(output)  
    
    class RETRIALRATE():
        """
        Parameters
        ----------
        Forecast : float
            The average number of arrivals per unit of time. (Forecast ≥ 0)
        AHT : float
            The Average Handling Time of a call. (AHT > 0)
        Agents : float
            Represents the number of agents; it can be real. (Agents ≥ 0)
        Lines : int
            The Lines parameter is the limit on the total number of customers that 
            can be in the system at the same time, consisting of: lines in use by 
            customers in service, and lines in use by customers that wait. A new 
            arriving customer will be blocked if all lines are occupied. 
            (Lines ≥ Agents, integer). 
            Note: setting a default of 5* your top interval arrival # is good 
            practice, but remember it’s really about the capacity your company has 
            bought from the telephony provider.
        Patience : float
            The average time a customer is willing to wait in the queue. A simple 
            estimator for the patience is calculated by dividing the total waiting 
            time (including the waiting times of the abandoned customers) by the 
            number of abandonments. It is important to filter out extreme values 
            in advance. (Patience ≥ 0)
        Retrials : float
            The probability that a customer who abandons, redials. (0 ≤ Retrials ≤ 1)      
    
        Returns
        -------
        float
            The average number of customers that retrial per unit of time.
        """
        def __init__(self,Forecast:float,AHT:float,Agents:float,Lines:int,Patience:float,Retrials:float):                 
            for var in list(locals().keys())[1:]:
                self.var=locals()[var]   
            return None
       
        def __new__(cls,Forecast:float,AHT:float,Agents:float,Lines:int,Patience:float,Retrials:float):              
            output['function']='retrialrateErlangX'
            for i in X.RETRIALRATE.__new__.__annotations__:
                output[i]=locals()[i]
            return request(output) 
    
    class BLOCKING():
        """
        Parameters
        ----------
        Forecast : float
            The average number of arrivals per unit of time. (Forecast ≥ 0)
        AHT : float
            The Average Handling Time of a call. (AHT > 0)
        Agents : float
            Represents the number of agents; it can be real. (Agents ≥ 0)
        Lines : int
            The Lines parameter is the limit on the total number of customers that 
            can be in the system at the same time, consisting of: lines in use by 
            customers in service, and lines in use by customers that wait. A new 
            arriving customer will be blocked if all lines are occupied. 
            (Lines ≥ Agents, integer). 
            Note: setting a default of 5* your top interval arrival # is good 
            practice, but remember it’s really about the capacity your company has 
            bought from the telephony provider.
        Patience : float
            The average time a customer is willing to wait in the queue. A simple 
            estimator for the patience is calculated by dividing the total waiting 
            time (including the waiting times of the abandoned customers) by the 
            number of abandonments. It is important to filter out extreme values 
            in advance. (Patience ≥ 0)
        Retrials : float
            The probability that a customer who abandons, redials. (0 ≤ Retrials ≤ 1)      

        Returns
        -------
        float
            The fraction of customers that are blocked.
        """
        def __init__(self,Forecast:float,AHT:float,Agents:float,Lines:int,Patience:float,Retrials:float):            
            for var in list(locals().keys())[1:]:
                self.var=locals()[var]   
            return None
       
        def __new__(cls,Forecast:float,AHT:float,Agents:float,Lines:int,Patience:float,Retrials:float):             
            if Retrials!=None:
                output['function']='blockingprobErlangX'
            for i in X.BLOCKING.__new__.__annotations__:
                output[i]=locals()[i]
            return request(output) 
    
    class OCCUPANCY():
        """
        Parameters
        ----------
        Forecast : float
            The average number of arrivals per unit of time. (Forecast ≥ 0)
        AHT : float
            The Average Handling Time of a call. (AHT > 0)
        Agents : float
            Represents the number of agents; it can be real. (Agents ≥ 0)
        Lines : int
            The Lines parameter is the limit on the total number of customers that 
            can be in the system at the same time, consisting of: lines in use by 
            customers in service, and lines in use by customers that wait. A new 
            arriving customer will be blocked if all lines are occupied. 
            (Lines ≥ Agents, integer). 
            Note: setting a default of 5* your top interval arrival # is good 
            practice, but remember it’s really about the capacity your company has 
            bought from the telephony provider.
        Patience : float
            The average time a customer is willing to wait in the queue. A simple 
            estimator for the patience is calculated by dividing the total waiting 
            time (including the waiting times of the abandoned customers) by the 
            number of abandonments. It is important to filter out extreme values 
            in advance. (Patience ≥ 0)
        Retrials : float
            The probability that a customer who abandons, redials. (0 ≤ Retrials ≤ 1)      
    
        Returns
        -------
        float
            The occupancy of the agents.
        """
        def __init__(self,Forecast:float,AHT:float,Agents:float,Lines:int,Patience:float,Retrials:float):                  
            for var in list(locals().keys())[1:]:
                self.var=locals()[var]   
            return None
       
        def __new__(cls,Forecast:float,AHT:float,Agents:float,Lines:int,Patience:float,Retrials:float):             
            if Retrials!=None:
                output['function']='occupancyErlangX'
            for i in X.OCCUPANCY.__new__.__annotations__:
                output[i]=locals()[i]
            return request(output)
    
    class AGENTS_BLOCKING():
        """
        Parameters
        ----------
        B : float
            The expected blocking probability. (0 < B < 1)
        Forecast : float
            The average number of arrivals per unit of time. (Forecast ≥ 0)
        AHT : float
            The Average Handling Time of a call. (AHT > 0)
        
        Returns
        -------
        float
            The optimal number of agents such that the blocking objective is satisfied.
        """
        def __init__(self,B:float,Forecast:float,AHT:float):
            for var in list(locals().keys())[1:]:
                self.var=locals()[var]   
            return None
       
        def __new__(cls,B:float,Forecast:float,AHT:float):
            output['function']='agentsBlockingErlangB'
            for i in X.AGENTS_BLOCKING.__new__.__annotations__:
                output[i]=locals()[i]
            return request(output)
    
    class AGENTS_OCCUPANCY():
        """
        Parameters
        ----------
        Occupancy : float
            The occupancy of the agents (0 < Occupancy ≤ 1)
        Forecast : float
            The average number of arrivals per unit of time. (Forecast ≥ 0)
        AHT : float
            The Average Handling Time of a call. (AHT > 0)
        Lines : int
            The Lines parameter is the limit on the total number of customers that 
            can be in the system at the same time, consisting of: lines in use by 
            customers in service, and lines in use by customers that wait. A new 
            arriving customer will be blocked if all lines are occupied. 
            (Lines ≥ Agents, integer). 
            Note: setting a default of 5* your top interval arrival # is good 
            practice, but remember it’s really about the capacity your company has 
            bought from the telephony provider.
        Patience : float
            The average time a customer is willing to wait in the queue. A simple 
            estimator for the patience is calculated by dividing the total waiting 
            time (including the waiting times of the abandoned customers) by the 
            number of abandonments. It is important to filter out extreme values 
            in advance. (Patience ≥ 0)
        Retrials : float
            The probability that a customer who abandons, redials. (0 ≤ Retrials ≤ 1)      

        Returns
        -------
        float
            The optimal number of agents such that the occupancy objective is satisfied.
        """
        def __init__(self,Occupancy:float,Forecast:float,AHT:float,Lines:int,Patience:float,Retrials:float):    
            for var in list(locals().keys())[1:]:
                self.var=locals()[var]   
            return None
       
        def __new__(cls,Occupancy:float,Forecast:float,AHT:float,Lines:int,Patience:float,Retrials:float):    
            output['function']='???'
            for i in X.AGENTS_OCCUPANCY.__new__.__annotations__:
                output[i]=locals()[i]
            return "The online version of AGENTS_OCCUPANCY calculator does not exist."

# =============================================================================
# ERLANG BLENDING FUNCTIONS
# In the blending model, agents will work on inbound as well as outbound calls. 
# If an agent becomes available, they will prioritize inbound calls and will 
# only take on outbound calls when other agents are left idle.
# =============================================================================
class BL:
    def __init__(self):
         return None
    
    class SLA():
        """
        Parameters
        ----------
        Forecast : float
            The average number of arrivals per unit of time. (Forecast ≥ 0)
        AHT : float
            The Average Handling Time of a call. (AHT > 0)
        Agents : float
            Represents the number of agents; it can be real. (Agents ≥ 0)
        Awt : float
            The Acceptable Waiting Time is the maximum allowed waiting time.
            Customers that wait shorter than the Awt have received, per definition,
            a good service. The service level is defined as the percentage of 
            customers that are served within the Awt. The time unit is the same as 
            the others and, hence, is not necessarily in seconds! (Awt ≥ 0)
        Threshold : float
            The number of agents that are kept idle before taking outbound calls into 
            service. (Threshold ≤ Agents)
            
        Returns
        -------
        float
            The expected service level.
        """
        def __init__(self,Forecast:float,AHT:float,Agents:float,Awt:float,Threshold:float):
            for var in list(locals().keys())[1:]:
                self.var=locals()[var]   
            return None
       
        def __new__(cls,Forecast:float,AHT:float,Agents:float,Awt:float,Threshold:float):
            output['function']='serviceLevelBlending'
            for i in BL.SLA.__new__.__annotations__:
                output[i]=locals()[i]
            return request(output)

    class ASA():
        """
        Parameters
        ----------
        Forecast : float
            The average number of arrivals per unit of time. (Forecast ≥ 0)
        AHT : float
            The Average Handling Time of a call. (AHT > 0)
        Agents : float
            Represents the number of agents; it can be real. (Agents ≥ 0)
        Threshold : float
            The number of agents that are kept idle before taking outbound calls into 
            service. (Threshold ≤ Agents)
        
        Returns
        -------
        float
            The average speed of answer.
        """
        def __init__(self,Forecast:float,AHT:float,Agents:float,Threshold:float):
            for var in list(locals().keys())[1:]:
                self.var=locals()[var]   
            return None
       
        def __new__(cls,Forecast:float,AHT:float,Agents:float,Threshold:float):
            output['function']='waitingtimeThresholdBlending'
            for i in BL.ASA.__new__.__annotations__:
                output[i]=locals()[i]
            return request(output)
    
    class OCCUPANCY():
        """
        Parameters
        ----------
        Forecast : float
            The average number of arrivals per unit of time. (Forecast ≥ 0)
        AHT : float
            The Average Handling Time of a call. (AHT > 0)
        Agents : float
            Represents the number of agents; it can be real. (Agents ≥ 0)
        Threshold : float
            The number of agents that are kept idle before taking outbound calls into 
            service. (Threshold ≤ Agents)
        
        Returns
        -------
        float
            The occupancy of the agents.
        """
        def __init__(self,Forecast:float,AHT:float,Agents:float,Threshold:float):
            for var in list(locals().keys())[1:]:
                self.var=locals()[var]   
            return None
        def __new__(cls,Forecast:float,AHT:float,Agents:float,Threshold:float):
            output['function']='occupancyThresholdBlending'
            for i in BL.OCCUPANCY.__new__.__annotations__:
                output[i]=locals()[i]
            return request(output)
        
    class OUTBOUND():
        """
        Parameters
        ----------
        Forecast : float
            The average number of arrivals per unit of time. (Forecast ≥ 0)
        AHT : float
            The Average Handling Time of a call. (AHT > 0)
        Agents : float
            Represents the number of agents; it can be real. (Agents ≥ 0)
        Threshold : float
            The number of agents that are kept idle before taking outbound calls into 
            service. (Threshold ≤ Agents)
        
        Returns
        -------
        float
            The occupancy of the agents.
        """
        def __init__(self,Forecast:float,AHT:float,Agents:float,Threshold:float):
            for var in list(locals().keys())[1:]:
                self.var=locals()[var]   
            return None
        
        def __new__(cls,Forecast:float,AHT:float,Agents:float,Threshold:float):
            output['function']='outboundThresholdBlending'
            for i in BL.OUTBOUND.__new__.__annotations__:
                output[i]=locals()[i]
            return request(output)
        
    class THRESHOLD():
        """
        Parameters
        ----------
        Forecast : float
            The average number of arrivals per unit of time. (Forecast ≥ 0)
        AHT : float
            The Average Handling Time of a call. (AHT > 0)
        Agents : float
            Represents the number of agents; it can be real. (Agents ≥ 0)
        SL : float
            The expected Service Level of an arbitrary non-blocked customer. (0 < SL < 1)
        Awt : float
            The Acceptable Waiting Time is the maximum allowed waiting time.
            Customers that wait shorter than the Awt have received, per definition,
            a good service. The service level is defined as the percentage of 
            customers that are served within the Awt. The time unit is the same as 
            the others and, hence, is not necessarily in seconds! (Awt ≥ 0)
        
        Returns
        -------
        float
            The threshold such that the service-level objective is satisfied.
        """
        def __init__(self,Forecast:float,AHT:float,Agents:float,SL:float,Awt:float):
            for var in list(locals().keys())[1:]:
                self.var=locals()[var]   
            return None
        
        def __new__(cls,Forecast:float,AHT:float,Agents:float,SL:float,Awt:float):
            output['function']='thresholdBlending'
            for i in BL.THRESHOLD.__new__.__annotations__:
                output[i]=locals()[i]
            return request(output)
        
    class ASA_SLA():
        """
        Parameters
        ----------
        Forecast : float
            The average number of arrivals per unit of time. (Forecast ≥ 0)
        AHT : float
            The Average Handling Time of a call. (AHT > 0)
        Agents : float
            Represents the number of agents; it can be real. (Agents ≥ 0)
        SL : float
            The expected Service Level of an arbitrary non-blocked customer. (0 < SL < 1)
        Awt : float
            The Acceptable Waiting Time is the maximum allowed waiting time.
            Customers that wait shorter than the Awt have received, per definition,
            a good service. The service level is defined as the percentage of 
            customers that are served within the Awt. The time unit is the same as 
            the others and, hence, is not necessarily in seconds! (Awt ≥ 0)
            
        Returns
        -------
        float
            The average speed of answer based on the service-level objective.
        """
        def __init__(self,Forecast:float,AHT:float,Agents:float,SL:float,Awt:float):
            for var in list(locals().keys())[1:]:
                self.var=locals()[var]   
            return None
        
        def __new__(cls,Forecast:float,AHT:float,Agents:float,SL:float,Awt:float):
            output['function']='waitingtimeServiceLevelBlending'
            for i in BL.ASA_SLA.__new__.__annotations__:
                output[i]=locals()[i]
            return request(output)

    class OCCUPANCY_SLA():
        """
        Parameters
        ----------
        Forecast : float
            The average number of arrivals per unit of time. (Forecast ≥ 0)
        AHT : float
            The Average Handling Time of a call. (AHT > 0)
        Agents : float
            Represents the number of agents; it can be real. (Agents ≥ 0)
        SL : float
            The expected Service Level of an arbitrary non-blocked customer. (0 < SL < 1)
        Awt : float
            The Acceptable Waiting Time is the maximum allowed waiting time.
            Customers that wait shorter than the Awt have received, per definition,
            a good service. The service level is defined as the percentage of 
            customers that are served within the Awt. The time unit is the same as 
            the others and, hence, is not necessarily in seconds! (Awt ≥ 0)
            
        Returns
        -------
        float
            The occupancy of the agents based on the service-level objective.
        """
        def __init__(self,Forecast:float,AHT:float,Agents:float,SL:float,Awt:float):
            for var in list(locals().keys())[1:]:
                self.var=locals()[var]   
            return None
       
        def __new__(cls,Forecast:float,AHT:float,Agents:float,SL:float,Awt:float):
            output['function']='occupancyServiceLevelBlending'
            for i in BL.OCCUPANCY_SLA.__new__.__annotations__:
                output[i]=locals()[i]
            return request(output)
        
    class OUTBOUND_SLA():
        """
        Parameters
        ----------
        Forecast : float
            The average number of arrivals per unit of time. (Forecast ≥ 0)
        AHT : float
            The Average Handling Time of a call. (AHT > 0)
        Agents : float
            Represents the number of agents; it can be real. (Agents ≥ 0)
        SL : float
            The expected Service Level of an arbitrary non-blocked customer. (0 < SL < 1)
        Awt : float
            The Acceptable Waiting Time is the maximum allowed waiting time.
            Customers that wait shorter than the Awt have received, per definition,
            a good service. The service level is defined as the percentage of 
            customers that are served within the Awt. The time unit is the same as 
            the others and, hence, is not necessarily in seconds! (Awt ≥ 0)
            
        Returns
        -------
        float
            The average number of outbound calls per unit of time based on the 
            service-level objective.
        """
        def __init__(self,Forecast:float,AHT:float,Agents:float,SL:float,Awt:float):
            for var in list(locals().keys())[1:]:
                self.var=locals()[var]   
            return None
       
        def __new__(cls,Forecast:float,AHT:float,Agents:float,SL:float,Awt:float):
            output['function']='outboundServiceLevelBlending'
            for i in BL.OUTBOUND_SLA.__new__.__annotations__:
                output[i]=locals()[i]
            return request(output)

# =============================================================================
# ERLANG CHAT FUNCTIONS
# In the model for chats, the distinguishing feature is that agents can handle 
# multiple chats in parallel.
# =============================================================================
class CHAT:
    def __init__(self):
         return None
    
    class SLA():
        """
        Parameters
        ----------
        Forecast : float
            The average number of arrivals per unit of time. (Forecast ≥ 0)
        AHT : list
            The Average Handling Time of a call. (AHT > 0). The difference between 
            this and the previous AHT parameter is that the AHT should be a range 
            of cells instead of a single number. The number of elements in the range
            determines the maximum number of concurrent chats that an agent can do. 
            This parameter is exclusively used in the Chat functions.
        Agents : float
            Represents the number of agents; it can be real. (Agents ≥ 0)
        Awt : float
            The Acceptable Waiting Time is the maximum allowed waiting time.
            Customers that wait shorter than the Awt have received, per definition,
            a good service. The service level is defined as the percentage of 
            customers that are served within the Awt. The time unit is the same as 
            the others and, hence, is not necessarily in seconds! (Awt ≥ 0)
        Lines : int
            The Lines parameter is the limit on the total number of customers that 
            can be in the system at the same time, consisting of: lines in use by 
            customers in service, and lines in use by customers that wait. A new 
            arriving customer will be blocked if all lines are occupied. 
            (Lines ≥ Agents, integer). 
            Note: setting a default of 5* your top interval arrival # is good 
            practice, but remember it’s really about the capacity your company has 
            bought from the telephony provider.
        Patience : float
            The average time a customer is willing to wait in the queue. A simple 
            estimator for the patience is calculated by dividing the total waiting 
            time (including the waiting times of the abandoned customers) by the 
            number of abandonments. It is important to filter out extreme values 
            in advance. (Patience ≥ 0)
           
        Returns
        -------
        float
            The expected service level.
        """
        def __init__(self,Forecast:float,AHT:list,Agents:float,Awt:float,Lines:int,Patience:float):
            for var in list(locals().keys())[1:]:
                self.var=locals()[var]   
            return None
       
        def __new__(cls,Forecast:float,AHT:list,Agents:float,Awt:float,Lines:int,Patience:float):
             Parallel=int(len(AHT))
             output['Parallel']=Parallel
             output['function']='serviceLevelErlangChat'
             for i in CHAT.SLA.__new__.__annotations__:
                 output[i]=locals()[i]
             return request(output)
    
    class AGENTS_SLA():
        """
        Parameters
        ----------
        SL : float
            The expected Service Level of an arbitrary non-blocked customer. (0 < SL < 1)
        Forecast : float
            The average number of arrivals per unit of time. (Forecast ≥ 0)
        AHT : list
            The Average Handling Time of a call. (AHT > 0). The difference between 
            this and the previous AHT parameter is that the AHT should be a range 
            of cells instead of a single number. The number of elements in the range
            determines the maximum number of concurrent chats that an agent can do. 
            This parameter is exclusively used in the Chat functions.
        Agents : float
            Represents the number of agents; it can be real. (Agents ≥ 0)
        Awt : float
            The Acceptable Waiting Time is the maximum allowed waiting time.
            Customers that wait shorter than the Awt have received, per definition,
            a good service. The service level is defined as the percentage of 
            customers that are served within the Awt. The time unit is the same as 
            the others and, hence, is not necessarily in seconds! (Awt ≥ 0)
        Lines : int
            The Lines parameter is the limit on the total number of customers that 
            can be in the system at the same time, consisting of: lines in use by 
            customers in service, and lines in use by customers that wait. A new 
            arriving customer will be blocked if all lines are occupied. 
            (Lines ≥ Agents, integer). 
            Note: setting a default of 5* your top interval arrival # is good 
            practice, but remember it’s really about the capacity your company has 
            bought from the telephony provider.
        Patience : float
            The average time a customer is willing to wait in the queue. A simple 
            estimator for the patience is calculated by dividing the total waiting 
            time (including the waiting times of the abandoned customers) by the 
            number of abandonments. It is important to filter out extreme values 
            in advance. (Patience ≥ 0)
            
        Returns
        -------
        float
            The optimal number of agents such that the service-level objective is satisfied.
        """
        def __init__(self,SL:float,Forecast:float,AHT:list,Awt:float,Lines:int,Patience:float):
            for var in list(locals().keys())[1:]:
                self.var=locals()[var]   
            return None
        def __new__(cls,SL:float,Forecast:float,AHT:list,Awt:float,Lines:int,Patience:float):
             Parallel=int(len(AHT))
             output['Parallel']=Parallel
             output['function']='agentsServiceLevelErlangChat'
             for i in CHAT.AGENTS_SLA.__new__.__annotations__:
                 output[i]=locals()[i]
             return request(output)

    class ASA():
        """
        Parameters
        ----------
        Forecast : float
            The average number of arrivals per unit of time. (Forecast ≥ 0)
        AHT : list
            The Average Handling Time of a call. (AHT > 0). The difference between 
            this and the previous AHT parameter is that the AHT should be a range 
            of cells instead of a single number. The number of elements in the range
            determines the maximum number of concurrent chats that an agent can do. 
            This parameter is exclusively used in the Chat functions.
        Agents : float
            Represents the number of agents; it can be real. (Agents ≥ 0)
        Lines : int
            The Lines parameter is the limit on the total number of customers that 
            can be in the system at the same time, consisting of: lines in use by 
            customers in service, and lines in use by customers that wait. A new 
            arriving customer will be blocked if all lines are occupied. 
            (Lines ≥ Agents, integer). 
            Note: setting a default of 5* your top interval arrival # is good 
            practice, but remember it’s really about the capacity your company has 
            bought from the telephony provider.
        Patience : float
            The average time a customer is willing to wait in the queue. A simple 
            estimator for the patience is calculated by dividing the total waiting 
            time (including the waiting times of the abandoned customers) by the 
            number of abandonments. It is important to filter out extreme values 
            in advance. (Patience ≥ 0)
            
        Returns
        -------
        float
            The average speed of answer.
        """
        def __init__(self,Forecast:float,AHT:list,Agents:float,Lines:int,Patience:float):
            for var in list(locals().keys())[1:]:
                self.var=locals()[var]   
            return None
        
        def __new__(cls,Forecast:float,AHT:list,Agents:float,Lines:int,Patience:float):
             Parallel=int(len(AHT))
             output['Parallel']=Parallel
             output['function']='waitingtimeErlangChat'
             for i in CHAT.ASA.__new__.__annotations__:
                 output[i]=locals()[i]
             return request(output)    
         
    class AGENTS_ASA():
        """
        Parameters
        ----------
        W : float
            The Average Speed of Answer (also known as average waiting time) is the time
            that an arbitrary customer with infinite patience would incur. (W > 0)
        Forecast : float
            The average number of arrivals per unit of time. (Forecast ≥ 0)
        AHT : list
            The Average Handling Time of a call. (AHT > 0). The difference between 
            this and the previous AHT parameter is that the AHT should be a range 
            of cells instead of a single number. The number of elements in the range
            determines the maximum number of concurrent chats that an agent can do. 
            This parameter is exclusively used in the Chat functions.
        Lines : int
            The Lines parameter is the limit on the total number of customers that 
            can be in the system at the same time, consisting of: lines in use by 
            customers in service, and lines in use by customers that wait. A new 
            arriving customer will be blocked if all lines are occupied. 
            (Lines ≥ Agents, integer). 
            Note: setting a default of 5* your top interval arrival # is good 
            practice, but remember it’s really about the capacity your company has 
            bought from the telephony provider.
        Patience : float
            The average time a customer is willing to wait in the queue. A simple 
            estimator for the patience is calculated by dividing the total waiting 
            time (including the waiting times of the abandoned customers) by the 
            number of abandonments. It is important to filter out extreme values 
            in advance. (Patience ≥ 0)
            
        Returns
        -------
        float
            The optimal number of agents such that the W objective is satisfied.
        """
        def __init__(self,W:float,Forecast:float,AHT:list,Lines:int,Patience:float):
            for var in list(locals().keys())[1:]:
                self.var=locals()[var]   
            return None
       
        def __new__(cls,W:float,Forecast:float,AHT:list,Lines:int,Patience:float):
             Parallel=int(len(AHT))
             output['Parallel']=Parallel
             output['function']='agentsWaitingTimeErlangChat'
             for i in CHAT.AGENTS_ASA.__new__.__annotations__:
                 output[i]=locals()[i]
             return request(output)   
         
    class ABANDON():
        """
        Parameters
        ----------
        Forecast : float
            The average number of arrivals per unit of time. (Forecast ≥ 0)
        AHT : list
            The Average Handling Time of a call. (AHT > 0). The difference between 
            this and the previous AHT parameter is that the AHT should be a range 
            of cells instead of a single number. The number of elements in the range
            determines the maximum number of concurrent chats that an agent can do. 
            This parameter is exclusively used in the Chat functions.
        Agents : float
            Represents the number of agents; it can be real. (Agents ≥ 0)
        Lines : int
            The Lines parameter is the limit on the total number of customers that 
            can be in the system at the same time, consisting of: lines in use by 
            customers in service, and lines in use by customers that wait. A new 
            arriving customer will be blocked if all lines are occupied. 
            (Lines ≥ Agents, integer). 
            Note: setting a default of 5* your top interval arrival # is good 
            practice, but remember it’s really about the capacity your company has 
            bought from the telephony provider.
        Patience : float
            The average time a customer is willing to wait in the queue. A simple 
            estimator for the patience is calculated by dividing the total waiting 
            time (including the waiting times of the abandoned customers) by the 
            number of abandonments. It is important to filter out extreme values 
            in advance. (Patience ≥ 0)
            
        Returns
        -------
        float
            The fraction of customers that abandon chats.
        """
        def __init__(self,Forecast:float,AHT:list,Agents:float,Lines:int,Patience:float):
            for var in list(locals().keys())[1:]:
                self.var=locals()[var]   
            return None
       
        def __new__(cls,Forecast:float,AHT:list,Agents:float,Lines:int,Patience:float):
             Parallel=int(len(AHT))
             output['Parallel']=Parallel
             output['function']='???'
             for i in CHAT.ABANDON.__new__.__annotations__:
                 output[i]=locals()[i]
             return "The online version of ABANDON calculator does not exist."
    
    class AGENTS_ABANDON():
        """
        Parameters
        ----------
        Ab : float
            The probability that an arbitrary customer will abandon. 
            (0 < Ab < 1)
        Forecast : float
            The average number of arrivals per unit of time. (Forecast ≥ 0)
        AHT : list
            The Average Handling Time of a call. (AHT > 0). The difference between 
            this and the previous AHT parameter is that the AHT should be a range 
            of cells instead of a single number. The number of elements in the range
            determines the maximum number of concurrent chats that an agent can do. 
            This parameter is exclusively used in the Chat functions.
        Lines : int
            The Lines parameter is the limit on the total number of customers that 
            can be in the system at the same time, consisting of: lines in use by 
            customers in service, and lines in use by customers that wait. A new 
            arriving customer will be blocked if all lines are occupied. 
            (Lines ≥ Agents, integer). 
            Note: setting a default of 5* your top interval arrival # is good 
            practice, but remember it’s really about the capacity your company has 
            bought from the telephony provider.
        Patience : float
            The average time a customer is willing to wait in the queue. A simple 
            estimator for the patience is calculated by dividing the total waiting 
            time (including the waiting times of the abandoned customers) by the 
            number of abandonments. It is important to filter out extreme values 
            in advance. (Patience ≥ 0)
            
        Returns
        -------
        float
            The optimal number of agents such that the abandonment objective is satisfied.
        """
        def __init__(self,ab:float,Forecast:float,AHT:list,Lines:int,Patience:float):
            for var in list(locals().keys())[1:]:
                self.var=locals()[var]   
            return None
       
        def __new__(cls,ab:float,Forecast:float,AHT:list,Lines:int,Patience:float):
             Parallel=int(len(AHT))
             output['Parallel']=Parallel
             output['function']='???'
             for i in CHAT.AGENTS_ABANDON.__new__.__annotations__:
                 output[i]=locals()[i]
             return "The online version of AGENTS_ABANDON calculator does not exist."
         
    class OCCUPANCY():
        """
        Parameters
        ----------
        Ab : float
            The probability that an arbitrary customer will abandon. 
            (0 < Ab < 1)
        Forecast : float
            The average number of arrivals per unit of time. (Forecast ≥ 0)
        AHT : list
            The Average Handling Time of a call. (AHT > 0). The difference between 
            this and the previous AHT parameter is that the AHT should be a range 
            of cells instead of a single number. The number of elements in the range
            determines the maximum number of concurrent chats that an agent can do. 
            This parameter is exclusively used in the Chat functions.
        Lines : int
            The Lines parameter is the limit on the total number of customers that 
            can be in the system at the same time, consisting of: lines in use by 
            customers in service, and lines in use by customers that wait. A new 
            arriving customer will be blocked if all lines are occupied. 
            (Lines ≥ Agents, integer). 
            Note: setting a default of 5* your top interval arrival # is good 
            practice, but remember it’s really about the capacity your company has 
            bought from the telephony provider.
        Patience : float
            The average time a customer is willing to wait in the queue. A simple 
            estimator for the patience is calculated by dividing the total waiting 
            time (including the waiting times of the abandoned customers) by the 
            number of abandonments. It is important to filter out extreme values 
            in advance. (Patience ≥ 0)
            
        Returns
        -------
        float
            The optimal number of agents such that the abandonment objective is satisfied.
        """
        def __init__(self,Forecast:float,AHT:list,Agents:float,Lines:int,Patience:float):
            for var in list(locals().keys())[1:]:
                self.var=locals()[var]   
            return None
       
        def __new__(cls,Forecast:float,AHT:list,Agents:float,Lines:int,Patience:float):
             Parallel=int(len(AHT))
             output['Parallel']=Parallel
             output['function']='???'
             for i in CHAT.OCCUPANCY.__new__.__annotations__:
                 output[i]=locals()[i]
             return "The online version of OCCUPANCY calculator does not exist."
    
    class AGENTS_OCCUPANCY():
        """
        Parameters
        ----------
        Occupancy : float
            The occupancy of the agents (0 < Occupancy ≤ 1)
        Forecast : float
            The average number of arrivals per unit of time. (Forecast ≥ 0)
        AHT : list
            The Average Handling Time of a call. (AHT > 0). The difference between 
            this and the previous AHT parameter is that the AHT should be a range 
            of cells instead of a single number. The number of elements in the range
            determines the maximum number of concurrent chats that an agent can do. 
            This parameter is exclusively used in the Chat functions.
        Lines : int
            The Lines parameter is the limit on the total number of customers that 
            can be in the system at the same time, consisting of: lines in use by 
            customers in service, and lines in use by customers that wait. A new 
            arriving customer will be blocked if all lines are occupied. 
            (Lines ≥ Agents, integer). 
            Note: setting a default of 5* your top interval arrival # is good 
            practice, but remember it’s really about the capacity your company has 
            bought from the telephony provider.
        Patience : float
            The average time a customer is willing to wait in the queue. A simple 
            estimator for the patience is calculated by dividing the total waiting 
            time (including the waiting times of the abandoned customers) by the 
            number of abandonments. It is important to filter out extreme values 
            in advance. (Patience ≥ 0)
       
        Returns
        -------
        float
            The optimal number of agents such that the occupancy objective is satisfied.
        """
        def __init__(self,Occupancy:float,Forecast:float,AHT:list,Lines:int,Patience:float):
            for var in list(locals().keys())[1:]:
                self.var=locals()[var]   
            return None
       
        def __new__(cls,Occupancy:float,Forecast:float,AHT:list,Lines:int,Patience:float):
             Parallel=int(len(AHT))
             output['Parallel']=Parallel
             output['function']='???'
             for i in CHAT.AGENTS_OCCUPANCY.__new__.__annotations__:
                 output[i]=locals()[i]
             return "The online version of AGENTS_OCCUPANCY calculator does not exist."
       
            
