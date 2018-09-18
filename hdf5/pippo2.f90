program pippo
  use HDF5
  implicit none
  integer, parameter :: bufsize = 1000000
  integer(hid_t) :: file_id, &
                    dataset_id,dataspace_id,datatype_id,prop_id
  integer :: rank 
  integer(HSIZE_T),dimension(1) :: dims,maxdims,offset
  INTEGER(HID_T) :: filespace_id,memspace_id
  integer :: data(bufsize)
  integer :: error,i,j

  rank = 1
  dims(1) = 100000000

  call h5open_f(error)

  call h5fcreate_f("ciao.h5", H5F_ACC_TRUNC_F, file_id, error)
  call h5screate_simple_f(rank,dims,dataspace_id, error)

  dims(1) = 1024 
  call h5pcreate_f(H5P_DATASET_CREATE_F, prop_id, error)
  call h5pset_chunk_f(prop_id, rank, dims, error)

  call h5tcopy_f(H5T_NATIVE_INTEGER,datatype_id, error)
  call h5dcreate_f(file_id,'test',datatype_id,dataspace_id,dataset_id,error,prop_id)


  CALL h5dget_space_f(dataset_id, filespace_id, error)
  dims(1) = bufsize

  do i=1,100000000/bufsize
    print *, "i = ",i,"/",100000000/bufsize
    offset = (i-1)*bufsize
    do j=1,bufsize
      data(j)=i
    enddo
    CALL h5sselect_hyperslab_f(filespace_id, H5S_SELECT_SET_F, &
                               offset, dims, error)

    CALL h5screate_simple_f(RANK, dims, memspace_id, error)

    CALL H5Dwrite_f(dataset_id, H5T_NATIVE_INTEGER, data, dims, error, &
                      mem_space_id=memspace_id, file_space_id=filespace_id)
    call h5sclose_f(memspace_id,error)
  enddo

  call h5dclose_f(dataset_id,error)
  call h5tclose_f(datatype_id,error)
  call h5sclose_f(dataspace_id,error)
  call h5close_f(file_id)
  
end



